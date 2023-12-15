# 아래 정리문
# from pymongo import MongoClient
# mongoClient = MongoClient("mongodb://localhost:27017")
# database = mongoClient["local"]
# collection = database['fruits']
# collection.insert_one({"name": "키위",
#                        "color": "갈색",
#                        "origin": "뉴질랜드"})
# dict_fruits = {"name": "오렌지", "color": "주황", "origin": "미국"}
# collection.insert_one(dict_fruits)
# pass


from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
mixed_fruit = {"name": "오렌지",
               "color": ["주황색", '갈색', '노란색'],
               "origin": "미국"}
result = collection.insert_one(mixed_fruit)
pass

# 분리 입력(fruits, fruits_colors)
# insert fruits 작업 진행
dict_fruit = {"name": "오렌지",
               "origin": "미국"}
result = collection.insert_one(dict_fruit)
# insertedId: ObjectId("657bf1307880e42cec1aeedc")
print("result.inserted_id : {}".format(result.inserted_id))
inserted_id = result.inserted_id



#insert fruits_colors 작업 진행
# [{"fruits_id" : ObjectId("657bf1307880e42cec1aeedc"), "color": "주황색"}
#  , {"fruits_id" : ObjectId("657bf1307880e42cec1aeedc"),"color": "갈색"}
#  , {"fruits_id" : ObjectId("657bf1307880e42cec1aeedc"),"color": "노란색"}]


# 아래 내용은 mongoDB를 통해서 진행했던걸 파이썬으로 만들어내는 과정이다.

fruit_colors = [{"color": "주황색"}
            , {"color": "갈색"}
            , {"color": "노란색"}]

list_fruits_colors = list()
for dict_color in fruit_colors :
    dict_color["fruits_id"] = inserted_id
    list_fruits_colors.append(dict_color)
    pass

# collection fruits colors
collection_fruits_colors = database["fruits_colors"]

collection_fruits_colors.insert_many(list_fruits_colors)

# find from fruits_colors
documents = collection_fruits_colors.find({ "fruits_id" : { "$eq" : inserted_id}})

pass
# db.fruits_colors.find({ fruits_id : { $eq : ObjectId("657bf1307880e42cec1aeedc")}}) ;