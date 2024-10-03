from app.config.common import MySQL, Flask 

mysql = MySQL()
    
def getConnection(app):
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='Anderson'
    app.config['MYSQL_PASSWORD']='1000540347db'
    app.config['MYSQL_DB']='papeleria_creativa'
    app.config['MYSQL_CURSORCLASS']='DictCursor'
    
    mysql.init_app(app)