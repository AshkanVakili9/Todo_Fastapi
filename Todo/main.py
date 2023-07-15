from fastapi import FastAPI, Depends
import models
from database import engine

from routers import auth, todos, users
from company import company_apis, dependencies


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(
    company_apis.router,
    prefix='/company_apis',
    tags=['companyapis'],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418:{'description': 'Internal Use Only'}}
)
