import requests
import xml.etree.ElementTree as ET
import re
from pymongo import MongoClient as mc
import matplotlib.pyplot as plt
from collections import Counter


def plot_histogram(codes, title):
    plt.figure(figsize=(25, 8))
    code_counter = Counter(codes)
    plt.bar(code_counter.keys(), code_counter.values())
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()


def remove_html(sentence):
    sentence = re.sub('(<([^>]+)>)', '', sentence)
    return sentence


client = mc('mongodb://10.100.54.134:27017/')
db = client['my_database']
collection = db['my_collection']

# API KEY
my_key = "ly64hh7wurkv221i4x41"
find = input("keyword: ")
start = 1
cnt = 0
# 샘플 url 변형해서 사용
endpoint = "https://www.ntis.go.kr/rndopen/openApi/natRnDSearch?apprvKey=" + my_key +\
           "&searchRnkn=&collection=rpaper&SRWR=" + find + f"&startPosition={start}&displayCnt=1000"
# api 호출
call = requests.get(endpoint)
# status = call.status_code
document = call.text
root = ET.fromstring(document)
count = int(root.find('COUNTLIST').find('COLCOUNT').text) # 논문갯수 카운트 확정
print(count)
count /= 1000
count = int(count) + 1
SC_codes = [] # histogram ScienceCode1,2,3
# SC2_codes = [] # histogram ScienceCode2
# SC3_codes = [] # histogram ScienceCode3

f = open(f"{find}.txt", "w", encoding='utf-8')
for i in range(count):
    # api 호출
    call = requests.get(endpoint)
    # status = call.status_code
    document = call.text
    root = ET.fromstring(document)

    Year = root.iter('Year')
    ResultTitle = root.iter('ResultTitle')
    JournalName = root.iter('JournalName')
    Abstract = root.iter('Full')
    ScienceClass1 = root.iter('ScienceClass1')
    ScienceClass2 = root.iter('ScienceClass2')
    ScienceClass3 = root.iter('ScienceClass3')

    for Y_, RT_, JN_, A_F, SC_1, SC_2, SC_3 in zip(Year, ResultTitle, JournalName, Abstract, ScienceClass1,
                                                   ScienceClass2, ScienceClass3):
        if str(Y_.text) == 'None':
            continue
        if str(RT_.text) == 'None':
            continue
        if str(JN_.text) == 'None':
            continue
        if str(A_F.text) == 'None':
            continue
        if str(SC_1.get('code')) == '':
            continue
        if str(SC_2.get('code')) == '':
            continue
        if str(SC_3.get('code')) == '':
            continue

        cnt = cnt + 1
        f.write(remove_html(Y_.text) + '\n')
        f.write(remove_html(RT_.text) + '\n')
        f.write(remove_html(JN_.text) + '\n')
        f.write(remove_html(A_F.text) + '\n')
        f.write(SC_1.get('code') + '\n')
        f.write(SC_2.get('code') + '\n')
        f.write(SC_3.get('code') + '\n')
        print(str(SC_1.get('code')))
        print(str(SC_2.get('code')))
        print(str(SC_3.get('code')))
        SC_codes.append(str(SC_1.get('code')))
        SC_codes.append(str(SC_2.get('code')))
        SC_codes.append(str(SC_3.get('code')))
        print(f'{cnt}th thesis')

        try:
            Year = remove_html(Y_.text)
            ResultTitle = remove_html(RT_.text)
            JournalName = remove_html(JN_.text)
            Abstract = remove_html(A_F.text)
            ScienceClass1 = SC_1.get('code')
            ScienceClass2 = SC_2.get('code')
            ScienceClass3 = SC_3.get('code')
            data = {
                'Year': Year,
                'ResultTitle': ResultTitle,
                'JournalName': JournalName,
                'Abstract': Abstract,
                'ScienceClass1': ScienceClass1,
                'ScienceClass2': ScienceClass2,
                'ScienceClass3': ScienceClass3
            }
            collection.insert_one(data)
        except IndexError:
            break

    print(f'Page: {i + 1}')
    print(endpoint)
    start += 1000
    endpoint = "https://www.ntis.go.kr/rndopen/openApi/natRnDSearch?apprvKey=" + my_key + "&searchRnkn=&collection=rpaper&SRWR=" + find + f"&startPosition={start}&displayCnt=1000"

f.close()

plot_histogram(SC_codes, 'ScienceClass_Code')