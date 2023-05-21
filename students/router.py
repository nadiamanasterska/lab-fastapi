from fastapi import APIRouter
from .storage import student_list
from .schema import StudentCreateSchema, StudentUpdateSchema



router = APIRouter()

@router.get("/")
async def get_student(): 
    return {"students": student_list}

@router.post("/")
async def crate_student(student: StudentCreateSchema):
    student_list.append(student)
    return student


@router.get("/{student_id}")
async def get_student(student_id: int):
    return student_list[student_id]



@router.patch("/{student_id}")
async def update_student(student: StudentUpdateSchema, student_id: int):
    student_list[student_id] = student
    return student