"""product config"""

SECRET_KEY = '123'
DEBUG = False
SQLALCHEMY_ECHO = False

#DB
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/demo"

#Redis配置
REDIS = {
    "host": "127.0.0.1",
    "port": 6379
}
