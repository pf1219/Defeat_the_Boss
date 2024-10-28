# Initialization
tick=0
py.event.clear()
music_combat.play(-1)

you_cord=[960+320,720+80]
you_bul=[]
player_size=80

if gamemode==0:
    random.seed(seed+(floor*100+pos[0]*10+pos[1])*176971)
else:
    random.seed(seed+(chunk[0]*1000+chunk[1]*100+pos[0]*10+pos[1])*176971)
enemy_type=random.choice([1,2,3,4,5,7,8,9])

if pos==[9,1]:
    if save_event[1]==0:
        enemy_type=6
    elif save_event[1]==1:
        enemy_type=10

    win.fill((0,0,0))
    write('Prepare for the BOSS FIGHT...',50,(255,0,0),(640,360))
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)

    win.fill((0,0,0))
    write('HP +20',200,(255,255,255),(640,360))
    you_HP=you_HP+20
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)

if enemy_type==1:
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(6,15)+floor*12
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(3,7)+floor*1.8
    op_AST=round((random.randint(6,20)+floor*8+difficulty*8-8)/10)
    op_ASP=46-floor*3
    op_BSP=floor*3+12
    op_BSZ=floor+6
    TPcooltime=0
    op_col=(255,0,0)
elif enemy_type==2: # Teleport
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(4,10)+floor*8
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=0
    op_AST=round((random.randint(5,18)+floor*6+difficulty*6-6)/10)
    op_ASP=55-floor*3
    op_BSP=floor*2.5+10
    op_BSZ=floor+6
    TPcooltime=220-floor*18
    op_col=(255,127,0)
elif enemy_type==3:
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(4,10)+floor*10
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(2,5)+floor*1.4
    op_AST=round((random.randint(5,18)+floor*6+difficulty*6-6)/10)
    op_ASP=60-floor*3
    op_BSP=floor*2+6
    op_BSZ=floor+6
    TPcooltime=0
    op_col=(255,0,127)
elif enemy_type==4:
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(4,10)+floor*10
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=0
    op_AST=round((random.randint(5,18)+floor*6+difficulty*6-6)/10)
    op_ASP=40-floor*3
    op_BSP=floor*3+10
    op_BSZ=floor+6
    TPcooltime=int(45-floor*4.5)
    op_col=(127,0,255)
elif enemy_type==5: # Random
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(6,15)+floor*10
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(3,6)+floor*1.6
    op_AST=round((random.randint(6,20)+floor*8+difficulty*8-8)/18)
    op_ASP=33-floor*2
    op_BSP=floor+6
    op_BSZ=floor+3
    TPcooltime=0
    op_col=(127,255,0)
elif enemy_type==6:
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=100
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=16
    op_AST=8+difficulty*2-2
    op_ASP=20
    op_BSP=18
    op_BSZ=12
    TPcooltime=180
    op_col=(127,127,127)
elif enemy_type==7:
    op_cord=[random.randint(340,940)+320,80]
    op_HP=random.randint(6,15)+floor*10
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(3,6)+floor*1.6
    op_AST=round((random.randint(6,20)+floor*8+difficulty*8-8)/20)
    op_ASP=80-floor*4
    op_BSP=floor+6
    op_BSZ=floor+3
    TPcooltime=0
    op_col=(200,0,200)
elif enemy_type==8: # Offspeed
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(6,15)+floor*12
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(3,7)+floor*1.8
    op_AST=round((random.randint(6,20)+floor*6+difficulty*6-6)/15)
    op_ASP=45-floor*3
    op_BSP=floor*2+9
    op_BSZ=floor+6
    TPcooltime=0
    op_col=(200,200,0)
elif enemy_type==9:
    op_cord=[random.randint(340,940)+320,0+80]
    op_HP=random.randint(4,10)+floor*10
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=random.randint(2,5)+floor*1.4
    op_AST=round((random.randint(5,18)+floor*6+difficulty*6-6)/10)
    op_ASP=60-floor*3
    op_BSP=floor*2+6
    op_BSZ=floor+6
    TPcooltime=0
    op_col=(0,255,127)
elif enemy_type==10:
    op_cord=[random.randint(340,940)+320,80]
    op_HP=80
    op_bul=[]
    op_buldir=[]
    op_bulspd=[]
    op_MS=18
    op_AST=5+difficulty
    op_AST=0
    op_ASP=15
    op_BSP=12
    op_BSZ=10
    shield=10
    shield_size=80
    shield_cord=[random.randint(340,940)+320,80]
    TPcooltime=0
    op_col=(127,127,127)
    
