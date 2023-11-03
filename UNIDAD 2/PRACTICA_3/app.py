from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.autor.autores import appautor
from routes.editorial.editoriales import appeditorial
from routes.editorial.editoralesView import appeditorialesv
from routes.libro.libros import applibro
app= Flask(__name__)
app.register_blueprint(appeditorialesv)
app.register_blueprint(applibro)
app.register_blueprint(appeditorial)
app.register_blueprint(appautor)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")