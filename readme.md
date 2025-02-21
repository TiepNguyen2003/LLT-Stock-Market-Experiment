HOW TO HOST

Requires python 3.12

- In VSCODE/your favorite IDE clone the repository

- Create a virtual environment using VSCode (or these https://www.arch.jhu.edu/python-virtual-environments/)
- Use the following commands
```
pip install -r requirements.txt
```


Create test.db using sqlite shell (google how to do this lol) if it is not already done

```
flask db init
flask db migrate -m "First Migration"
flask db upgrade
```

This creates a file called app.db which will save your data. This step does not need to be repeated

Running the website can be done with deploy.py
