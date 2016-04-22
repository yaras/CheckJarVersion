# Requirements

* JDK must be on `%PATH%` (tools: `jar` and `javap`)

# Usage

Run:

`check_jar_version.exe [path to scan]`

# What it does

- Script scans given path for jars
- For each jar:
 - script finds any class included in this jar by executing `jar tfv Library.jar`
 - script finds minor/major version in result of executing `javap -verbose -cp Library.jar package.name.ClassName`
- As result script prints:
```
Library1.jar                      ('major version: 51', 'minor version: 0')
Library2.jar                      ('major version: 51', 'minor version: 0')
...
```


 # Start hacking source

 ```
python -m venv .env
.env\Scripts\activate.bat
pip install -r requirements.txt

hack hack hack

pyinstaller --onefile check_jar_version.py
 ```
