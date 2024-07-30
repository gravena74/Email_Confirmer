from flask import jsonify, Blueprint, request


from src.email_sender.email_sender import email_select

from src.main.test.test_connection import test_connection, test_connection_home

from src.controllers.email_creator import EmailsCreator

trips_routes_bp = Blueprint("trip_routes", __name__)

# Importando a conexão
from src.models.setting.db_connection import db_connection_handler


@trips_routes_bp.route("/register", methods=["POST"])
def registry1_email():
    conn = db_connection_handler.connect()
    controller = EmailsCreator(conn)
    controller.repository_registry_email(request.json)
    email_select()
    return test_connection_home()

    



    
    
