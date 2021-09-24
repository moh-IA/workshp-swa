import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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
    tasks=[
        {
            "id": 1,
            "label": "🍔 Eat",
            "status": ""
        },
        {
            "id": 2,
            "label": "🛏 Sleep",
            "status": ""
        },
        {
            "id": 3,
            "label": "</> Code",
            "status": ""
        }
    ]
    return func.HttpResponse(json.dumps(tasks), status_code=200)

