from random import randint

easy = 10
hard = 5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"축하합니다. 정답은 {answer}입니다.")

def set_difficulty():
    level = input("난이도를 선택하세요. easy or hard: ")
    if level == "easy":
        return easy
    else:
        return hard
    
def game():
    print("숫자 맞추기 게임을 하러 오신 여러분들 환영합니다!")
    print("1부터 100까지의 수 중 한 숫자를 고르시오.")
    answer = randint(1,100) # including both number

    
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"당신에게는 {turns}번의 기회가 남았습니다.")
        guess = int(input("숫자를 추측해보세요: "))
        turns = check_answer(guess,answer,turns)
        

        if turns == 0:
            print("실패! 더 이상 시도할 수 없습니다.")
            print(f"정답은 {answer}입니다.")
            return
        elif guess != answer:
            print("다시 생각해보세요!")
            
        
game()