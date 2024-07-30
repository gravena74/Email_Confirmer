from typing import Dict, Tuple, List
from src.models.setting.db_connection import db_connection_handler

conn = db_connection_handler.connect()

def registry_email(email_info: Dict):
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO emails_to_invite 
            (id, owner_name, owner_email, phase, status) 
            VALUES 
            (%s, %s, %s, %s, %s)
            ''',
        (
            email_info["id"], 
            email_info["owner_name"], 
            email_info["owner_email"], 
            email_info["phase"], 
            email_info["status"], 
        )
        )
    conn.commit()
    cursor.close()