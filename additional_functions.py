import logging
import azure.functions as func

bp = func.Blueprint()

@bp.function_name('SecondHTTPFunction')
@bp.route(route="newroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting the second HTTP Function request.')

    name = req.params.get('name')
    if name:
        message = f"Hello, {name}, so glad this Function worked!!"
    else:
        message = "Hello, so glad this Function worked!"
    return func.HttpResponse(
        message,
        status_code=200
    )