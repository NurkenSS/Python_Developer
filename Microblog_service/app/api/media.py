from fastapi import APIRouter, File, UploadFile
from typing import List
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "uploads"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/upload_media/")
async def upload_media(files: List[UploadFile] = File(...)):
    """Загружает медиафайлы на сервер"""
    file_paths = []
    
    for file in files:
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        
        file_paths.append(file_path)
    
    return {"file_paths": file_paths}

@router.get("/media/{filename}")
async def get_media(filename: str):
    """Возвращает медиафайл по имени"""
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")
    