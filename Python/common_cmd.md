# Most used Python commands

```py
# Get installed version
python --version
```

```py
# Install modules using PIP
python -m pip install <module>
```

```py
#Create a Virtual Environment
python -m venv <env path>
python -m venv .venv
```

```py
#Run a Virtual Environment in Power Shell
.<env>\Scripts\Activate
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

```py
# Save dependencies in a file
pip freeze > requirements.txt
```

```py
# Install dependencies from file
pip install -r requirements.txt
```

```py
# See packages dependencies
pip show pandas
```

```py
# Run Python script as module
cd <parent_of_package>
python -m <package>.<subpkg>.<module>
```