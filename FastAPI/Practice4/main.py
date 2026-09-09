from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from ai_service import stream_ai

app = FastAPI()

@app.get("/stream", response_class=StreamingResponse)
def stream(text: str):
    return StreamingResponse(
        stream_ai(text),
        media_type="text/plain"
    )