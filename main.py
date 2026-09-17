from fastapi import FastAPI
from sqlalchemy.orm import Session
from schemas import StudentCourseDepartmentCreate

from database import SessionLocal
from models import Student, Course, Department

from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentPatch,
    CourseCreate,
    CoursePatch,
    DepartmentCreate,
    DepartmentPatch
)

app = FastAPI(
    title="Student Management System"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI Connected Successfully"
    }


# ==========================
# STUDENT APIS
# ==========================

@app.get("/students")
def get_students():

    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    db.close()

    if not student:
        return {"message": "Student Not Found"}

    return student


@app.post("/students")
def create_student(student: StudentCreate):

    db = SessionLocal()

    existing_email = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_email:
        db.close()
        return {"message": "Email already exists"}

    course = db.query(Course).filter(
        Course.course_id == student.course_id
    ).first()

    if not course:
        db.close()
        return {"message": "Invalid Course ID"}

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        branch=student.branch,
        created_by=student.created_by,
        course_id=student.course_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    db.close()

    return {
        "message": "Student Added Successfully",
        "student_id": new_student.id
    }


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):

    db = SessionLocal()

    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not existing_student:
        db.close()
        return {"message": "Student Not Found"}

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.branch = student.branch
    existing_student.updated_by = student.updated_by
    existing_student.course_id = student.course_id

    db.commit()
    db.refresh(existing_student)

    db.close()

    return {"message": "Student Updated Successfully"}


@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentPatch):

    db = SessionLocal()

    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not existing_student:
        db.close()
        return {"message": "Student Not Found"}

    data = student.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(existing_student, key, value)

    db.commit()
    db.refresh(existing_student)

    db.close()

    return {"message": "Student Patched Successfully"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        db.close()
        return {"message": "Student Not Found"}

    db.delete(student)
    db.commit()

    db.close()

    return {"message": "Student Deleted Successfully"}


# ==========================
# COURSE APIS
# ==========================

@app.get("/courses")
def get_courses():

    db = SessionLocal()

    courses = db.query(Course).all()

    db.close()

    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: int):

    db = SessionLocal()

    course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    db.close()

    if not course:
        return {"message": "Course Not Found"}

    return course


@app.post("/courses")
def create_course(course: CourseCreate):

    db = SessionLocal()

    new_course = Course(
        course_name=course.course_name
    )

    db.add(new_course)
    db.commit()

    db.close()

    return {"message": "Course Added Successfully"}


@app.put("/courses/{course_id}")
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

    db.close()

    return {"message": "Course Updated Successfully"}


@app.patch("/courses/{course_id}")
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
    db.close()
    return {"message": "Course Patched Successfully"}


@app.delete("/courses/{course_id}")
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

    return {"message": "Course Deleted Successfully"}


# ==========================
# DEPARTMENT APIS
# ==========================

@app.get("/departments")
def get_departments():

    db = SessionLocal()

    departments = db.query(Department).all()

    db.close()

    return departments


@app.get("/departments/{department_id}")
def get_department(department_id: int):

    db = SessionLocal()

    department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    db.close()

    if not department:
        return {"message": "Department Not Found"}

    return department


@app.post("/departments")
def create_department(department: DepartmentCreate):

    db = SessionLocal()

    new_department = Department(
        department_name=department.department_name
    )

    db.add(new_department)
    db.commit()

    db.close()

    return {"message": "Department Added Successfully"}


@app.put("/departments/{department_id}")
def update_department(
    department_id: int,
    department: DepartmentCreate
):

    db = SessionLocal()

    existing_department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if not existing_department:
        db.close()
        return {"message": "Department Not Found"}

    existing_department.department_name = department.department_name

    db.commit()

    db.close()

    return {"message": "Department Updated Successfully"}


@app.patch("/departments/{department_id}")
def patch_department(
    department_id: int,
    department: DepartmentPatch
):

    db = SessionLocal()

    existing_department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if not existing_department:
        db.close()
        return {"message": "Department Not Found"}

    if department.department_name is not None:
        existing_department.department_name = department.department_name

    db.commit()

    db.close()

    return {"message": "Department Patched Successfully"}


@app.delete("/departments/{department_id}")
def delete_department(department_id: int):

    db = SessionLocal()

    department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if not department:
        db.close()
        return {"message": "Department Not Found"}

    db.delete(department)
    db.commit()

    db.close()

    return {"message": "Department Deleted Successfully"}


# ==========================
# ALL DATA
# ==========================

@app.get("/all-data")
def get_all_data():

    db = SessionLocal()

    students = db.query(Student).all()
    courses = db.query(Course).all()
    departments = db.query(Department).all()

    db.close()

    return {
        "students": students,
        "courses": courses,
        "departments": departments
    }
#Two table combined data 
@app.get("/student-course/{student_id}")
def get_student_course_by_id(student_id: int):

    db = SessionLocal()

    result = (
        db.query(
            Student.id,
            Student.name,
            Student.email,
            Course.course_name
        )
        .join(
            Course,
            Student.course_id == Course.course_id
        )
        .filter(Student.id == student_id)
        .first()
    )

    db.close()

    if not result:
        return {"message": "Student Not Found"}

    return {
        "id": result.id,
        "name": result.name,
        "email": result.email,
        "course_name": result.course_name
    }
#three table combined data
@app.get("/student-course-department")
def get_all_details():

    db = SessionLocal()

    result = (
        db.query(
            Student.name,
            Course.course_name,
            Department.department_name
        )
        .join(
            Course,
            Student.course_id == Course.course_id
        )
        .join(
            Department,
            Course.department_id == Department.department_id
        )
        .all()
    )

    db.close()

    output = []

    for row in result:
        output.append({
            "student_name": row.name,
            "course_name": row.course_name,
            "department_name": row.department_name
        })

    return output

@app.post("/student-course-department")
def create_student_course_department(
    data: StudentCourseDepartmentCreate
):

    db = SessionLocal()

    # Check Department
    department = db.query(Department).filter(
        Department.department_name == data.department_name
    ).first()

    if not department:
        db.close()
        return {
            "message": "Department Not Found"
        }

    # Check Course
    course = db.query(Course).filter(
        Course.course_name == data.course_name,
        Course.department_id == department.department_id
    ).first()

    if not course:
        db.close()
        return {
            "message": "Course Not Found"
        }

    # Check Email
    existing_student = db.query(Student).filter(
        Student.email == data.email
    ).first()

    if existing_student:
        db.close()
        return {
            "message": "Email Already Exists"
        }

    # Create Student
    student = Student(
        name=data.name,
        age=data.age,
        email=data.email,
        branch=data.branch,
        created_by=data.created_by,
        course_id=course.course_id
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    response = {
        "student_id": student.id,
        "student_name": student.name,
        "course_name": course.course_name,
        "department_name": department.department_name,
        "message": "Student Added Successfully"
    }

    db.close()

    return response
@app.post("/student-course")
def create_student_course(student: StudentCreate):

    db = SessionLocal()

    course = db.query(Course).filter(
        Course.course_id == student.course_id
    ).first()

    if not course:
        db.close()
        return {"message": "Invalid Course ID"}

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        branch=student.branch,
        created_by=student.created_by,
        course_id=student.course_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    result = {
        "student_id": new_student.id,
        "student_name": new_student.name,
        "course_name": course.course_name
    }

    db.close()

    return result