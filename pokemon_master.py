'''
Author: Anchit Mehta
Purpose: To be the best there ever was. 
Real Purpose: To defeat all pokemon trainers in Pokemon Fire Red.
'''
from threading import currentThread
import pandas as pd
from pyscreeze import pixel 
import pytesseract
from PIL import ImageGrab 
import pyautogui as pag
import numpy as np
import time
import random
import datetime

##################################################
###         Stage 0 -- Type Effectivness       ###
##################################################
attacker=[
    'normal','fire','water','grass','electric','ice','fighting',
    'poison','ground','flying','psychic','bug','rock','ghost',
    'dragon','dark','steel'] #17 types

list1=[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5]               #normal
list2=[1,0.5,0.5,2,1,2,1,1,1,1,1,2,0.5,1,0.5,1,2]           #fire
list3=[1,2,0.5,0.5,1,1,1,1,2,1,1,1,2,1,0.5,1,1]             #water
list4=[1,0.5,2,0.5,1,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5]     #grass
list5=[1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1]             #electric
list6=[0,0.5,0.5,2,1,0.5,1,1,2,2,1,1,1,1,2,1,0.5]           #ice
list7=[2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2]           #fighting
list8=[1,1,1,2,1,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0]           #poison
list9=[1,2,1,0.5,2,1,1,2,1,0,1,0.5,2,1,1,1,2]               #ground
list10=[1,1,1,2,0.5,1,2,1,1,1,1,2,0.5,1,1,1,0.5]            #flying
list11=[1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5]              #physic
list12=[1,0.5,1,2,1,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5]      #bug
list13=[1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5]            #rock
list14=[0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,0.5]              #ghost
list15=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5]                #dragon
list16=[1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,0.5]            #dark
list17=[0,0.5,0.5,1,1,2,1,1,1,1,1,1,2,1,1,1,0.5]            #steel

df = pd.DataFrame(list(zip(list1,list2,list3,list4,list5,list6,list7,list8,list9,
                    list10,list11,list12,list13,list14,list15,list16,list17)),
                    columns=attacker,
                    index=attacker)

##################################################
###         Stage 1 -- Move Classification     ###
##################################################
class Moves:
    def __init__(self,type,category,power,accuracy):
        self.type=type
        self.category=category
        self.power=power 
        self.accuracy=accuracy

tackle=Moves('normal','physical',35,95)
bubble=Moves('water','special',20,100)
water_gun=Moves('water','special',40,100)
peck=Moves('flying','physical',35,100)
double_kick=Moves('fighting','physical',30,100)
bite=Moves('dark','special',60,100)
rock_tomb=Moves('rock','physical',50,80)
thrash=Moves('normal','physical',90,100)
confusion=Moves('psychic','special',50,100)
psybeam=Moves('psychic','special',65,100)
ember=Moves('fire','special',40,100)
psychic=Moves('psychic','special',90,100)
surf=Moves('water','special',95,100)
strength=Moves('normal','physical',80,100)
brick_break=Moves('fighting','physical',75,100)
flamethrower=Moves('fire','special',95,100)
extremespeed=Moves('normal','physical',80,100)
aerial_ace=Moves('flying','physical',60,100)
twister=Moves('dragon','special',40,100)
drill_peck=Moves('flying','physical',80,100)
thunderbolt=Moves('electric','special',95,100)
wing_attack=Moves('flying','physical',60,100)
ancientpower=Moves('rock','physical',60,100)
earthquake=Moves('ground','physical',100,100)
dragon_claw=Moves('dragon','special',80,100)

'''
MOVE 1 ----------- MOVE 2
MOVE 3 ----------- MOVE 4
'''

##################################################
###         Stage 2 -- Pokemon Dictionary      ###
##################################################
class Pokemon:
    def __init__(self,name,type,defense=None,sp_defense=None,type2=None):
        self.name=name
        self.type=type
        self.type2=type2
        self.defense=defense
        self.sp_defense=sp_defense


