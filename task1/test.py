# import json
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client['countries_db']
# collection_currency = db['currency1']
#
# with open('src\\students.json') as f:
#     file_data = json.load(f)
#
# collection_currency.insert_many(file_data)
#
# client.close()
# client = MongoClient('localhost', 27017)
# db = client['countries_db']
# collection_currency = db['currency1']
# print(collection_currency.find({"room": 6}).count())




import pandas as pd
