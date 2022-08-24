import sqlite3
class Database:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()





        def new_table(self,urun):
            self.cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,Tarih TEXT,Fiyat TEXT,Miktar TEXT)".format(urun.upper()))
            self.connection.commit()
        def add_data(self,table_name,tarih,fiyat,miktar):
            self.cursor.execute("Insert into {} (Tarih,Fiyat,Miktar)  Values(?,?,?)".format(table_name),(tarih,fiyat,miktar))
            self.connection.commit()
        def add_table_name(self,table_name):
            table_names = self.get_data("tableListExecutionInfo01")
            element_list = []

            for i in table_names:
                element_list.append(i[0])
            if table_name in element_list:
                pass
            else:
                self.cursor.execute("Insert into tableListExecutionInfo01 Values(?)", (str(table_name).upper(),))
                self.connection.commit()
        def update_data(self,table,task):
            sql = ''' UPDATE {}
              SET Tarih = ? ,
                  Fiyat = ? ,
                  Miktar = ?
              WHERE id = ?'''.format(table)
            self.cursor.execute(sql,task)
            self.connection.commit()


        def get_data(self,table):
            self.cursor.execute("Select * from {}".format(table))
            data_ = self.cursor.fetchall()
            return data_

        def get_data_by_id(self,table_name,id):
            self.cursor.execute("SELECT * FROM {} WHERE id = {}".format(table_name,str(id+1)))
            self.connection.commit()
            data = self.cursor.fetchall()
            return data


        def rows_count(self,table_name):
            query = "SELECT COUNT(*) FROM {}".format(table_name)
            self.cursor.execute(query)
            count = self.cursor.fetchall()
            count_ = count[0][0]
            return count_

        def delete_data(self,data):
            self.cursor.execute("DELETE FROM tableListExecutionInfo01 WHERE TABLE_NAMES = ?;",(data,))
            self.connection.commit()
        def delete_table(self,table_name):
            self.cursor.execute("DROP TABLE {}".format(table_name))
            self.connection.commit()
        def averager(self,urun):
            self.cursor.execute("Select Fiyat from {}".format(urun).upper())
            price_data = self.cursor.fetchall()
            self.cursor.execute("Select Miktar from {}".format(urun).upper())
            quantity_data = self.cursor.fetchall()

            quantity = 0
            total = 0
            for i,j in zip(price_data,quantity_data):
                total +=float(i[0])*float(j[0])
            for j in quantity_data:
                quantity += int(j[0])

            return total/quantity

        def quantity_retriever(self,urun):
                self.cursor.execute("Select Fiyat from {}".format(urun).upper())
                price_data = self.cursor.fetchall()
                self.cursor.execute("Select Miktar from {}".format(urun).upper())
                quantity_data = self.cursor.fetchall()
                total = 0
                for i, j in zip(price_data, quantity_data):
                    total += float(i[0]) * float(j[0])
                return total










