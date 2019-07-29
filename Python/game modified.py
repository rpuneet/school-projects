main_ques=raw_input("\nChoose Your Option.(1,2,3,4):")
while main_ques<>4:
    print '\n\t\t\t....A SHADOW PRODUCTION.... \n\nWhich game do you want to play?\n\n1.HANGMAN\n2.TIC TAC TOE\n3.CALENDER.\n4.Quit.'
    

                        #HANGMAN starts from here.

#######################################################################################################################################################
###########################################################################################################################################################
##########################################################################################################################################################

    if main_ques=='1':
        print '''             A Shadow Production....... :)
                                        ______
    |      |        /\       |\     |  |         |\      /|       /\       |\     |
    |      |       /  \      | \    |  |         | \    / |      /  \      | \    |
    |______|      |____|     |  \   |  |   ___   |  \  /  |     |____|     |  \   |
    |      |     /      \    |   \  |  |      |  |   \/   |    /      \    |   \  |
    |      |    /        \   |    \ |  |      |  |        |   /        \   |    \ | 
    |      |   /          \  |     \|  |______|  |        |  /          \  |     \|
        '''
        while True:
            print "\nOptions:-\n\n1.Play\n2.Instructions\n3.Quit"
            ques=raw_input("Choose your option.(1,2,3):")
            if ques=='2':
                print'''
        Hangman is a word guessing game.
        Here the words are movie.
        That means you have to gues movie names.
        With every correct guess that letter will be displayed at its position in the name.
        If Your guess is wrong 1 chance will be deducted.You have 9 chances.
        If you guess the movie correctly then you will win the game.
        Else you will loose when all the chances are gone.


        '''
            elif ques=='1':
                break
            elif ques=='3':
                break
            else:
                print 'Input was wrong.'
                continue
        while ques=="1": 
            movie_names = ('koi mil gaya',\
                           '3 idiots',\
                           'hum dil de chuke sanam',\
                           'shahgird','london dreams',\
                           '2 states',\
                           'mausam',\
                           'maine pyar kiya',\
                           'heropanti',\
                           'mujhse shadi karogi',\
                           'ra one',\
                           'rockstar',\
                           'jab we met',\
                           'the xpose',\
                           'mai tera hero',\
                           'queen',\
                           'raaz',\
                           'gulab gang',\
                           'bewakoofiyaan',\
                           'sholay',\
                           'highway',\
                           'gunday',\
                           'shadi ke side effects',\
                           'hasee to phasee',\
                           'roti kapda aur makan',\
                           'tare zameen par',\
                           'rang de basanti',\
                           'lagaan',\
                           'swades',\
                           'dil chahta hai',\
                           'gangs of wasseypur',\
                           'guru',\
                           'barfi',\
                           'devdas',\
                           'bhaag milkha bhaag',\
                           'andaz apna apna',\
                           'paan singh tomar',\
                           'mother india',\
                           'chakde india',\
                           'zindagi na milegi dobara',\
                           'dilwale dulhania le jayenge',\
                           'black',\
                           'golmaal',\
                           'vicky donor',\
                           'mughal e azam',\
                           'chupke chupke',\
                           'rock on',\
                           'jaane tu ya jaane na',\
                           'munna bhai mbbs',\
                           'lage raho munna bhai',\
                           'bobbie',\
                           'coolie',\
                           'deewar',\
                           'hum aapke hain kon',\
                           'jodhaa akbar',\
                           'kabhi alvida na kehna',\
                           '1942 a love story',\
                           'kabhi khushi kabhie gham',\
                           'dil to pagal hai',\
                           'kaho naa pyaar hai',\
                           'krissh',\
                           'dhoom',\
                           'kal ho naa ho',\
                           'baazigar',\
                           'kuch kuch hota hai',\
                           'agneepath',\
                           'umrao jaan')
            lnmovie=len(movie_names)
            import random
            num=random.randint(0,lnmovie-1)
            mv1=movie_names[num]
            realword=mv1
            ln = len(mv1)
            mv1l=list(mv1)
            mv2 = ""
            for i in range(0,ln):
                mv2+=" "
            mv2l=list(mv2)
            for i in range(0,ln):
                if mv1l[i].isalnum():
                    mv2l[i]="-"
                else:
                    mv2l[i]=" "
            word=""
            for k in mv2l:
                word+=k
            wordlist = list(word)
            newword=""
            for m in wordlist:
                newword+=m
            chance=9
            mv1lst=[]
            while chance<>0:
                print "                              ",newword
                print "Chances left =",chance
                dash = "-"
                dashfinder=newword.find(dash)
                if str(dashfinder)=="-1":
                    print """                               You Won The GAME!!!!!!!
                                       CONGRATULATIONS...!!!
                                       :) :) :D :D :) :) :D :D"""
                    
                    break
                else:
                    guess = raw_input("Guess a letter:")
                    tr = mv1.find(guess)
                    if str(tr)=="-1":
                        print "Your guess was wrong."
                        chance -=1
                        continue
                    else:
                        while True:
                            tr2= mv1.find(guess)
                            if str(tr2)=="-1":
                                break
                            else:
                                wordlist = list(newword)
                                wordlist[tr2]=guess
                                newword=""
                                for l in wordlist:
                                    newword+=l
                                mv1l[tr2]=" "
                                mv1=""
                                for m in mv1l:
                                    mv1+=m
            else:
                print """                             No Chance left
                                     You Lost!!!!!!
                                     :( :( :( :( :(

                                     """
                print "MOVIE WAS                    ",realword.upper()
                print '''

        '''
            ques = raw_input("Do you want to play again?(1 for yes):")
        else:
            print '''                           ....Thank You For Playing Hangman....
                                       '''
        print'''

          '''
        q=raw_input("Press Enter to quit the game or (a) to go back to the main menu.")


