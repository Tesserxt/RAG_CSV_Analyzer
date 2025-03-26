import uvicorn
from csv_query_api import CSVQueryAPI

api = CSVQueryAPI()
app = api.app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
