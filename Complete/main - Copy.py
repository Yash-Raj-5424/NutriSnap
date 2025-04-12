# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# import shutil
# import uuid
# import os
# from analyze import analyze_food_image  # Your existing function in a separate file
# import pandas as pd

# app = FastAPI()

# # Allow frontend (CORS)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # or specify your frontend domain
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.post("/analyze")
# async def analyze_image(file: UploadFile = File(...)):
#     filename = f"{uuid.uuid4()}.jpg"
#     file_path = os.path.join(UPLOAD_FOLDER, filename)
    
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
    
#     df = analyze_food_image(file_path)

#     if df.empty:
#         return JSONResponse(content={"error": "Could not identify food"}, status_code=400)
    
#     return df.to_dict(orient="records")
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Test: Check if it's an image file
        if file.content_type.startswith("image/"):
            # Do your image analysis logic here...
            return {
                "filename": file.filename,
                "message": "Image received and processed successfully"
            }
        else:
            raise HTTPException(status_code=400, detail="Uploaded file is not an image")

    except Exception as e:
        print("Error during analysis:", e)  # <-- See this in terminal
        raise HTTPException(status_code=500, detail="Failed to analyze image")
