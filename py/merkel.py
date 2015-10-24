import facebook
import requests
import json
import codecs
import datetime
from textblob_de import TextBlobDE as TextBlob
import datetime
import re

start_time = datetime.datetime.now()

access_token ="CAACEdEose0cBAOZBCAzAA5ozSbOsoFTnBUuh4LGYzyjJ1lTVSCkZByP8apvvj60Xi6kWf15kQkysmGfdWz2xTAgTGqrllF0PgC94A0VOHXgQWT5TxNaEqzQX8NqNYGd6XdRhII7hpxQLhaKsSy9hgTESqdUypGVY3f7XHokZBrYA9KgOUeKcQnNdLHLF5BatSTZC725fwwZDZD"
graph = facebook.GraphAPI(access_token)
user = "59788447049"
merkel = graph.get_object(user)
posts = graph.get_connections(merkel["id"], "posts", limit=1)
posts_data = posts["data"]
kommentare = []
max_pages = 9999999
pages = 1

for i in posts_data:
    com_page_data = i["comments"]
    while True:
        try:
            com_data = com_page_data["data"]
            for comment in com_data:
                kommentare.append(comment["message"])
                if pages >= max_pages:
                    print "max pages erreicht"
                    break
            com_page_data = requests.get(com_page_data["paging"]["next"]).json()
            pages += 1
        except KeyError:
            if "error" in com_page_data:
                print com_page_data["error"]["message"]
            break
            
#kommentare_str = ''.join(kommentare)
polarity_list =[]
for kommentar in kommentare:
    blob = TextBlob(kommentar)
    polarity_list.append(blob.sentiment)

end_time = datetime.datetime.now()
print end_time - start_time

einzelne_saetze = []
for satzsammlung in satzliste:
    for satz in satzsammlung:
        einzelne_saetze.append(satz)

pos_file = open("pos.txt", "w")
neg_file = open("neg.txt", "w")

for satz in einzelne_saetze:
    entscheidung = input(satz + "     p oder n?")
    if entscheidung == "p":
        pos_file.write(satz + "\n")
    elif entscheidung == "n":
        neg_file.write(satz + "\n")
    else:
        continue