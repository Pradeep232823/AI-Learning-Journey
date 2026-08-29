from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import FastAPI.Project4_FastAPI_Basics.calculator as calculator

app = FastAPI()

class CalculateRequest(BaseModel):
    operation : str
    a: float
    b: float | None = None

@app.post("/calculate")
def calculate_request(request : CalculateRequest):

    requires_b = ["add", "subtract", "multiply", "divide", "power", "percentage"]
    
    if request.operation in requires_b and request.b is None:
        raise HTTPException(
            status_code=400,
            detail=f"The '{request.operation}' operation requires a 'b' value."
        )
        
    if request.operation in ["divide", "percentage"] and request.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide or calculate percentage by zero."
        )
    
    total = 0

    match request.operation:
        case "add":
            total = calculator.add(request.a, request.b)
        case "subtract":
            total = calculator.subtract(request.a, request.b)
        case "multiply":
            total = calculator.multiply(request.a, request.b)
        case "divide":
            total = calculator.divide(request.a, request.b)
        case "power":
            total = calculator.power(request.a, request.b)
        case "percentage":
            total = calculator.percentage(request.a, request.b)
        case "square_root":
            if request.a < 0:
                raise HTTPException(
                    status_code=400,
                    detail="Cannot calculate the square root of a negative number."
                )
            total = calculator.square_root(request.a)
        case _:
            raise HTTPException(
                status_code=400,
                detail="Invalid operation"
            )
    return {"operation" : request.operation, "result" : total}