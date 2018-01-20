from __future__ import print_function
import os.path
import sys
from gensim.corpora import WikiCorpus
import warnings
import logging


if __name__ == '__main__':
	

	if len(sys.argv) < 3:
		print("Please provide two arguments, first one is path to the wikipedia dump, second one is path to the output file")
		print("Example command: python3 preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt")
		sys.exit()
	
	logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

	
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	
	wiki = WikiCorpus(inputFile, lemmatize=False, dictionary={})
	logging.info("Wikipedia dump is opened.")
	output = open(outputFile,"w",encoding="utf-8")
	logging.info("Output file is opened.")

	i = 0
	for text in wiki.get_texts():
		output.write(str(b" ".join(text), "utf-8")+"\n")
		i+=1
		if (i % 10000 == 0):
			logging.info("Saved " + str(i) + " articles.")
		

	output.close()
