# Turkish Pre-trained Word2Vec Model
(Turkish version is below. / Türkçe için aşağıya bakın.)

This tutorial introduces how to train word2vec model for Turkish language from Wikipedia dump. This code is written in Python 3 by using [gensim](https://radimrehurek.com/gensim/) library. Turkish is an agglutinative language and there are many words with the same lemma and different suffixes in the wikipedia corpus. I will write Turkish lemmatizer to increase quality of the model.

## Prerequisites
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Gensim](https://radimrehurek.com/gensim/install.html)

## Getting the Corpus
We need to have big corpus to train word2vec model. You can access all wikipedia articles written in Turkish language from [wikimedia dumps](https://dumps.wikimedia.org/trwiki/). The available one is 20180101 for this day and you can download all articles until 01/01/2018 by this link, [20180101](https://dumps.wikimedia.org/trwiki/20180101/trwiki-20180101-pages-articles.xml.bz2). Of course, you can use another corpus to train word2vec model but you must modify your corpus to train a model with gensim library, explained below.

## Preprocessing the Corpus
To train word2vec model with gensim library, you need to put each document into a line without punctuations. So, the output file should include all articles and each article should be in a line. Gensim library provides methods to do this preprocessing step. However, tokenize function is modified for Turkish language. You can run preprocess.py to modify your wikipedia dump corpus. It takes two arguments. First one is the path to the wikipedia dump(without extracting). Second one is the path to the output file. For example:
```
preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt
```

## Training Word2Vec Model
After preprocessing the corpus, training word2vec model with gensim library is very easy. You can use the code below to create word2vec model. First argument is revised corpus and the second one is name of the model. 
```
trainCorpus.py wiki.tr.txt trmodel
```
This command creates 3 output file. First is trmodel which should be loaded to the gensim library. Others include word vectors in numpy for hierarchical softmax and negative sampling.

#TO-DO#
You can download [pretrained model](##TO-DO##) which is created by following steps in this tutorial.
#TO-DO#

## Using Word2Vec Model and Examples
You can use the model after loading it.
```
from gensim.models import Word2Vec
model = Word2Vec.load("trmodel")
```

![](https://farm5.staticflickr.com/4743/39094244344_7f80345b93_o_d.png)

This is a classic example for word2vec. The most similar word vector for king+woman-man is queen as expected. Second one is "of king(kralı)", third one is "king's(kralın)". If the model was trained with lemmatization tool for Turkish language, the results would be more clear.



![](https://farm5.staticflickr.com/4607/39094244434_d37288334e_o_d.png)

Turkish is an aggluginative language. I have investigated this property. I analyzed most similar vector for +geliyor(he/she/it is coming)-gelmek(to come)+gitmek(to go). Most similar vector is gidiyor(he/she/it is going) as expected. Second one is "I am going". Third one is "going down" but it is another word in Turkish. Fourth one is went, fifth one is "I will go". So, we can see effects of tense and possesive suffixes in word2vec models.



![](https://farm5.staticflickr.com/4611/39094244524_c9419a39b2_o_d.png)

This finds the different words between [apple, orange, strawberry, house] as house.

</br>
</br>
</br>

# Eğitilmiş Türkçe Word2Vec Modeli
Bu çalışma Wikipedia'daki Türkçe makalelerden Türkçe word2vec modelinin nasıl çıkarılabileceğini anlatmak için yapılmıştır. Kod [gensim](https://radimrehurek.com/gensim/) kütüphanesi kullanılarak Python 3 ile yazılmıştır. Gelecek zamanlarda, Türkçe "lemmatization" algoritmasıyla aynı kök ve yapım ekleri fakat farklı çekim eklerine sahip kelimelerin aynı kelimeye işaret etmesi sağlanarak modelin kalitesi arttırılacaktır.

## Gereksinimler
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Gensim](https://radimrehurek.com/gensim/install.html)

## Korpusu Edinmek
Word2vec modellerini eğitmek için büyük korpuslara ihtiyaç duyuluyor. Açık kaynaklı bir örnek olarak, Türkçe dilinde yazılmış tüm wikipedia makalelerine [buradan](https://dumps.wikimedia.org/trwiki/) ulaşabilirsiniz. Şu anda yayınlanmış olan 20180101 adlı korpus ve [bu link](https://dumps.wikimedia.org/trwiki/20180101/trwiki-20180101-pages-articles.xml.bz2) üzerinden indirebilirsiniz. Tabii ki başka bir korpus da kullanabilirsiniz fakat gensim ile eğitebilmek için korpusunuz aşağıda belirtildiği gibi düzenlemelisiniz.

## Korpusu Düzenlemek
Gensim kütüphanesi ile word2vec modeli eğitebilmek için korpusunuzu belli bir şekilde düzenlemeniz gerekmektedir. Her bir makale, noktalama işaretlerinden ayıklanmış bir şekilde, bir satıra yazılmalıdır. Her bir satırda bir adet makale bulunacak şekilde bir dosyaya yazılmalıdır. Gensim kütüphanesi wikipedia korpusuna özel olarak bazı metodlar sunuyor. Yine de Türkçe dili için ayırıcı(tokenizer) fonksiyonu düzenlenmiştir. preprocess.py dosyasını çalıştırarak kendi wikipedia korpusunuzu düzenleyebilirsiniz. Bu python kodu iki tane argüman alıyor. İlki, wikipedia korpusunuzun dosya yolu(wikipedia korpusunuzu ayıklamadan). İkinci argüman ise çıktı dosyanızın yolu olacak. Örneğin:
```
preprocess.py trwiki-20180101-pages-articles.xml.bz2 wiki.tr.txt
```

## Word2Vec Modelini Eğitmek
Korpusu düzenledikten sonra, gensim kütüphanesiyle word2vec modelini kolayca eğitebilirsiniz. Word2Vec modeli oluşturmak için aşağıdaki kodu kullanabilirsiniz. İlk argüman düzenlenmiş korpus dosyasının yolu, ikinci argüman ise modelin adı olacak.
```
trainCorpus.py wiki.tr.txt trmodel
```
Bu komut ile 3 adet dosya oluşur. İlki, trmodel adında gensim kütüphanesini kullarak load edeceğiniz bir dosyadır. Diğerleri ise hierarchical softmax ve negative sampling kullanılarak numpy kütüphanesi ile oluşturulmuş kelime vektörlerini içerir.

#TO-DO#
Yukarıdaki adımlar izlenerek oluşturulmuş word2vec modelini [buradan](##TO-DO##) indirebilirsiniz.
#TO-DO#

## Word2Vec Modelini Kullanmak/Örnekler
Modeli aşağıdaki şekilde yükledikten sonra kullanabilirsiniz.
```
from gensim.models import Word2Vec
model = Word2Vec.load("trmodel")
```

![](https://farm5.staticflickr.com/4743/39094244344_7f80345b93_o_d.png)

Bu word2vec için klasik bir örnektir. Kral kelime vektöründen erkek kelime vektörü çıkarılıp kadın eklendiğinde en yakın kelime vektörü kraliçe oluyor. Benzerlerin bir çoğu da kral ve kraliçenin ek almış halleri oluyor. Türkçe sondan eklemeli bir dil olduğu için bazı sonuçlar beklenildiği gibi çıkmayabiliyor. Eğer word2vec'i kelimelerin lemmalarını bularak eğitebilseydik, çok daha temiz sonuçlar elde edebilirdik.



![](https://farm5.staticflickr.com/4607/39094244434_d37288334e_o_d.png)

Bu örnekte ise filler için zaman eklerinin etkisini inceledik. En benzer kelime vektörleri beklenen sonuç ile alakalı çıktı. 


![](https://farm5.staticflickr.com/4611/39094244524_c9419a39b2_o_d.png)

Bu method ise kelime listesi arasındaki farklı olanı bulmaya yarıyor ve beklenildiği gibi çalışıyor.

