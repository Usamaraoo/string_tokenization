# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
#
# ex = '''18-D,Ghazi Park,Peco Road,Opp. Treet Corp.,Kot Lakhpat'''
#
#
# def preprocess(sent):
#     sent = nltk.word_tokenize(sent)
#     sent = nltk.pos_tag(sent)
#     return sent
#
#
# sent = preprocess(ex)
#
# pattern = 'NP: {<DT>?<JJ>*<NN>}'
# cp = nltk.RegexpParser(pattern)
# cs = cp.parse(sent)
# print(cs)
import nltk
from nltk.tokenize import word_tokenize
text = "Paisa Akhbar,14-Trust Bldg.,Chowk Urdu Bazar,Post Box No.1338"
tokens = nltk.word_tokenize(text)
bigrm = nltk.bigrams(tokens)
print(*map(' '.join, bigrm), sep=',')
