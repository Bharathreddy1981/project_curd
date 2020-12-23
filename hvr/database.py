
import pymysql
def base():

    connect = pymysql.connect(
        host="localhost",
        user="root",
        passwd="Vangala@09",
        db="votepoll"
    )

    return connect

