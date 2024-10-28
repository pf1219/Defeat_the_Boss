py.event.clear()
music_explore.play(-1)

# 1 Combat
# 2 Encounter
# 3 Inspect
# 4 Market
# 5 Shelter
# 6 Boss

random.seed(seed)
map2=[[[[0 for j in range(5)] for i in range(5)] for k in range(7)] for l in range(7)]
floor=0
chunk=[3,3]
boss_chunk=[random.randint(0,6),random.randint(0,6)]
pos=random.choice([[0,2],[4,2],[2,0],[2,4]])
visited=[]
defeated_chunk=[]
defeated_chunk.append(chunk.copy())
combat_chunk=[]
if difficulty==0:
    exploration=15
elif difficulty==0:
    exploration=10
elif difficulty==0:
    exploration=8
elif difficulty==0:
    exploration=5

timer=600
while timer>0:
    timer=timer-1
    win2.fill((255,255,255))

    write2("FLAT GAMEMODE",100,(0,0,0),(960,100))

    write2("GAIN MAP",80,(0,0,0),(960,300))
    write2("Win Combat (MAP +2)",60,(0,0,0),(960,400))
    write2("Level Up (MAP +3)",60,(0,0,0),(960,480))

    write2("SPEND MAP",80,(0,0,0),(960,640))
    write2("Explore, Inspect, Market, Shelter (MAP -1)",60,(0,0,0),(960,740))
    write2("Move to new region (MAP -1)",60,(0,0,0),(960,820))

    write2("Click to continue...",40,(0,0,0),(960,960))

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            timer=-1
        
    py.display.update()
    fps.tick(60)

for l in range(7):
    for k in range(7):
        for i in [1,2,3]:
            for j in [1,2,3]:
                if difficulty==0:
                    map2[l][k][j][i]=random.choice([0]*38+[5]*3+[2]*3+[3]*6+[4]*4)
                elif difficulty==1:
                    map2[l][k][j][i]=random.choice([0]*39+[5]*2+[2]*3+[3]*6+[4]*4)
                elif difficulty==2:
                    map2[l][k][j][i]=random.choice([0]*39+[5]*1+[2]*3+[3]*6+[4]*4)
                else:
                    map2[l][k][j][i]=random.choice([0]*40+[2]*3+[3]*6+[4]*4)
        if random.random()<0.5 or [l,k]==[3,3]:
            map2[l][k][random.randint(1,3)][random.randint(1,3)]=1
            add_combat=True
        else:
            add_combat=False
        if [l,k]==boss_chunk:
            if not add_combat:
                map2[l][k][random.randint(1,3)][random.randint(1,3)]=1
            while True:
                boss_i=random.randint(1,3)
                boss_j=random.randint(1,3)
                if map2[l][k][boss_i][boss_j]!=1:
                    map2[l][k][boss_i][boss_j]=6
                    break

while True:
    win2.fill((255,255,255))
    write2('EXPLORE',50,(0,0,0),(960,50))
    write2('SEED: '+str(seed),15,(127,127,127),(1820,1065))
    game_end=0

    level=LV(EXP)
    floor=level
    if floor>7:
        floor=7
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
                if (pos[1]+1) in range(5) and (map2[chunk[0]][chunk[1]][pos[0]][pos[1]+1] in [0,1] or exploration>0):
                    pos[1]=pos[1]+1
                    if map2[chunk[0]][chunk[1]][pos[0]][pos[1]] not in [0,1]:
                        exploration=exploration-1
                elif pos[1]==4 and chunk[1]<6 and (exploration>0 or [chunk[0],chunk[1]+1] in defeated_chunk):
                    chunk[1]=chunk[1]+1
                    pos[1]=0
                    if chunk not in defeated_chunk:
                        exploration=exploration-1
                        defeated_chunk.append(chunk.copy())
            elif event.key==K_UP or event.key==K_KP_8:
                if (pos[1]-1) in range(5) and (map2[chunk[0]][chunk[1]][pos[0]][pos[1]-1] in [0,1] or exploration>0):
                    pos[1]=pos[1]-1
                    if map2[chunk[0]][chunk[1]][pos[0]][pos[1]] not in [0,1]:
                        exploration=exploration-1
                elif pos[1]==0 and chunk[1]>0 and (exploration>0 or [chunk[0],chunk[1]-1] in defeated_chunk):
                    chunk[1]=chunk[1]-1
                    pos[1]=4
                    if chunk not in defeated_chunk:
                        exploration=exploration-1
                        defeated_chunk.append(chunk.copy())
            elif event.key==K_RIGHT or event.key==K_KP_6:
                if (pos[0]+1) in range(5) and (map2[chunk[0]][chunk[1]][pos[0]+1][pos[1]] in [0,1] or exploration>0):
                    pos[0]=pos[0]+1
                    if map2[chunk[0]][chunk[1]][pos[0]][pos[1]] not in [0,1]:
                        exploration=exploration-1
                elif pos[0]==4 and chunk[0]<6 and (exploration>0 or[chunk[0]+1,chunk[1]] in defeated_chunk):
                    chunk[0]=chunk[0]+1
                    pos[0]=0
                    if chunk not in defeated_chunk:
                        exploration=exploration-1
                        defeated_chunk.append(chunk.copy())
            elif event.key==K_LEFT or event.key==K_KP_4:
                if (pos[0]-1) in range(5) and (map2[chunk[0]][chunk[1]][pos[0]-1][pos[1]] in [0,1] or exploration>0):
                    pos[0]=pos[0]-1
                    if map2[chunk[0]][chunk[1]][pos[0]][pos[1]] not in [0,1]:
                        exploration=exploration-1
                elif pos[0]==0 and chunk[0]>0 and (exploration>0 or [chunk[0]-1,chunk[1]] in defeated_chunk):
                    chunk[0]=chunk[0]-1
                    pos[0]=4
                    if chunk not in defeated_chunk:
                        exploration=exploration-1
                        defeated_chunk.append(chunk.copy())
            if event.key==K_q:
                game_end=1

    if map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==1 and ([chunk,pos] in visited)==False:
        music_explore.stop()
        exec(open(path('combat.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
        combat_chunk.append(chunk.copy())
    elif map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==2 and ([chunk,pos] in visited)==False:
        music_explore.stop()
        exec(open(path('encounter.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
    elif map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==3 and ([chunk,pos] in visited)==False:
        music_explore.stop()
        exec(open(path('inspect2.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
    elif map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==4 and ([chunk,pos] in visited)==False:
        music_explore.stop()
        exec(open(path('market.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
    elif map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==5 and ([chunk,pos] in visited)==False:
        music_explore.stop()
        exec(open(path('shelter.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
    elif map2[chunk[0]][chunk[1]][pos[0]][pos[1]]==6 and ([chunk,pos] in visited)==False and (chunk in combat_chunk):
        music_explore.stop()
        pos=[9,1]
        exec(open(path('combat.py'),encoding='utf-8').read())
        music_explore.play(-1)
        py.event.clear()
        visited.append([chunk.copy(),pos.copy()].copy())
        music_explore.stop()
        break

    if game_end==1 or you_HP<=0:
        break

    draw_status()
    draw_map2(map2,chunk,pos)
    
    draw_item()
    py.display.update()
    fps.tick(60)
