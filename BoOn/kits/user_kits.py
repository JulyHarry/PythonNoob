from typing import Any

from .common import get_db_connection

ERROR_TIP_USER = "用户名已存在，请更改用户名后重新注册！"
ERROR_TIP_EMAIL = "邮箱已存在，请更改邮箱后重新注册，或使用该邮箱直接登录！"
ERROR_CODE_USER = "01"
ERROR_CODE_EMAIL = "02"
SUCCESS_FLAG = "PASS"


def create_user(info: tuple):
    not_exists_email = not_exists_info(email=info[0], username='')
    if not_exists_email == ERROR_CODE_EMAIL:
        return ERROR_TIP_EMAIL

    not_exists_user = not_exists_info(username=info[1], email='')
    if not_exists_user == ERROR_CODE_USER:
        return ERROR_TIP_USER

    sql = "insert into user_info (email, username, nickname, password, registertime) value (%s, %s, %s, %s, curtime())"
    con, cursor = get_db_connection()
    cursor.execute(sql, info)
    con.commit()
    cursor.close()
    con.close()
    return "over"


def not_exists_info(**info: Any) -> str:
    con, cursor = get_db_connection()
    if info['username']:
        sql = "select 1 from user_info where username = %s"
        cursor.execute(sql, (info['username'],))
        cnt = cursor.fetchone()
        if cnt:
            return ERROR_CODE_USER
    if info['email']:
        sql = "select 1 from user_info where email = %s"
        cursor.execute(sql, (info['email'],))
        cnt = cursor.fetchone()
        if cnt:
            return ERROR_CODE_EMAIL
    cursor.close()
    con.close()
    return SUCCESS_FLAG
