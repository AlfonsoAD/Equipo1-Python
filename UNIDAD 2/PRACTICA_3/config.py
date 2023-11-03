class BasicConfig:
    USER_DB='postgres'
    PASS_DB='C3m0nchi28'
    URL_DB='localhost'
    NAME_DB='practica_3'
    FULL_URL_BD=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_BD
    SQLALCHEMY_TRACK_NOTIFICATIONS=False
    SECRET_KEY = "llave"