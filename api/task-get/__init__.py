from collections import UserDict, UserList
import logging
import json
from re import T
from pymongo import MongoClient
import azure.functions as func





def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client = MongoClient("mongodb://mohamed:ji1mRUIY2iSGyYCaPcOXidzx2xhs3jSKFNSHG9rw5JCopN8I4NAVyMWsy8Uf1SWyROwsBJUteoY4epcEjad5EA%3D%3D@mohamed.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mohamed@")
    database = client["workshop-swa"]
    response = database["tasks"].find(
        {'userId': "f5182bebff11b5cde1f22e34e9d736c1"})
    tasks = []
    for task in response:
        del task['_id']
        tasks.append(task)

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    # tasks = [
    #     {
    #         "id": 1,
    #         "label": "🍔 Eat",
    #         "status": ""
    #     },
    #     {
    #         "id": 2,
    #         "label": "🛏 Sleep",
    #         "status": ""
    #     },
    #     {
    #         "id": 3,
    #         "label": "</> Code",
    #         "status": ""
    #     }
    # ]
    return func.HttpResponse(json.dumps(tasks), status_code=200)
