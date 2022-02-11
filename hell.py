# import gensim
# from gensim import models
# from gensim.models import Word2Vec
import timeit

# model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True) #without *norm_only* param


# print(model.similarity('woman', 'man'))
# print(model.similarity('spain', 'france'))
# print(model.similarity('school', 'book'))
# print(model.similarity('teacher', 'student'))
# print(model.similarity('music', 'viola'))

mysetup = '''
import gensim
from gensim import models
from gensim.models import Word2Vec
import timeit

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
'''
mycode = '''
model.similarity('woman', 'man')
'''
 
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))