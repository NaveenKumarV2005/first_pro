
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Python Calculator API",
    description="Dockerized Calculator Application",
    version="1.0.0"
)

# Frontend directory
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


# Request model
class Calculation(BaseModel):
    num1: float
    num2: float
    operation: str


# Frontend route
@app.get("/", include_in_schema=False)
def home():
    logger.info("Frontend requested")

    index_file = FRONTEND_DIR / "index.html"

    if not index_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Frontend index.html not found"
        )

    return FileResponse(index_file)


# Health check
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "Python Calculator API"
    }


# Calculator API
@app.post("/calculate")
def calculate(data: Calculation):

    a = data.num1
    b = data.num2
    operation = data.operation.lower().strip()

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
            logger.warning("Division by zero attempted")

            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )

        result = a / b

    else:
        logger.warning("Invalid operation: %s", operation)

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
