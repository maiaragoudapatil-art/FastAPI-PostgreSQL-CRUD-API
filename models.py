from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# STUDENT TABLE
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    branch = Column(String)

    created_by = Column(String)
    updated_by = Column(String)

    course_id = Column(Integer)


# COURSE TABLE
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String)

    department_id = Column(Integer)


# DEPARTMENT TABLE
class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String)
