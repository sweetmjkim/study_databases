### mongodb function
insertOne() : db.fruits.insertOne({...})
delete : db.posts.deleteMany({}) ;
전체 보고 할때 : db.fruits.find({}) ;
해당하는 내용만 출력 : db.posts.find({}, {_id:1, title :1, category:1, likes:1}) ;