from flask import Flask

from blueprints import qa_bp, user_bp, test_bp
from config import flask_config

app = Flask(__name__)
app.config.from_object(flask_config)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9100, debug=True)
