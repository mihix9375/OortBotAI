from pathlib import Path
import sqlite3

# DataBase Variable
aiDir   = Path(__file__).parent
dbPath  = aiDir / '../data/database.sqlite' # use score, images and tasks

# DataBase Instance
conn    = sqlite3.connect(dbPath)
cur     = conn.cursor()

def WaitForImage():
    cur.execute("SELECT * FROM images WHERE ")
    print(cur.fetchall())

if __name__ == "__main__":
	WaitForImage()
