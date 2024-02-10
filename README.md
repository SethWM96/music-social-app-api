# Project Set Up

Set up virtual environment
```
python3 -m venv venv
```
Activate Virtual Environment
```
source venv/bin/activate
```
Install Dependencies
```
pip install -r requirements.txt
```
Update dependencies/requirements.txt
```
pip freeze > requirements.txt
```
Deactivate Virtual Environment
```
deactivate
```

# Run Project
To run locally
```
uvicorn main:app --reload
```
