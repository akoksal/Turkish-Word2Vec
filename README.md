# Turkish Pre-trained Word2Vec Model
(Turkish version is below. / Türkçe için aşağıya bakın.)

This tutorial includes how to train word2vec model for Turkish language from Wikipedia dump. This code is written in Python 3 by using [gensim](https://radimrehurek.com/gensim/) library. Turkish is an agglutinative language and there are many words with the same lemma and different suffixes in the wikipedia corpus. I will write Turkish lemmatizer to increase quality of the model.

## Prerequisites
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Gensim](https://radimrehurek.com/gensim/install.html)

## Getting the Corpus
We need to have big corpus to train word2vec model. You can access all wikipedia articles written in Turkish language from [wikimedia dumps](https://dumps.wikimedia.org/trwiki/). The available one is 20180101 for this day and you can download all articles until 01/01/2018 by this link, [20180101](https://dumps.wikimedia.org/trwiki/20180101/trwiki-20180101-pages-articles.xml.bz2). Of course, you can use another corpus to train word2vec model but you must modify your corpus to train a model with gensim library, explained below.

## Preprocessing the Corpus
To train word2vec model with gensim library, you need to put each document into a line without punctuations. So, the output file should include all articles and each article should be in a line. Gensim library provides methods to do this preprocessing step. However, tokenize function is modified for Turkish language. You can run preprocess.py to modify your wikipedia dump corpus. It takes two arguments. First one is the path to the wikipedia dump(without extracting). Second one is the path to the output file. For example:
'''
preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt
'''
<br />
<br />
<br />
<br />
<br />
# Eğitilmiş Türkçe Word2Vec Modeli
Bu çalışma Wikipedia'daki Türkçe makalelerden Türkçe word2vec modelinin nasıl çıkarılabileceğini anlatmak için yapılmıştır. Kod [gensim](https://radimrehurek.com/gensim/) kütüphanesi kullanılarak Python 3 ile yazılmıştır. Gelecek zamanlarda, Türkçe "lemmatization" algoritmasıyla aynı kök ve yapım ekleri fakat farklı çekim eklerine sahip kelimelerin aynı kelimeye işaret etmesi sağlanarak modelin kalitesi arttırılacaktır.

## Gereksinimler
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Gensim](https://radimrehurek.com/gensim/install.html)

## Korpusu Edinmek
Word2vec modellerini eğitmek için büyük korpuslara ihtiyaç duyuluyor. Açık kaynaklı bir örnek olarak, Türkçe dilinde yazılmış tüm wikipedia makalelerine [buradan](https://dumps.wikimedia.org/trwiki/) ulaşabilirsiniz. Şu anda yayınlanmış olan 20180101 adlı korpus ve [bu link](https://dumps.wikimedia.org/trwiki/20180101/trwiki-20180101-pages-articles.xml.bz2) üzerinden indirebilirsiniz. Tabii ki başka bir korpus da kullanabilirsiniz fakat gensim ile eğitebilmek için korpusunuz aşağıda belirtildiği gibi düzenlemelisiniz.

## Korpusu Düzenlemek
Gensim kütüphanesi ile word2vec modeli eğitebilmek için korpusunuzu belli bir şekilde düzenlemeniz gerekmektedir. Her bir makale, noktalama işaretlerinden ayıklanmış bir şekilde, bir satıra yazılmalıdır. Her bir satırda bir adet makale bulunacak şekilde bir dosyaya yazılmalıdır. Gensim kütüphanesi wikipedia korpusuna özel olarak bazı metodlar sunuyor. Yine de Türkçe dili için ayırıcı(tokenizer) fonksiyonu düzenlenmiştir. preprocess.py dosyasını çalıştırarak kendi wikipedia korpusunuzu düzenleyebilirsiniz. Bu python kodu iki tane argüman alıyor. İlki, wikipedia korpusunuzun dosya yolu(wikipedia korpusunuzu ayıklamadan). İkinci argüman ise çıktı dosyanızın yolu olacak. Örneğin:
'''
preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt
'''