#############################################################################################################################################################



                      #TIC TAC TOE starts from here

        
###########################################################################################################################################################
############################################################################################################################################
#############################################################################################################################################3

    if main_ques=='2':
        print '''\n                   A SHADOW PRODUCTION...
        _______     ____        _______  ___   ____       _______  ____   ____
           |    |  |               |    |   | |              |    |    | |
           |    |  |               |    |---| |              |    |    | |---
           |    |  |____           |    |   | |____          |    |____| |____
        '''
        while True:
            print "\n\nOptions:-\n\n1.Play\n2.Instructions\n3.Quit"
            ques1=raw_input("\nChoose your option.(1,2,3):")
            if ques1=='2':
                print '''\n\nTIC TAC TOE is a 2 player game.
        Every player gets chance alternatively.
        Player 1 gets O and Player 2 gets X.
        You have to get your respective symbols in a straight line either horizontally vertically or diagonally to win.
        The input chart is as follows:
        \t\t\t\t   |   |
        \t\t\t\t 1 | 2 | 3
        \t\t\t\t___|___|___
        \t\t\t\t   |   |
        \t\t\t\t 4 | 5 | 6
        \t\t\t\t___|___|___
        \t\t\t\t   |   |
        \t\t\t\t 7 | 8 | 9
        \t\t\t\t   |   |
        You have to input the number of the respective place where you want put you symbol


        '''
                a2=raw_input("Press Enter to continue.")
            elif ques1=='1':
                user1=raw_input("\nEnter name of player 1:")
                user2=raw_input("\nEnter name of player 2:")
                line1="\t\t   |   |   \n"
                line2="\t\t   |   |   \n"
                line3="\t\t___|___|___\n"
                line4="\t\t   |   |   \n"
                line5="\t\t   |   |   \n"
                line6="\t\t___|___|___\n"
                line7="\t\t   |   |   \n"
                line8="\t\t   |   |   \n"
                line9="\t\t   |   |   \n"
                turn=1
                strinp=""
                lst2=list(line2)
                lst5=list(line5)
                lst8=list(line8)
                while True:
                    line=line1+line2+line3+line4+line5+line6+line7+line8+line9
                    print line
                    checkhor=lst2[3]==lst2[7]==lst2[11]<>" " or lst5[3]==lst5[7]==lst5[11]<>" " or lst8[3]==lst8[7]==lst8[11]<>" "
                    checkver=lst2[3]==lst5[3]==lst8[3]<>" " or lst2[7]==lst5[7]==lst8[7]<>" " or lst2[11]==lst5[11]==lst8[11]<>" "
                    checkdig=lst2[3]==lst5[7]==lst8[11]<>" " or lst2[11]==lst5[7]==lst8[3]<>" "
                    check=checkhor or checkver or checkdig
                    if check==True:
                        if turn==0:
                            print "\n\t\t\t",user1,"""WINS..... :):):)
        \t\tCONGRATULATIONS""",user1,"....... :):):D:D\n\n"
                            break
                        else :
                             print "\n\t\t\t",user2,""""WINS..... :):):)
        \t\tCONGRATULATIONS""",user2,"....... :):):D:D\n\n"
                        break
                    checkdr=lst2[3]==" " or lst2[7]==" " or lst2[11]==" " or lst5[3]==" " or lst5[7]==" " or lst5[11]==" " or lst8[3]==" " or lst8[7]==" " or lst8[11]==" "
                    if checkdr==False:
                        print "\n\n\t\t\t//....MATCH DRAW....\\\n"
                        break
                    if turn==1:
                        print "                              ",user1,"'s turn"
                        tic=input("Enter your option.:(1-9):")
                        if strinp.find(str(tic))==-1:
                            if tic==1:
                                lst2=list(line2)
                                lst2[3]="O"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==2:
                                lst2=list(line2)
                                lst2[7]="O"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==3:
                                lst2=list(line2)
                                lst2[11]="O"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==4:
                                lst5=list(line5)
                                lst5[3]="O"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==5:
                                lst5=list(line5)
                                lst5[7]="O"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==6:
                                lst5=list(line5)
                                lst5[11]="O"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==7:
                                lst8=list(line8)
                                lst8[3]="O"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            if tic==8:
                                lst8=list(line8)
                                lst8[7]="O"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            if tic==9:
                                lst8=list(line8)
                                lst8[11]="O"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            turn=0
                            strinp+=str(tic)
                        else:
                            print "\n\n\t\t....That place is already full.....\n\n"
                    else:
                        print "                              ",user2,"'s turn"
                        tic=input("Enter your option.:(1-9)")
                        if strinp.find(str(tic))==-1:
                            if tic==1:
                                lst2=list(line2)
                                lst2[3]="X"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==2:
                                lst2=list(line2)
                                lst2[7]="X"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==3:
                                lst2=list(line2)
                                lst2[11]="X"
                                line2=""
                                for i in lst2:
                                    line2+=i
                            if tic==4:
                                lst5=list(line5)
                                lst5[3]="X"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==5:
                                lst5=list(line5)
                                lst5[7]="X"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==6:
                                lst5=list(line5)
                                lst5[11]="X"
                                line5=""
                                for i in lst5:
                                    line5+=i
                            if tic==7:
                                lst8=list(line8)
                                lst8[3]="X"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            if tic==8:
                                lst8=list(line8)
                                lst8[7]="X"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            if tic==9:
                                lst8=list(line8)
                                lst8[11]="X"
                                line8=""
                                for i in lst8:
                                    line8+=i
                            turn=1
                            strinp+=str(tic)
                        else:
                            print "\n\n\t\t....That place is already full.....\n\n"
            else:
                print '''\n\n\t\t\t\t  Have a good DAY
        \t\t\t\t...:):):):D:D:D...'''
                a=raw_input("Press Enter to exit this game.")
                break


