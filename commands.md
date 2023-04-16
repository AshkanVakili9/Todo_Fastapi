pip install fastapi[all]

pip freeze > req.txt  

cd Todo

uvicorn main:app --reload
uvicorn auth:app --reload
