from flask import Flask

from web.apps import about_bp, cookies_bp, delete_bp, edit_bp, error_bp, hello_bp, index_bp, login_bp, new_bp, post_bp, \
    session_bp
from web.config import flask_config

app = Flask(__name__)
app.config.from_object(flask_config)
app.register_blueprint(about_bp)
app.register_blueprint(cookies_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(error_bp)
app.register_blueprint(hello_bp)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(new_bp)
app.register_blueprint(post_bp)
app.register_blueprint(session_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
