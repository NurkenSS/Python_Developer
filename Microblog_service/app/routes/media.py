import os
import shutil 
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse


router = APIRouter()

@router.post("/upload_media/")
async def upload_media(file: UploadFile = File(...)):
    media_dir = "media"
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)
    
    file_path = os.path.join(media_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename}

@router.get("/media/{filename}")
async def get_media(filename: str):
    file_path = os.path.join("media", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")
