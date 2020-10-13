
import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()

    fileList = ('information.docx','Hello.txt','myImage.png',\
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    for entry in fileList:
        if entry.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)",  (entry,)) 
            print(entry)
    conn.commit()
conn.close()
