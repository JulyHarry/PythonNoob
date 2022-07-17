from flask import Flask, session, g

from BoOn.kits import get_db_connection
from blueprints import qa_bp, user_bp, test_bp
from config import flask_config

app = Flask(__name__)
app.config.from_object(flask_config)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
app.register_blueprint(test_bp)


@app.before_request
def check_login():
    account = session.get('account')
    user_info_dict = {'account': account}

    def get_user_info(user_info_dict):
        sql = "select * from user_info where username = %(account)s or email = %(account)s"
        con, cursor = get_db_connection()
        cursor.execute(sql, user_info_dict)
        res = cursor.fetchone()
        return res

    user_info = get_user_info(user_info_dict)
    if account:
        # setattr(g, 'account', account)
        g.user_info = user_info
        # print(g.get('account'), g.account)
        # print(g.user_info['username'], g.user_info['email'])


@app.context_processor
def context_processor():
    if hasattr(g, "user_info"):
        contents = {"id": g.user_info['id'],
                    "username": g.user_info['username'],
                    "email": g.user_info['email'],
                    "nickname": g.user_info['nickname']}
        return dict(userinfo=contents)
    else:
        return {}


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9100, debug=True)
