# -*- coding: utf-8 -*-
from mcdreforged.api.all import *
import re
import random

PLUGIN_METADATA = {
    'id': 'RandomTeams',
    'version': '1.0.0',
    'name': 'Randomly divide players into teams'
}

nplayers=0
nteams=0
doteams=False
parts=[]
player=[]
player1=[]
playercolorid=[]
playercolor=[]
color=["red","blue","yellow","green","aqua","gold","light_purple","gray","dark_gray","dark_purple","dark_blue","dark_aqua","dark_red","dark_green"]
f=[]
def on_info(server:ServerInterface, info:Info):
    global doteams,nteams,nplayers,player1,player,playercolor,playercolorid,color,f
    if info.is_from_server:
        if doteams == True:
            res=re.search(r'There are (?P<num>\d+) of a max of 20 players online: (?P<name>.*)',info.content)
            if res == None:
                pass
            else:
                nplayers = eval(res['num'])
                player = res['name'].split(', ')
                randomspread(nplayers,nteams,server)
                getcolor(server,nteams)
                doteams = False

    if info.is_player:
        parts=info.content.split()
        if parts[0] == '!!teams' and len(parts) == 2 and parts[1].isdigit():
            nteams=0
            nplayers=0
            nteams = eval(parts[1])
            doteams=True
            parts=[]
            player=[]
            player1=[]
            playercolorid=[]
            playercolor=[]
            f=[]
            server.execute('/team leave @a')
            for i in color:
                server.execute(f'/team remove {i}')
            server.execute('/list')
        else:
            if parts[0] == '!!teams':
                server.execute('/tellraw @a ["",{"text":"[错误]","color":"red","bold":true},{"text":"分队指令格式不符,格式:!!teams <队伍数量>","color":"yellow","bold":false}]')

def randomspread(nplayers,nteams,server:ServerInterface):
    global doteams,player,playercolor,playercolorid,color,f,player1
    n=nplayers
    p=0
    for i in range(nplayers):
        playercolorid.append(0)
    for i in range(n):
        k = int(random.random()*n)
        player1.append(f'{player[k]}')
        player.remove(f'{player[k]}')
        playercolorid[i]=p%nteams
        n=n-1
        p=p+1
        i=i+1

def getcolor(server:ServerInterface,nteams):
    global doteams,nplayers,player,playercolor,playercolorid,color,f,player1
    i=0
    j=0
    while i < nteams:
        server.execute(f'/team add {color[i]}')
        server.execute(f'/team modify {color[i]} color {color[i]}')
        i = i+1
    while j < nplayers:
        server.execute(f'/team join {color[playercolorid[j]]} {player1[j]}')
        j = j+1


        
    


