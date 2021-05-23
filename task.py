"""
Created on Sat May 22 22:58:17 2021
@author: ALAA
"""
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet


cat = 'cat.n.01'
dog = 'dog.n.01'
entity = 'entity.n.01'

def getWord(k,w):
    for ss in w:
        for hyper in ss.hypernyms():         
              if (hyper.name() == cat):
                  print(k + " is a cat")
              elif (hyper.name()==dog):
                  print(k + " is a dog")
              elif (hyper.name()==entity):
                  print(k + " is not a dog or a cat")  
              else:  
                   return getWord(k,hyper.hypernyms())

getWord('king',wordnet.synsets('king'))
getWord('working_dog',wordnet.synsets('working_dog'))
getWord('domestic_cat',wordnet.synsets('domestic_cat'))



