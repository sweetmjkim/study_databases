# fruit_info 리스트를 mongo 저장
# 최소 2개의 function :connect, insert
fruit_list =[
    {"name": "사과", "color": "빨강", "origin": "한국"},
    {"name": "바나나", "color": "노랑", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황", "origin": "미국"}
]

def connect() : # f(x)
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database['fruits']
    return collection

def insert(collection,fruit_list) :         # collection에 넣기 위한 함수
    collection.insert_many(fruit_list)

insert(connect(),fruit_list) # insert(f(x)의 결과, 내가 넣을 셀들)

# #########################

# # fruit_info 리스트를 mongo 저장
# # 최소 2개의 function :connect, insert
# fruit_list =[
#                 {"name": "사과", "color": "빨강", "origin": "한국"},
#                 {"name": "바나나", "color": "노랑", "origin": "필리핀"},
#                 {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
#                 {"name": "오렌지", "color": "주황", "origin": "미국"}
#                 ]

# def connect() : # f(x)
#     from pymongo import MongoClient
#     mongoClient = MongoClient("mongodb://localhost:27017")
#     database = mongoClient["local"]
#     collection = database['fruits'] #f(x)의 결과
#     return collection #f(x)의 결과

# fruits=connect()

# fruits.insert_many(fruit_list)





