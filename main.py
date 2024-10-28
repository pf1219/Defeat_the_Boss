# Module Import
import pygame as py
import sys, os, random, time, csv, string, math
from pygame.locals import *
py.mixer.pre_init(44100,16,2,4096)
py.init()

# Display Setting
flags = py.SCALED | py.RESIZABLE | py.FULLSCREEN
win2=py.display.set_mode((1920,1080),flags)
win=py.Surface((1280,720))
py.display.set_caption('Defeat the Boss')
fps=py.time.Clock()

# Functions
def path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    relative_path='resource/'+relative_path
    return os.path.join(base_path, relative_path)

# Logo
icon = py.image.load(path('logo.png'))
py.display.set_icon(icon)

# Loading
win2.fill((0,0,0))
font=py.font.Font(path('font.ttf'),100)
text=font.render('DEFEAT THE BOSS',False,(255,0,0))
text_rect=text.get_rect(center=(960,440))
win2.blit(text,text_rect)
font=py.font.Font(path('font.ttf'),50)
text=font.render('- A Roguelike Adventure -',False,(0,255,0))
text_rect=text.get_rect(center=(960,560))
win2.blit(text,text_rect)
text=font.render('Loading...',False,(0,0,255))
text_rect=text.get_rect(center=(960,800))
win2.blit(text,text_rect)
py.display.update()

exec(open(path('resource.py'),encoding='utf-8').read())
exec(open(path('function.py'),encoding='utf-8').read())
randomize()

# Initial Setting
floor=0

EXP=0
save_event=[0 for i in range(100)]
# 0 Medical Textbook
# 1 Alternative Boss

MS_list=[10,12,14,16,18,20,22,24]
AST_list=[3,4,5,6,7,8,9,10]
ASP_list=[45,42,39,36,33,30,27,25]
BSP_list=[18,21,24,28,32,36,40,45]
BSZ_list=[8,10,12,14,16,18,20,23]

MS=0
AST=0
ASP=0
BSP=0
BSZ=0
DOD=0

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

weapon='None'
armor='None'
totem='None'
tool='None'
tool_time=0

weapon2=''
armor2=''
totem2=''
tool2=''

combat_control=0

# Gameplay
exec(open(path('mainscreen.py'),encoding='utf-8').read())
if gamemode==0:
    for floor in range(1,8):
        exec(open(path('explore.py'),encoding='utf-8').read())
        if you_HP<=0 or game_end==1:
            py.quit()
            sys.exit()
else:
    exec(open(path('explore2.py'),encoding='utf-8').read())
    if you_HP<=0 or game_end==1:
        py.quit()
        sys.exit()

# Ending
timer=600
while timer>0:
    timer=timer-1
    
    win2.fill((0,0,0))

    write2('DEFEAT THE BOSS',100,(255,0,0),(960,100))
    write2('- A Roguelike Adventure -',50,(0,255,0),(960,200))

    write2('VICTORY',200,(255,255,255),(960,540))
    
    write2("Click to continue",30,(255,255,255),(960,900))

    for event in py.event.get():
        if event.type==MOUSEBUTTONDOWN:
            timer=-1
    py.display.update()
    fps.tick(60)
exec(open(path('credit.py'),encoding='utf-8').read())
py.quit()
sys.exit()
