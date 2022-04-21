class Mainmenu:
    def mainmenu(self):
        # MAINMENU: 1.PDF모음, 2.강의추천, 3.자습서추천, 4.환경설정
        print('┌─────────────────┐')
        print('│⌕ 메뉴 선택       │  ')
        print('└─────────────────┘ ')
        print('↳ 1. PDF모음     ')
        print('↳ 2. 강의추천     ')
        print('↳ 3. 자습서추천   ')
        print('↳ 4. 환경설정     ')
        print('↳ 5. 내PC지키미     ')

        menu = input('메뉴를 선택하세요: ')                    #사용자가 메뉴 선택하게 하자
        menu = int(menu)                                    #인덱스를 위해 문자를 순자로 바꿔주자

        if (menu ==1):
            print("1번 [PDF모음] 메뉴로 이동합니다.")
            import pdf                                #pdf 파일로 임폴트 하자
            show_menu = pdf.Pdf_Package()             #pdf 파일에 Pdf_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Pdf_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==2):
            print("2번 [강의추천] 메뉴로 이동합니다.")
            import lecture                            #lecture 파일로 임폴트 하자
            show_menu = lecture.Lecture_Package()     #lecture 파일에 Lecture_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Pdf_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==3):
            print("3번 [자습서추천] 메뉴로 이동합니다.")
            import tutorial                           #tutorial 파일로 임폴트 하자
            show_menu = tutorial.Tutorial_Package()   #tutorial 파일에 Tutorial_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Tutorial_Package 클래스에 detailmenu 함수를 보여주자

        elif (menu ==4):
            print("4번 [환경설정] 메뉴로 이동합니다.")
            import enviroment                         #enviroment 파일로 임폴트 하자
            show_menu = enviroment.Env_Package()      #enviroment 파일에 Env_Package 클래스에 들어가자
            show_menu.detailmenu()                          #Env_Package 클래스에 detailmenu 함수를 보여주자


        elif (menu == 5):
            print("5번 [내pc지키미] 메뉴로 이동합니다.")
            import pcKeeper  # pcKeeper 파일로 임폴트 하자
            show_menu = pcKeeper.Mypc_Package()  # pcKeeper 파일에 Mypc_Package 클래스에 들어가자
            show_menu.detailmenu()  # Mypc_Package 클래스에 detailmenu 함수를 보여주자

        else:
            print(" ╭┈┈┈┈╯   ╰┈┈┈╮")
            print("  ╰┳┳╯  ╰┳┳╯")
            print("   💧 　　 💧")
            print("  💧　 　　 💧")
            print(" 💧   ╰┈┈╯   💧  ")
            print(" 💧  ╭━━━━━╮　 💧")
            print("   💧  ┈┈┈┈   1-5을 선택해 주세요ㅠㅠ  ")  # 1번부터 5번까지 고르지 않았을 경우엔 에러메세지를 보내주자
            import menu  # menu 파일로 임폴트 하자
            show_file = menu.Mainmenu()  # menu 파일에 Mainmenu 클래스에 들어가자
            show_file.mainmenu()  # Mainmenu 클래스에 mainmenu 함수를 보여주자





