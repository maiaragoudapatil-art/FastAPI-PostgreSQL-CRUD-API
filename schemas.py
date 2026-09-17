from pydantic import BaseModel
from typing import Optional


# ==================
# STUDENT SCHEMAS
# ==================

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    branch: str
    created_by: str
    course_id: int


class StudentUpdate(BaseModel):
    name: str
    age: int
    email: str
    branch: str
    updated_by: str
    course_id: int


class StudentPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    branch: Optional[str] = None
    updated_by: Optional[str] = None
    course_id: Optional[int] = None

class CourseCreate(BaseModel):
    course_name: str


class CoursePatch(BaseModel):
    course_name: Optional[str] = None


class DepartmentCreate(BaseModel):
    department_name: str


class DepartmentPatch(BaseModel):
    department_name: Optional[str] = None

from pydantic import BaseModel

class StudentCourseDepartmentCreate(BaseModel):
    name: str
    age: int
    email: str
    branch: str
    created_by: str

    course_name: str
    department_name: str