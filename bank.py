# 계좌번호 중복방지  = 완성
# 출금금액이 잔액보다 큰경우 방지 = 완성
# 금액이 문자인경우/ 이름이 숫자인경우 = 완성



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
        if accountnumber.isalpha() :
            print("===잘못된 입력입니다.===\n")
            continue
        else :
            pass
        if accountnumber in total :
            print("===이미 존재하는 계좌번호입니다.===")
            continue
        else :
            pass
        name = input("이름을 입력해주세요 : ")
        if name.isdigit() :
            print("===잘못된 입력입니다.===\n")
            continue
        else :
            pass
        money = input("입금할 금액을 입력해주세요 :")
        if money.isalpha() :
            print("===잘못된 입력입니다.===\n")
            continue
        else :
            pass
        newaccount = account.Main_account(accountnumber, name, money)
        total[accountnumber] = newaccount
        print("##계좌개설을 완료하였습니다##")
        print("=====================\n")

    elif question == "2" :
        print("======입금하기======")
        identify = input("입금하실 계좌번호를 입력해주세요 : ")
        if identify in total :
            print("계좌이름 : ", total[identify].name)
            print("계좌잔고 : ", total[identify].money, "원")            
            depositmoney = input("입금하실 금액을 입력해주세요 : ")
            if depositmoney.isalpha() :
                print("===잘못된 입력입니다.===\n")
                continue
            else :
                pass
            total[identify].deposit(int(depositmoney))
            print()
            print("##계좌잔고 : ", total[identify].money, "원##")
            print("##입금이 완료되었습니다##")
            print("=====================\n")
        
        else : 
          print("===잘못된 입력입니다.===\n")

    elif question == "3" :
        print("======출금하기======")
        identify = input("출금하실 계좌번호를 입력해주세요 : ")
        if identify in total :
            print("계좌이름 : ", total[identify].name)
            print("계좌잔고 : ", total[identify].money , "원")            
            withdrawmoney = input("출금하실 금액을 입력해주세요 : ")
            if withdrawmoney.isalpha() :
                print("===잘못된 입력입니다.===\n")
                continue
            else :
                pass
            if int(withdrawmoney) > int(total[identify].money) :
                print("잔액 부족")
                continue
            else :
                pass
            total[identify].withdraw(int(withdrawmoney))
            print()
            print("##계좌잔고 : ", total[identify].money, "원##")
            print("##출금이 완료되었습니다##")
            print("=====================\n")
                    
        else : 
          print("===잘못된 입력입니다.===\n")
    
    elif question == "4" :
        print("======전체조회======")
        for i in total:
            print("계좌번호 : ", total[i].account, "/ 이름 :", total[i].name, "/ 잔액 : ", total[i].money, "원")
        print("====================\n")

    
    elif question == "5" :
        print("======계좌이체======")
    
    elif question == "6" :
        break;

    else :
        print("===잘못된 입력입니다.===\n")


print("##프로그램을 종료합니다.##")
