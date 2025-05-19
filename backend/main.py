from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app import models
from app.routes import router

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS : pour autoriser les requêtes depuis le frontend (ex. navigateur local ou Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou restreins à ["http://localhost:5500"] si besoin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ajout du routeur principal
app.include_router(router)
