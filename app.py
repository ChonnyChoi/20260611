import random
import time
import streamlit

def number_guess():
    print("\n=== 숫자 맞추기 게임 ===")
    answer = random.randint(1, 100)

    while True:
        guess = int(input("1~100 사이 숫자를 입력하세요: "))

        if guess < answer:
            print("UP!")
        elif guess > answer:
            print("DOWN!")
        else:
            print("정답!")
            break

def rock_paper_scissors():
    print("\n=== 가위바위보 ===")

    choices = ["가위", "바위", "보"]
    computer = random.choice(choices)
    user = input("가위, 바위, 보 중 입력: ")

    print("컴퓨터:", computer)

    if user == computer:
        print("무승부!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("승리!")
    else:
        print("패배!")

def coin_flip():
    print("\n=== 동전 던지기 ===")
    result = random.choice(["앞면", "뒷면"])
    print("결과:", result)

def dice_roll():
    print("\n=== 주사위 굴리기 ===")
    result = random.randint(1, 6)
    print("주사위:", result)

def quiz_game():
    print("\n=== 퀴즈 게임 ===")

    questions = {
        "대한민국의 수도는?": "서울",
        "1 + 1 = ?": "2",
        "파이썬을 만든 사람 성은?": "반로섬"
    }

    score = 0

    for q, a in questions.items():
        user = input(q + " ")
        if user == a:
            print("정답!")
            score += 1
        else:
            print("오답! 정답:", a)

    print(f"점수: {score}/{len(questions)}")

def reaction_test():
    print("\n=== 반응속도 테스트 ===")
    print("준비...")

    wait_time = random.randint(2, 5)
    time.sleep(wait_time)

    print("지금!")

    start = time.time()
    input("엔터를 누르세요!")
    end = time.time()

    print(f"반응속도: {end - start:.3f}초")

while True:
    print("\n===================")
    print(" 미니게임 모음 ")
    print("===================")
    print("1. 숫자 맞추기")
    print("2. 가위바위보")
    print("3. 동전 던지기")
    print("4. 주사위 굴리기")
    print("5. 퀴즈 게임")
    print("6. 반응속도 테스트")
    print("0. 종료")

    choice = input("선택: ")

    if choice == "1":
        number_guess()
    elif choice == "2":
        rock_paper_scissors()
    elif choice == "3":
        coin_flip()
    elif choice == "4":
        dice_roll()
    elif choice == "5":
        quiz_game()
    elif choice == "6":
        reaction_test()
    elif choice == "0":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")
