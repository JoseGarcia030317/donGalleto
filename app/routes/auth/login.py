from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['POST'])
def login():
    """Login para los usuarios
    ---
    responses:
      200:
        description: Login exitoso
      401:
        description: Usuario o contraseña inválido
    """
    return jsonify({"message": "Login successful"})