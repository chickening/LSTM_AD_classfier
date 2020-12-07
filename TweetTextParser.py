import json # JSON
import os #파일관련 용도
import re #정규 표현식
dataSrc = './data'
resultSrc = './texts.txt'
fileList = os.listdir(dataSrc)
i = 0
stride = 53      # 데이터 수 줄이기위한 건너뛰기 Range(1 ~ INF)
striding = 0
with open(resultSrc, 'wt', encoding = 'UTF-8') as result_file:
        for file in fileList:
                with open(dataSrc + '/' + file, 'rt', encoding='UTF-8') as json_file:
                        for line in json_file:
                                striding = (striding + 1) % stride
                                if(striding != 0):  # 건너뛰기
                                        continue
                                json_data = json.loads(line.rstrip('\n'))
                                text = json_data['text']
                                result_file.write(json.dumps(text, ensure_ascii=False) + '\n')
                i += 1
                print('%.2f%%' % (i * 100 / len(fileList)))
                