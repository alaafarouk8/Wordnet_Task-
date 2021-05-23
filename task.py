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
    for syn in w:
        for hyper in syn.hypernyms(): 
              if (hyper.name() == cat):
                  return k + " is a cat"
              elif (hyper.name()==dog):
                  return k + " is a dog"
              else:
                   for i in hyper.hypernyms():
                       if (i.name() == cat):
                           return k + " is a cat"
                       elif (i.name()==dog):
                           return k + " is a dog"
                       
    return k + " is not a dog or a cat" 
    
   
w = input("enter word: ")
a = wordnet.synsets(w)  
print (getWord(w, a))  

     

"""
getWord('working_dog','working_dog')
getWord('domestic_cat','domestic_cat')
getWord('wildcat','wildcat')

"""
