# Initialization
if gamemode==0:
    random.seed(seed+(floor*100+pos[0]*10+pos[1])*931225)
else:
    random.seed(seed+(chunk[0]*1000+chunk[1]*100+pos[0]*10+pos[1])*931225)
py.event.clear()
music_encounter.play(-1)
EXP_gain=0

win2.fill((255,255,255))
write2('ENCOUNTER',50,(0,0,0),(960,50))

win.blit(bg2,(0,0))
win_rect=win.get_rect(center=(960,440))
win2.blit(win,win_rect)
draw_status()
draw_item()
py.display.update()

time.sleep(0.5)

# Pick Result
result=random.choice(range(len(encounter_list)))
result2=encounter_list[result]

# Show Result
while True:
    win.fill((0,0,0))
    win.blit(bg2,(0,0))
    choice=0

    FS=round(min(1800/len(result2[1]),50))
    write(result2[1],FS,(255,255,255),(640,240))
    write('Press A or B key!',30,(255,255,255),(640,360))
    write(result2[2],50,(255,255,255),(640,420))
    write(result2[3],50,(255,255,255),(640,500))

    for event in py.event.get():
        if event.type==KEYDOWN:
            if event.key==K_a:
                choice=1
            elif event.key==K_b:
                choice=2

    if choice!=0:
        if result2[0]=='1':
            if choice==1:
                you_HP=you_HP-3
        elif result2[0]=='2':
            if choice==1:
                you_HP=you_HP-3
        elif result2[0]=='3':
            if choice==1:
                GOLD=GOLD+7
            elif choice==2:
                ASP=ASP-3
        elif result2[0]=='4':
            if choice==1:
                GOLD=GOLD+5
            elif choice==2:
                you_HP=you_HP-3
        elif result2[0]=='5':
            if choice==1:
                AST=AST+1
            elif choice==2:
                you_HP=you_HP+3
        elif result2[0]=='6':
            if choice==1:
                you_HP=you_HP+4
            elif choice==2:
                EXP_gain=6
        elif result2[0]=='7':
            if choice==1:
                you_HP=you_HP+6
            elif choice==2:
                MS=MS+2
        elif result2[0]=='8':
            if choice==1:
                EXP_gain=7
            elif choice==2:
                you_HP=you_HP+4
        elif result2[0]=='9':
            if choice==1:
                randomize()
                you_HP=you_HP+random.randint(-3,3)
        elif result2[0]=='10':
            if choice==1:
                EXP_gain=10
            elif choice==2:
                EXP_gain=9
                you_HP=you_HP+2
                save_event[0]=1
        elif result2[0]=='11':
            if choice==1:
                EXP_gain=10
                you_HP=you_HP-8
            elif choice==2:
                you_HP=you_HP-4
        elif result2[0]=='12':
            if choice==1:
                you_HP=you_HP+6
            elif choice==2:
                you_HP=you_HP-3
        elif result2[0]=='13':
            if choice==1:
                EXP_gain=5
        break

    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    draw_status()
    draw_item()
    py.display.update()
    fps.tick(60)

win.fill((0,0,0))
win.blit(bg2,(0,0))
if choice==1:
    FS=round(min(1800/len(result2[4]),80))
    write(result2[4],FS,(255,255,255),(640,360))
else:
    FS=round(min(1800/len(result2[5]),80))
    write(result2[5],FS,(255,255,255),(640,360))
win_rect=win.get_rect(center=(960,440))
win2.blit(win,win_rect)
py.display.update()
time.sleep(3)

if you_HP<=0:
    win.fill((0,0,0))
    write('GAME OVER',200,(255,0,0),(640,360))
    win_rect=win.get_rect(center=(960,440))
    win2.blit(win,win_rect)
    py.display.update()
    time.sleep(2)

if you_HP>0:
    getEXP()
music_encounter.stop()
