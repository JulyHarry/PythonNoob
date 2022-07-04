from flask import Flask

import config
from blueprints import qa_bp
from blueprints import user_bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9100, debug=True)
