import sqlite3

conn = sqlite3.connect('test3.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT, \
        col_type TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test3.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_file, col_type) VALUES (?, ?)", \
                ('Hello.txt','text'))
    cur.execute("INSERT INTO tbl_files(col_file,col_type) VALUES (?,?)", \
                ('World.txt',"text"))
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png',\
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for entry in fileList:
    if entry.endswith(".txt"):
        print(entry)
