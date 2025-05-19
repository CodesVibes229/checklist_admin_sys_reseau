from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, auth, models
from .database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Utilisateur déjà inscrit.")
    hashed = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Utilisateur créé avec succès."}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Identifiants invalides.")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/tasks", response_model=list[schemas.Task])
def get_tasks(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return crud.get_tasks_by_user(db, user_id=current_user.id)

@router.post("/tasks")
def save_tasks(tasks: list[schemas.TaskCreate], current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    # Supprime les anciennes tâches de l'utilisateur avant d'ajouter les nouvelles
    crud.delete_tasks_by_user(db, user_id=current_user.id)
    for task in tasks:
        crud.create_task(db, task, user_id=current_user.id)
    return {"message": "Progression sauvegardée avec succès."}
