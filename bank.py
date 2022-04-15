from information import account
total = {}


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
        accountnumber = input("계좌번호를 입력해주세요 : ")
        name = input("이름을 입력해주세요 : ")
        money = input("입금할 금액을 입력해주세요 :")
        newaccount = account.Main_account(accountnumber, name, money)
        total[accountnumber] = newaccount
        print("##계좌개설을 완료하였습니다##")
        print("=====================")

    elif question == "2" :
        print("======입금하기======")
        identify = input("입금하실 계좌번호를 입력해주세요 : ")
        if identify in total :
            print("계좌이름 : ", total[identify].name)
            print("계좌잔고 : ", total[identify].money)            
            depositmoney = input("입금하실 금액을 입력해주세요 : ")
            total[identify].deposit(int(depositmoney))
            print()
            print("##계좌잔고 : ", total[identify].money, "원##")
            print("##입금이 완료되었습니다##")
            print("=====================")
        
        else : 
          print("===잘못된 입력입니다.===")

    elif question == "3" :
        print("======출금하기======")
        identify = input("출금하실 계좌번호를 입력해주세요 : ")
        if identify in total :
            print("계좌이름 : ", total[identify].name)
            print("계좌잔고 : ", total[identify].money)            
            withdrawmoney = input("출금하실 금액을 입력해주세요 : ")
            total[identify].withdraw(int(withdrawmoney))
            print()
            print("##계좌잔고 : ", total[identify].money, "원##")
            print("##출금이 완료되었습니다##")
            print("=====================")
                    
        else : 
          print("===잘못된 입력입니다.===")
    
    elif question == "4" :
        print("======전체조회======")
        for i in total:
            print("계좌번호 : ", total[i], "/ 이름 :", total[i].name, "/ 잔액 : ", total[i].money)

    
    elif question == "5" :
        print("======계좌이체======")
    
    elif question == "6" :
        print("======프로그램 종료======")

    else :
        print("===잘못된 입력입니다.===")