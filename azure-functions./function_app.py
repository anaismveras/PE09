import azure.functions as func
import logging
import datetime
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="calculate_age", methods=["POST"])
def calculate_age(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        logging.info(f"Request body: {req_body}")

        birth_year = req_body.get('birth_year')
        birth_month = req_body.get('birth_month')
        birth_day = req_body.get('birth_day')

        if not all([birth_year, birth_month, birth_day]):
            return func.HttpResponse(
                "Please provide birth_year, birth_month, and birth_day in the request body.",
                status_code=400
            )
        today = datetime.date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        response_message = f"Your age is: {age}"
        logging.info(f"Response message: {response_message}")
        return func.HttpResponse(json.dumps(response_message), status_code=200)
    except ValueError:
        return func.HttpResponse(
            "Invalid input. Please ensure birth_year, birth_month, and birth_day are integers.",
            status_code=400
        )
    