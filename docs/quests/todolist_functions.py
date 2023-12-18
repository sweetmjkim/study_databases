# ToDo 리스트 생성
todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."}
    ]

def connect() :
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database["todolist"]
    return todo_list

def insert(collection,todo_list) :
    collection.insert_many(todo_list)
    
insert(connect(),todo_list)


# Input Your Name:  참여자1

# ToDo List 중 하나 선택 하세요 !
# 1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5.팀 멤버와의 1:1 면담
# Title 번호 :  1
# Status:  완료
# 종료 여부 : c

# ToDo List 중 하나 선택 하세요 !
# 1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5.팀 멤버와의 1:1 면담
# Title 번호 :  2
# Status:  진행 중
# 종료 여부 : q

# ------------------------
# Input Your Name:  참여자2
# 1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5. 팀 멤버와의 1:1 면담
# Title 번호 :  3
# Status:  진행 중
# 종료 여부 : q

# ------------------------
# Input Your Name:  참여자3

# 1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5. 팀 멤버와의 1:1 면담
# Title 번호 :  5
# Status:  진행 중
# 종료 여부 : x

# ------------------------
# 프로그램이 종료되었습니다.