bulbasaur=Pokemon('bulbasaur','grass',49,65,'poison')
charmander=Pokemon('charmander','fire',43,50)
squirtle=Pokemon('squirtle','water',65,64)
weedle=Pokemon('eedle','bug',30,20,'poison')
caterpie=Pokemon('caterpie','bug',35,20)
kakuna=Pokemon('kakuna','bug',50,25,'poison')
metapod=Pokemon('tapod','bug',55,25)
rattata=Pokemon('ratta','normal',35,35)
pidgey=Pokemon('pidge','flying',35,35)
geodude=Pokemon('geodude','rock',50,50,'ground')
sandshrew=Pokemon('sand','ground',50,50)
onix=Pokemon('onix','rock',50,50,'ground')
ekans=Pokemon('ekans','poison',44,54)
spearow=Pokemon('spear','normal',30,31,'flying')
nidoran=Pokemon('nidoran','poison',52,40)
jigglypuff=Pokemon('jigglypuff','normal',20,25)
clefairy=Pokemon('clefair','normal',35,35)
magnemite=Pokemon('agne','electric',35,35,'steel')
voltorb=Pokemon('oltorb','electric',35,35)
zubat=Pokemon('zubat','flying',35,35,'poison')
grimer=Pokemon('gri','poison',35,35)
koffing=Pokemon('koff','poison',35,35)
abra=Pokemon('abra','psychic',10,35)
oddish=Pokemon('oddish','grass',55,65,'poison')
bellsporout=Pokemon('bellsp','grass',55,65,'poison')
mankey=Pokemon('anke','fighting',30,30)
machop=Pokemon('chop','fighting',30,30)
slowpoke=Pokemon('poke','water',35,35,'psychic')
horsea=Pokemon('horse','water',35,35)
shellder=Pokemon('shellder','water',35,35)
goldeen=Pokemon('goldeen','water',35,35)
staryu=Pokemon('star','water',35,35,'psychic')
drowzee=Pokemon('zee','psychic',35,35)
butterfree=Pokemon('butter','bug',35,35,'flying')
raticate=Pokemon('raticate','normal')
poliwag=Pokemon('poli','water')
nidorino=Pokemon('dorin','poison')
tentacool=Pokemon('cool','water',type2='poison')
growlithe=Pokemon('lithe','fire')
pikachu=Pokemon('achu','electric')
ponyta=Pokemon('pon','fire')
ivysaur=Pokemon('saur','grass',type2='poison')
raichu=Pokemon('aichu','electric')
beedrill=Pokemon('beedrill','bug',type2='flying')
venonat=Pokemon('enonat','bug',type2='poison')
meowth=Pokemon('quth','normal')
meowth2=Pokemon('outh','normal')
cubone=Pokemon('bone','ground')
graveler=Pokemon('grav','rock',type2='ground')
vulpix=Pokemon('ulpi','fire')
arbok=Pokemon('arbo','poison')
kangaskhan=Pokemon('kangas','normal')
rhyhorn=Pokemon('horn','rock',type2='ground')
gyarados=Pokemon('rados','water',type2='flying')
gastly=Pokemon('astl','ghost',type2='poison')
haunter=Pokemon('haunter','ghost',type2='poison')
marowak=Pokemon('maro','ground')
golbat=Pokemon('golbat','poison',type2='flying')
weepinbell=Pokemon('eepinbell','grass',type2='poison')
gloom=Pokemon('gloom','grass',type2='poison')
exeggcute=Pokemon('egg','grass',type2='psychic')
victreebel=Pokemon('reebel','grass',type2='poison')
tangela=Pokemon('angela','grass')
vileplume=Pokemon('eplume','grass',type2='poison')
weezing=Pokemon('eezing','poison')
muk=Pokemon('muk','poison')
hypno=Pokemon('hypno','psychic')
primeape=Pokemon('eape','fighting')
machoke=Pokemon('choke','fighting')
hitmonlee=Pokemon('onlee','fighting')
hitmonchan=Pokemon('onchan','fighting')
mr_mime=Pokemon('mr.','psychic')
alakazam=Pokemon('ala','psychic')
nidoqueen=Pokemon('queen','ground',type2='psychic')
venomoth=Pokemon('veno','bug',type2='poison')
ninetails=Pokemon('tails','fire')
rapidash=Pokemon('dash','fire')
arcanine=Pokemon('arca','fire')
dugtrio=Pokemon('dugt','ground')
nidoking=Pokemon('nidoking','poison',type2='ground')
dewgong=Pokemon('gong','water',type2='ice')
cloyster=Pokemon('cloyst','water',type2='ice')
slowbro=Pokemon('slowbro','water',type2='psychic')
jynx=Pokemon('ynx','ice',type2='psychic')
lapras=Pokemon('lapras','water',type2='ice')
machamp=Pokemon('machamp','fighting')
gengar=Pokemon('gengar','ghost',type2='poison')
dragonair=Pokemon('onair','dragon')
aerodactyl=Pokemon('aerodactyl','rock',type2='flying')
dragonite=Pokemon('dragonite','flying',type2='dragon')
rhydon=Pokemon('rhydon','ground',type2='rock')


