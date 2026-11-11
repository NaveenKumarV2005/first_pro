
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Python Calculator API",
    description="Dockerized calculator application",
    version="1.0.0"
)

class Calculation(BaseModel):
    num1: float
    num2: float
    operation: str

@app.get("/")
def home():
    return {
        "message": "Python Calculator API is running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/calculate")
def calculate(data: Calculation):

    a = data.num1
    b = data.num2
    operation = data.operation.lower()

    logger.info(
        "Calculation request: %s %s %s",
        a, operation, b
    )

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = a / b

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation"
        )

    logger.info("Calculation result: %s", result)

    return {
        "num1": a,
        "num2": b,
        "operation": operation,
        "result": result
    }
