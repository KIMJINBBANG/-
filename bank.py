from information import account

while True:
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 계좌이체")
    print("6. 프로그램 종료")
    print("=====================")
    question = input("입력 : ")
    
    if question == "1" :
        print("======계좌개설======")
        account = input("계좌번호를 입력해주세요 : ")
        name = input("이름을 입력해주세요 : ")
        deposit = input("입금할 금액을 입력해주세요 :")
        print("##계좌개설을 완료하였습니다##")
        print("=====================")

    if question == "2" :
        print("======입금하기======")
        identify = input("입금하실 계좌번호를 입력해주세요 : ")
        if identify == account :
            print(name)
            print(deposit)


    if question == "3" :
        print("======출금하기======")
    
    if question == "4" :
        print("======전체조회======")
    
    if question == "5" :
        print("======계좌이체======")
    
    if question == "6" :
        print("======프로그램 종료======")

    else :
        print("===잘못된 입력입니다.===")