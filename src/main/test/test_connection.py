from typing import Dict

def test_connection() -> Dict:
    try:
        return{
            "body": "Parabens",
            "status_code": 201
        }
    
    except Exception as exception:
        return{
            "body": {"error": "Bad request", "message": str(exception)},
            "status_code": 400
        } 
    

def test_connection_home():
    try:
        return{
            "body": "Parabens dev",
            "status_code": 201
        }

    except Exception as exception:
        return {
            "body": {"erro": "Bad request", "message": str(exception)},
            "status_code": 400
        }