import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def generate_jwt_token(subject, secret_key, algorithm="HS256"):
    payload = {"sub": subject}
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

def main():
    secret_key = os.getenv('JWT_SECRET_KEY')
    if not secret_key:
        raise ValueError("A chave secreta JWT_SECRET_KEY não está definida nas variáveis de ambiente.")

    subject = "techchallenge"
    token = generate_jwt_token(subject, secret_key)

    print(f"Token JWT gerado: {token}")

if __name__ == "__main__":
    main()