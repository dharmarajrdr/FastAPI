from fastapi import FastAPI, HTTPException

from db_config import SessionLocal, engine
from user import User
import user

app = FastAPI()

user.Base.metadata.create_all(bind=engine)

@app.get("/users")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

@app.get("/users/search")
def search_users(name: str = None):
    db = SessionLocal()
    users = db.query(User).filter(User.name.ilike(f"%{name}%")).all()
    db.close()
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
