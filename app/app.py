import logging
from decimal import Decimal
from typing import Annotated, Any

from fastapi import FastAPI, HTTPException, Request, Depends
from prometheus_client import Counter, make_asgi_app
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db import get_session
from models import Employee, EmployeeCreate


# TODO this is a quick and dirty solution
logger = logging.getLogger('uvicorn.error')

# Some Prometheus metrics
REQUESTS = Counter("http_requests_success", "Successful HTTP requests")
INSERTS_ALL =Counter("insert_requests_all", "All insert requests")
INSERTS_SUCC = Counter("insert_requests_success", "Successful insert requests")
QUERY_ALL =Counter("query_requests_all", "All query requests")
QUERY_SUCC = Counter("query_requests_success", "Successful query requests")

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/employees")
async def insert(request: EmployeeCreate, session: AsyncSession=Depends(get_session)):
    employee = Employee(**dict(request))
    logger.info(f"insert: {request} {employee}")
    try:
        session.add(employee)
        await session.commit()
        await session.refresh(employee)
    finally:
        INSERTS_ALL.inc()
    INSERTS_SUCC.inc()
    return {"status": "ok"}


@app.get("/employees_by_salary")
async def get_by_salary(min_salary: Decimal=None, max_salary: Decimal=None, session: AsyncSession=Depends(get_session)):
    try:
        if min_salary is None and max_salary is None:
            raise HTTPException(status_code=400, detail="At least one of: min_salary, max_salary is required")
        query = select(Employee)
        if min_salary is not None:
            query = query.filter(Employee.salary >= min_salary)
        if max_salary is not None:
            query = query.filter(Employee.salary <= max_salary)
        result = await session.exec(query)
        QUERY_SUCC.inc()
        return {"result": result.all()}
    finally:
        QUERY_ALL.inc()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.middleware("http")
async def request_counter(request: Request, call_next):
    REQUESTS.inc()
    return await call_next(request)
