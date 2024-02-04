pip install fastapi[all]

pip freeze > req.txt  

cd Todo

uvicorn main:app --reload
uvicorn auth:app --reload


uvicorn main:app --reload --host 192.168.1.21 --port 8000
