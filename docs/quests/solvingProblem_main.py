# 아래는 5개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화

# 문제1 : Python의 생성자 함수 이름은 무엇인가요?
# 1. __init__
# 2. main__
# 3. __str__
# 4. __del__
# 답을 입력하세요: 1
# 정답입니다!

# 문제2 : Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?
# 1. print('Hello, World!')
# 2. console.log('Hello, World!')
# 3. printf('Hello, World!')
# 4. echo 'Hello, World!'
# 답을 입력하세요: 1
# 정답입니다!

# 문제3 : Python의 주석을 나타내는 기호는 무엇인가요?
# 1. //
# 2. /* */
# 3. #
# 4. --
# 답을 입력하세요: 3
# 정답입니다!

# 문제4 : Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?
# 1. size()
# 2. length()
# 3. len()
# 4. sizeof()
# 답을 입력하세요: 3
# 정답입니다!

# 문제5 : Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?
# 1. str()
# 2. int()
# 3. char()
# 4. float()
# 답을 입력하세요: 2
# 정답입니다!

# option) 최종 점수: 100


def question():
    question_list = [
                    "문제1 : Python의 생성자 함수 이름은 무엇인가요? (점수: 20점)",
                    "문제2 : Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요? (점수: 20점)",
                    "문제3 : Python의 주석을 나타내는 기호는 무엇인가요? (점수: 20점)",
                    "문제4 : Python에서 리스트의 길이를 반환하는 함수는 무엇인가요? (점수: 20점)",
                    "문제5: Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요? (점수: 20점)"
                    ]
    answer_list = [
                "1. __init__, 2. main__, 3. __str__, 4. __del__",
                "1. print('Hello, World!'), 2. console.log('Hello, World!'), 3. printf('Hello, World!'), 4. echo 'Hello, World!'",
                "1.  //, 2. /* */, 3. #, 4. --"
                "1. size(), 2. length(), 3. len(), 4. sizeof()",
                "1. str(), 2. int(), 3. char(), 4. float()"
                ]

    user_answer = []

    for a in range(len(question_list)): 
        print(question_list[a])
        print(answer_list[a])
        input_answer = int(input("- 정답:"))
        user_answer.append(input_answer)
        pass
    pass
    return user_answer

def result_cal(user_answer) :
    pass
    correct_answer = [1,1,3,3,2]
    score_list=[20,20,20,20,20]
    score=[]
    for i in range(len(user_answer)):
       if user_answer[i] == correct_answer[i] :
            score.append(int(score_list[i]))
            user_sum = sum(score)

    if user_sum >=30 :
        user_score = "A"
    elif user_sum >=20 :
        user_score = "B"
    else:
        user_score = "C"
    print ("--------결과---------")
    print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}, 5번{}".format(user_answer[0], user_answer[1],user_answer[2], user_answer[3], user_answer[4]))
    print("당신 응답 합계 : {}점".format(user_sum))
    print("학점은 {}입니다.".format(user_score))
 
result_cal(question())




