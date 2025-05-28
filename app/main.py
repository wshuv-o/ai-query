from fastapi import FastAPI, UploadFile, File
from app.pdf_utils import extract_appraisal_date

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PDF Extractor is running"}

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    content = await file.read()
    result = extract_appraisal_date(content)
    return result
