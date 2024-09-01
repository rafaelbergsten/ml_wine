from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests
from flasgger import Swagger
from dotenv import load_dotenv
import os

app = Flask(__name__)
swagger = Swagger(app)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

def fetch_data_from_embrapa(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Endpoint para dados de Produção
@app.route('/api/producao', methods=['GET'])
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
    url = os.getenv('EMBRAPA_URL_PRODUCAO')
    data = fetch_data_from_embrapa(url)
    return jsonify({"data": data})

# Endpoint para dados de Processamento
@app.route('/api/processamento', methods=['GET'])
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
    url = os.getenv('EMBRAPA_URL_PROCESSAMENTO')
    data = fetch_data_from_embrapa(url)
    return jsonify({"data": data})

# Endpoint para dados de Comercialização
@app.route('/api/comercializacao', methods=['GET'])
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
    url = os.getenv('EMBRAPA_URL_COMERCIALIZACAO')
    data = fetch_data_from_embrapa(url)
    return jsonify({"data": data})

# Endpoint para dados de Importação
@app.route('/api/importacao', methods=['GET'])
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
    url = os.getenv('EMBRAPA_URL_IMPORTACAO')
    data = fetch_data_from_embrapa(url)
    return jsonify({"data": data})

# Endpoint para dados de Exportação
@app.route('/api/exportacao', methods=['GET'])
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
    url = os.getenv('EMBRAPA_URL_EXPORTACAO')
    data = fetch_data_from_embrapa(url)
    return jsonify({"data": data})

if __name__ == '__main__':
    app.run(debug=True)