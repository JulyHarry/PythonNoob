import configparser

import pymysql.cursors
from flask import Flask, render_template, request, url_for, flash, redirect
from pymysql import connect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Fighting!!!!!!!!'


def get_mysql_info():
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    object = 'MYSQL-INFO'
    dict = {"user": cf.get(object, "user"), "password": cf.get(object, "password"), "host": cf.get(object, "host"),
            "port": cf.get(object, "port"), "database": cf.get(object, "database")}
    return dict


# 创建一个函数用来获取数据库链接
def get_db_connection():
    # 创建数据库链接到database.db文件
    item = get_mysql_info()
    con = connect(user=item['user'], password=item['password'], host=item['host'], port=int(item['port']),
                  database=item['database'], cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    return con, cursor


# 根据post_id从数据库中获取post
def get_post(post_id):
    con, cursor = get_db_connection()
    cursor.execute('SELECT * FROM web.content WHERE contentid = %(id)s', {'id': post_id})
    # cursor.execute('SELECT * FROM web.content WHERE contentid = %(id)s', {'id': post_id})
    post = cursor.fetchone()
    con.close()
    return post


@app.route('/')
def index():
    # 调用上面的函数，获取链接
    con, cursor = get_db_connection()
    # 查询所有数据，放到变量posts中
    cursor.execute('SELECT * FROM web.content order by modifytime desc, contentid desc')
    posts = cursor.fetchall()
    cursor.close()
    con.close()
    # 把查询出来的posts传给网页
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/posts/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('标题不能为空!')
        elif not content:
            flash('内容不能为空')
        else:
            con, cursor = get_db_connection()
            cursor.execute(
                'INSERT INTO web.content (title, content, author, createtime, modifytime) VALUES (%s, %s, %s, curtime(),curtime())',
                (title, content, 'harry'))
            con.commit()
            cursor.close()
            con.close()
            return redirect(url_for('index'))

    return render_template('new.html')


@app.route('/posts/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            con, cursor = get_db_connection()
            cursor.execute('UPDATE content SET title = %s, content = %s, modifytime = curtime() WHERE contentid = %s',
                           (title, content, id))
            con.commit()
            cursor.close()
            con.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/posts/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    con, cursor = get_db_connection()
    cursor.execute('DELETE FROM content WHERE contentid = %(id)s', {'id': id})
    con.commit()
    cursor.close()
    con.close()
    flash('"{}" 删除成功!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')