import json
import random
import keras
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

textSrc = './texts.txt'
ad_data_src = './ad_data.txt'
not_ad_data_src = './not_ad_data.txt'
model = load_model('lstm_ad_model.h5')
ad_num = 0
not_ad_num = 0
with open('token.text', 'rb') as token_file:
    token = pickle.load(token_file)
with open(textSrc, 'rt', encoding='utf-8') as text_file:
    for line in text_file:
        text = json.loads(line.rstrip('\n'))
        target = pad_sequences(token.texts_to_sequences([text]), maxlen = 200)
        #print(target)
        y = model.predict_classes(target)
        if(y == 1):
            print(text + " : 광고")
            #if(yesno == 'y'):
            #    with open(ad_data_src, 'at', encoding= 'utf-8') as ad_data_file:
            #        ad_data_file.write(json.dumps(text, ensure_ascii=False) + '\n')
            #elif(yesno == 'n'):
            #    with open(not_ad_data_src, 'at', encoding= 'utf-8') as not_ad_data_file:
            #        not_ad_data_file.write(json.dumps(text, ensure_ascii=False) + '\n')
            ad_num += 1
            with open('./finded_ad.txt', 'at', encoding= 'utf-8') as finded_ad_file:
                finded_ad_file.write(json.dumps(text,ensure_ascii=False)+ '\n')
        else:
            not_ad_num += 1
print("광고수 : %d  광고가 아닌 데이터 수 : %d " % (ad_num, not_ad_num))