pokemon_list = [
    bulbasaur,charmander,squirtle,
    weedle,caterpie,kakuna,metapod,rattata,pidgey,
    geodude,sandshrew,onix,
    ekans,spearow,nidoran,jigglypuff,clefairy,
    magnemite,voltorb,zubat,grimer,koffing,abra,
    oddish,bellsporout,mankey,machop,slowpoke,horsea,
    shellder,goldeen,staryu,drowzee,butterfree,raticate,
    poliwag,nidorino,tentacool,growlithe,pikachu,
    ponyta,ivysaur,raichu,beedrill,venonat,meowth,meowth2,
    cubone,graveler,vulpix,arbok,kangaskhan,rhyhorn,
    gyarados,gastly,haunter,marowak,golbat,weepinbell,
    gloom,exeggcute,victreebel,tangela,vileplume,
    weezing,muk,hypno,primeape,machoke,hitmonchan,hitmonlee,
    mr_mime,alakazam,nidoqueen,venomoth,ninetails,rapidash,
    arcanine,dugtrio,nidoking,dewgong,cloyster,slowbro,lapras,
    machamp,gengar,dragonair,aerodactyl,dragonite,rhydon,jynx
    ]

##################################################
###         Stage 3 -- My Pokemon Team         ###
##################################################
class myTeam:
    def __init__(self,name,image,type,move1,move2=None,move3=None,move4=None,type2=None):
        self.type=type
        self.name=name
        self.image = image
        self.move1=move1
        self.move2=move2
        self.move3=move3
        self.move4=move4
        self.type2=type2


my_squirtle=myTeam('blast','squirtle.png','water',
                    surf,bubble,water_gun,bite)

my_abra=myTeam('azam','abra.png','psychic',
                    psychic,psybeam,confusion)

my_growilithe=myTeam('arcanine','growilithe.png','fire',
                    flamethrower,strength,bite,extremespeed)

my_dragonite=myTeam('dragonite','dragonite.png','flying',
                    aerial_ace,twister,earthquake,dragon_claw,type2='dragon')

my_zapdos=myTeam('zapdos','zapdos.png','electric',
                    drill_peck,thunderbolt,type2='flying')

my_aerodactyl=myTeam('aerodac','aerodactyl.png','rock',
                        wing_attack,ancientpower,bite,type2='flying')

myTeam_list = [my_squirtle,my_abra,my_growilithe,
                my_dragonite,my_zapdos,my_aerodactyl         
]

