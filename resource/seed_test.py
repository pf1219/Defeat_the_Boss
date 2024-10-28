import random
sel_seed=-1
sel_com=-1
seed=0
while True:
    seed=seed+1
    if seed%1000000==0:
        print(seed)

    num_com=0
    for floor in range(1,8):
        random.seed(seed)
        boss_chunk=[random.randint(0,6),random.randint(0,6)]

    if boss_chunk==[3,3]:
        print(seed)
        break
