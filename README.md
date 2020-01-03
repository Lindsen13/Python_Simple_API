# A simple Python API example

Build with Flask. The api consist of an authentication method, and has 2 endpoints. 

The first endpoint (http://localhost:5000/) retrieved the list of items made during the current session. The second endpoint (http://localhost:5000/element) adds new elements and returns the list.

Based on code snippets from  https://flask-httpauth.readthedocs.io/en/latest/ and https://requests.readthedocs.io/en/master/user/authentication/. To run the API:

```console
$git clone https://github.com/Lindsen13/Python_Simple_API.git
$cd Python_Simple_API
$python3 -m venv env
$source env/bin/activate
$python3 -m pip install -r requirements.txt
$export FLASK_APP=app.py
$flask run
```

...and run for the testing script, use a different terminal:

```console
$cd reposity
$source env/bin/activate
$python3 test_api.py
```

Thanks :-)
