from graphics import *
while(True):
    win=GraphWin("Tic Tac Toe",1500,700)
    win.setBackground('lightblue')

    #############################################################################
    ##############   Main Menu   #####################################


    ########################   TIC    ################
    T1=Line(Point(112,25),Point(112,125))
    T1.setWidth(10)
    T1.draw(win)
    T2=Line(Point(50,25),Point(175,25))
    T2.setWidth(10)
    T2.draw(win)

    I=Line(Point(200,25),Point(200,125))
    I.setWidth(10)
    I.draw(win)

    C1=Circle(Point(275,75),50)
    C1.setWidth(10)
    C1.draw(win)

    C1h=Rectangle(Point(290,20),Point(335,130))
    C1h.setFill('lightblue')
    C1h.setOutline('lightblue')

    C1h.draw(win)



    ####################################### TAC #########################


    T3=Line(Point(437,25),Point(437,125))
    T3.setWidth(10)
    T3.draw(win)
    T4=Line(Point(375,25),Point(500,25))
    T4.setWidth(10)
    T4.draw(win)

    A1=Line(Point(500,125),Point(540,20))
    A1.setWidth(10)
    A1.draw(win)
    A2=Line(Point(580,125),Point(540,20))
    A2.setWidth(10)
    A2.draw(win)
    A3=Line(Point(520,75),Point(560,75))
    A3.setWidth(10)
    A3.draw(win)


    C2=Circle(Point(635,75),50)
    C2.setWidth(10)
    C2.draw(win)

    C2h=Rectangle(Point(650,20),Point(695,135))
    C2h.setFill('lightblue')
    C2h.setOutline('lightblue')
    C2h.draw(win)




    #################################    TOE   #############################

    T5=Line(Point(797,25),Point(797,125))
    T5.setWidth(10)
    T5.draw(win)
    T6=Line(Point(735,25),Point(860,25))
    T6.setWidth(10)
    T6.draw(win)

    Ot=Circle(Point(910,75),50)
    Ot.setWidth(10)
    Ot.draw(win)


    E1=Line(Point(985,25),Point(985,125))
    E1.setWidth(10)
    E1.draw(win)
    E2=Line(Point(980,25),Point(1050,25))
    E2.setWidth(10)
    E2.draw(win)
    E3=Line(Point(980,125),Point(1050,125))
    E3.setWidth(10)
    E3.draw(win)
    E4=Line(Point(985,75),Point(1020,75))
    E4.setWidth(10)
    E4.draw(win)











    #############################################################################
    #############################################################################
    #############################################################################







    

    try:
        if(opt==1):
            opt=0


    except:



    
        prp1=Text(Point(250,300),'PLAYER 1 ')
        prp2=Text(Point(250,450),'PLAYER 2 ')
        prp1.setSize(26)
        prp2.setSize(26)
        prp1.draw(win)
        prp2.draw(win)
        pl1=Entry(Point(600,300),12)
        pl2=Entry(Point(600,450),12)
        pl1.setSize(26)
        pl2.setSize(26)
        pl1.setFill('white')
        pl2.setFill('white')
        pl1.draw(win)
        pl2.draw(win)
        win.getMouse()
        prp1.undraw()
        prp2.undraw()
        pl1.undraw()
        pl2.undraw()


        player1=pl1.getText()
        player2=pl2.getText()
        player1=player1.upper()
        player2=player2.upper()




    ##########################################    Score sheet  ################

    tbl=Rectangle(Point(685,150),Point(1025,700))
    tbl.setWidth(3)
    tbl.draw(win)

    verl=Line(Point(855,150),Point(855,700))
    verl.setWidth(3)
    verl.draw(win)


    for i in range(190,700,30):
        pq=Line(Point(685,i),Point(1025,i))
        pq.setWidth(3)
        pq.draw(win)


    tblpl1=Text(Point(770,170),player1[:9])
    tblpl1.draw(win)
    tblpl1.setSize(20)
    tblpl2=Text(Point(940,170),player2[:9])
    tblpl2.setSize(20)
    tblpl2.draw(win)




    line1=Line(Point(200,150),Point(200,600))
    line1.setWidth(5)
    line1.draw(win)
    line2=Line(Point(350,150),Point(350,600))
    line2.setWidth(5)
    line2.draw(win)
    line3=Line(Point(50,300),Point(500,300))
    line3.setWidth(5)
    line3.draw(win)
    line4=Line(Point(50,450),Point(500,450))
    line4.setWidth(5)
    line4.draw(win)



    chance=1
    pl1w=0
    pl2w=0


    X1=Text(Point(125,225),'X')
    X1.setSize(36)
    X2=Text(Point(275,225),'X')
    X2.setSize(36)
    X3=Text(Point(425,225),'X')
    X3.setSize(36)
    X4=Text(Point(125,375),'X')
    X4.setSize(36)
    X5=Text(Point(275,375),'X')
    X5.setSize(36)
    X6=Text(Point(425,375),'X')
    X6.setSize(36)
    X7=Text(Point(125,525),'X')
    X7.setSize(36)
    X8=Text(Point(275,525),'X')
    X8.setSize(36)
    X9=Text(Point(425,525),'X')
    X9.setSize(36)


    O1=Text(Point(125,225),'O')
    O1.setSize(36)
    O2=Text(Point(275,225),'O')
    O2.setSize(36)
    O3=Text(Point(425,225),'O')
    O3.setSize(36)
    O4=Text(Point(125,375),'O')
    O4.setSize(36)
    O5=Text(Point(275,375),'O')
    O5.setSize(36)
    O6=Text(Point(425,375),'O')
    O6.setSize(36)
    O7=Text(Point(125,525),'O')
    O7.setSize(36)
    O8=Text(Point(275,525),'O')
    O8.setSize(36)
    O9=Text(Point(425,525),'O')
    O9.setSize(36)
    for k in range(205,660,30):
        bl1=''
        bl2=''
        bl3=''
        bl4=''
        bl5=''
        bl6=''
        bl7=''
        bl8=''
        bl9=''




        i=1







        
        while(i<=9):
            if(chance==1):
                tblpl1.setOutline('green')
                tblpl2.setOutline('black')
            if(chance==2):
                tblpl2.setOutline('green')
                tblpl1.setOutline('black')
            i+=1
            ch=win.getMouse()
            chx=ch.getX()
            chy=ch.getY()
            if (chx>50 and chx<200 and chy>150 and chy<300 and bl1==''):
                if(chance==1):
                    X1.draw(win)
                    bl1='X'
                if(chance==2):
                    O1.draw(win)
                    bl1='O'
                    
            elif (chx>200 and chx<350 and chy>150 and chy<300 and bl2==''):
                if(chance==1):
                    X2.draw(win)
                    bl2='X'
                if(chance==2):
                    O2.draw(win)
                    bl2='O'
            elif (chx>350 and chx<500 and chy>150 and chy<300 and bl3==''):
                if(chance==1):
                    X3.draw(win)
                    bl3='X'
                if(chance==2):
                    O3.draw(win)
                    bl3='O'
            elif (chx>50 and chx<200 and chy>300 and chy<450 and bl4==''):
                if(chance==1):
                    X4.draw(win)
                    bl4='X'
                if(chance==2):
                    O4.draw(win)
                    bl4='O'
            elif (chx>200 and chx<350 and chy>300 and chy<450 and bl5==''):
                if(chance==1):
                    X5.draw(win)
                    bl5='X'
                if(chance==2):
                    O5.draw(win)
                    bl5='O'
            elif (chx>350 and chx<500 and chy>300 and chy<450 and bl6==''):
                if(chance==1):
                    X6.draw(win)
                    bl6='X'
                if(chance==2):
                    O6.draw(win)
                    bl6='O'
            elif (chx>50 and chx<200 and chy>450 and chy<600 and bl7==''):
                if(chance==1):
                    X7.draw(win)
                    bl7='X'
                if(chance==2):
                    O7.draw(win)
                    bl7='O'
            elif (chx>200 and chx<350 and chy>450 and chy<600 and bl8==''):
                if(chance==1):
                    X8.draw(win)
                    bl8='X'
                if(chance==2):
                    O8.draw(win)
                    bl8='O'
            elif (chx>350 and chx<500 and chy>450 and chy<600 and bl9==''):
                if(chance==1):
                    X9.draw(win)
                    bl9='X'
                if(chance==2):
                    O9.draw(win)
                    bl9='O'
            else:
                i-=1
                continue
            check1=(bl1==bl2==bl3=='X' or bl1==bl2==bl3=='O')
            check2=(bl4==bl5==bl6=='X' or bl4==bl5==bl6=='O')
            check3=(bl7==bl8==bl9=='X' or bl7==bl8==bl9=='O')
            check4=(bl1==bl4==bl7=='X' or bl1==bl4==bl7=='O')
            check5=(bl2==bl5==bl8=='X' or bl2==bl5==bl8=='O')
            check6=(bl3==bl6==bl9=='X' or bl3==bl6==bl9=='O')
            check7=(bl1==bl5==bl9=='X' or bl1==bl5==bl9=='O')
            check8=(bl3==bl5==bl7=='X' or bl3==bl5==bl7=='O')
            if (check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8):
                if (chance==1):
                    w=Text(Point(770,k),'W')
                    w.setSize(17)
                    w.setOutline('green')


                    l=Text(Point(940,k),'L')
                    l.setSize(17)
                    l.setOutline('red')


                    w.draw(win)
                    l.draw(win)

                    pl1w+=1
                    break
                else:
                    w=Text(Point(940,k),'W')
                    w.setSize(17)
                    w.setOutline('green')

                    l=Text(Point(770,k),'L')
                    l.setSize(17)
                    l.setOutline('red')
                    w.draw(win)
                    l.draw(win)

                    pl2w+=1
                    break




            
            
            if (chance==1):
                chance=2
            else:
                chance=1
        else:
            d1=Text(Point(770,k),'D')
            d1.setSize(17)
            d1.setOutline('orange')


            d2=Text(Point(940,k),'D')
            d2.setSize(17)
            d2.setOutline('orange')


            d1.draw(win)
            d2.draw(win)
        try:
            X1.undraw()
            X2.undraw()
            X3.undraw()
            X4.undraw()
            X5.undraw()
            X6.undraw()
            X7.undraw()
            X8.undraw()
            X9.undraw()
            O1.undraw()
            O2.undraw()
            O3.undraw()
            O4.undraw()
            O5.undraw()
            O6.undraw()
            O7.undraw()
            O8.undraw()
            O9.undraw()
        except:
            abcd=1
            

    ttw1=Text(Point(770,690),pl1w)
    ttw1.setSize(17)
    ttw2=Text(Point(940,690),pl2w)
    ttw2.setSize(17)
    ttw1.draw(win)
    ttw2.draw(win)

    winner=''
    whowin=Text(Point(300,690),winner)
    if (pl1w>pl2w):
        winner=player1+'  WINS'
    elif(pl1w<pl2w):
        winner=player2+'  WINS'
    else:
        winner='DRAW'
    whowin=Text(Point(300,690),winner)
    whowin.setSize(36)
    whowin.setOutline('green')
    whowin.draw(win)



    reag=Rectangle(Point(500,600),Point(680,700))
    reag.setFill('yellow')
    lnag=Line(Point(500,650),Point(680,650))
    lnag.setWidth(5)
    reag.setWidth(5)
    reag.draw(win)
    lnag.draw(win)


    ext=Text(Point(590,675),'EXIT')
    ext.setSize(20)
    ext.setOutline('red')

    ext.draw(win)



    plag=Text(Point(590,625),'PLAY AGAIN')
    plag.setSize(20)
    plag.setOutline('red')
    plag.draw(win)



    while(True):
        choice=win.getMouse()
        chcx=choice.getX()
        chcy=choice.getY()
        if(chcx>500 and chcx<680 and chcy>600 and chcy<650):
            opt=1
            break
        if(chcx>500 and chcx<680 and chcy>650 and chcy<700):
            opt=0
            break

    win.close()
    if(opt==1):
        continue
    if(opt==0):
        break





    

