DB_HOST = "ec2-3-212-45-192.compute-1.amazonaws.com"
DB_NAME = "dfpepcvicmsta4"
DB_USER = "hwgowiqroobgjf"
DB_PASS = "51a027b9cfef25de62de2945463639ba0ab4b95cf3c2ea6c8c96c15cd48a13b8"

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)










conn.close()