##################################################
###         Stage 4 -- Screenshot Functions    ###
##################################################
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Get first enemy pokemon and return pokemon object
def get_first_enemy():
    time.sleep(1)
    im = pag.screenshot(region=(71,123,265,150))
    im.save('enemy_first_pokemon.png')
    x = pytesseract.image_to_string('enemy_first_pokemon.png')
    x = x.lower()
    counter = 1

    for i in pokemon_list:
        counter += 1
        if i.name in x:
            return i
        if counter > len(pokemon_list):
            print(x)
            print('Enemy pokemon not found... please select (the number) which pokemon we are fighting:')
            print('#','---','Pokemon Name')
            for i in range(len(pokemon_list)):
                print(i,'---',pokemon_list[i].name)
            name = int(input())
            name = pokemon_list[name]
            time.sleep(3)
            return name 

#get my pokemon and return pokemon object
def get_my_pokemon():
    time.sleep(1)
    im = pag.screenshot(region=(39,528,420,130))
    im.save('my_first_pokemon.png')
    x = pytesseract.image_to_string('my_first_pokemon.png')
    x = x.lower()

    counter = 1

    for i in myTeam_list:
        counter += 1
        if i.name in x:
            return i
        if counter > len(myTeam_list):
            print(x)
            print('Team pokemon not found... please select (the number) which pokemon you are using:')
            print('#','---','Pokemon Name')
            for i in range(len(myTeam_list)):
                print(i,'---',myTeam_list[i].name)
            name = int(input())
            name = myTeam_list[name]
            time.sleep(3)
            return name 

#Get message text and return the lower case text
def detect_message():
    im = pag.screenshot(region=(34,527,750,170))
    im.save('message.png')
    x = pytesseract.image_to_string('message.png')
    x = x.lower()

    return x

##################################################
###         Stage 5 -- Supporting Functions    ###
##################################################

#pass in key from keyboard to press
def click(keystroke):
    time.sleep(0.5)
    pag.keyDown(keystroke)
    time.sleep(0.1)
    pag.keyUp(keystroke)
    time.sleep(0.2)

#Based on two pokemon objects, determine which move I should make and return a move index
def power(my_pokemon,enemy_pokemon):
    power1 = 1
    power2 = 1
    power3 = 1
    power4 = 1

    #determine modifiers for STAB type1
    if my_pokemon.move1 is not None and my_pokemon.move1.type == my_pokemon.type:
        power1 = 1.5
    if my_pokemon.move2 is not None and my_pokemon.move2.type == my_pokemon.type:
        power2 = 1.5
    if my_pokemon.move3 is not None and my_pokemon.move3.type == my_pokemon.type:
        power3 = 1.5
    if my_pokemon.move4 is not None and my_pokemon.move4.type == my_pokemon.type:
        power4 = 1.5
    
    #determine modifiers for STAB type2 my pokemon
    if my_pokemon.type2 is not None:
        if my_pokemon.move1 is not None and my_pokemon.move1.type == my_pokemon.type2:
            power1 = 1.5
        if my_pokemon.move2 is not None and my_pokemon.move2.type == my_pokemon.type2:
            power2 = 1.5
        if my_pokemon.move3 is not None and my_pokemon.move3.type == my_pokemon.type2:
            power3 = 1.5
        if my_pokemon.move4 is not None and my_pokemon.move4.type == my_pokemon.type2:
            power4 = 1.5

    #determine move type advantage
    enemy_type = enemy_pokemon.type

    if my_pokemon.move1 is not None:
        power1 = power1 * df.loc[enemy_type][my_pokemon.move1.type]
    if my_pokemon.move2 is not None:
        power2 = power2 * df.loc[enemy_type][my_pokemon.move2.type]
    if my_pokemon.move3 is not None:
        power3 = power3 * df.loc[enemy_type][my_pokemon.move3.type]
    if my_pokemon.move4 is not None:
        power4 = power4 * df.loc[enemy_type][my_pokemon.move4.type]


    #determine secondary type advantage if it exists 
    if enemy_pokemon.type2 is not None:
        enemy_type2 = enemy_pokemon.type2

        if my_pokemon.move1 is not None:
            power1 = power1 * df.loc[enemy_type2][my_pokemon.move1.type]
        if my_pokemon.move2 is not None:
            power2 = power2 * df.loc[enemy_type2][my_pokemon.move2.type]
        if my_pokemon.move3 is not None:
            power3 = power3 * df.loc[enemy_type2][my_pokemon.move3.type]
        if my_pokemon.move4 is not None:
            power4 = power4 * df.loc[enemy_type2][my_pokemon.move4.type]

    #include move power
    if my_pokemon.move1 is not None:
        power1 = power1*my_pokemon.move1.power
    if my_pokemon.move2 is not None:
        power2 = power2*my_pokemon.move2.power
    if my_pokemon.move3 is not None:
        power3 = power3*my_pokemon.move3.power
    if my_pokemon.move4 is not None:
        power4 = power4*my_pokemon.move4.power


    #take moves accuracy into consideration to return expected damage
    '''
    if my_pokemon.move1 is not None:
        power1 = power1*my_pokemon.move1.accuracy/100
    if my_pokemon.move2 is not None:
        power2 = power2*my_pokemon.move2.accuracy/100
    if my_pokemon.move3 is not None:
        power1 = power3*my_pokemon.move3.accuracy/100
    if my_pokemon.move4 is not None:
        power2 = power4*my_pokemon.move4.accuracy/100
    '''

    #determine move to pass on
    if my_pokemon.move2 is None:
        power2 = 0
    if my_pokemon.move3 is None:
        power3 = 0
    if my_pokemon.move4 is None:
        power4 = 0    

    power_list = [power1,power2,power3,power4]
    print('My Pokemon Move Powers: ',power_list)
    move_index = power_list.index(max(power_list))

    #if two moves do the same theoretical damage toss a coin
    for i in range(len(power_list)):
        if i != move_index and power_list[i] == power_list[move_index]:
            print('Same power moves identified. 50/50 shot.')
            x = random.randrange(0,2)
            if x == 0:
                return move_index 
            if x == 1:
                return i 

    return move_index

