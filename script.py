import psycopg2
import datetime


DB_HOST = "ec2-3-229-161-70.compute-1.amazonaws.com"
DB_NAME = "d517flfe58gr3p"
DB_USER = "sheoivbahrzzrs"
DB_PASS = "e1b47aa3fd303bf9c67a57b208967cf38ef701831c849aa5e3e1410cb2a24f8d"


table_name = "test"


"""
 [Json({'a': 100})] # Jsonb
"""




created_at = dt = datetime.datetime.now()
gem_id = dt.second # placeholder
# hackernews_username



class Scripts:
    def __init__(self, dbname, user, password, host):
        conn = None
        cur = None


    def connect(self):
        self.conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.cur = self.conn.cursor()


    def close(self):
        self.conn.close()


    def create_table(self, table_name):
        """psycopg2.errors.UndefinedTable: relation "d517flfe58gr3p" does not exist
        LINE 1: INSERT INTO d517flfe58gr3p (gem_id, hackernews_username, dis..."""
        self.connect()
        SQL = "CREATE TABLE " + table_name
        data = "(id serial PRIMARY KEY, num integer, data varchar);"
        self.cur.execute(SQL, data)
        self.close()


    def save_record(self):
        self.connect()
        # use %s for all
        SQL = "INSERT INTO " + TABLE_NAME + "  (name) VALUES (%s);" # Note: no quotes
        data = ("O'Reilly", )
        self.cur.execute(SQL, data)

        self.close()


    def query_record(self):
        """
        cur.execute("INSERT INTO " + DB_NAME + 
            " (gem_id, hackernews_username, discord_username, wallet_address) VALUES (%s, %s, %s, %s)",
            (100, "hnid", "dis_un", "0xwallet123"))
        """
        self.connect()
        cur.execute("SELECT * FROM " + DB_NAME + ";")
        cur.fetchone()
        self.close()














