import psycopg2

class Connection:
    def __init__(self):
        self.con = psycopg2.connect(database="db_muERPv8p0",
                               host="localhost",
                               user="postgres",
                               password="success8085.com",
                               port=8085)

        self.cur = self.con.cursor()
        self.cur.execute("SELECT * from public.tbl_j_person")
        self.result = self.cur.fetchall()

    def execute(self, query):
        self.cur.execute(query)
        self.result = self.cur.fetchall()
        return self.result
