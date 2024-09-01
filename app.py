import logging
import os
from logging.handlers import RotatingFileHandler

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flasgger import Swagger
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required

app = Flask(__name__)
swagger = Swagger(app)

load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)


def extract_table_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table", {"class": "tb_base tb_dados"})
    extracted_data = []

    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]
        rows = table.find("tbody").find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            if len(cells) == len(headers):
                row_data = {
                    headers[i]: cells[i].get_text(strip=True)
                    for i in range(len(headers))
                }
                extracted_data.append(row_data)

    return extracted_data


def fetch_and_process_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        sanitized_data = extract_table_data(html_content)
        return sanitized_data
    else:
        return {"error": "Failed to retrieve data"}


if not app.debug:
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler(
        "logs/flask_app.log", maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("Application startup")


@app.route("/api/producao", methods=["GET"])
@jwt_required()
def producao():
    """
    Get production data from Embrapa.
    ---
    responses:
      200:
        description: A list of production data
        schema:
          type: object
          properties:
            data:
              type: string
              description: The data returned from Embrapa
    """
    url = os.getenv("EMBRAPA_URL_PRODUCAO")
    data = fetch_and_process_data(url)
    return jsonify({"data": data})


@app.route("/api/processamento", methods=["GET"])
@jwt_required()
def processamento():
    """
    Get processing data from Embrapa.
    ---
    responses:
      200:
        description: A list of processing data
        schema:
          type: object
          properties:
            data:
              type: string
              description: The data returned from Embrapa
    """
    url = os.getenv("EMBRAPA_URL_PROCESSAMENTO")
    data = fetch_and_process_data(url)
    return jsonify({"data": data})


@app.route("/api/comercializacao", methods=["GET"])
@jwt_required()
def comercializacao():
    """
    Get commercialization data from Embrapa.
    ---
    responses:
      200:
        description: A list of commercialization data
        schema:
          type: object
          properties:
            data:
              type: string
              description: The data returned from Embrapa
    """
    url = os.getenv("EMBRAPA_URL_COMERCIALIZACAO")
    data = fetch_and_process_data(url)
    return jsonify({"data": data})


@app.route("/api/importacao", methods=["GET"])
@jwt_required()
def importacao():
    """
    Get import data from Embrapa.
    ---
    responses:
      200:
        description: A list of import data
        schema:
          type: object
          properties:
            data:
              type: string
              description: The data returned from Embrapa
    """
    url = os.getenv("EMBRAPA_URL_IMPORTACAO")
    data = fetch_and_process_data(url)
    return jsonify({"data": data})


@app.route("/api/exportacao", methods=["GET"])
@jwt_required()
def exportacao():
    """
    Get export data from Embrapa.
    ---
    responses:
      200:
        description: A list of export data
        schema:
          type: object
          properties:
            data:
              type: string
              description: The data returned from Embrapa
    """
    url = os.getenv("EMBRAPA_URL_EXPORTACAO")
    data = fetch_and_process_data(url)
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run()