############################################################################################################################################################




                    #Calender Starts Form Here

#######################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


    if main_ques=='3':
        print '\t\t\t.....A SHADOW PRODUCTION.....'
        while True:
            print "\n\n\n"+80*'*'+"\n\nOptions:-\n\n1.Monthly Calender.\n2.Find Day With Date.\n3.Exit.\n\n"
            Ques=input("Make your Choice.... :")
            if Ques==1 or Ques==2:
                year=input("\nEnter Year:")
                month=input("Enter Month:")
                date=1
                if Ques==2:
                    date=input("Enter Date:")
                cc=year-1
                yy1=5*(cc%4)
                yy2=4*(cc%100)
                yy3=6*(cc%400)
                strtday=(1+yy1+yy2+yy3)%7
                lstday=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                mnthstrt=lstday[strtday]
                def leap_year(year):
                    lp1=year%4
                    if lp1==0:
                        lp2=year%100
                        if lp2==0:
                            if year%400==0:
                                leap_year=True
                            else:
                                leap_year=False
                        else:
                            leap_year = True
                    else :
                        leap_year=False
                    return leap_year

                if leap_year(year)==True:
                    lstmnth=[0,31,29,31,30,31,30,31,31,30,31,30,31]
                if leap_year(year)==False:
                    lstmnth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
                daysnum=0
                for i in  range(1,month):
                    daysnum+=lstmnth[i]
                daysnum+=(date-1)
                numday=daysnum%7
                modday=(numday+strtday)%7
                the_day=lstday[modday]
                if Ques==2:
                    print "\n\nThe day on",date,'/',month,'/',year,'was','\n\n\t\t\t\t',the_day


                lstmnth2=['','January','February','March','April','May','June','July','August','September','October','November','December']
                calender='\n\n\t\t\t'+lstmnth2[month]+'  '+str(year)+"\n\n \tSun\tMon\tTue\tWed\tThu\tFri\tSat\n"
                date=1
                num=modday
                tb=' \t '
                null=' '
                strt=(num*(null+tb))
                num2=num+1
                calender+=strt
                print strtday
                while True:
                    calender+=tb+str(date)
                    if num2%7==0:
                        calender+='\n'
                    
                    strt+=tb
                    num2+=1
                    if date==lstmnth[month]:
                        break
                    date+=1
                
                if Ques==1:
                    print calender
            if Ques==3:
                break
          


#############################################################################################################################################################      


    if main_ques==4:
        break
        
    main_ques=raw_input("\nChoose Your Option.(1,2,3,4):")
