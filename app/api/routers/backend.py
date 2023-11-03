from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.backend import service_backend

router = APIRouter()
#TODO: poner el bucket name como variable de ambiente
@router.post("/upload-file/")
async def upload_file_to_gcs( event_id: str, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        filename = file.filename
        ruta = f"{event_id}/{filename}"
        success = await service_backend.upload_blob_async("teatro-files", ruta, contents)
        if success:
            return {"message": "File uploaded successfully."}
        else:
            return {"message": "Failed to upload the file."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))