from fastapi import FastAPI
from app.database import engine, Base
from app.routers import links

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Short URL API", description="Encurtador de Links com FastAPI")

app.include_router(links.router)