# Turkish Pre-trained Word2Vec Model
(Turkish version is below. / Türkçe için aşağıya bakın.)

This tutorial introduces how to train word2vec model for Turkish language from Wikipedia dump. This code is written in Python 3 by using [gensim](https://radimrehurek.com/gensim/) library. Turkish is an agglutinative language and there are many words with the same lemma and different suffixes in the wikipedia corpus. I will write Turkish lemmatizer to increase quality of the model.

You can checkout [wiki-page](https://github.com/akoksal/Turkish-Word2Vec/wiki) for more details. If you just want to download the pretrained model you can use [this link](https://drive.google.com/open?id=1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww) and you can look for examples in [5. Using Word2Vec Model and Examples](https://github.com/akoksal/Turkish-Word2Vec/wiki/5.-Using-Word2Vec-Model-and-Examples) page in github wiki. Some of them are below:

```
word_vectors.most_similar(positive=["kral","kadın"],negative=["erkek"])
```
![](https://farm1.staticflickr.com/908/41109901304_84392dccdd.jpg)

This is a classic example for word2vec. The most similar word vector for king+woman-man is queen as expected. Second one is "of king(kralı)", third one is "king's(kralın)". If the model was trained with lemmatization tool for Turkish language, the results would be more clear.

<br>
<br>

```
word_vectors.most_similar(positive=["geliyor","gitmek"],negative=["gelmek"])
```
![](https://farm1.staticflickr.com/953/27979111838_7849d93f9e.jpg)

Turkish is an aggluginative language. I have investigated this property. I analyzed most similar vector for +geliyor(he/she/it is coming)-gelmek(to come)+gitmek(to go). Most similar vector is gidiyor(he/she/it is going) as expected. Second one is "I am going". Third one is "lets go". So, we can see effects of tense and possesive suffixes in word2vec models.

</br>
</br>
</br>

# Eğitilmiş Türkçe Word2Vec Modeli
Bu çalışma Wikipedia'daki Türkçe makalelerden Türkçe word2vec modelinin nasıl çıkarılabileceğini anlatmak için yapılmıştır. Kod [gensim](https://radimrehurek.com/gensim/) kütüphanesi kullanılarak Python 3 ile yazılmıştır. Gelecek zamanlarda, Türkçe "lemmatization" algoritmasıyla aynı kök ve yapım ekleri fakat farklı çekim eklerine sahip kelimelerin aynı kelimeye işaret etmesi sağlanarak modelin kalitesi arttırılacaktır.

Ayrıntılar için github [wiki sayfasını](https://github.com/akoksal/Turkish-Word2Vec/wiki) ziyaret edebilirsiniz. Eğer sadece eğitilmiş modeli kullanmak isterseniz [buradan](https://drive.google.com/open?id=1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww) indirebilirsiniz. Aynı zamanda örneklere bakmak için github wikisinde bulunan [5. Word2Vec Modelini Kullanmak/Örnekler](https://github.com/akoksal/Turkish-Word2Vec/wiki/5.-Word2Vec-Modelini-Kullanmak-%C3%96rnekler) sayfasına bakabilirsiniz. Bazı örnekler aşağıda mevcuttur:

```
word_vectors.most_similar(positive=["kral","kadın"],negative=["erkek"])
```
![](https://farm1.staticflickr.com/908/41109901304_84392dccdd.jpg)

Bu word2vec için klasik bir örnektir. Kral kelime vektöründen erkek kelime vektörü çıkarılıp kadın eklendiğinde en yakın kelime vektörü kraliçe oluyor. Benzerlerin bir çoğu da kral ve kraliçenin ek almış halleri oluyor. Türkçe sondan eklemeli bir dil olduğu için bazı sonuçlar beklenildiği gibi çıkmayabiliyor. Eğer word2vec'i kelimelerin lemmalarını bularak eğitebilseydik, çok daha temiz sonuçlar elde edebilirdik.


<br>
<br>

```
word_vectors.most_similar(positive=["geliyor","gitmek"],negative=["gelmek"])
```
![](https://farm1.staticflickr.com/953/27979111838_7849d93f9e.jpg)

Bu örnekte ise filler için zaman eklerinin etkisini inceledik. En benzer kelime vektörleri beklenen sonuç ile alakalı çıktı. 


