from flask import Flask, jsonify
from config import Config
from flask_cors import CORS
from flasgger import Swagger

# Importar los blueprints de las nuevas ubicaciones
from routes.auth.login import auth

# Crear instancia de Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar Swagger para la documentación
swagger = Swagger(app)

# Activar CORS
CORS(app)

# Registrar los blueprints
app.register_blueprint(auth, url_prefix='/api')

# Manejo de errores personalizados
@app.errorhandler(404)
def not_found(error):
    return jsonify({"code": 404, "error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"code": 500, "error": "Internal server error"}), 500

# Comentario de prueba para hacer commit

# Ejecutar la aplicación localmente
if __name__ == '__main__':
    app.run(port=5000)
