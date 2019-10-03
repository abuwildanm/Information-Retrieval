import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('Dataset/data_sms_spam.csv')
# print(data.head())
# print(data.count())

# random urutan dan split data training & testing
x_train, x_test, y_train, y_test = train_test_split(data['teks'], data['label'], test_size=0.4)
# print(x_train.count(), x_test.count())

# transform ke tfidf dan train dengan naive bayes
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
text_clf.fit(x_train, y_train)

# coba prediksi data baru
sms_baru = ['Anda mendapatkan hadiah mobil','nanti ketemu dimana?']
pred = text_clf.predict(sms_baru)
print("Hasil prediksi: {}".format(pred))

#hitung akurasi data test
pred = text_clf.predict(x_test)
akurasi = np.mean(pred==y_test)
print("Akurasi: {}".format(akurasi))