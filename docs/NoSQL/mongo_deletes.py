from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
list_fruits = [
    {"name": "사과", "color": "빨강", "origin": "한국"},
    {"name": "바나나", "color": "노랑", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황", "origin": "미국"},
]
insert_rusult = collection.insert_many(list_fruits)

list_inserted_ids = insert_rusult.inserted_ids

# delete inserted records by _ids
collection.delete_many({"_id":list_inserted_ids[0]})

pass
