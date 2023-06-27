import pymongo
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


client = mc('mongodb://10.100.54.134:27017/')
db = client['paper']
collection = db['paper_collection']
result = collection.find().sort('_id', pymongo.ASCENDING)
RCMN_CD = [] # histogram RCMN_CD1,2,3
x_labels = []  # x 축 값 저장을 위한 리스트

for doc in result:
    CD1, CD2, CD3 = doc['RCMN_CD1'], doc['RCMN_CD2'], doc['RCMN_CD3']

    if isinstance(CD1, str):
        RCMN_CD.append(CD1)
        print(CD1)
        x_labels.append(str(CD1))
    if isinstance(CD2, str):
        RCMN_CD.append(CD2)
        print(CD2)
        x_labels.append(str(CD2))
    if isinstance(CD3, str):
        RCMN_CD.append(CD3)
        print(CD3)
        x_labels.append(str(CD3))

    print('-----')

# 중복된 x 값 제거
x_labels = list(set(x_labels))
# 알파벳 순서로 x 축 값 정렬
x_labels.sort()

# 공백 추가 및 x_labels에 대한 y 값 출력
x_labels_with_y = []
for label in x_labels:
    count = RCMN_CD.count(label)
    x_labels_with_y.append(f"{label} {count}")

# 추가된 x_labels_with_y와 RCMN_CD를 이용하여 히스토그램 생성
plot_histogram(RCMN_CD, 'RCMN_CD')

# x_labels_with_y_original 파일로 저장
with open('x_labels_with_y_original.txt', 'w') as file:
    file.write('\n'.join(x_labels_with_y))

# x_labels_with_y를 파일로 저장
with open('x_labels_with_y.txt', 'w') as file:
    file.write('\n'.join(x_labels_with_y))
