from app.config.common import Flask
from app.db.conectiondb import getConnection 
from app.views import userRegister

def create_app():
    app = Flask (__name__)

    getConnection(app)

    app.register_blueprint(userRegister.bp)

    return app