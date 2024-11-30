import os


class Config:
    SECRET_KEY =  "" #os.getenv("SECRET_KEY", "my_secret_key")   Llave secreta para JWT
    JWT_SECRET_KEY = "" # os.getenv("JWT_SECRET_KEY", "my_jwt_secret_key")
    DEBUG = True
    # Puedes agregar más configuraciones aquí según las necesites
    #
    #
    #
    #
    #