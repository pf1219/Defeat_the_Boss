music_main.play(-1)
seed=-1
difficulty=0
gamemode=0

while True:
    win2.fill((0,0,0))
    cont=1

    write2('DEFEAT THE BOSS',150,(255,0,0),(960,240))
    write2('- A Roguelike Adventure -',75,(0,255,0),(960,370))

    PLAY=Rect(0,0,320,150)
    PLAY.center=(960,600)
    py.draw.rect(win2,(0,0,255),PLAY)
    write2("PLAY",100,(255,255,255),(960,600))

    QUIT=Rect(0,0,240,100)
    QUIT.center=(760,800)
    py.draw.rect(win2,(255,0,0),QUIT)
    write2("QUIT",50,(255,255,255),(760,800))

    CREDIT=Rect(0,0,240,100)
    CREDIT.center=(1160,800)
    py.draw.rect(win2,(0,255,0),CREDIT)
    write2("CREDIT",50,(255,255,255),(1160,800))

    write2('LHS1219',60,(255,255,255),(960,1000))

    if seed==-1:
        write2('Press number key to enter seeds',15,(127,127,127),(160,1050))
    else:
        write2('SEED: '+str(seed),15,(127,127,127),(100,1050))

    write2('Beta 0.1 (2024.10.28)',25,(255,255,255),(1730,1040))

    write2('DIFFICULTY',25,(255,255,255),(1600,50))
    DIF=Rect(0,0,170,50)
    DIF.center=(1780,50)
    if difficulty==0:
        py.draw.rect(win2,(127,127,255),DIF)
        write2('EASY',25,(0,0,0),DIF.center)
    elif difficulty==1:
        py.draw.rect(win2,(127,255,127),DIF)
        write2('NORMAL',25,(0,0,0),DIF.center)
    elif difficulty==2:
        py.draw.rect(win2,(255,127,127),DIF)
        write2('HARD',25,(0,0,0),DIF.center)
    elif difficulty==3:
        py.draw.rect(win2,(127,127,127),DIF)
        write2('EXTREME',25,(0,0,0),DIF.center)

    write2('GAMEMODE',25,(255,255,255),(140,50))
    GM=Rect(0,0,170,50)
    GM.center=(320,50)
    if gamemode==0:
        py.draw.rect(win2,(255,255,0),GM)
        write2('TOWER',25,(0,0,0),GM.center)
    elif gamemode==1:
        py.draw.rect(win2,(255,255,0),GM)
        write2('FLAT',25,(0,0,0),GM.center)

    write2('COMBAT CONTROL',25,(255,255,255),(820,50))
    CTR=Rect(0,0,170,50)
    CTR.center=(1050,50)
    if combat_control==0:
        py.draw.rect(win2,(255,255,0),CTR)
        write2('KEYBOARD',25,(0,0,0),CTR.center)
    elif combat_control==1:
        py.draw.rect(win2,(255,255,0),CTR)
        write2('MOUSE',25,(0,0,0),CTR.center)

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if PLAY.collidepoint(event.pos):
                cont=0
            if CREDIT.collidepoint(event.pos):
                exec(open(path('credit.py'),encoding='utf-8').read())
            if QUIT.collidepoint(event.pos):
                py.quit()
                sys.exit()
            if DIF.collidepoint(event.pos):
                difficulty=difficulty+1
                if difficulty>3:
                    difficulty=0
            if GM.collidepoint(event.pos):
                gamemode=1-gamemode
            if CTR.collidepoint(event.pos):
                combat_control=1-combat_control
        elif event.type==KEYDOWN:
            if event.key==K_DELETE:
                seed=-1
            elif event.key==K_KP_ENTER:
                cont=0
            elif event.key >= 48 and event.key <= 57:
                new_digit=event.key-48
                if seed==-1:
                    seed=new_digit
                elif seed*10+new_digit <= 9999999999:
                    seed=seed*10+new_digit
            elif event.key >= K_KP_1 and event.key <= K_KP_0:
                if event.key==K_KP_0:
                    new_digit=0
                else:
                    new_digit=event.key-K_KP_1+1
                if seed==-1:
                    seed=new_digit
                elif seed*10+new_digit <= 9999999999:
                    seed=seed*10+new_digit
            elif event.key==K_BACKSPACE:
                if seed!=-1:
                    seed=seed//10

    if cont==0:
        break

    py.display.update()
    fps.tick(60)

music_main.stop()
if seed==-1:
    random.seed(int((time.time()*10000000)%10000000000))
    seed_digit=[random.randint(0,9) for i in range(10)]
    seed=0
    for i in range(10):
        seed=seed*10+seed_digit[i]

if difficulty==0:
    GOLD=20
    you_HP=20
    MS=2
    AST=1
    ASP=-3
    BSP=2
    BSZ=2
elif difficulty==1:
    GOLD=10
    you_HP=15
elif difficulty==2:
    GOLD=0
    you_HP=10
else:
    GOLD=0
    you_HP=5
    MS=-2
    ASP=3
    BSP=-2
    BSZ=-2
