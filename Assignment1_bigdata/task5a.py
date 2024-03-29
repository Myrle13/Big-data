from mrjob.job import MRJob
class MRWordCount(MRJob):
    def mapper(self, _, line):
        yield "words", len(line.split()) # count num of words
    def reducer(self, key, values):
        yield key, sum(values)

if _name_ == '_main_':
MRWordCount.run() 