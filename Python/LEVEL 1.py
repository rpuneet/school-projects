from graphics import*
win=GraphWin("Goal",107532523,700907)
win.setBackground('lightblue')

######################################################################################
###############################   Mapping   #####################################
#########################################################################


######################    LEVEL 1   ######################################

horline1=Line(Point(200,200),Point(800,200))
horline1.draw(win)

horline2=Line(Point(200,650),Point(400,650))
horline2.draw(win)

horline3=Line(Point(400,400),Point(600,400))
horline3.draw(win)

horline4=Line(Point(600,650),Point(800,650))
horline4.draw(win)




#############################################


verline1=Line(Point(200,200),Point(200,650))
verline1.draw(win)

verline2=Line(Point(400,400),Point(400,650))
verline2.draw(win)

verline3=Line(Point(600,400),Point(600,650))
verline3.draw(win)

verline4=Line(Point(800,200),Point(800,650))
verline4.draw(win)


############################################################################################

#######################  GOAL POST  ################

goal=Rectangle(Point(600,600),Point(800,650))
goal.setFill('green')
goal.draw(win)


#################   BALL  #########################

curx=225
cury=225
ball=Circle(Point(curx,cury),15)
ball.setFill('red')
ball.draw(win)

################# TELEPORTER  #####################

tel=Rectangle(Point(750,200),Point(800,250))
tel.setFill('yellow')
tel.draw(win)



##################################################################################################


########################################   CONTROLS   #############################################

con1=Rectangle(Point(950,425),Point(1025,500))
con1.draw(win)

con2=Rectangle(Point(1025,500),Point(1100,575))
con2.draw(win)

con3=Rectangle(Point(950,575),Point(1025,650))
con3.draw(win)

con4=Rectangle(Point(875,500),Point(950,575))
con4.draw(win)



#####################################################

up=Line(Point(987,440),Point(987,485))
up.setWidth(5)
up.setArrow('first')
up.draw(win)

down=Line(Point(987,590),Point(987,635))
down.setWidth(5)
down.setArrow('last')
down.draw(win)

left=Line(Point(890,537),Point(935,537))
left.setWidth(5)
left.setArrow('first')
left.draw(win)

right=Line(Point(1040,537),Point(1085,537))
right.setWidth(5)
right.setArrow('last')
right.draw(win)

T1=Line(Point(987,515),Point(987,560))
T1.setWidth(5)
T1.draw(win)

T2=Line(Point(965,515),Point(1010,515))
T2.setWidth(5)
T2.draw(win)



############################################################################
#########################   MAPPING DONE  ##################################
############################################################################


############################################################################
########################  GAMEPLAY    #####################################
##########################################################################


################################  FUNCTIONS  #################################


limx=curx
limy=cury

#######  MOVE BALL ########

def move_ball(movedir):
    ### UPWARD ##
    if(movedir=='u'):
        curx=ball.getCenter().getX()
        cury=ball.getCenter().getY()
        dif=int(cury-tel_lim(movedir)-25)
        for i in range(dif):
            ball.move(0,-1)
            for j in range(1000):
                for k in range(2):
                    junk=1
    ##  DOWNWARD  ##
    if(movedir=='d'):
        curx=ball.getCenter().getX()
        cury=ball.getCenter().getY()
        dif=int(tel_lim(movedir)-cury-25)
        for i in range(dif):
            ball.move(0,1)
            for j in range(1000):
                for k in range(2):
                    junk=1

    ## RIGHT  ##
    if(movedir=='r'):
        curx=ball.getCenter().getX()
        cury=ball.getCenter().getY()
        dif=int(tel_lim(movedir)-curx-25)
        for i in range(dif):
            ball.move(1,0)
            for j in range(1000):
                for k in range(2):
                    junk=1

    ## LEFT  ##
    if(movedir=='l'):
        curx=ball.getCenter().getX()
        cury=ball.getCenter().getY()
        dif=int(curx-tel_lim(movedir)-25)
        for i in range(dif):
            ball.move(-1,0)
            for j in range(1000):
                for k in range(2):
                    junk=1




#########   SET LIMIT   ##########

def set_lim(movedir):
    curx=ball.getCenter().getX()
    cury=ball.getCenter().getY()
    if(movedir=='u'):
        limy=200
        return limy
    if(movedir=='d'):
        if(curx>400 and curx<600):
            limy=400
            return limy
        else:
            limy=650
            return limy
    if(movedir=='r'):
        if(curx<400 and cury>400 and cury<650):
            limx=400
            return limx
        else:
            limx=800
            return limx
    if(movedir=='l'):
        if(curx>600 and cury>400 and cury<650):
            limx=600
            return limx
        else:
            limx=200
            return limx


#############  Teleprter's Limit  ################

def tel_lim(movedir):
    curx=ball.getCenter().getX()
    cury=ball.getCenter().getY()
    telx1=tel.getP1().getX()
    tely1=tel.getP1().getY()
    telx2=tel.getP2().getX()
    tely2=tel.getP2().getY()
    
    if(movedir=='u'):
        if(curx>telx1 and curx<telx2 and cury>tely2 ):
            limy=tely2
            return limy
       
        else:
            return set_lim(movedir)

    if(movedir=='d'):
        if(curx>telx1 and curx<telx2 and cury<tely2):
            limy=tely1
            return limy
       
        else:
            return set_lim(movedir)

    if(movedir=='r'):
        if(cury>tely1 and cury<tely2 and curx<telx1):
            limx=telx1
            return limx
       
        else:
            return set_lim(movedir)

    if(movedir=='l'):
        if(cury>tely1 and cury<tely2 and curx>telx2):
            limx=telx2
            return limx
       
        else:
            return set_lim(movedir)


###################################################################

#######################   TELEPORTER  ##############################

'''ball.undraw()
tel.undraw()
ball2=ball
ball=Circle(tel.getCenter(),15)
ball.setFill('red')
ball.draw(win)
tel=Rectangle(Point(ball2.getCenter().getX()-25,ball2.getCenter().getY()-25),Point(ball2.getCenter().getX()+25,ball2.getCenter().getY()+25))
tel.setFill('yellow')
tel.draw(win)'''

###############################################################







##############################################################################
#############################################################################
####################################   MAIN GAME  #######################################
#################################################################################
##############################################################################


while(True):
    ch=win.getMouse()
    chx=ch.getX()
    chy=ch.getY()

    if(chx>950 and chx<1025 and chy>425 and chy<500):
        movedir='u'
        move_ball(movedir)

    elif(chx>1025 and chx<1100 and chy>500 and chy<575):
        movedir='r'
        move_ball(movedir)

    elif(chx>875 and chx<950 and chy>500 and chy<575):
        movedir='l'
        move_ball(movedir)

    elif(chx>950 and chx<1025 and chy>575 and chy<650):
        movedir='d'
        move_ball(movedir)

    elif(chx>950 and chx<1025 and chy>500 and chy<575):
        ball.undraw()
        tel.undraw()
        ball2=ball
        ball=Circle(tel.getCenter(),15)
        ball.setFill('red')
        ball.draw(win)
        tel=Rectangle(Point(ball2.getCenter().getX()-25,ball2.getCenter().getY()-25),Point(ball2.getCenter().getX()+25,ball2.getCenter().getY()+25))
        tel.setFill('yellow')
        tel.draw(win)
    curx=ball.getCenter().getX()
    cury=ball.getCenter().getY()
    if(curx>600 and curx<800 and cury>600 and cury<650):
        break
print('You win')
        






























    





