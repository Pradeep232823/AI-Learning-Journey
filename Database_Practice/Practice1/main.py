from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers.students import router as student_router

app = FastAPI()

@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

app.include_router(student_router)