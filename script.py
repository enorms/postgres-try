DB_HOST = "ec2-3-229-161-70.compute-1.amazonaws.com"
DB_NAME = "d517flfe58gr3p"
DB_USER = "sheoivbahrzzrs"
DB_PASS = "e1b47aa3fd303bf9c67a57b208967cf38ef701831c849aa5e3e1410cb2a24f8d"
TABLE_NAME = "test"

import psycopg2
import datetime

"""
 [Json({'a': 100})] # Jsonb
"""




conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

created_at = dt = datetime.datetime.now()
gem_id = dt.second # placeholder
# hackernews_username

"""psycopg2.errors.UndefinedTable: relation "d517flfe58gr3p" does not exist
LINE 1: INSERT INTO d517flfe58gr3p (gem_id, hackernews_username, dis..."""
SQL = "CREATE TABLE " + TABLE_NAME
data = "(id serial PRIMARY KEY, num integer, data varchar);"
cur.execute(SQL, data)



# use %s for all
SQL = "INSERT INTO " + TABLE_NAME + "  (name) VALUES (%s);" # Note: no quotes
data = ("O'Reilly", )
cur.execute(SQL, data) # Note: no % operator

"""
cur.execute("INSERT INTO " + DB_NAME + 
    " (gem_id, hackernews_username, discord_username, wallet_address) VALUES (%s, %s, %s, %s)",
    (100, "hnid", "dis_un", "0xwallet123"))
"""


cur.execute("SELECT * FROM " + DB_NAME + ";")
cur.fetchone()







conn.close()