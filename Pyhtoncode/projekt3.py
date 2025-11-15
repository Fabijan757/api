import requests
import mysql.connector


url = "https://api.tvmaze.com/shows"
response = requests.get(url)
data = response.json()   


shows_100 = data[:100]

rows = []

for show in shows_100:
    show_id = show.get("id")
    name = show.get("name")
    language = show.get("language")
    
    
    rating_block = show.get("rating") or {}
    rating = rating_block.get("average")
    
 
    genres_list = show.get("genres", [])
    genres = ", ".join(genres_list)

    rows.append((show_id, name, rating, genres, language))


conn = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="NovaLozinka",   
    database="test_baza"      
)

cursor = conn.cursor()


sql = """
INSERT INTO tv_shows (id, name, rating, genres, language)
VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    rating = VALUES(rating),
    genres = VALUES(genres),
    language = VALUES(language);
"""

cursor.executemany(sql, rows)
conn.commit()

print("Gotovo! 100 serija je spremljeno u MySQL.")

cursor.close()
conn.close()
