1.安装Django
```bash
pip install django
```
2.查看Django版本
```bash
python -m django --version
```
3.新建Django项目
```bash
django-admin startproject [project name]
```
- 项目目录
```bash
idannywu/
    manage.py
    idannywu/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
4.启动服务器
```bash
python manage.py runserver            默认端口8000
python manage.py runserver 8080       绑定8080端口
python manage.py runserver 0:8000     绑定8000端口
```
5.创建app
```bash
python manage.py startapp [app name]
```
- app目录
```bash
dannny_app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```
6.创建数据库模型
```bash
python manage.py migrate
python manage.py makemigrations polls   创建数据表
python manage.py sqlmigrate polls 0001  数据迁移

```
7.API
```bash
python manage.py shell      调试
```
8.创建管理员账号
```bash
py manage.py createsuperuser
```