import pymssql
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env")

host_db = config["HOST_db"]
user_db = config["USER_db"]
passw_db = config["PASSWORD_db"]
name_db = config["DATABASE_db"]


def connect_to_database():
    conn = pymssql.connect(
        host=host_db,
        user=user_db,
        password=passw_db,
        database=name_db,
    )
    return conn
