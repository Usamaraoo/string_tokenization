from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
from nltk.corpus import webtext

import psycopg2

connection = psycopg2.connect(host='localhost', user='postgres', password='root', port=5432, database='fulfillments')
cursor = connection.cursor()

# textWords = [w.lower() for w in webtext.words('grail.txt')]  # txt file to ise
strng = 'Suit #15,3rd Flr.,Shan Arcade,Civic Centre,New Garden Town'
text_words = strng.split(',')
textWords = strng.split(',')
finder = TrigramCollocationFinder.from_words(textWords)
tri = finder.nbest(TrigramAssocMeasures.likelihood_ratio, 3)

# On trigram
# for word in tri:
#     print('To Search', word[0] + word[1], word[2])
#     cursor.execute(f"""
#       SELECT name , similarity(name, $${word[0] + word[1], word[2]}$$) AS sml
#         FROM public.app_administrativearea where p_name='Lahore'
#         ORDER BY sml DESC,name;
#     """)
#     record = cursor.fetchone()
#     to_process = record if record[1] > 0.1 else None
#     print('result',to_process)

# On single word
# for word in tri:
#     for single_world in word:
#         print('word to search', single_world)
#         cursor.execute(f"""
#         SELECT name , similarity(name, '{single_world}') AS sml
#         FROM public.app_administrativearea where p_name='Lahore'
#         ORDER BY sml DESC,name;
#         """)
#         record = cursor.fetchone()
#         to_process = record if record[1] > 0.2 else None
#         print('result', to_process)

# closing cur and con
cursor.close()
connection.close()
