from pymongo import MongoClient as mc

client = mc('mongodb://10.100.54.134:27017/')
db = client['my_database']
collection = db['my_collection']

f = open('비정형 데이터.txt', 'r', encoding='utf-8')
content = f.readlines()
i = 0
while True:
    try:
        Year = content[i].strip()
        ResultTitle = content[i + 1].strip()
        JournalName = content[i + 2].strip()
        Abstract = content[i + 3].strip()
        ScienceClass1 = content[i + 4].strip()
        ScienceClass2 = content[i + 5].strip()
        ScienceClass3 = content[i + 6].strip()
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
        i += 7
    except IndexError:
        break
f.close()