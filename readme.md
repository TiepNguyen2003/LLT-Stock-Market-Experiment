HOW TO HOST

Requires python 3.12

- In VSCODE/your favorite IDE clone the repository

- Create a virtual environment using VSCode (or these https://www.arch.jhu.edu/python-virtual-environments/)
- Use the following commands
```
pip install -r requirements.txt
```


Use the following commands to create the database

```
flask db init
flask db migrate -m "First Migration"
flask db upgrade
```

This creates a file called app.db which will save your data. This step does not need to be repeated

Running the website can be done with


```
flask run
```