rage_damage=random.randint(1,2)
phase=1
visible=1

if enemy_type==2:
    TP_left=TPcooltime
elif enemy_type==4:
    TP_left=1
elif enemy_type==6:
    TP_left=TPcooltime
refractory=0
move=0
direction=1
col1=0
col2=0
tool_duration=0
if op_AST<1:
    op_AST=1

random.seed(int((time.time()*10000000)%1000000000))

while True:
    win2.fill((255,255,255))
    R=Rect(320,80,1280,720)
    win2.fill((0,0,0),R)
    tick=tick+1
    end=0

# Input
    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_q:
                you_HP=0
                end=1
            if event.key==K_KP_1:
                end=1
            if event.key==K_x and tool_used==0:
                tool_used=1
                tool_duration=tool_time*60
                you_MS=you_MS+tMS
                you_AST=you_AST+tAST
                you_ASP=you_ASP+tASP
                you_BSP=you_BSP+tBSP
                you_BSZ=you_BSZ+tBSZ
                you_DOD=you_DOD+tDOD
                you_HP=you_HP+tHP
                in_range()
        elif event.type==MOUSEBUTTONDOWN:
            if event.button==3:
                tool_used=1
                tool_duration=tool_time*60
                you_MS=you_MS+tMS
                you_AST=you_AST+tAST
                you_ASP=you_ASP+tASP
                you_BSP=you_BSP+tBSP
                you_BSZ=you_BSZ+tBSZ
                you_DOD=you_DOD+tDOD
                you_HP=you_HP+tHP
                in_range()

    if tool_duration>0:
        write2('TOOL ACTIVE',30,(0,0,0),(1800,1000))
        LS=math.ceil(tool_duration/60)
        write2('LEFT: '+str(LS),50,(0,0,0),(1800,900))
        tool_duration=tool_duration-1
    if tool_duration==1:
        you_MS=you_MS-tMS
        you_AST=you_AST-tAST
        you_ASP=you_ASP-tASP
        you_BSP=you_BSP-tBSP
        you_BSZ=you_BSZ-tBSZ
        you_DOD=you_DOD-tDOD
        in_range()

    if combat_control==0:
        keys=py.key.get_pressed()
        if keys[K_RIGHT] or keys[K_d] or keys[K_KP_6]:
            you_cord[0]=you_cord[0]+you_MS
        if keys[K_LEFT] or keys[K_a] or keys[K_KP_4]:
            you_cord[0]=you_cord[0]-you_MS
        if (keys[K_SPACE] or keys[K_KP_8]) and refractory==0:
            you_bul.append([you_cord[0],you_cord[1]])
            refractory=you_ASP
    else:
        mpos=py.mouse.get_pos()
        if mpos[0]>(you_cord[0]+you_MS):
            you_cord[0]=you_cord[0]+you_MS
        elif mpos[0]<(you_cord[0]-you_MS):
            you_cord[0]=you_cord[0]-you_MS
        if py.mouse.get_pressed()[0] and refractory==0:
            you_bul.append([you_cord[0],you_cord[1]])
            refractory=you_ASP

    if you_cord[0]<320+player_size:
        you_cord[0]=320+player_size
    if you_cord[0]>1600-player_size:
        you_cord[0]=1600-player_size

    if refractory>0:
        refractory=refractory-1

