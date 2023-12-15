quiz_list = [           # 삽입 리스트
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "answer_number": 2,
        "score": 20
    }
]


def connect() :          # # mongodb에 있는 특정 collection에 연결하기 위한 함수
    from pymongo import MongoClient                 # mongdbcompass를 python 과 연동.
    mongoClient = MongoClient("mongodb://localhost:27017")  # mongdbcompass의 포트에 연결하는 변수 지정.
    database = mongoClient["local"]             # 해당 포트에 접속해서 database에 연결.
    collection = database["solvingproblem"]     # database에서 solvingproblem 이라는 collection에 연결.
    return collection       # collection이 이 모든 과정을 반환할 값으로 선언

def insert() :          # collection에 내용 집어넣기 위한 함수
    collection.insert_many(quiz_list)
    
# insert(connect(),quiz_list) 
#-------------------------------------------------------------------------------#

collection = connect()
def run():
    quiz_list = list(collection.find())
    user_name = input("이름을 입력해 주세요:")
    final_score = 0
    for i in range(len(quiz_list)):
        quiz = quiz_list[i]
        print(str(i+1) + ". " + quiz["question"], end=" ")
        print(str(quiz["score"])+"점") 
        for j in range(len(quiz["choices"])):
            choice = quiz["choices"][j]
            print(str(j+1)+". "+choice)
        user_answer =int(input("답을 입력해 주세요(번호로 입력): ")) 
        if user_answer == quiz["answer_number"]:
            final_score += quiz["score"]
        collection.update_many({'_id': quiz['_id']}, {"$set": {user_name: user_answer}}) 
    print(user_name + "님의 점수는 " + str(final_score) + "점 입니다.")
    return