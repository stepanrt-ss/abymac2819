import pymysql

host = "93.93.207.69"
user = "gen_user"
password = "SvF49R?Jivn@(b"
db_name = "default_db"
con = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor)
