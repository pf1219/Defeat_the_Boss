font_list=[py.font.Font(path('font.ttf'),i) for i in range(1,300)]
def write(string,size,color,cord):
    font=font_list[size]
    text=font.render(string,True,color)
    text_rect=text.get_rect(center=cord)
    win.blit(text,text_rect)

def write2(string,size,color,cord):
    font=font_list[size]
    text=font.render(string,True,color)
    text_rect=text.get_rect(center=cord)
    win2.blit(text,text_rect)

def distance(cord1,cord2):
    xdist=(cord1[0]-cord2[0])**2
    ydist=(cord1[1]-cord2[1])**2
    return((xdist+ydist)**0.5)

def draw_map2(map2,chunk,pos):
    global win, win2, icon_combat
    win.fill((0,0,0))
    for i in range(5):
        for j in range(5):
            R=Rect(0,0,100,100)
            R.center=[i*100+440,j*100+160]
            if map2[chunk[0]][chunk[1]][i][j]==0:
                py.draw.rect(win,(255,255,255),R)
            if map2[chunk[0]][chunk[1]][i][j]==2:
                if [chunk,[i,j]] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(0,255,0),R)
                icon_encounter_rect=icon_encounter.get_rect(center=[i*100+440,j*100+160])
                win.blit(icon_encounter,icon_encounter_rect)
            if map2[chunk[0]][chunk[1]][i][j]==3:
                if [chunk,[i,j]] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(0,0,255),R)
                icon_inspect_rect=icon_inspect.get_rect(center=[i*100+440,j*100+160])
                win.blit(icon_inspect,icon_inspect_rect)
            if map2[chunk[0]][chunk[1]][i][j]==4:
                if [chunk,[i,j]] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(255,180,0),R)
                icon_market_rect=icon_market.get_rect(center=[i*100+440,j*100+160])
                win.blit(icon_market,icon_market_rect)
            if map2[chunk[0]][chunk[1]][i][j]==5:
                if [chunk,[i,j]] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(160,0,255),R)
                icon_shelter_rect=icon_shelter.get_rect(center=[i*100+440,j*100+160])
                win.blit(icon_shelter,icon_shelter_rect)
            if map2[chunk[0]][chunk[1]][i][j]==1:
                if [chunk,[i,j]] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(255,0,0),R)
                icon_combat_rect=icon_combat.get_rect(center=[i*100+440,j*100+160])
                win.blit(icon_combat,icon_combat_rect)
            if map2[chunk[0]][chunk[1]][i][j]==6:
                if chunk not in combat_chunk:
                    py.draw.rect(win,(255,255,255),R)
                else:
                    py.draw.rect(win,(90,60,110),R)
                    icon_boss_rect=icon_boss.get_rect(center=[i*100+440,j*100+160])
                    win.blit(icon_boss,icon_boss_rect)

    icon_pawn_rect=icon_pawn.get_rect(center=[pos[0]*100+440,pos[1]*100+160])
    win.blit(icon_pawn,icon_pawn_rect)

    write('Use arrow keys to explore',30,(255,255,255),(1025,680))
    if chunk not in defeated_chunk:
        write('Win combat to move beyond',30,(255,255,255),(255,680))
    
    icon_up_rect=icon_up.get_rect(center=[2*100+440,-1*100+160])
    if chunk[1]>0 and (exploration>0 or [chunk[0],chunk[1]-1] in defeated_chunk):
        if [chunk[0],chunk[1]-1] in defeated_chunk:
            win.blit(icon_up2,icon_up_rect)
        else:
            win.blit(icon_up,icon_up_rect)
    icon_down_rect=icon_down.get_rect(center=[2*100+440,5*100+160])
    if chunk[1]<6 and (exploration>0 or [chunk[0],chunk[1]+1] in defeated_chunk):
        if [chunk[0],chunk[1]+1] in defeated_chunk:
            win.blit(icon_down2,icon_down_rect)
        else:
            win.blit(icon_down,icon_down_rect)
    icon_right_rect=icon_right.get_rect(center=[5*100+440,2*100+160])
    if chunk[0]<6 and (exploration>0 or [chunk[0]+1,chunk[1]] in defeated_chunk):
        if [chunk[0]+1,chunk[1]] in defeated_chunk:
            win.blit(icon_right2,icon_right_rect)
        else:
            win.blit(icon_right,icon_right_rect)
    icon_left_rect=icon_left.get_rect(center=[-1*100+440,2*100+160])
    if chunk[0]>0 and (exploration>0 or [chunk[0]-1,chunk[1]] in defeated_chunk):
        if [chunk[0]-1,chunk[1]] in defeated_chunk:
            win.blit(icon_left2,icon_left_rect)
        else:
            win.blit(icon_left,icon_left_rect)

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)


