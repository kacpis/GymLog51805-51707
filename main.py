from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="GymLog API", version="3.0.0")

# Prosta baza danych w pamięci RAM na potrzeby etapu 3
USERS_DB = {
    "test@gymlog.pl": "haslo123"
}
WORKOUTS_DB = [
    {"id": 1, "name": "Góra Ciała - Wtorek", "user_id": 51805, "status": "completed"}
]

# Modele danych
class UserRegister(BaseModel):
    email: str
    password: str

class WorkoutCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    status: Optional[str] = "planned"

# 1. Obszar Auth
@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister):
    if user.email in USERS_DB:
        raise HTTPException(status_code=400, detail="Użytkownik o tym mailu już istnieje.")
    USERS_DB[user.email] = user.password
    return {"message": f"Użytkownik {user.email} zarejestrowany pomyślnie."}

@app.post("/auth/login")
def login_user(user: UserRegister):
    if user.email not in USERS_DB or USERS_DB[user.email] != user.password:
        raise HTTPException(status_code=401, detail="Niepoprawny login lub hasło.")
    return {"access_token": "zalogowano-pomyślnie-token-etap3", "token_type": "bearer"}

# 2. Obszar Workouts
@app.get("/workouts")
def get_workouts():
    return WORKOUTS_DB

@app.post("/workouts", status_code=status.HTTP_201_CREATED)
def create_workout(workout: WorkoutCreate):
    new_id = len(WORKOUTS_DB) + 1
    new_workout = {"id": new_id, "name": workout.name, "user_id": 51805, "status": workout.status}
    WORKOUTS_DB.append(new_workout)
    return {"message": "Trening utworzony pomyślnie", "workout": new_workout}
