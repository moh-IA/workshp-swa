import logging
import json
import os
from pymongo import MongoClient
import azure.functions as func



COSMOSDB_CONN_STRING = str(os.environ["ConnectionString"])
print(os.environ)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client = MongoClient(COSMOSDB_CONN_STRING)
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