#Provided a move index, make the move
def move_movements(move_index):
    click('z') #click fight

    if move_index==0:
        click('i')
        click('j')
        click('z')
    if move_index==1:
        click('i')
        click('l')
        click('z')
    if move_index==2:
        click('k')
        click('j')
        click('z')
    if move_index==3:
        click('k')
        click('l')
        click('z')

#pass in string and return a number flag to determine next actions
def read_message(message):
    '''    
    --> Keys
        0 = everyone is alive... keep fighting
        1 = foe fainted
        2 = learning new move
        3 = new enemy pokemon coming out
        4 = my pokemon fainted
        5 = no PP remaining in move
        999 = trainer defeated 
    '''

    time.sleep(2)
    #print(message)
    #print('#########################################')

    if 'fight' in message:
        return 0
    if 'foe' in message and 'faint' in message:
        return 1
    if 'learn' in message:
        return 2
    if 'about' in message:
        return 3
    if 'faint' in message and 'foe' not in message:
        return 4
    if 'no pp' in message:
        return 5
    if 'defeat' in message:
        return 999

#based off of message return enemy pokemon coming out
def identify_next_enemy_pokemon():
    x = detect_message()
    for i in pokemon_list:
        if i.name in x:
            return i

#based off of next enemy pokemon coming out determine which i should switch to
def big_brain(enemy_pokemon):
    move_power = 0
    best_pokemon = None

    for my_pokemon in myTeam_list:
        power1 = 1
        power2 = 1
        power3 = 1
        power4 = 1

        #determine modifiers for STAB
        if my_pokemon.move1.type == my_pokemon.type:
            power1 = 1.5
        if my_pokemon.move2 is not None and my_pokemon.move2.type == my_pokemon.type:
            power2 = 1.5
        if my_pokemon.move3 is not None and my_pokemon.move3.type == my_pokemon.type:
            power3 = 1.5
        if my_pokemon.move4 is not None and my_pokemon.move4.type == my_pokemon.type:
            power4 = 1.5
        
        #determine modifiers for STAB type2 my pokemon
        if my_pokemon.type2 is not None:
            if my_pokemon.move1 is not None and my_pokemon.move1.type == my_pokemon.type2:
                power1 = 1.5
            if my_pokemon.move2 is not None and my_pokemon.move2.type == my_pokemon.type2:
                power2 = 1.5
            if my_pokemon.move3 is not None and my_pokemon.move3.type == my_pokemon.type2:
                power3 = 1.5
            if my_pokemon.move4 is not None and my_pokemon.move4.type == my_pokemon.type2:
                power4 = 1.5

        #determine move type advantage
        enemy_type = enemy_pokemon.type

        power1 = power1 * df.loc[enemy_type][my_pokemon.move1.type]
        if my_pokemon.move2 is not None:
            power2 = power2 * df.loc[enemy_type][my_pokemon.move2.type]
        if my_pokemon.move3 is not None:
            power3 = power3 * df.loc[enemy_type][my_pokemon.move3.type]
        if my_pokemon.move4 is not None:
            power4 = power4 * df.loc[enemy_type][my_pokemon.move4.type]

        #determine secondary type advantage if it exists 
        if enemy_pokemon.type2 is not None:
            enemy_type2 = enemy_pokemon.type2

            power1 = power1 * df.loc[enemy_type2][my_pokemon.move1.type]
            if my_pokemon.move2 is not None:
                power2 = power2 * df.loc[enemy_type2][my_pokemon.move2.type]
            if my_pokemon.move3 is not None:
                power3 = power3 * df.loc[enemy_type2][my_pokemon.move3.type]
            if my_pokemon.move4 is not None:
                power4 = power4 * df.loc[enemy_type2][my_pokemon.move4.type]

        #determine move to pass on
        if my_pokemon.move2 is None:
            power2 = 0
        if my_pokemon.move3 is None:
            power3 = 0
        if my_pokemon.move4 is None:
            power4 = 0

        #include move power
        power1 = power1*my_pokemon.move1.power
        if my_pokemon.move2 is not None:
            power2 = power2*my_pokemon.move2.power
        if my_pokemon.move3 is not None:
            power3 = power3*my_pokemon.move3.power
        if my_pokemon.move4 is not None:
            power4 = power4*my_pokemon.move4.power


        power_list = [power1,power2,power3,power4]
        max_power = max(power_list)
        print(f'{my_pokemon.name} vs. {enemy_pokemon.name}')
        print(power_list)
        print('---------------')

        if max_power > move_power:
            #print(max_power)
            move_power = max_power 
            best_pokemon = my_pokemon 

    return best_pokemon

