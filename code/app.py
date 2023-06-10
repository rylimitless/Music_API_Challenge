from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
import sqlite3

conn = sqlite3.connect('Database/music.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS music
               (id TEXT PRIMARY KEY,
                title TEXT,
                artist INTEGER,
                duration INTEGER,
                genre TEXT,
                release_date TEXT
                )''')

app = FastAPI()

class Music(BaseModel):
    id:str
    title:str=Field(min_length=5)
    artist:str
    duration:int
    genre:str
    release_date:str

running_db = {}

@app.get('/')
async def ms_list():
    cur.execute('''SELECT * FROM music
    ''')

    song_list = cur.fetchall()
    if song_list== []:
        return {"Message": "No entries in the database"}
    
    for i in song_list:
        if i not in running_db:
            running_db[i[0]] = {
                'title':i[1],
                'artist':i[2],
                'duration':i[3],
                'genre':i[4],
                'release_date':i[5]
            }
    return running_db


@app.get('/music/{id}/')
async def getItem(id:str):
    cur.execute('''SELECT * FROM music
    where id=?''',(id,))
    entry = cur.fetchall()
    if not entry:
        return {"Message": "No such entry"}
    
    return {
        id:entry[0][0],
        'title':entry[0][1],
        'artist':entry[0][2],
        'duration':entry[0][3],
        'genre':entry[0][4],
        'release_date':entry[0][5]
        }      


@app.post('/music/')
async def addMusic(music:Music):
    dct = music.dict()
    cur.execute('''SELECT * FROM music where id=?''',(dct['id'],))
    song_list = cur.fetchall()
    if song_list != []:
        return {"Message": "Already exists"}
    
    cur.execute('''INSERT INTO music VALUES(?,?,?,?,?,?)''',\
                (dct['id'],dct['title'],dct['artist'],dct['duration'],\
                 dct['genre'],dct['release_date']))
    conn.commit()
    return {"msg": "Added successfully"}

if __name__ == "__main__":
    uvicorn.run(app)
