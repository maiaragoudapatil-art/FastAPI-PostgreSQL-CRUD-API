from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Course
from schemas import CourseCreate, CoursePatch

router = APIRouter()


# GET ALL COURSES
@router.get("/courses")
def get_courses():

    db = SessionLocal()

    courses = db.query(Course).all()

    db.close()

    return courses


# GET COURSE BY ID
@router.get("/courses/{course_id}")
def get_course(course_id: int):

    db = SessionLocal()

    course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    db.close()

    if not course:
        return {"message": "Course Not Found"}

    return course


# CREATE COURSE
@router.post("/courses")
def create_course(course: CourseCreate):

    db = SessionLocal()

    new_course = Course(
        course_name=course.course_name
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    db.close()

    return {
        "message": "Course Added Successfully",
        "course_id": new_course.course_id
    }


# UPDATE COURSE
@router.put("/courses/{course_id}")
def update_course(course_id: int, course: CourseCreate):

    db = SessionLocal()

    existing_course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    if not existing_course:
        db.close()
        return {"message": "Course Not Found"}

    existing_course.course_name = course.course_name

    db.commit()
    db.refresh(existing_course)

    db.close()

    return {
        "message": "Course Updated Successfully"
    }


# PATCH COURSE
@router.patch("/courses/{course_id}")
def patch_course(course_id: int, course: CoursePatch):

    db = SessionLocal()

    existing_course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    if not existing_course:
        db.close()
        return {"message": "Course Not Found"}

    if course.course_name is not None:
        existing_course.course_name = course.course_name

    db.commit()
    db.refresh(existing_course)

    db.close()

    return {
        "message": "Course Patched Successfully"
    }


# DELETE COURSE
@router.delete("/courses/{course_id}")
def delete_course(course_id: int):

    db = SessionLocal()

    course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    if not course:
        db.close()
        return {"message": "Course Not Found"}

    db.delete(course)
    db.commit()

    db.close()

    return {
        "message": "Course Deleted Successfully"
    }