#input is the best option pokemon to switch to and the output is navigating to pokemon
def send_next(next_pokemon):

    locations = {
        'first': (404,136),
        'second': (411,237),
        'third': (405,327),
        'fourth': (411,425),
        'fifth': (411,525)
    }

    pixel_locations = {
        'first':(485,161),
        'second':(485,257),
        'third':(485,353),
        'fourth':(485,450),
        'fifth':(485,548)
    }

    bright_pixel=(168,232,248)
    dark_pixel=(128,192,216)

    print(next_pokemon.name)
    time.sleep(3)
    try:
        x,y = pag.locateCenterOnScreen(next_pokemon.image,confidence=0.6)
        print(x,y)
        for key in locations:
            x_location = locations[key][0]
            y_location = locations[key][1]
            if y_location - 20 <= y <= y_location + 20 and x_location - 20 <= x <= x_location + 20:
                if key == 'first':
                    print(f'{key} location')
                    while pag.pixelMatchesColor(pixel_locations['first'][0],
                                                pixel_locations['first'][1],
                                                dark_pixel,
                                                tolerance=10):
                                                click('k')
                                                time.sleep(1)
                    click('z')
                    click('z')
                if key == 'second':
                    print(f'{key} location')
                    while pag.pixelMatchesColor(pixel_locations['second'][0],
                                                pixel_locations['second'][1],
                                                dark_pixel,
                                                tolerance=10):
                                                click('k')
                                                time.sleep(1)
                    click('z')
                    click('z')
                if key == 'third':
                    print(f'{key} location')
                    while pag.pixelMatchesColor(pixel_locations['third'][0],
                                                pixel_locations['third'][1],
                                                dark_pixel,
                                                tolerance=10):
                                                click('k')
                                                time.sleep(1)
                    click('z')
                    click('z')
                if key == 'fourth':
                    print(f'{key} location')
                    while pag.pixelMatchesColor(pixel_locations['fourth'][0],
                                                pixel_locations['fourth'][1],
                                                dark_pixel,
                                                tolerance=10):
                                                click('k')
                                                time.sleep(1)
                    click('z')
                    click('z')
                if key == 'fifth':
                    print(f'{key} location')
                    while pag.pixelMatchesColor(pixel_locations['fifth'][0],
                                                pixel_locations['fifth'][1],
                                                dark_pixel,
                                                tolerance=10):
                                                click('k')
                                                time.sleep(1)
                    click('z')
                    click('z')
    except:
        print('Best pokemon already out. Hitting B.')
        click('x')


