from fastapi import FastAPI
from mylib.sqs import *
from mylib.extracting_emails_function import *
import uvicorn
import os


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "This is a Extracting Emails API Microservice. Call using /search"
    }


@app.get("/search")
async def search():
    """This is an extracting emails microservice"""

    sqs_queue()
    result=extract()
    # print('result',result)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
