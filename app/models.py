from datetime import date
from decimal import Decimal

from sqlmodel import SQLModel, Field

from settings import DB_URL


class EmployeeBase(SQLModel):
    name: str
    born: date
    salary: Decimal


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
