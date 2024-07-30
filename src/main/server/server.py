from flask import Flask, request, jsonify
from src.main.routes.email_route import trips_routes_bp

app = Flask(__name__)

app.register_blueprint(trips_routes_bp)
