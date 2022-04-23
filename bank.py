# 계좌번호 중복방지  = 완성 ->( 토비 : 계좌번호가 중복될 경우 제대로 입력할 때까지 다시 입력하도록 수정!)
# 출금금액이 잔액보다 큰경우 방지 = 완성 ->(잔액보다 작은 금액을 입력할 때까지 다시 입력하도록 수정!)
# 금액이 문자인경우/ 이름이 숫자인경우 = 완성 ->( 토비 : 입력이 잘못된 경우 제대로 입력할 때까지 다시 입력하도록 수정!)

#입금/출금할 때 존재하지 않는 계좌번호를 입력한 경우 =기존에 개설된 계좌번호를 입력할 때까지 다시 입력하도록 수정!
#전체조회할 때 아직 개설된 계좌가 없을 경우 = 계좌가 없다고 알려주도록 수정!
#입/출금시 아직 개설된 계좌가 없는 경우 = 개설된 계좌가 없으므로 메인 메뉴로 돌아가도록 수정!
#(또 고쳐야할 예외처리 발견하는 대로 고치겠습니다!)


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
        print("\n======계좌개설======")
        accountnumber = input("\n계좌번호를 입력해주세요 : ")


        while (accountnumber.isdigit()==False):
        
             print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
             accountnumber = input("\n계좌번호를 입력해주세요 : ")
             
        while (accountnumber in total):
              print("\n이미 존재하는 계좌번호입니다. 다시 입력해주세요.\n")
              accountnumber = input("\n계좌번호를 입력해주세요 : ")

              while (accountnumber.isdigit()==False):
        
               print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
               accountnumber = input("\n계좌번호를 입력해주세요 : ")
              

        name=input("이름을 입력해주세요 : ")
        
        while (name.isalpha()==False) :
             print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
             name=input("이름을 입력해주세요 : ")
             
            
        money = input("입금할 금액을 입력해주세요 :")

        while (money.isdigit()==False) :
             print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
             money = input("입금할 금액을 입력해주세요 :")
             
            
        newaccount = account.Main_account(accountnumber, name, money)
        total[accountnumber] = newaccount
        print("\n##계좌개설을 완료하였습니다##")
        print("=====================\n")
    
                    
    elif question == "2":
         
        print("======입금하기======")

        if (total=={}):
            print("\n개설된 계좌가 없습니다. 메뉴로 돌아갑니다!\n")
            continue
        
        identify = input("입금하실 계좌번호를 입력해주세요 : ")

        
        while (identify not in total):
            print("\n존재하지 않는 계좌번호입니다. 다시 입력해주세요. : \n")
            identify = input("입금하실 계좌번호를 입력해주세요 : ")
            
        print("계좌이름 : ", total[identify].name)
        print("계좌잔고 : ", total[identify].money, "원")            
        depositmoney = input("입금하실 금액을 입력해주세요 : ")
  
        while (depositmoney.isdigit()==False) :
             print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
             depositmoney = input("입금할 금액을 입력해주세요 :")

            
        total[identify].deposit(int(depositmoney))
        print()
        print("##계좌잔고 : ", total[identify].money, "원##")
        print("##입금이 완료되었습니다##")
        print("=====================\n")
        
        

    elif question == "3" :
        print("======출금하기======")

        if (total=={}):
            print("\n개설된 계좌가 없습니다. 메뉴로 돌아갑니다!\n")
            continue
        
        identify = input("출금하실 계좌번호를 입력해주세요 : ")


        while (identify not in total):
            print("\n존재하지 않는 계좌번호입니다. 다시 입력해주세요.  \n")
            identify = input("입금하실 계좌번호를 입력해주세요 : ")
            
        
        print("계좌이름 : ", total[identify].name)
        print("계좌잔고 : ", total[identify].money , "원")            
        withdrawmoney = input("출금하실 금액을 입력해주세요 : ")

        while (withdrawmoney.isdigit()==False) :
             print("\n* 잘못된 입력입니다. 다시 입력해주세요. *\n")
             withdrawmoney = input("입금할 금액을 입력해주세요 :")
            
            
        while (int(withdrawmoney) > int(total[identify].money)) :
                print("\n* 잔액이 부족합니다. " + str(total[identify].money) + "원 이하의 금액을 입력해주세요. * \n")
                withdrawmoney = input("입금할 금액을 입력해주세요 : ")
                
           
        total[identify].withdraw(int(withdrawmoney))
        print()
        print("##계좌잔고 : ", total[identify].money, "원##")
        print("##출금이 완료되었습니다##")
        print("=====================\n")
                    
    
    
    elif question == "4" :
        print("======전체조회======")
        
        for i in total:
            print("계좌번호 : ", total[i].account, "/ 이름 :", total[i].name, "/ 잔액 : ", total[i].money, "원")

        print("====================\n")

        if (total=={}):
            print("계좌가 존재하지 않습니다.\n")

    
    elif question == "5" :
        print("======계좌이체======")
    
    elif question == "6" :
        break;

    else :
        print("===잘못된 입력입니다.===\n")


print("##프로그램을 종료합니다.##")


     
