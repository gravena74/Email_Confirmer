import uuid
from typing import Dict
from src.models.repository.email_registry import registry_email
from src.models.setting.db_connection import db_connection_handler


db_connection_handler.connect()
email_id = str(uuid.uuid4())


class EmailsCreator:
    def __init__(self, conn) -> None:
        self.__conn = conn

    def repository_registry_email(self, body: Dict) -> Dict:
        try:
            emails_info = {
            "id": email_id,
            "owner_name": body["owner_name"],
            "owner_email": body["owner_email"],
            "phase": body["phase"],
            "status": "0"
            }

            registry_email(emails_info)
            
            return {
                    "body": {"activityId": id},
                    "status_code": 201
                }
        
        except Exception as exception:
            return{
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

