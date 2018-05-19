from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import nltk
import math
import re
import os
import redis

def index(word_dic):
    for i in range(0, 75):
        path = './WEBPAGES/WEBPAGES_RAW/' + str(i)
        for loc in os.listdir(path):
            print(path + "/" + loc)
            html_doc = open(path + "/" + loc ,"r")
            html_content = html_doc.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
            viewable_text = soup.getText()
            
            words = word_tokenize(viewable_text)
            tokenize(words, word_dic, i, loc)
    for i in word_dic.values():
        for j in i:
            j[3] = math.log10((5 * 500) / len(i)) * j[3]
                    

def tokenize(words, word_dic, i, j):
    mini_word_dic = defaultdict(list)
    for w in words:
        temp = ps.stem(w.lower())
        if temp not in mini_word_dic:
            mini_word_dic[temp].append([i, j, 1])
            
        else:
            mini_word_dic[temp][0][2] = mini_word_dic[temp][0][2] + 1
    tf(words, mini_word_dic)
    for key, values in mini_word_dic.iteritems():
        if key not in word_dic:
            word_dic[key] = values
        else:
            word_dic[key].append(values[0])
    
            
def tf(words, mini_word_dic):
    for key, values in mini_word_dic.iteritems():
        
        values[0].append(float(values[0][1])/len(words))

r = redis.Redis(
    host="search-engine-redis.lbhnyx.ng.0001.usw1.cache.amazonaws.com",
    port=6379)


word_dic = defaultdict(list)       
ps = PorterStemmer()
index(word_dic)
for key, value in word_dic.iteritems():
    string = ""
    for i in value:
        for j in i:
            string = string + (str(j) + "|")
            
        string = string + "|"
    r.set(key, string)








