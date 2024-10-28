# Initialization
py.event.clear()
if gamemode==0:
    random.seed(seed+(floor*100+pos[0]*10+pos[1])*608561)
else:
    random.seed(seed+(chunk[0]*1000+chunk[1]*100+pos[0]*10+pos[1])*608561)
music_market.play(-1)

win2.fill((255,255,255))
write2('MARKET',50,(0,0,0),(960,50))

win.blit(bg3,(0,0))
win_rect=win.get_rect(center=(960,440))
win2.blit(win,win_rect)
draw_status()
draw_item()
py.display.update()

time.sleep(0.5)

# Pick Result
result=random.sample(range(len(item_list)),k=3)
result2=[item_list[result[i]] for i in range(len(result))]

# Draw Result
lack=0
EXP_gain=0
while True:
    win.fill((0,0,0))
    win.blit(bg3,(0,0))
    choice=0

    write('Press A~C key to purchase or D key to not to purchase.',30,(255,255,255),(640,100))
    col=[(255,0,0),(0,255,0),(0,0,255)]
    avail=[1,1,1]
    for i in range(3):
        write(string.ascii_uppercase[i],50,col[i],(100,i*180+200))
        write(result2[i][2],40,col[i],(640,i*180+200))
        STR='COST: '+result2[i][4]
        if result2[i][2] in [weapon,armor,totem,tool]:
            avail[i]=0
            write('EQUIPPED',40,(127,127,127),(1080,i*180+200))
        elif result2[i][2]=="Docter's License" and save_event[0]==0:
            avail[i]=0
            write('REQUIRES MEDICAL TEXTBOOK',20,(127,127,127),(1080,i*180+200))
        elif result2[i][2]=="Mysterious Map" and save_event[1]==1:
            avail[i]=0
            write('ALREADY PURCHASED',20,(127,127,127),(1080,i*180+200))
        elif GOLD>=int(result2[i][4]):
            write(STR,40,col[i],(1080,i*180+200))
        else:
            avail[i]=0
            write(STR,40,(127,127,127),(1080,i*180+200))
        STR=result2[i][0].upper()+': '+result2[i][3]
        FS=round(min(1800/len(STR),30))
        write(STR,FS,col[i],(640,i*180+260))

    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_a:
                if avail[0]==1:
                    choice=1
                else:
                    lack=100
            elif event.key==K_b:
                if avail[1]==1:
                    choice=2
                else:
                    lack=100
            elif event.key==K_c:
                if avail[2]==1:
                    choice=3
                else:
                    lack=100
            elif event.key==K_d:
                choice=4

    if lack>0:
        write("This item is unavailable.",40,(255,255,255),(640,680))
        lack=lack-1

    if choice!=0:
        break

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()

if choice!=4:
    result2=result2[choice-1]
    k=item_name.index(result2[2])
    GOLD=GOLD-int(result2[4])

    if result2[0]=='one time':
        if result2[1]=='101':
            AST=AST+1
        elif result2[1]=='102':
            ASP=ASP-3
        elif result2[1]=='103':
            AST=AST+2
            MS=MS-4
        elif result2[1]=='104':
            you_HP=you_HP+2
        elif result2[1]=='105':
            you_HP=you_HP+4
        elif result2[1]=='106':
            EXP_gain=10
        elif result2[1]=='107':
            you_HP=you_HP+6
        elif result2[1]=='108':
            you_HP=you_HP+8
        elif result2[1]=='109':
            you_HP=you_HP+10
        elif result2[1]=='110':
            you_HP=you_HP+3
            EXP_gain=5
        elif result2[1]=='111':
            you_HP=you_HP+2
            EXP_gain=9
            save_event[0]=1
        elif result2[1]=='112':
            you_HP=you_HP+random.randint(0,5)
            EXP_gain=random.randint(0,15)
        elif result2[1]=='113':
            you_HP=you_HP+12
        elif result2[1]=='114':
            AST=AST+2
        elif result2[1]=='115':
            save_event[1]=1

    else:
        while True:
            win.fill((0,0,0))
            win2.fill((255,255,255))
            win.blit(bg3,(0,0))
            choice=0

            FS=round(min(1800/len(item_list[k][0].upper()+': '+item_list[k][3]),50))
            write(item_list[k][0].upper()+': '+item_list[k][3],FS,(0,255,0),(640,200))
            text='Will you equip '+item_list[k][2]+'?'
            text_size=min(80,int(2000/len(text)))
            write(text,text_size,(0,0,255),(640,350))
            write('Press Y or N key!',80,(0,0,255),(640,500))
            write('You can have only one '+item_list[k][0]+'.',25,(255,255,255),(640,630))
            if item_list[k][0]=='weapon':
                current_item=weapon
            elif item_list[k][0]=='armor':
                current_item=armor
            elif item_list[k][0]=='totem':
                current_item=totem
            elif item_list[k][0]=='tool':
                current_item=tool
            if current_item!='None':
                write('If you press Y, your current '+item_list[k][0]+' ('+current_item+') will be lost.',25,(255,255,255),(640,660))
            write('If you press N, this item ('+item_list[k][2]+') will be lost.',25,(255,255,255),(640,690))
            if item_list[k][0]=='tool':
                write('You can use tool once per every combat.',25,(255,255,255),(640,100))

            for event in py.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_y:
                        choice=1
                    elif event.key==K_n:
                        choice=-1

            if choice!=0:
                if choice==1:
                    if item_list[k][0]=='weapon':
                        weapon=item_list[k][2]
                        weapon2=item_list[k][3]
                    elif item_list[k][0]=='armor':
                        armor=item_list[k][2]
                        armor2=item_list[k][3]
                    elif item_list[k][0]=='totem':
                        totem=item_list[k][2]
                        totem2=item_list[k][3]
                    elif item_list[k][0]=='tool':
                        tool=item_list[k][2]
                        tool2=item_list[k][3]
                        tool_time=int(item_list[k][5])
                break

            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            draw_status()
            draw_item()
            py.display.update()
            fps.tick(60)

if you_HP<=0:
    win.fill((0,0,0))
    write('GAME OVER',200,(255,255,255),(640,360))
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)
else:
    getEXP()

music_market.stop()
