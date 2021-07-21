from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

import pandas as pd

import psycopg2

df = pd.read_csv('final.csv')
address = list(df['pickup'])

connection = psycopg2.connect(host='localhost', user='postgres', password='root', port=5432, database='fulfillments')
cursor = connection.cursor()
#
# ignored_word = set(stopwords.words('english'))  # words to ignore
# strng = '27/6, floor Mehmood Mkt,Old Anarkli, defence'
results = []


def bi_gram(adrs):
    text_words = adrs.split(',')
    finder = BigramCollocationFinder.from_words(text_words)
    # filterStop = lambda w: len(w) < 3 or w in ignored_word or w in ['Road', 'building',
    #                                                                 'floor']  # adding more filtering rull
    # finder.apply_word_filter(filterStop)
    Bigram = finder.nbest(BigramAssocMeasures.likelihood_ratio, 5)
    print('Bigram', Bigram)
    # On whole Bigram
    for i in Bigram:
        print('for search', i[0] + i[1])
        cursor.execute(f"""
        SELECT name , similarity(name, $${i[0]} {i[1]}$$ ) AS sml
        FROM public.app_administrativearea where p_name='Lahore'
        ORDER BY sml DESC,name;
        """)
        record = cursor.fetchone()
        results.append(record)

    print('record', record)
    sim = results[0]
    for no, i in enumerate(results):
        if results[no][1] > sim[1]:
            sim = results[no]
    print('this is hight sim', sim)

    # On each word
    # for bigrm in rslt:
    #     for word in bigrm:
    #         print('word to search', word)
    #         cursor.execute(f"""
    #         SELECT name , similarity(name, '{word}') AS sml
    #         FROM public.app_administrativearea where p_name='Lahore'
    #         ORDER BY sml DESC,name;"""
    #                        )
    #         record = cursor.fetchone()
    #         to_process = record if record[1] > 0.3 else ''
    #         print('result', to_process)


# for no, i in enumerate(address):
#     print(no, 'Address', i)
#     bi_gram(i)
# closing cur and con


bi_gram('Gulberg Centre,10-S 84/D/1,Main Boulevard,Gulberg-III')
cursor.close()
connection.close()