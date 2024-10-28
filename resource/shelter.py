# Initialization
if gamemode==0:
    random.seed(seed+(floor*100+pos[0]*10+pos[1])*528597)
else:
    random.seed(seed+(chunk[0]*1000+chunk[1]*100+pos[0]*10+pos[1])*528597)
py.event.clear()
music_shelter.play(-1)
EXP_gain=0

win2.fill((255,255,255))
write2('SHELTER',50,(0,0,0),(960,50))

win.blit(bg4,(0,0))
win_rect=win.get_rect(center=(960,440))
win2.blit(win,win_rect)
draw_status()
draw_item()
py.display.update()

time.sleep(0.5)

# Randomization
HP_gain=random.randint(1+floor//2,3+floor//2)
EXP_journal=random.choice(['physiology','biochemistry','pharmacology','anatomy','epidemiology','cardiology','pulmonology','gastroenterology','rheumatology','endocrinology','microbiology'])
EXP_gain_amout=random.randint(1+floor//2,3+floor//2)
STAT_inc=random.randint(1,6)

# Sell item
refund=[0,0,0,0]
refund_percentage=[random.random()*0.4+0.6 for i in range(4)]
if weapon!='None':
    refund[0]=int(int(item_list[[item_list[i][2] for i in range(len(item_list))].index(weapon)][4])*refund_percentage[0])
if armor!='None':
    refund[1]=int(int(item_list[[item_list[i][2] for i in range(len(item_list))].index(armor)][4])*refund_percentage[1])
if totem!='None':
    refund[2]=int(int(item_list[[item_list[i][2] for i in range(len(item_list))].index(totem)][4])*refund_percentage[2])
if tool!='None':
    refund[3]=int(int(item_list[[item_list[i][2] for i in range(len(item_list))].index(tool)][4])*refund_percentage[3])

# Choice
choice=0
while choice==0:
    win.fill((0,0,0))
    win.blit(bg4,(0,0))

    write('What will you do? Press A~D key.',30,(255,255,255),(640,100))
    write('A. Rest (HP +'+str(HP_gain)+')',50,(255,255,255),(640,200))
    write('B. Read '+EXP_journal+' journal (EXP +'+str(EXP_gain_amout)+')',50,(255,255,255),(640,320))
    if STAT_inc==1:
        write('C. Training (Move Speed +1)',50,(255,255,255),(640,440))
    elif STAT_inc==2:
        write('C. Training (Attack Strength +1)',50,(255,255,255),(640,440))
    elif STAT_inc==3:
        write('C. Training (Attack Cooltime -2)',50,(255,255,255),(640,440))
    elif STAT_inc==4:
        write('C. Training (Bullet Speed +1)',50,(255,255,255),(640,440))
    elif STAT_inc==5:
        write('C. Training (Bullet Size +1)',50,(255,255,255),(640,440))
    elif STAT_inc==6:
        write('C. Training (Dodge Percentage +4)',50,(255,255,255),(640,440))
    if sum(refund)>0:
        write('D. Sell item (GOLD +?)',50,(255,255,255),(640,560))
    else:
        write('D. No item to sell',50,(127,127,127),(640,560))

    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_a:
                choice=1
            elif event.key==K_b:
                choice=2
            elif event.key==K_c:
                choice=3
            elif event.key==K_d and sum(refund)>0:
                choice=4

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()
    fps.tick(60)

if choice==1:
    you_HP=you_HP+HP_gain
elif choice==2:
    EXP_gain=EXP_gain_amout
elif choice==3:
    if STAT_inc==1:
        MS=MS+1
    elif STAT_inc==2:
        AST=AST+1
    elif STAT_inc==3:
        ASP=ASP-2
    elif STAT_inc==4:
        BSP=BSP+1
    elif STAT_inc==5:
        BSZ=BSZ+1
    elif STAT_inc==6:
        DOD=DOD+4

while choice==4:
    win.fill((0,0,0))
    win.blit(bg4,(0,0))

    write('Press A~D key to sell item or E key to sell nothing.',30,(255,255,255),(640,100))
    if weapon!='None':
        write('A',50,(255,255,255),(100,200))
        text='Sell '+weapon
        text_size=min(50,int(1000/len(text)))
        write(text,text_size,(255,255,255),(640,200))
        write('GAIN: '+str(refund[0]),50,(255,255,255),(1080,200))
    else:
        write('A',50,(127,127,127),(100,200))
        write('No weapon to sell',50,(127,127,127),(640,200))
    if armor!='None':
        write('B',50,(255,255,255),(100,320))
        text='Sell '+armor
        text_size=min(50,int(1000/len(text)))
        write(text,text_size,(255,255,255),(640,320))
        write('GAIN: '+str(refund[1]),50,(255,255,255),(1080,320))
    else:
        write('B',50,(127,127,127),(100,320))
        write('No armor to sell',50,(127,127,127),(640,320))
    if totem!='None':
        write('C',50,(255,255,255),(100,440))
        text='Sell '+totem
        text_size=min(50,int(1000/len(text)))
        write(text,text_size,(255,255,255),(640,440))
        write('GAIN: '+str(refund[2]),50,(255,255,255),(1080,440))
    else:
        write('C',50,(127,127,127),(100,440))
        write('No totem to sell',50,(127,127,127),(640,440))
    if tool!='None':
        write('D',50,(255,255,255),(100,560))
        text='Sell '+tool
        text_size=min(50,int(1000/len(text)))
        write(text,text_size,(255,255,255),(640,560))
        write('GAIN: '+str(refund[3]),50,(255,255,255),(1080,560))
    else:
        write('D',50,(127,127,127),(100,560))
        write('No tool to sell',50,(127,127,127),(640,560))

    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_a and weapon!='None':
                weapon='None'
                weapon2=''
                GOLD=GOLD+refund[0]
                choice=0
            elif event.key==K_b and armor!='None':
                armor='None'
                armor2=''
                GOLD=GOLD+refund[1]
                choice=0
            elif event.key==K_c and totem!='None':
                totem='None'
                totem2=''
                GOLD=GOLD+refund[2]
                choice=0
            elif event.key==K_d and tool!='None':
                tool='None'
                tool2=''
                GOLD=GOLD+refund[3]
                choice=0
            elif event.key==K_e:
                choice=0

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()
    fps.tick(60)

if you_HP<=0:
    win.fill((0,0,0))
    write('GAME OVER',200,(255,0,0),(640,360))
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)

if you_HP>0:
    getEXP()
    
music_shelter.stop()
