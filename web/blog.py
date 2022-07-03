from flask import Flask

from apps.about import bp as about
from apps.delete import bp as delete
from apps.edit import bp as edit
from apps.error import bp as error
from apps.hello import bp as hello
from apps.index import bp as index
from apps.new import bp as new
from apps.post import bp as post
from apps.test import bp as test

app = Flask(__name__)
app.config.from_object("flask_config")
app.register_blueprint(edit)
app.register_blueprint(post)
app.register_blueprint(about)
app.register_blueprint(delete)
app.register_blueprint(error)
app.register_blueprint(hello)
app.register_blueprint(index)
app.register_blueprint(new)
app.register_blueprint(test)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
