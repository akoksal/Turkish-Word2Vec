# Turkish Pre-trained Word2Vec Model
(Turkish version is below. / Türkçe için aşağıya bakın.)

This tutorial includes how to train word2vec model for Turkish language from Wikipedia dump. This code is written in Python 3 by using [gensim](https://radimrehurek.com/gensim/) library. Turkish is an agglutinative language and there are many words with the same lemma and different suffixes in the wikipedia corpus. I will write Turkish lemmatizer to increase quality of the model.

## Prerequisites
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Gensim](https://radimrehurek.com/gensim/install.html)

## Getting the Corpus
We need to have big corpus to train word2vec model. You can access all wikipedia articles written in Turkish language from [wikimedia dumps](https://dumps.wikimedia.org/trwiki/). The available one is 20180101 for this day and you can download all articles until 01/01/2018 by this link, [20180101](https://dumps.wikimedia.org/trwiki/20180101/trwiki-20180101-pages-articles.xml.bz2). Of course, you can use another corpus to train word2vec model but you must modify your corpus to train a model with gensim library, explained below.

## Preprocessing the Corpus
To train word2vec model with gensim library, you need to put each document into a line without punctuations. So, the output file should include all articles and each article should be in a line. Gensim library provides methods to do this preprocessing step. You can run preprocess.py to modify your wikipedia dump corpus. It takes two arguments. First one is the path to the wikipedia dump(without extracting). Second one is the path to the output file. For example:
'''
preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt
'''


#TO-DO#
Tutorial to explain how to create word2vec model 
#TO-DO#

# Eğitilmiş Türkçe Word2Vec Modeli
Bu çalışma Wikipedia'daki Türkçe makalelerden Türkçe word2vec modelinin nasıl çıkarılabileceğini anlatmak için yapılmıştır. Kod [gensim](https://radimrehurek.com/gensim/) kütüphanesi kullanılarak Python 3 ile yazılmıştır. Gelecek zamanlarda, Türkçe "lemmatization" algoritmasıyla aynı kök ve yapım ekleri fakat farklı çekim eklerine sahip kelimelerin aynı kelimeye işaret etmesi sağlanarak modelin kalitesi arttırılacaktır.

#TO-DO#
Tutorial to explain how to create word2vec model 
#TO-DO#

#TO-DO#
Link for Pretrained Model
#TO-DO#
