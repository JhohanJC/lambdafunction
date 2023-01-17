import json
import os 
import mercadopago
def lambda_handler(event, context):
    # TODO implement
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    bodyGet = json.loads(event["body"])
    preference_data = {
        "items": bodyGet["items"]
    }
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Headers' : 'Content-Type',
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods' : 'OPTIONS, POST, GET',
        },
        'body': json.dumps(preference),
    }
