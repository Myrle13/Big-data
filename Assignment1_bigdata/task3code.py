from mrjob.job import MRJob
import re

WORD_RE= re.compile(r"[\w']+")
lo = 'bio_location'
au = 'Australia'

class MRMostUsedWord(MRJob):

    def mapper(self,_,line):
        for word in WORD_RE.findall(line):
            if word != lo and word != au:
               yield(word.lower(),1)


    def reducer(self,word,counts):
        yield word,sum(counts)


if __name__=='__main__':
   MRMostUsedWord.run()
