import models
import schemas
import crud

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List


# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI()


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# -----------------------------
# CREATE EMPLOYEE
# -----------------------------

@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, employee)


# -----------------------------
# GET ALL EMPLOYEES
# -----------------------------

@app.get("/employees", response_model=List[schemas.EmployeeOut])
def get_employees(
    db: Session = Depends(get_db)
):
    return crud.get_employees(db)


# -----------------------------
# GET SINGLE EMPLOYEE
# -----------------------------

@app.get("/employee/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(db, emp_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


# -----------------------------
# UPDATE EMPLOYEE
# -----------------------------

@app.put("/employee/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(
    emp_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    db_employee = crud.update_employee(
        db,
        emp_id,
        employee
    )

    if db_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return db_employee


# -----------------------------
# DELETE EMPLOYEE
# -----------------------------

@app.delete("/employee/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.delete_employee(db, emp_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {
        "message": "Employee deleted successfully",
        "employee": employee
    }