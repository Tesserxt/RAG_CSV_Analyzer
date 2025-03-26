from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import uuid
from database import MongoDBHandler
from huggingface_client import HuggingFaceClient


class CSVQueryAPI:
    def __init__(self):
        self.app = FastAPI()
        self.db_handler = MongoDBHandler()
        self.hf_client = HuggingFaceClient()
        self.setup_routes()
    
    def setup_routes(self):
        self.app.get("/")(self.home)
        self.app.post("/upload")(self.upload_csv)
        self.app.get("/files")(self.list_files)
        self.app.post("/query")(self.query_csv)
        self.app.post("/query-llm")(self.query_llm)
        self.app.delete("/")(self.delete_file)
    
    async def home(self):
        return {"message": "FastAPI & Motor connected!"}
    
    async def upload_csv(self, file: UploadFile = File(...)):
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        df = pd.read_csv(file.file)
        file_id = str(uuid.uuid4())
        csv_data = df.to_dict(orient="records")
        
        await self.db_handler.insert_file(file_id, file.filename, csv_data)
        return {"file_id": file_id, "message": "Upload successful"}
    
    async def list_files(self):
        files = await self.db_handler.get_files()
        if not files:
            raise HTTPException(status_code=500, detail="Internal Server Error")
        return {"files": files}
    
    async def query_csv(self, file_id: str, query: str):
        file_data = await self.db_handler.get_file_data(file_id)
        if not file_data:
            raise HTTPException(status_code=404, detail="File not found")
        df = pd.DataFrame(file_data["data"])
        matches = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        return {"results": matches.to_dict(orient='records')}
    
    async def delete_file(self, file_id: str):
        await self.db_handler.delete_file(file_id)
        return {"message": "File deleted successfully"}
    
    async def query_llm(self, file_id: str, query: str):
        file_data = await self.db_handler.get_file_data(file_id)
        if not file_data:
            raise HTTPException(status_code=404, detail="File not found")
        df = pd.DataFrame(file_data["data"])
        csv_text = df.to_string(index=False)
        response = self.hf_client.generate_response(csv_text, query)
        return {"response": response}
