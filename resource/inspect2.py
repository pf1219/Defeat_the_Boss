# Initialization
if gamemode==0:
    random.seed(seed+(floor*100+pos[0]*10+pos[1])*304639)
else:
    random.seed(seed+(chunk[0]*1000+chunk[1]*100+pos[0]*10+pos[1])*304639)
py.event.clear()
music_inspect.play(-1)
EXP_gain=0

win2.fill((255,255,255))
write2('INSPECT',50,(0,0,0),(960,50))

win.blit(bg,(0,0))
win_rect=win.get_rect(center=(960,440))
win2.blit(win,win_rect)
draw_status()
draw_item()
py.display.update()

time.sleep(1)

# Pick Result
result=random.choice(range(len(inspect_list)))
result2=inspect_list[result]
if random.random()<0.3:
    result2=['event','999','Nothing Happended..','EXP +1']

# Show Result
if result2[0]=='event':
    win.fill((0,0,0))
    win.blit(bg,(0,0))

    FS=round(min(1800/len(result2[2]),80))
    write(result2[2],FS,(255,255,255),(640,260))
    FS=round(min(1800/len(result2[3]),80))
    write(result2[3],FS,(255,255,255),(640,420))

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()
    time.sleep(3)

    if result2[1]=='999':
        EXP_gain=1
    elif result2[1]=='11':
        you_HP=you_HP+2
    elif result2[1]=='12':
        you_HP=you_HP-1
    elif result2[1]=='13':
        you_HP=you_HP-2
    elif result2[1]=='14':
        AST=AST+1
    elif result2[1]=='15':
        AST=AST+2
        MS=MS-4
    elif result2[1]=='16':
        MS=MS+2
        you_HP=you_HP-1
    elif result2[1]=='17':
        you_HP=you_HP-3
    elif result2[1]=='18':
        if GOLD>=3:
            you_HP=you_HP+4
            GOLD=GOLD-3
    elif result2[1]=='19':
        you_HP=you_HP+2
        EXP_gain=5
    elif result2[1]=='20':
        you_HP=you_HP-2
        AST=AST+1
        ASP=ASP-2
    elif result2[1]=='21':
        you_HP=you_HP-10
        EXP_gain=20
    elif result2[1]=='22':
        GOLD=GOLD+3
    elif result2[1]=='23':
        GOLD=GOLD+6
    elif result2[1]=='24':
        GOLD=GOLD+8
    elif result2[1]=='25':
        GOLD=GOLD+10
    elif result2[1]=='26':
        GOLD=GOLD+15
        you_HP=you_HP-2
    elif result2[1]=='27':
        EXP_gain=2
    elif result2[1]=='28':
        EXP_gain=5
    elif result2[1]=='29':
        EXP_gain=7
    elif result2[1]=='30':
        EXP_gain=10
    elif result2[1]=='31':
        EXP_gain=3
    elif result2[1]=='32':
        EXP_gain=6
    elif result2[1]=='33':
        EXP_gain=9
        you_HP=you_HP+2
        save_event[0]=1
    elif result2[1]=='34':
        you_HP=you_HP+6
    elif result2[1]=='35':
        GOLD=GOLD+12
    elif result2[1]=='36':
        you_HP=you_HP+4
    elif result2[1]=='37':
        AST=AST+1
    elif result2[1]=='38':
        EXP_gain=4
    elif result2[1]=='39':
        you_HP=you_HP+3
    elif result2[1]=='40':
        you_HP=you_HP-3
        MS=MS+4
    elif result2[1]=='41':
        GOLD=GOLD+9
    elif result2[1]=='42':
        EXP_gain=5
    elif result2[1]=='43':
        if GOLD>=2:
            EXP_gain=4
            GOLD=GOLD-2
    elif result2[1]=='44':
        EXP_gain=12
    elif result2[1]=='45':
        you_HP=you_HP-1
        EXP_gain=4
    elif result2[1]=='46':
        you_HP=you_HP-2
        EXP_gain=5
    elif result2[1]=='47':
        you_HP=you_HP-3
        EXP_gain=3

elif result2[0]=='item':
    win.fill((0,0,0))
    win.blit(bg,(0,0))

    FS=round(min(1800/len('You acquired an item: '+result2[2]),50))
    write('You acquired an item: '+result2[2],FS,(255,255,255),(640,260))
    k=item_name.index(result2[2])
    FS=round(min(1800/len(item_list[k][0].upper()+': '+item_list[k][3]),50))
    write(item_list[k][0].upper()+': '+item_list[k][3],FS,(255,255,255),(640,420))

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()
    time.sleep(2)

    while True:
        win.fill((0,0,0))
        win.blit(bg,(0,0))

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

        win_rect=win.get_rect(center=(960,440))
        win2.blit(win,win_rect)
        draw_status()
        draw_item()
        py.display.update()
        fps.tick(60)
        choice=0

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

if you_HP<=0:
    win.fill((0,0,0))
    write('GAME OVER',200,(255,0,0),(640,360))
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)

if you_HP>0:
    getEXP()
music_inspect.stop()