##################################################
###         Stage 6 -- Combat                  ###
##################################################
#'''
trainer = True #is the trainer battle still happening
enemy_pokemon = True #is 1v1 combat still happening
first_enemy = True #are we on the first enemy pokemon
my_side = None 
their_side = None

time.sleep(2)
time0 = datetime.datetime.now()
#'''
while trainer:
    while enemy_pokemon:
        if first_enemy:
            my_side = get_my_pokemon()
            their_side = get_first_enemy()
            x = power(my_side,their_side)
            move_movements(x)
            time.sleep(10)
        else:
            my_side = get_my_pokemon()
            their_side = next_pokemon
            x = power(get_my_pokemon(),next_pokemon)
            move_movements(x)
            time.sleep(10)

        y = read_message(detect_message())
        if y == 0:
            print('Everyone is alive. Keep fighting.')
            continue 
        if y == 1:
            print('Enemy pokemon has fainted. Exit 1v1 combat loop.')
            enemy_pokemon = False 
            first_enemy = False
        if y == 4:
            print('I died. Exit combat 1v1 loop.')
            enemy_pokemon = False 
        if y == 5:
            print('Move out of PP. Removing it from list.')
            if x == 0:
                my_side.move1.power = 0
            if x == 1:
                my_side.move2.power = 0 
            if x == 2:
                my_side.move3.power = 0
            if x == 3:
                my_side.move4.power = 0
            click('z')
            time.sleep(1)
            click('x')

    z = read_message(detect_message())
    #print(z)
    if z == 3:
        print('Next pokemon is coming out!')
        next_pokemon = identify_next_enemy_pokemon()
        time.sleep(1)
        choose_my_next = big_brain(next_pokemon)
        if choose_my_next == my_side:
            print('My current Pokemon is best to proceed - do not switch.')
            click('z')
            time.sleep(1)
            click('x')
            time.sleep(4)
        else:
            time.sleep(1)
            click('z')
            time.sleep(1)
            click('z')
            send_next(choose_my_next)
            time.sleep(4)
        enemy_pokemon=True
    if z == 999:
        print('Battle won! Enemy trainer defeated.')
        battle_duration = datetime.datetime.now()-time0
        print(f'Duration: {battle_duration}')
        trainer = False
        click('z')
        click('z')
        click('z')
    if z == 2:
        print('New move incoming. Please take over and then restart combat.')
        trainer = False
    if z == 4:
        print('My pokemon has fainted you noob.')
        print('Choose another pokemon...')
        myTeam_list.remove(my_side)
        choose_my_next = big_brain(their_side)
        time.sleep(1)
        click('z') #acknowledge i fainted
        send_next(choose_my_next)
        time.sleep(4)
        enemy_pokemon=True

    if z != 2 and z != 3 and z != 4 and z!=5 and z != 999:
        click('z')
        print('hit A... waiting on a flag')
        time.sleep(1)
#'''

#print(detect_message())