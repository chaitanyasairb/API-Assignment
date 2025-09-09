from typing import Optional, List
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="String to Characters")

# ✅ Allow frontend (index.html) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development, allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextIn(BaseModel):
    text: str

@app.post("/chars", response_model=Optional[List[str]])
def string_to_chars(payload: TextIn) -> Optional[List[str]]:
    s = payload.text
    if len(s) == 0:
        return None
    return list(s)

@app.post("/chars/file", response_model=Optional[List[str]])
async def string_to_chars_file(file: UploadFile = File(...)):
    content = await file.read()
    s = content.decode("utf-8").strip()
    if len(s) == 0:
        return None
    return list(s)
