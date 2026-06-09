from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="GymLog API", version="2.0.0")

# Modele danych (Szkic API)
class UserRegister(BaseModel):
    email: str
    password: str

class WorkoutCreate(BaseModel):
    name: str

# 1. Obszar Auth (Zgłoszenie projektu)
@app.post("/auth/register")
def register_user(user: UserRegister):
    return {"message": f"Użytkownik {user.email} zarejestrowany pomyślnie."}

@app.post("/auth/login")
def login_user(user: UserRegister):
    return {"access_token": "mocked-jwt-token-xyz", "token_type": "bearer"}

# 2. Obszar Workouts (Zgłoszenie projektu)
@app.get("/workouts")
def get_workouts():
    return [{"id": 1, "name": "Góra Ciała - Wtorek", "user_id": 51805}]

@app.post("/workouts")
def create_workout(workout: WorkoutCreate):
    return {"id": 2, "name": workout.name, "message": "Trening utworzony."}
