#import MR Job
from mrjob.job import MRJob

#create class
class Bacon_count(MRJob):

    def mapper(self, _, line):

        for word in line.split():
            if word.lower() == "thou":
                yield "thou", 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Bacon_count.run()
