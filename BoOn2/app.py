# -*- coding: utf-8 -*-
from flask import Flask

from BoOn2.config import flask_config
from BoOn2.blueprints import ibp

app = Flask(__name__)
app.config.from_object(flask_config)
app.register_blueprint(ibp)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
