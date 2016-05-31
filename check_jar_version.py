import os
import subprocess
import sys

# jar tfv lib.jar | grep class | head
# javap -verbose -cp lib.jar package.ClassName | head

def find_all_jars(path):
	for (path, dirs, files) in os.walk(path):
		for f in files:
			abs_path = os.path.join(path, f)

			if abs_path.endswith('.jar'):
				yield abs_path

def find_any_class_in_result(result):
	for line in result.split('\n'):
		if line.strip().endswith('.class'):
			return line.replace('/', '.').replace('.class', '').strip()

	return None

def get_class_description(path, cls):
	output = subprocess.check_output(['javap', '-verbose', '-cp', path, cls])

	minor = None
	major = None

	for line in output.decode('1250').split('\n'):
		if 'minor version' in line:
			minor = line.strip()

		if 'major version' in line:
			major = line.strip()

		if minor and major:
			break

	return (major, minor)

def get_jar_version(path):
	result = subprocess.check_output(['jar', 'tf', path])

	cls = find_any_class_in_result(result.decode('1250'))

	desc = get_class_description(path, cls)

	return desc

def main(path):
	print('Path:', path)
	print('--------------------------')

	for jar in find_all_jars(path):
		print(jar[len(path)+1:].ljust(45, ' '), get_jar_version(jar))

if __name__ == '__main__':
	path = '.'

	if len(sys.argv) > 1:
		path = sys.argv[1].replace('/', '\\')

		if path.endswith('\\'):
			path = path[:-1]

	main(path)
