from fastapi import APIRouter
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/students")
def get_students():
    return {"message": "Students API"}