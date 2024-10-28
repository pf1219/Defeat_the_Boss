timer=600
while timer>0:
    timer=timer-1
    
    win2.fill((0,0,0))

    write2("MUSIC",80,(0,255,0),(960,80))

    write2("Encounter, Inspect, Combat Theme by LHS1219",30,(255,255,255),(960,150))
    write2("Main Screen, Explore, Market Theme by ES-Sound",30,(255,255,255),(960,200))
    write2("Evening by Kevin MacLeod (incompetech.com)",30,(255,255,255),(960,250))
    write2("Licensed under Creative Commons: By Attribution 4.0 License",20,(255,255,255),(960,280))
    write2("Player Hit, Opponent Hit, Player Dodge sound effects by Mixkit",30,(255,255,255),(960,330))
    
    write2("IMAGE",80,(0,255,0),(960,430))
    write2("Inspect background image by mali maeder",30,(255,255,255),(960,500))
    write2("pexels.com/photo/119809",20,(255,255,255),(960,530))
    write2("Encounter background image by Mark Plötz",30,(255,255,255),(960,580))
    write2("pexels.com/photo/1029696",20,(255,255,255),(960,610))
    write2("Market background image by Ricky Esquivel",30,(255,255,255),(960,660))
    write2("pexels.com/photo/1745747",20,(255,255,255),(960,690))
    write2("Shelter background image by KAL VISUALS",30,(255,255,255),(960,740))
    write2("images.unsplash.com/photo-1533243367503-0b7337004671",20,(255,255,255),(960,770))

    write2("Click to continue",30,(255,255,255),(960,900))

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            timer=-1
    py.display.update()
    fps.tick(60)

timer=600
while timer>0:
    timer=timer-1
    
    win2.fill((0,0,0))

    write2("ICON",80,(0,255,0),(960,80))

    write2("Boss icon by Royyan Wijaya",30,(255,255,255),(960,150))
    write2("flaticon.com/free-icon/mask_5825274",20,(255,255,255),(960,180))

    write2("Combat icon by Freepik",30,(255,255,255),(960,230))
    write2("flaticon.com/free-icon/battle_7921649",20,(255,255,255),(960,260))

    write2("Encounter icon by Freepik",30,(255,255,255),(960,310))
    write2("flaticon.com/free-icon/conversation_1357708",20,(255,255,255),(960,340))

    write2("Heart icon by Kiranshastry",30,(255,255,255),(960,390))
    write2("flaticon.com/free-icon/heart_833472",20,(255,255,255),(960,420))

    write2("Inspect icon by Freepik",30,(255,255,255),(960,470))
    write2("flaticon.com/free-icon/magnifying-glass_324654",20,(255,255,255),(960,500))

    write2("Market icon by Gregor Cresnar",30,(255,255,255),(960,550))
    write2("flaticon.com/free-icon/shop_126122",20,(255,255,255),(960,580))

    write2("Player icon by max.icons",30,(255,255,255),(960,630))
    write2("flaticon.com/free-icon/adventurer_2822371",20,(255,255,255),(960,660))

    write2("Shelter icon by Freepik",30,(255,255,255),(960,710))
    write2("flaticon.com/free-icon/bonfire_1331111",20,(255,255,255),(960,740))

    write2("Shield icon by Freepik",30,(255,255,255),(960,790))
    write2("flaticon.com/free-icon/shield_786245",20,(255,255,255),(960,820))
    
    write2("Click to continue",30,(255,255,255),(960,900))

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            timer=-1
    py.display.update()
    fps.tick(60)

timer=600
while timer>0:
    timer=timer-1
    
    win2.fill((0,0,0))

    write2("FONT",80,(0,255,0),(960,80))
    write2("Rubik Dirt by NaN, Luke Prowse",30,(255,255,255),(960,150))

    write2("This program is licensed under GNU General Public License version 3 (GPLv3)",30,(255,255,255),(960,250))
    
    write2("Click to exit",30,(255,255,255),(960,900))

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            timer=-1
    py.display.update()
    fps.tick(60)
