from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.contact_routes import contact_bp
from routes.sos_routes import sos_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(contact_bp, url_prefix="/api")
app.register_blueprint(sos_bp, url_prefix="/api")

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host='192.168.1.76', port=5000, debug=True)
    app.run(host='192.168.1.76', port=5000, debug=True)