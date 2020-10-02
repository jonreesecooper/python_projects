import sqlite3

def databaseCreate():
    conn = sqlite3.connect('newfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename varchar(255) \
            )")
        conn.commit()
    conn.close()

def tableAppend():
    conn = sqlite3.connect('newfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('information.docx')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('Hello.txt')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('myImage.png')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('myMovie.mpg')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('World.txt')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('data.pdf')")
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('myPhoto.jpg')")
        conn.commit()
    conn.close()

def getData():
    conn = sqlite3.connect('newfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT col_filename FROM tbl_files WHERE col_filename LIKE "%txt"')
        varTxt = cur.fetchall()
        for item in varTxt:
            msg = "Result 1: {}\nResult 2: {}".format(item[0],item[1])
        print(msg)
    


if __name__ == "__main__":
    databaseCreate()
    tableAppend()
    getData()
