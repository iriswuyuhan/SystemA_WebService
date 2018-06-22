import pymssql

class Connection:
    def __init__(self):
        self.conn_host='DESKTOP-RTM81OG'
        self.conn_db='departmenta'
        self._connect_()

    def _connect_(self):
        self.conn=pymssql.connect(server=self.conn_host,database=self.conn_db)
        self.cursor=self.conn.cursor()

    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self,sql):
        self.cursor.execute(sql)
        self._commit_()

    def _commit_(self):
        self.conn.commit()

    def close(self):
        self.conn.close()