def draw_map(map,pos):
    global win, win2, icon_combat, floor
    win.fill((0,0,0))
    for i in range(len(map)):
        for j in [1,0,2]:
            R=Rect(0,0,100,100)
            R.center=[i*100+180,j*100+260]
            if map[i][j]==0:
                py.draw.rect(win,(255,255,255),R)
            if map[i][j]==2:
                if [i,j] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(0,255,0),R)
                icon_encounter_rect=icon_encounter.get_rect(center=[i*100+180,j*100+260])
                win.blit(icon_encounter,icon_encounter_rect)
            if map[i][j]==3:
                if [i,j] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(0,0,255),R)
                icon_inspect_rect=icon_inspect.get_rect(center=[i*100+180,j*100+260])
                win.blit(icon_inspect,icon_inspect_rect)
            if map[i][j]==4:
                if [i,j] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(255,180,0),R)
                icon_market_rect=icon_market.get_rect(center=[i*100+180,j*100+260])
                win.blit(icon_market,icon_market_rect)
            if map[i][j]==5:
                if [i,j] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(160,0,255),R)
                icon_shelter_rect=icon_shelter.get_rect(center=[i*100+180,j*100+260])
                win.blit(icon_shelter,icon_shelter_rect)
            if map[i][j]==1:
                if [i,j] in visited:
                    py.draw.rect(win,(160,160,160),R)
                else:
                    py.draw.rect(win,(255,0,0),R)
                icon_combat_rect=icon_combat.get_rect(center=[i*100+180,j*100+260])
                win.blit(icon_combat,icon_combat_rect)
            if i==(floor+2) and j==1:
                R2=Rect(0,0,105,105)
                R2.center=[i*100+180,j*100+260]
                py.draw.rect(win,(255,255,0),R2,5)

    icon_pawn_rect=icon_pawn.get_rect(center=[pos[0]*100+180,pos[1]*100+260])
    win.blit(icon_pawn,icon_pawn_rect)

    write('FLOOR '+str(floor),75,(255,255,255),(640,100))
    write('Use arrow keys to explore!',30,(255,255,255),(640,640))

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)

def LV(EXP):
    LV_list=[0,15,35,60,90,125,170,210]
    k=sum([int(EXP>=LV_list[i]) for i in range(len(LV_list))])
    return(k)

you_MS=0
you_AST=0
you_ASP=0
you_BSP=0
you_BSZ=0
def draw_status():
    LV_list=[0,15,35,60,90,125,170,210]
    write2('PLAYER STATS',30,(0,0,0),(165,170))
    write2('LV '+str(level),60,(0,0,0),(165,240))
    if level==8:
        write2('EXP '+str(EXP)+'/MAX',25,(0,0,0),(165,290))
    else:
        write2('EXP '+str(EXP)+'/'+str(LV_list[level]),25,(0,0,0),(165,290))
    write2('Move Speed',25,(0,0,0),(140,340))
    write2('Attack Strength',25,(0,0,0),(140,380))
    write2('Attack Cooltime',25,(0,0,0),(140,420))
    write2('Bullet Speed',25,(0,0,0),(140,460))
    write2('Bullet Size',25,(0,0,0),(140,500))
    write2('Dodge Percentage',25,(0,0,0),(140,540))
    write2(str(you_MS),25,(0,0,255),(285,340))
    write2(str(you_AST),25,(0,0,255),(285,380))
    write2(str(you_ASP),25,(255,0,0),(285,420))
    write2(str(you_BSP),25,(0,0,255),(285,460))
    write2(str(you_BSZ),25,(0,0,255),(285,500))
    write2(str(you_DOD),25,(0,0,255),(285,540))

    write2('GOLD '+str(GOLD),50,(220,180,0),(165,605))
    if gamemode==1:
        write2('MAP '+str(exploration),50,(0,180,255),(165,670))

    icon_heart_rect=icon_heart.get_rect(center=(490,50))
    win2.blit(icon_heart,icon_heart_rect)
    write2('YOUR HP: '+str(you_HP),30,(0,0,0),(360,50))

