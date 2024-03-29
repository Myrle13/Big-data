from mrjob.job import MRJob
import re

WORD_RE= re.compile(r"[\w']+")

h = 'health'

class MRCountHealth(MRJob):

    def mapper(self,_,line):
        for word in WORD_RE.findall(line):
           if word == h:
              yield word,1



    def reducer(self,word,counts):
        yield word,sum(counts)

if _name__=='__main_':
   MRCountHealth.run()