from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import nltk
import math

def index(word_dic):
    for i in range(0, 75):
        for j in range(0, 500):
            html_doc = open("./WEBPAGES/WEBPAGES_RAW/" + str(i) + "/" + str(j), "r")
            html_content = html_doc.read()

            soup = BeautifulSoup(html_content, 'html.parser').get_text()

            words = word_tokenize(soup)

            
            tokenize(words, word_dic, i, j)
    for i in word_dic.values():
        for j in i:
            j[2] = math.log10((5 * 500) / len(i)) * j[2]
                    

def tokenize(words, word_dic, i, j):
    mini_word_dic = defaultdict(list)
    for w in words:
        temp = ps.stem(w)
        
        if temp not in mini_word_dic:
            mini_word_dic[temp].append([[i, j], 1])
            
        else:
            mini_word_dic[temp][0][1] = mini_word_dic[temp][0][1] + 1
    tf(words, mini_word_dic)
    for key, values in mini_word_dic.iteritems():
        if key not in word_dic:
            word_dic[key] = values
        else:
            word_dic[key].append(values[0])
    
            
def tf(words, mini_word_dic):
    for key, values in mini_word_dic.iteritems():
        
        values[0].append(float(values[0][1])/len(words))

word_dic = defaultdict(list)       
ps = PorterStemmer()
index(word_dic)

##for key, values in word_dic.iteritems():
    ##if len(values) > 1:
       ##print(key + " :" + str(values))
##html_doc = open(str(4), "r")
##html_content = html_doc.read()
##
##soup = BeautifulSoup(html_content, 'html.parser').get_text()
##
##words = word_tokenize(soup)
##
##print(len(words))
##tokenize(words, word_dic)
##tf(word_dic)
##
print(word_dic)





