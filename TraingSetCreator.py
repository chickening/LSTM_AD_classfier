#테스트 생성기
#자동 아닙니다 수동입니다ㅎㅎ
import json # JSON
import os #파일관련 용도
import random
adResultSrc = './ad_data.txt'
notAdResultSrc = './not_ad_data.txt'
textDataSrc = './texts.txt'
usingRandom = True
usingKeyword = False
randomRange = 1000
keywordList = ['합격', '보장']
i = 0
print('광고면 y 아니면 n 클릭! 그만은 exit')
with open(textDataSrc , 'rt', encoding = 'UTF-8') as json_text_file:
    with open(adResultSrc, 'at', encoding = 'UTF-8') as ad_data_file:
        with open(notAdResultSrc, 'at', encoding= 'UTF-8') as not_ad_data_file:
            for line in json_text_file:
                text = json.loads(line.rstrip('\n'))
                if usingKeyword:    #키워드 검사
                    existKeyword = False
                    for keyword in keywordList:
                        if(text.find(keyword) != -1):
                            existKeyword = True
                    if not existKeyword:
                        continue
                
                if (random.randrange(0, randomRange) == 0 or not usingRandom): #랜덤 데이터 데이터 편향 막기 위해서
                    print(text)
                    yesno = input('답: ')
                    if yesno == 'y':
                        ad_data_file.write(json.dumps(text, ensure_ascii=False) + '\n')
                    elif yesno == 'n':
                        not_ad_data_file.write(json.dumps(text, ensure_ascii=False) + '\n')
                    elif yesno == 'exit':
                        break
                    
    
                