def draw_item():
    write2('ITEMS',40,(0,0,0),(165,950))
    write2('WEAPON',30,(0,0,0),(350,860))
    write2('ARMOR',30,(0,0,0),(350,920))
    write2('TOTEM',30,(0,0,0),(350,980))
    write2('TOOL',30,(0,0,0),(350,1040))
    write2(weapon+': '+weapon2,30,(0,0,0),(1200,860))
    write2(armor+': '+armor2,30,(0,0,0),(1200,920))
    write2(totem+': '+totem2,30,(0,0,0),(1200,980))
    write2(tool+': '+tool2,30,(0,0,0),(1200,1040))

def draw_item2():
    if tool_used==0:
        write2('TOOL',40,(0,0,0),(165,900))
        write2(tool+': '+tool2,40,(0,0,0),(960,900))
        write2('Press X key to use the tool!',30,(0,0,0),(960,1000))
    else:
        write2('TOOL',40,(127,127,127),(165,900))
        write2(tool+': '+tool2,40,(127,127,127),(960,900))
        write2('Tool already used!',30,(127,127,127),(960,1000))
    write2('Press arrow key to move, space key to shoot.',30,(0,0,0),(960,1040))

def randomize():
    k=int(time.time()*10000)%10000000
    random.seed(k)

def apply_item():
    global iMS, iAST, iASP, iBSP, iBSZ, iDOD, tMS, tAST, tASP, tBSP, tBSZ, tDOD, tHP
    iMS=0
    iAST=0
    iASP=0
    iBSP=0
    iBSZ=0
    iDOD=0
    tMS=0
    tAST=0
    tASP=0
    tBSP=0
    tBSZ=0
    tDOD=0
    tHP=0
    if weapon=='Bow':
        iAST=iAST+1
        iASP=iASP+2
    elif weapon=='Crossbow':
        iAST=iAST+2
        iASP=iASP+5
    elif weapon=='Pistol':
        iAST=iAST+3
        iBSP=iBSP+5
        iBSZ=iBSZ-6
    elif weapon=='Shotgun':
        iBSZ=iBSZ+8
        iBSP=iBSP+10
    elif weapon=='Axe':
        iAST=iAST+4
        iBSP=iBSP-6
    elif weapon=='Blaster':
        iBSP=iBSP+25
        iBSZ=iBSZ-3
    elif weapon=='Bazooka':
        iAST=iAST+6
        iASP=iASP+18
    elif weapon=='Firework':
        iAST=iAST+3
    elif weapon=='Gatling Gun':
        iAST=iAST-1
        iASP=iASP-6
    elif weapon=='Rifle':
        iAST=iAST+3
        iBSP=iBSP+4
    elif weapon=='Machine Gun':
        iAST=iAST+5
    if armor=='Cotton Armor':
        iDOD=iDOD+15
    elif armor=='Leather Armor':
        iDOD=iDOD+20
    elif armor=='Elytra':
        iDOD=iDOD+20
        iMS=iMS+8
    elif armor=='Gold Armor':
        iDOD=iDOD+25
        iMS=iMS-4
    elif armor=='Wood Armor':
        iDOD=iDOD+30
        iASP=iASP+4
    elif armor=='Diamond Armor':
        iDOD=iDOD+40
        iMS=iMS-6
    elif armor=='Enchanted Armor':
        iDOD=iDOD+45
        iAST=iAST-1
    elif armor=='Iron Armor':
        iDOD=iDOD+35
    elif armor=='Bulletproof Vest':
        iDOD=iDOD+40
    elif armor=='Quantum Armor':
        iDOD=iDOD+50
    if totem=='Feather Sneakers':
        iMS=iMS+6
    elif totem=='Lucky Totem':
        iDOD=iDOD+15
    elif totem=='Spyglass':
        iBSZ=iBSZ+10
    elif totem=='Sneakers':
        iMS=iMS+4
    elif totem=='Scope':
        iBSZ=iBSZ+15
        iASP=iASP+3
    elif totem=='Football Boots':
        iMS=iMS+6
        iASP=iASP-2
    elif totem=='Cellphone':
        iDOD=iDOD+20
        iMS=iMS-3
    elif totem=='Baseball Glove':
        iBSP=iBSP+8
    if tool=='Golden Apple':
        tASP=tASP-6
    elif tool=='Silver Apple':
        tASP=tASP-4
    elif tool=='Diamond Melon':
        tAST=tAST+4
    elif tool=='Regeneration Potion':
        tHP=tHP+2
    elif tool=='Ultimate Strength Potion':
        tHP=tHP-2
        tAST=tAST+7
    elif tool=='Invincible Potion':
        tDOD=tDOD+60
    elif tool=="Docter's License":
        tHP=tHP+LV(EXP)+2
    elif tool=="Golden Carrot":
        tAST=tAST+2
    elif tool=="Golden Banana":
        tBSP=tBSP+15
    elif tool=="Diamond Bread":
        tBSZ=tBSZ+10

