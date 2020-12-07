# 광고 LSTM 학습입니다.
# 학습 데이터 80% 검증 데이터 20%
import json
import random
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Flatten
from keras.models import load_model
import matplotlib.pyplot as plt

ad_data_src = './ad_data.txt'
not_ad_data_src = './not_ad_data.txt'
sorted_x_train = []
sorted_y_train = [] # 1 : 광고 0 : 광고아님
percent_veri = 0.2  # 검증 데이터 퍼센트
with open(ad_data_src, 'rt', encoding='utf-8-sig') as json_file:
    for line in json_file:
        sorted_x_train += [json.loads(line.rstrip('\n'))]
        sorted_y_train += [1]
with open(not_ad_data_src, 'rt', encoding='utf-8-sig') as json_file:
    for line in json_file:
        sorted_x_train += [json.loads(line.rstrip('\n'))]
        sorted_y_train += [0]
dataNum = len(sorted_x_train)
num_veri = (int)(dataNum * percent_veri)
nums = list(range(0, dataNum - 1))
for i in range(0, dataNum * 10): #데이터 섞어 주기
    ra = random.randrange(0, dataNum - 1)
    rb = random.randrange(0, dataNum - 1)
    t = nums[ra]
    nums[ra] = nums[rb]
    nums[rb] = t
x_train = list(range(0, dataNum - 1))
y_train = list(range(0, dataNum - 1))
for i in range(0, dataNum - 1):
    x_train[i] = sorted_x_train[nums[i]]
    y_train[i] = sorted_y_train[nums[i]]
#for i in range(0, dataNum - 1):
#    print("%s %d" % (x_train[i], y_train[i]))

token = Tokenizer(num_words = 10000, split = ' ')
token.fit_on_texts(x_train)
x_train = pad_sequences(token.texts_to_sequences(x_train), maxlen = 200)
model = Sequential()
model.add(Embedding(10000, 128))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(x_train[num_veri:], y_train[num_veri:], epochs= 12  , batch_size= 256, validation_data=(x_train[:num_veri], y_train[:num_veri]))

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()
loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')
acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')
loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()

with open('token.text', 'wb') as token_file:
    pickle.dump(token, token_file)
model.save('lstm_ad_model.h5')