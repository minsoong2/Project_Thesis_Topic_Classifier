from pymongo import MongoClient as mc
import pymongo
import matplotlib.pyplot as plt
from collections import Counter


def plot_histogram(codes, title):
    plt.figure(figsize=(25, 8))
    code_counter = Counter(codes)
    plt.bar(code_counter.keys(), code_counter.values())
    plt.xticks(rotation=90)
    plt.title(title)
    plt.xlim(0, max(code_counter.keys()))
    plt.ylim(0, 2000)
    plt.show()


client = mc('mongodb://10.100.54.134:27017/')
db = client['paper']
collection = db['new_collection1']
result = collection.find().sort('_id', pymongo.ASCENDING)

RCMN_CD = [] # histogram RCMN_CD1,2,3
# RCMN_CD2 = [] # histogram RCMN_CD2
# RCMN_CD3 = [] # histogram RCMN_CD3

for doc in result:
    CD1, CD2, CD3 = doc['RCMN_CD1_INDEX'], doc['RCMN_CD2_INDEX'], doc['RCMN_CD3_INDEX']
    print(CD1)
    print(CD2)
    print(CD3)
    print('-----')
    RCMN_CD.append(CD1)
    RCMN_CD.append(CD2)
    RCMN_CD.append(CD3)

plot_histogram(RCMN_CD, 'RCMN_CD')