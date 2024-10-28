py.event.clear()
music_explore.play(-1)

# 1 Combat
# 2 Encounter
# 3 Inspect
# 4 Market

random.seed(seed+floor*224179)

map=[[0 for j in range(3)] for i in range(floor+3)]
for i in range(floor+3):
    for j in range(3):
        if difficulty==0:
            map[i][j]=random.choice([0]*28+[5]*3+[1]*2+[2]*3+[3]*6+[4]*4)
        elif difficulty==1:
            map[i][j]=random.choice([0]*29+[5]*2+[1]*2+[2]*3+[3]*6+[4]*4)
        elif difficulty==2:
            map[i][j]=random.choice([0]*29+[5]*1+[1]*3+[2]*3+[3]*6+[4]*4)
        else:
            map[i][j]=random.choice([0]*30+[1]*3+[2]*3+[3]*6+[4]*4)
map[0][1]=0
map[floor+2][1]=1
pos=[0,1]
visited=[]

while True:
    win2.fill((255,255,255))
    write2('EXPLORE',50,(0,0,0),(960,50))
    write2('SEED: '+str(seed),15,(127,127,127),(1820,1065))
    game_end=0

    level=LV(EXP)
    apply_item()
    you_MS=MS_list[level-1]+MS+iMS
    you_AST=AST_list[level-1]+AST+iAST
    you_ASP=ASP_list[level-1]+ASP+iASP
    you_BSP=BSP_list[level-1]+BSP+iBSP
    you_BSZ=BSZ_list[level-1]+BSZ+iBSZ
    you_DOD=DOD+iDOD
    in_range()
    tool_used=0

    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_DOWN or event.key==K_KP_5:
                if (pos[1]+1) in [0,1,2]:
                    pos[1]=pos[1]+1
            elif event.key==K_UP or event.key==K_KP_8:
                if (pos[1]-1) in [0,1,2]:
                    pos[1]=pos[1]-1
            elif event.key==K_RIGHT or event.key==K_KP_6:
                if (pos[0]+1) in range(floor+3):
                    pos[0]=pos[0]+1
            elif event.key==K_LEFT or event.key==K_KP_4:
                if (pos[0]-1) in range(floor+3):
                    pos[0]=pos[0]-1
            if event.key==K_q:
                game_end=1

    if map[pos[0]][pos[1]]==1 and (pos in visited)==False:
        music_explore.stop()
        exec(open(path('combat.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append(pos.copy())
        if pos==[floor+2,1]:
            music_explore.stop()
            break
    elif map[pos[0]][pos[1]]==2 and (pos in visited)==False:
        music_explore.stop()
        exec(open(path('encounter.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append(pos.copy())
    elif map[pos[0]][pos[1]]==3 and (pos in visited)==False:
        music_explore.stop()
        exec(open(path('inspect2.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append(pos.copy())
    elif map[pos[0]][pos[1]]==4 and (pos in visited)==False:
        music_explore.stop()
        exec(open(path('market.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append(pos.copy())
    elif map[pos[0]][pos[1]]==5 and (pos in visited)==False:
        music_explore.stop()
        exec(open(path('shelter.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append(pos.copy())

    if game_end==1 or you_HP<=0:
        break

    draw_status()
    draw_map(map,pos)
    
    draw_item()
    py.display.update()
    fps.tick(60)
