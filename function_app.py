import azure.functions as func
import datetime
import json
import logging
from additional_functions import bp

app = func.FunctionApp()
app.register_blueprint(bp)

@app.function_name('FirstHTTPFunction')
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Wow this first HTTP Function works!!!!",
        status_code=200
    )
