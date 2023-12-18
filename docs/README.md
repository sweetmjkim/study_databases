### mongodb function

|제목|내용|
|--|--|
|insertOne()|db.fruits.insertOne({...});|
|delete|db.posts.deleteMany({}) ;|
|전체 보고 할때|db.fruits.find({}) ;|
|해당하는 내용만 출력|db.posts.find({}, {_id:1, title :1, category:1, likes:1}) ;|
|동일한 objectid을 넣기 위한|db.fruits_colors.insertMany({"fruits_id" : ObjectId("657bf1307880e42cec1aeedc"), "color": "주황색","갈색", "노란색"}); 동일한부분 넣는다.|
|메인 objectid으로 하위 objectid 리스트 확인|db.fruits_colors.find({ fruits_id : { $eq : ObjectId("657bf1307880e42cec1aeedc")}}) ;|
|||
|||
|||
|||
|||