def enemy():
    global enemy_type
    write2('OPPONENT',30,op_col,(1760,200))
    if enemy_type==1:
        write2('AI Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent move randomly",20,op_col,(1760,390))
        write2("and shoots bullet.",20,op_col,(1760,420))
    elif enemy_type==2:
        write2('Teleport Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent teleports",20,op_col,(1760,390))
        write2("and shoots bullet.",20,op_col,(1760,420))
    elif enemy_type==3:
        write2('Target Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent shoots bullet",20,op_col,(1760,390))
        write2("toward your position.",20,op_col,(1760,420))
    elif enemy_type==4:
        write2('Follow Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent follows you",20,op_col,(1760,390))
        write2("and shoots bullet.",20,op_col,(1760,420))
    elif enemy_type==5:
        write2('Random Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent move randomly",20,op_col,(1760,390))
        write2("and shoots bullet randomly.",20,op_col,(1760,420))
    elif enemy_type==7:
        write2('Multiple Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent move randomly",20,op_col,(1760,390))
        write2("and shoots multiple bullets.",20,op_col,(1760,420))
    elif enemy_type==8:
        write2('Offspeed Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent move randomly",20,op_col,(1760,390))
        write2("and shoots bullet",20,op_col,(1760,420))
        write2("with variable speed.",20,op_col,(1760,450))
    elif enemy_type==9:
        write2('Curve Shooter',30,op_col,(1760,300))
        write2('Attack Strength '+str(op_AST),25,op_col,(1760,350))
        write2("Opponent move randomly",20,op_col,(1760,390))
        write2("and shoots curve bullets.",20,op_col,(1760,420))
    elif enemy_type==6:
        write2('the BOSS',40,op_col,(1760,300))
        write2('Attack Strength ?',25,op_col,(1760,350))
        write2("???",20,op_col,(1760,390))
        write2("PHASE "+str(phase),30,op_col,(1760,430))
    elif enemy_type==10:
        write2('the INVINCIBLE',35,op_col,(1760,300))
        write2('Attack Strength ?',25,op_col,(1760,350))
        write2("???",20,op_col,(1760,390))
        icon_shield_rect=icon_shield.get_rect(center=(1740,430))
        win2.blit(icon_shield,icon_shield_rect)
        write2(str(shield),30,(0,0,0),(1780,430))

def in_range():
    global you_MS, you_AST, you_ASP, you_BSP, you_BSZ, you_DOD
    if you_MS<1:
        you_MS=1
    if you_AST<1:
        you_AST=1
    if you_ASP<1:
        you_ASP=1
    if you_BSP<1:
        you_BSP=1
    if you_BSZ<1:
        you_BSZ=1

def getEXP():
    global EXP, EXP_gain, you_HP, exploration
    if LV(EXP)<LV(EXP+EXP_gain):
        timer=60
        while timer>0:
            timer=timer-1
            win.fill((0,0,0))
            write('LEVEL UP!',200,(0,0,255),(640,360))
            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            py.event.get()
            py.display.update()
            fps.tick(60)

        timer=60
        you_HP=you_HP+LV(EXP+EXP_gain)
        if gamemode==1:
            exploration=exploration+3
        while timer>0:
            timer=timer-1
            win.fill((0,0,0))
            if gamemode==1:
                write('HP +'+str(LV(EXP+EXP_gain)),200,(255,255,255),(640,240))
                write('MAP +3',200,(255,255,255),(640,480))
            else:
                write('HP +'+str(LV(EXP+EXP_gain)),200,(255,255,255),(640,360))
            win_rect=win.get_rect(center=(960,440))
            win2.blit(win,win_rect)
            py.event.get()
            py.display.update()
            fps.tick(60)
            
    EXP=EXP+EXP_gain

def gamemode1():
    global exploration
    timer=60
    exploration=exploration+2
    while timer>0:
        timer=timer-1
        win.fill((0,0,0))

        write('MAP +2',150,(255,255,255),(640,360))

        py.event.get()
        win2.blit(win,win_rect)
        py.display.update()
        fps.tick(60)
        
    if boss_chunk!=chunk:
        timer=60
        randomize()
        random_value=random.random()
        while timer>0:
            timer=timer-1
            win.fill((0,0,0))
            write("MYSTERIOUS COMPASS",60,(255,255,255),(640,50))
            if boss_chunk[0]==chunk[0]:
                if boss_chunk[1]>chunk[1]:
                    compass2=py.transform.rotate(compass,270)
                    compass2_rect=compass2.get_rect(center=(640,385))
                    win.blit(compass2,compass2_rect)
                else:
                    compass2=py.transform.rotate(compass,90)
                    compass2_rect=compass2.get_rect(center=(640,385))
                    win.blit(compass2,compass2_rect)
            elif boss_chunk[1]==chunk[1]:
                if boss_chunk[0]>chunk[0]:
                    compass2=py.transform.rotate(compass,0)
                    compass2_rect=compass2.get_rect(center=(640,385))
                    win.blit(compass2,compass2_rect)
                else:
                    compass2=py.transform.rotate(compass,180)
                    compass2_rect=compass2.get_rect(center=(640,385))
                    win.blit(compass2,compass2_rect)
            else:
                if random_value<0.5:
                    if boss_chunk[1]>chunk[1]:
                        compass2=py.transform.rotate(compass,270)
                        compass2_rect=compass2.get_rect(center=(640,385))
                        win.blit(compass2,compass2_rect)
                    else:
                        compass2=py.transform.rotate(compass,90)
                        compass2_rect=compass2.get_rect(center=(640,385))
                        win.blit(compass2,compass2_rect)
                else:
                    if boss_chunk[0]>chunk[0]:
                        compass2=py.transform.rotate(compass,0)
                        compass2_rect=compass2.get_rect(center=(640,385))
                        win.blit(compass2,compass2_rect)
                    else:
                        compass2=py.transform.rotate(compass,180)
                        compass2_rect=compass2.get_rect(center=(640,385))
                        win.blit(compass2,compass2_rect)
            py.event.get()
            win2.blit(win,win_rect)
            py.display.update()
            fps.tick(60)

