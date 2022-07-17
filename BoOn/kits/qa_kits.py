from BoOn.kits import get_db_connection


def create_question(info: dict) -> bool:
    sql = "insert into questions_info (title, content, author, publishtime, updatetime) " \
          "values " \
          "(%(title)s, %(content)s, %(author)s, curtime(), curtime())"
    con, cursor = get_db_connection()
    cursor.execute(sql, info)
    con.commit()
    cursor.close()
    con.close()


def check_primary(info: dict) -> bool:
    sql = 'select 1 from questions_info where title = %(title)s and author = %(author)s'
    con, cursor = get_db_connection()
    cursor.execute(sql, info)
    cnt = cursor.fetchone()
    if cnt:
        return True
    return False
