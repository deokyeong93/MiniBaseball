from random import *

answer = input("동네에서 알아주는 투수 나까무라, \n어느날 운동장에서 혼자 벽에 공을 던지며 놀고있었는데 \n혼자 야구를 하는 것이 재미가 없게 느껴졌다. \n심심했던 나까무라는 핸드폰으로 '나'를 불러 \n1대1 야구 대결을 제안했다.\n응하시겠습니까?\n yes or no ? ")

if answer == "yes":
    pass
    print("경기규칙 : 안타와 볼넷 합계 2번 승리, 삼진 : 1번 패배 ")
else:
    print("아.. 우리의 왕따 나까무라.. 화이팅!\nGame Over")
    import sys
    sys.exit()  # 이렇게 스크립트를 마무리하면 되는건가? 방법을 모르겠음..


score = 0
strike = 0
ball = 0
hit = 0


player = {1: "이대호", 2: "추신수", 3: "이승엽"}
num = input("캐릭터를 골라주세요!\n1 : 이대호, 2 : 추신수, 3 : 이승엽\n당신의 선택은?")
print("탁월한 선택입니다.")
selector = player[int(num)]

for i in range(1, 100):  # randrange를 여기다 써서 iterable오류 발생(타입오류)
    print("투수! 공을 던졌습니다!")
    print("스트라이크 : {0} 볼: {1}".format(strike, ball))
    act = input("휘두른다? 기다린다?")
    km = randrange(135, 151)
    print("구속 : {0}km".format(km))
    # continue한 번 써보기 위해 작성// 경우의 수가 나와도 건너뛰고 반복문을 다시 진행한다.
    if 135 <= km < 140:
        # continue
        if act == "휘두른다":
            print("{0} 안타! 안타! 쳤습니다~ 저 선수 방망이 참 잘쳐요~".format(selector))
            strike = 0
            score += 1
            hit += 1
            if score >= 2:
                print("이겼습니다~~~{0}~~~ 오늘의 승자는 {0}입니다!!!".format(selector))
                break
            else:
                print("아~ 아직 안타가 더 필요합니다...")
        else:
            print("스투~~~라익!")
            strike += 1
            if strike == 3:
                print("{0} 삼진 아웃! 경기 끝났습니다...\n 오늘 경기의 승자는 나까무라!".format(selector))
                break
            else:
                pass
    elif 140 <= km < 151:
        if act == "휘두른다":
            print("스투~~~라익!, 방망이가 헛도네요...")
            strike += 1
            if strike == 3:
                print("삼진 아웃! 경기 끝났습니다...\n 오늘 경기의 승자는 나까무라!")
                break
            else:
                pass
        else:
            print("볼")
            ball += 1
            if ball == 4:
                print(
                    "포볼! 타자 공을 잘 골라내면서 경기 끝났습니다...\n 오늘 경기의 승자는 {0}".format(selector))
                score += 1
                strike = 0
                ball = 0
                if score >= 2:
                    print("이겼습니다~~~{0}~~~ 오늘의 승자는 {0}입니다!!!".format(selector))
                    break
                else:
                    print("아~ 아직 점수가 더 필요합니다...")
            else:
                pass

# 사용했던 구문만 사용중,,, 에러처리, 클래스, 모듈에 약점..dir도 아직 잘...
