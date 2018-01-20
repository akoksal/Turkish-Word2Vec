from __future__ import print_function
import logging
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':

	if len(sys.argv) < 3:
		print("Please provide two arguments, first one is path to the revised corpus, second one is path to the output file for model")
		print("Example command: python3 word2vec.py wiki.tr.txt trmodel")
		sys.exit()

	
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

	model = Word2Vec(LineSentence(inputFile), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
	model.save(outputFile)