# Opponent Move
    if enemy_type==1:
        move=move+1
        k=op_MS/10
        if random.random()<((-20+move)/1200*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(0)
            op_bulspd.append(op_BSP)
    elif enemy_type==2:
        TP_left=TP_left-1
        if TP_left==0:
            op_cord[0]=random.randint(340,940)+320
            TP_left=TPcooltime
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(0)
            op_bulspd.append(op_BSP)
    elif enemy_type==3:
        move=move+1
        k=op_MS/10
        if random.random()<((-25+move)/1400*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            k=(-1*op_cord[0]+you_cord[0])/(720/op_BSP)
            op_buldir.append(k)
            op_bulspd.append(op_BSP)
    elif enemy_type==4:
        TP_left=TP_left-1
        if TP_left==0:
            op_MS=(-1*op_cord[0]+you_cord[0])/TPcooltime
            TP_left=TPcooltime
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(0)
            op_bulspd.append(op_BSP)
    elif enemy_type==5:
        move=move+1
        k=op_MS/10
        if random.random()<((-20+move)/1200*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(random.randint(-5,5))
            op_bulspd.append(op_BSP)
    elif enemy_type==7:
        move=move+1
        k=op_MS/10
        if random.random()<((-20+move)/1200*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(-op_BSP*0.6)
            op_bulspd.append(op_BSP)
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(0)
            op_bulspd.append(op_BSP)
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(op_BSP*0.6)
            op_bulspd.append(op_BSP)
    elif enemy_type==8:
        move=move+1
        k=op_MS/10
        if random.random()<((-20+move)/1200*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(0)
            op_bulspd.append((0.2+random.random())*op_BSP)
    elif enemy_type==9:
        move=move+1
        k=op_MS/10
        if random.random()<((-25+move)/1400*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(random.choice([-1,1]))
            op_bulspd.append(op_BSP)
    elif enemy_type==10:
        move=move+1
        k=op_MS/10
        if random.random()<((-20+move)/1200*k) or op_cord[0]<(320+player_size) or op_cord[0]>(1600-player_size):
            direction=direction*-1
            move=0
        op_cord[0]=op_cord[0]+direction*op_MS
        if tick%op_ASP==1:
            op_bul.append([op_cord[0],op_cord[1]])
            op_buldir.append(random.randint(-5,5))
            op_bulspd.append(op_BSP)
        if shield==0:
            op_col=(127,0,0)
    elif enemy_type==6:
        TP_left=TP_left-1
        if op_HP<25:
            op_col=(125,0,0)
            op_AST=11+difficulty*2-2
            op_BSP=24
            op_MS=28
            rage_damage=random.randint(2,4)
            phase=4
        elif op_HP<50:
            op_col=(155,70,70)
            op_AST=10+difficulty*2-2
            op_BSP=22
            op_MS=24
            rage_damage=random.randint(1,4)
            phase=3
        elif op_HP<75:
            op_col=(145,100,100)
            op_AST=9+difficulty*2-2
            op_BSP=20
            op_MS=20
            rage_damage=random.randint(1,3)
            phase=2
        else:
            rage_damage=random.randint(1,2)
        if TP_left>90:
            op_cord[0]=random.randint(320+player_size,1600-player_size)
            visible=0
            if TP_left in [134,135,136]:
                win2.fill(op_col,R)
            if TP_left==135:
                if random.randint(1,100)<=you_DOD:
                    damage1=0
                    hit_dodge.play()
                else:
                    damage1=rage_damage
                    hit_player.play()
                you_HP=you_HP-damage1
                col1=10
        else:
            visible=1
            if TP_left%10==0:
                k=random.choice([-1,1])*random.randint(int(op_MS*0.5),op_MS)
                op_cord[0]=op_cord[0]+k
                if op_cord[0]<(320+player_size):
                    op_cord[0]=(350+player_size)
                if op_cord[0]>(1600-player_size):
                    op_cord[0]=(1580-player_size)
            py.draw.circle(win2,op_col,op_cord,player_size)
            if tick%op_ASP==1:
                op_bul.append([op_cord[0],op_cord[1]])
                k=(-1*op_cord[0]+you_cord[0])/(720/op_BSP)+random.randint(-5,5)
                op_buldir.append(k)
                op_bulspd.append(op_BSP)
        if TP_left==0:
            TP_left=TPcooltime

# Draw Player, Enemy
    if enemy_type!=6:
        py.draw.circle(win2,op_col,op_cord,player_size)
    if enemy_type==10 and shield>0:
        py.draw.circle(win2,(255,255,255),shield_cord,shield_size)
    py.draw.circle(win2,(0,0,255),you_cord,player_size)

# Draw Bullet
    for i in range(len(you_bul)):
        if you_bul[i][1]>80:
            you_bul[i][1]=you_bul[i][1]-you_BSP
            py.draw.circle(win2,(0,0,255),you_bul[i],you_BSZ)
            if enemy_type==10:
                if distance(you_bul[i],op_cord)<(player_size+you_BSZ) and shield==0:
                    you_bul[i][1]=-1000
                    op_HP=op_HP-you_AST
                    col2=10
                    damage2=you_AST
                    hit_enemy.play()
                elif distance(you_bul[i],op_cord)<(player_size+you_BSZ) and shield>0:
                    you_bul[i][1]=-1000
                elif distance(you_bul[i],shield_cord)<(shield_size+you_BSZ) and shield>0:
                    you_bul[i][1]=-1000
                    shield=shield-1
                    shield_size=30+shield*5
                    shield_cord=[random.randint(340,940)+320,80]
                    hit_enemy.play()
            elif distance(you_bul[i],op_cord)<(player_size+you_BSZ) and visible==1:
                you_bul[i][1]=-1000
                op_HP=op_HP-you_AST
                col2=10
                damage2=you_AST
                hit_enemy.play()
            if you_bul[i][0]<320 or you_bul[i][0]>1600:
                you_bul[i][1]=-1000
    for i in range(len(op_bul)):
        if op_bul[i][1]<800:
            if enemy_type==9:
                op_bul[i][0]=op_bul[i][0]+op_buldir[i]*op_bulspd[i]*(op_bul[i][1]-80)/720
            else:
                op_bul[i][0]=op_bul[i][0]+op_buldir[i]
            op_bul[i][1]=op_bul[i][1]+op_bulspd[i]
            py.draw.circle(win2,op_col,op_bul[i],op_BSZ)
            if distance(op_bul[i],you_cord)<(player_size+op_BSZ):
                op_bul[i][1]=2000
                if random.randint(1,100)<=you_DOD:
                    damage1=0
                    hit_dodge.play()
                else:
                    damage1=op_AST
                    hit_player.play()
                you_HP=you_HP-damage1
                col1=10
            if op_bul[i][0]<320 or op_bul[i][0]>1600:
                op_bul[i][1]=3000

    if you_HP<0:
        you_HP=0
    if op_HP<0:
        op_HP=0

    R=Rect(320,800,1280,player_size)
    py.draw.rect(win2,(255,255,255),R)
    R=Rect(320,80-player_size,1280,player_size)
    py.draw.rect(win2,(255,255,255),R)
    write2('COMBAT',50,(0,0,0),(960,50))

# Inform Left HP
    icon_heart_rect=icon_heart.get_rect(center=(490,50))
    win2.blit(icon_heart,icon_heart_rect)
    icon_heart_rect=icon_heart.get_rect(center=(1410,50))
    win2.blit(icon_heart,icon_heart_rect)
    if col1>0:
        write2('YOUR HP: '+str(you_HP),30,(0,0,255),(360,50))
        write2(str(damage1),damage1*5+20,(0,0,255),[you_cord[0]+20,you_cord[1]-120])
        col1=col1-1
    else:
        write2('YOUR HP: '+str(you_HP),30,(0,0,0),(360,50))
    if col2>0 and enemy_type!=6:
        write2('ENEMY HP: '+str(op_HP),30,op_col,(1560,50))
        write2(str(damage2),damage2*5+20,op_col,[op_cord[0]+20,op_cord[1]+120])
        col2=col2-1
    else:
        write2('ENEMY HP: '+str(op_HP),30,(0,0,0),(1560,50))

    if enemy_type==6:
        if col2>0 and TP_left<=90:
            write2('ENEMY HP: '+str(op_HP),30,op_col,(1560,50))
            write2(str(damage2),damage2*5+20,op_col,[op_cord[0]+20,op_cord[1]+120])
        else:
            write2('ENEMY HP: '+str(op_HP),30,(0,0,0),(1560,50))
        col2=col2-1

    draw_item2()
    enemy()

    py.display.update()
    if tick==1:
        time.sleep(0.5)
    fps.tick(60)

# Combat result
    if op_HP<=0 or you_HP<=0 or end==1:
        time.sleep(1)
        if you_HP<=0:
            win.fill((0,0,0))
            write('GAME OVER',200,(255,0,0),(640,360))
            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            py.display.update()
            time.sleep(2)
            break
        else:
            win.fill((0,0,0))
            write('YOU WON!',200,(255,255,255),(640,360))
            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            py.display.update()
            time.sleep(2)

            win.fill((0,0,0))
            EXP_gain=random.randint(5,10)+floor
            GOLD_gain=random.randint(0,6)+floor
            write('EXP +'+str(EXP_gain),150,(255,255,255),(640,260))
            write('GOLD +'+str(GOLD_gain),150,(255,255,255),(640,460))
            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            py.display.update()
            time.sleep(2)

            if gamemode==1:
                gamemode1()
            getEXP()
            GOLD=GOLD+GOLD_gain

            break

music_combat.stop()
