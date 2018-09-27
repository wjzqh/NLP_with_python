#-*- coding -*-
from nltk.corpus import brown
import nltk

def tabulate(cfdist, words, categories):
  print '%-16s' % 'Category',
  for word in words:
    print '%6s' % word,
  print
  for category in categories:
    print '%-16s' % category,
    for word in words:
      print '%6d' % cfdist[category][word],
    print

cfd = nltk.ConditionalFreqDist(
          (genre,word)
          for genre in brown.categories()
          for word in brown.words(categories=genre))

if __name__ == '__main__':
  genres = ['news','religion','hobbies','science_fiction','romance','humor']
  modals = ['can','could','may','might','must','will']
  tabulate(cfd,modals,genres)