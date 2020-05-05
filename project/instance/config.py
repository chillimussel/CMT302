"""
configuration file for the whole application
"""
DATABASE_AUTH = {
    'username':'root', # db username
    'password':'root', # db password
    'host':'localhost', # db host
    'port':'3306',# db port
    'table':{ # db table
        'name':'shopdb' # db table name
    }
}

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{table}?charset=utf8mb4'.format(
    username=DATABASE_AUTH['username'],
    password=DATABASE_AUTH['password'],
    host=DATABASE_AUTH['host'],
    port=DATABASE_AUTH['port'],
    table=DATABASE_AUTH['table']['name']
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET KEY'
