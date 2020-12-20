db={
    'user':'root',
    'password':'mysql',
    'host':'192.168.0.5',
    'port':'3306',
    'database':'miniter'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"