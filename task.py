# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:58:17 2021

@author: ALAA
"""
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

def getWord(words):
    syn=wordnet.synsets(words)[0]
    word=syn.hypernyms()
    word2=word[0].lemmas()[0].name()
    if (word2=="dog"):
        print(words + " is a dog")
    elif(word2=="cat"):
        print(words + " is a cat")
    else:
        print(words + " is not a cat or dog")
            

getWord('working_dog')
getWord('king')
getWord('domestic_cat')
getWord('poodle')
getWord('wild')
getWord('leonberg')
getWord('puppy')
getWord('dalmatian')
syn = wordnet.synsets('dog')[0]
print(syn.hyponyms())


