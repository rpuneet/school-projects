print "\n\n\t\t\t/....A SHADOW PRODUCTION....\\n"
while True:
    line1="\t\t _____ _____\n"
    line2="\t\t| | | | | | |\n"
    line3="\t\t|_|_|_|_|_|_|\n"
    line4="\t\t| | | | | | |\n"
    line5="\t\t|_|_|_|_|_|_|\n"
    lisline2=list(line2)
    lisline4=list(line4)
    import random
    block1=line1+line2+line3+line4+line5
    x=random.randint(1,6)
    while True:
        y=random.randint(1,6)
        if y<>x:
            break
    while True:
        z=random.randint(1,6)
        if z<>y and z<>x:
            break
    while True:
        a=random.randint(1,6)
        if a<>y and a<>x and a<>z:
            break
    while True:
        b=random.randint(1,6)
        if b<>y and b<>x and b<>z and b<>a:
            break
    while True:
        c=random.randint(1,6)
        if c<>y and c<>x and c<>z and c<>a and c<>b:
            break

    num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
    lstnum=list(num)
    lisline2[3]=lstnum[0]
    lisline2[5]=lstnum[1]
    lisline2[7]=lstnum[2]
    lisline4[3]=lstnum[3]
    lisline4[5]=lstnum[4]
    lisline4[7]=lstnum[5]
    line2=""
    for i in lisline2:
        line2+=i
    line4=""
    for i in lisline4:
        line4+=i
    block1=line1+line2+line3+line4+line5
    vl1=line2[3]+line4[3]
    vl2=line2[5]+line4[5]
    vl3=line2[7]+line4[7]
    hl1=line2[3]+line2[5]+line2[7]
    hl2=line4[3]+line4[5]+line4[7]



    while True:
        line6="\t\t _____ _____\n"
        line7="\t\t| | | | | | |\n"
        line8="\t\t|_|_|_|_|_|_|\n"
        line9="\t\t| | | | | | |\n"
        line10="\t\t|_|_|_|_|_|_|\n"
        lisline7=list(line7)
        lisline9=list(line9)
        import random
        block2=line6+line7+line8+line9+line10
        x=random.randint(1,6)
        while True:
            y=random.randint(1,6)
            if y<>x:
                break
        while True:
            z=random.randint(1,6)
            if z<>y and z<>x:
                break
        while True:
            a=random.randint(1,6)
            if a<>y and a<>x and a<>z:
                break
        while True:
            b=random.randint(1,6)
            if b<>y and b<>x and b<>z and b<>a:
                break
        while True:
            c=random.randint(1,6)
            if c<>y and c<>x and c<>z and c<>a and c<>b:
                break

        num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
        lstnum=list(num)
        lisline7[3]=lstnum[0]
        lisline7[5]=lstnum[1]
        lisline7[7]=lstnum[2]
        lisline9[3]=lstnum[3]
        lisline9[5]=lstnum[4]
        lisline9[7]=lstnum[5]
        line7=""
        for i in lisline7:
            line7+=i
        line9=""
        for i in lisline9:
            line9+=i
        if vl1.find(line7[3])==-1 and vl1.find(line9[3])==-1:
            if vl2.find(line7[5])==-1 and vl1.find(line9[5])==-1:
                if vl3.find(line7[7])==-1 and vl1.find(line9[7])==-1:
                    break
            
    block2=line6+line7+line8+line9+line10
    hl3=line7[3]+line7[5]+line7[7]
    hl4=line9[3]+line9[5]+line9[7]








    while True:
        x=random.randint(1,6)
        if hl1.find(str(x))==-1:
            break
    while True:
        y=random.randint(1,6)
        if y<>x and hl1.find(str(y))==-1:
            break
    while True:
        z=random.randint(1,6)
        if z<>y and z<>x and hl1.find(str(z))==-1:
            break
    while True:
        a=random.randint(1,6)
        if a<>y and a<>x and a<>z and hl2.find(str(a))==-1:
            break
    while True:
        b=random.randint(1,6)
        if b<>y and b<>x and b<>z and b<>a and hl2.find(str(b))==-1:
            break
    while True:
        c=random.randint(1,6)
        if c<>y and c<>x and c<>z and c<>a and c<>b and hl2.find(str(c))==-1:
            break

    num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
    lstnum=list(num)
    lisline2[9]=lstnum[0]
    lisline2[11]=lstnum[1]
    lisline2[13]=lstnum[2]
    lisline4[9]=lstnum[3]
    lisline4[11]=lstnum[4]
    lisline4[13]=lstnum[5]
    line2=""
    for i in lisline2:
        line2+=i
    line4=""
    for i in lisline4:
        line4+=i
    block1=line1+line2+line3+line4+line5
    vl4=line2[9]+line4[9]
    vl5=line2[11]+line4[11]
    vl6=line2[13]+line4[13]














    strnum=""
    while True:
        while True:
            x=random.randint(1,6)
            if hl3.find(str(x))==-1:
                break
        while True:
            y=random.randint(1,6)
            if y<>x and hl3.find(str(y))==-1:
                break
        while True:
            z=random.randint(1,6)
            if z<>y and z<>x and hl3.find(str(z))==-1:
                break
        while True:
            a=random.randint(1,6)
            if a<>y and a<>x and a<>z and hl4.find(str(a))==-1:
                break
        while True:
            b=random.randint(1,6)
            if b<>y and b<>x and b<>z and b<>a and hl4.find(str(b))==-1:
                break
        while True:
            c=random.randint(1,6)
            if c<>y and c<>x and c<>z and c<>a and c<>b and hl4.find(str(c))==-1:
                break

        num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)

        if strnum.find(num)==-1:
            lstnum=list(num)
            lisline7[9]=lstnum[0]
            lisline7[11]=lstnum[1]
            lisline7[13]=lstnum[2]
            lisline9[9]=lstnum[3]
            lisline9[11]=lstnum[4]
            lisline9[13]=lstnum[5]
            line7=""
            for i in lisline7:
                line7+=i
            line9=""
            for i in lisline9:
                line9+=i
            if vl4.find(line7[9])==-1 and vl4.find(line9[9])==-1:
                if vl5.find(line7[11])==-1 and vl5.find(line9[11])==-1:
                    if vl6.find(line7[13])==-1 and vl6.find(line9[13])==-1:
                        break
            strnum+=num+" "
    block2=line6+line7+line8+line9+line10




    vl1=line2[3]+line4[3]+line7[3]+line9[3]
    vl2=line2[5]+line4[5]+line7[5]+line9[5]
    vl3=line2[7]+line4[7]+line7[7]+line9[7]














    strnum2=""





    line11="\t\t _____ _____\n"
    line12="\t\t| | | | | | |\n"
    line13="\t\t|_|_|_|_|_|_|\n"
    line14="\t\t| | | | | | |\n"
    line15="\t\t|_|_|_|_|_|_|\n"
    lisline12=list(line12)
    lisline14=list(line14)
    while True:
        x=random.randint(1,6)
        while True:
            y=random.randint(1,6)
            if y<>x:
                break
        while True:
            z=random.randint(1,6)
            if z<>y and z<>x:
                break
        while True:
            a=random.randint(1,6)
            if a<>y and a<>x and a<>z:
                break
        while True:
            b=random.randint(1,6)
            if b<>y and b<>x and b<>z and b<>a:
                break
        while True:
            c=random.randint(1,6)
            if c<>y and c<>x and c<>z and c<>a and c<>b:
                break
        num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)
        

        if strnum2.find(num)==-1:
            lstnum=list(num)
            lisline12[3]=lstnum[0]
            lisline12[5]=lstnum[1]
            lisline12[7]=lstnum[2]
            lisline14[3]=lstnum[3]
            lisline14[5]=lstnum[4]
            lisline14[7]=lstnum[5]
            line12=""
            for i in lisline12:
                line12+=i
            line14=""
            for i in lisline14:
                line14+=i
            strnum2+=num+" "

            if vl1.find(line12[3])==-1 and vl1.find(line12[3])==-1:
                if vl2.find(line12[5])==-1 and vl2.find(line14[5])==-1:
                    if vl3.find(line12[7])==-1 and vl3.find(line14[7])==-1:
                        break
    block3=line11+line12+line13+line14+line15


















    vl4=line2[9]+line4[9]+line7[9]+line9[9]
    vl5=line2[11]+line4[11]+line7[11]+line9[11]
    vl6=line2[13]+line4[13]+line7[13]+line9[13]

    hl5=line12[3]+line12[5]+line12[7]
    hl6=line14[3]+line14[5]+line14[7]





















    chance2=1
    strnum3=""
    while True:
        chance2=1
        strnum3=""
        while chance2<37:
            while True:
                x=random.randint(1,6)
                if hl5.find(str(x))==-1:
                    break
            while True:
                y=random.randint(1,6)
                if y<>x and hl5.find(str(y))==-1:
                    break
            while True:
                z=random.randint(1,6)
                if z<>y and z<>x and hl5.find(str(z))==-1:
                    break
            while True:
                a=random.randint(1,6)
                if a<>y and a<>x and a<>z and hl6.find(str(a))==-1:
                    break
            while True:
                b=random.randint(1,6)
                if b<>y and b<>x and b<>z and b<>a and hl6.find(str(b))==-1:
                    break
            while True:
                c=random.randint(1,6)
                if c<>y and c<>x and c<>z and c<>a and c<>b and hl6.find(str(c))==-1:
                    break

            num=str(x)+str(y)+str(z)+str(a)+str(b)+str(c)

            if strnum3.find(num)==-1:
                lstnum=list(num)
                lisline12[9]=lstnum[0]
                lisline12[11]=lstnum[1]
                lisline12[13]=lstnum[2]
                lisline14[9]=lstnum[3]
                lisline14[11]=lstnum[4]
                lisline14[13]=lstnum[5]
                line12=""
                for i in lisline12:
                    line12+=i
                line14=""
                for i in lisline14:
                    line14+=i
                strnum3+=num+" "
                chance2+=1
                if vl4.find(line12[9])==-1 and vl4.find(line14[9])==-1:
                    if vl5.find(line12[11])==-1 and vl5.find(line14[11])==-1:
                        if vl6.find(line12[13])==-1 and vl6.find(line14[13])==-1:
                            break
        if chance2<>36:
            break
    block3=line11+line12+line13+line14+line15


    print block1,block2,block3


    avsdv=input("Press Enter to exit. and 1 for next puzzle.")


