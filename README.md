# A simple Python API example

Build with Flask. Based on code snippets from  https://flask-httpauth.readthedocs.io/en/latest/ and https://requests.readthedocs.io/en/master/user/authentication/. To run the API:

$cd reposity
$python3 -m venv env
$source env/bin/activate
$python3 -m pip install -r requirements.txt
$export FLASK_APP=app.py
$flask run

...and run for the testing script, use a different terminal:

$cd reposity
$source env/bin/activate
$python3 test_api.py

Thanks :-)
