from fastapi import APIRouter

router = APIRouter()

@router.get("/departments")
def get_departments():
    return {"message": "Departments API"}