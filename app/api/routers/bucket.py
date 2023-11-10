from typing import List
from fastapi import APIRouter, File, UploadFile, HTTPException, Response 
from app.services.bucket import service_bucket
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from app.schemas.bucket import FileData
router = APIRouter()
@router.post("/upload-file/")
async def upload_file_to_gcs( event_id: str, file: UploadFile = File(...)):

    try:
        contents = await file.read()
        filename = file.filename
        ruta = f"{event_id}/{filename}"
        success = await service_bucket.upload_blob_async( ruta, contents)
        if success:
            print(ruta)
            return {"message": "File uploaded successfully."}
        else:
            return {"message": "Failed to upload the file."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/download-file/{file_path:path}",response_class=JSONResponse,
    response_model=FileData,)
async def download_file_from_gcs(file_path: str):
    try:
        file_data = await service_bucket.get_file_by_route(file_path)
        if file_data['file_bytes'] is not None:
            return Response(content=file_data['file_bytes'], media_type=file_data['content_type'])
        else:
            return HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@router.get("/download-folder/{folder_path:path}")
async def download_files_from_folder(folder_path: str):
    try:
        files_data = await service_bucket.download_blobs_in_folder(folder_path)
        if files_data:
            return files_data
        else:
            raise HTTPException(status_code=404, detail="No files found in the specified folder")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download-folder/{folder_path:path}")
async def download_files_from_folder(folder_path: str):
    try:
        files_data = await service_bucket.download_blobs_in_folder(folder_path)
        if files_data:

            def file_generator(files_data):
                for file_data in files_data:
                    yield file_data['file_bytes']

            return StreamingResponse(file_generator(files_data), media_type="application/octet-stream")
        else:
            raise HTTPException(status_code=404, detail="No files found in the specified folder")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))