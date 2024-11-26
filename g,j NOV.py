import pgzrun
import random

#variables
HEIGHT=500
WIDTH=500
TITLE="B.O.B"
texts=0
level=0
drawcomputer=False
saladinfo=False
troll=False
riddleactivate=False
display_riddle=False
stage=0
price_display_tomato=False
cash=0
start_earning=False
tomato_owned=False
inventory=[]
move_tomato=False
toothbrush_owned=False
carrot_owned=False
#actors
bank=Actor('bank')
background=Actor("healthgamebg")
computer=Actor("computer")
info_display_unit=Actor("infodisplay")
salad=Actor("salad")
house=Actor("house")
houses=[]
mainhouse=Actor("big3house")
paper=Actor("paper")
paper_on_table=Actor('paperontable')
nex_button=Actor("nextbutton")
main_character=Actor("robot_idle")
main_character.x=250
main_character.y=250
tomato=Actor('tomato')
cabbage=Actor('cabbage')
target_store=Actor('targetstore')
walmart=Actor("walmart")
costcos=Actor("costcos")
shelves=Actor('shelves')
shelve_list=[]
wrong_house_anim=Actor("wrong_house1")
clock=0
houseanim=["wrong_house1", "wrong_house2", "wrong_house3"]
earn_button=Actor('button')
money_sack=Actor('money_sack')
coin=Actor('coin_gold')
toothbrush=Actor('toothbrush')
carrot=Actor('carrot')
def draw():
    global texts
    global level
    global cash
    global tomato_owned
    global move_tomato
    global toothbrush_owned
    global carrot_owned
    if level==0:
        
        if texts==0:  
            screen.clear()  
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Long ago, there lived 4 chefs...",color="white",center=(250,250))   
        if texts==1:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("the 4th chef named Bob had no money...", color="white",center=(250,250))        
        if  texts==2:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("One day after a long day of work...", color="white", center=(250,250))
        if texts==3:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob had a loaf of bread, some lettuce", color="white", center=(250,250))
            screen.draw.text("sauce and some grilled beef...", color="white", center=(250,280))
        if texts==4:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("so Bob put the grilled beef,", color="white", center=(250,250))
            screen.draw.text(" sauce and lettuce between the 2 buns...", color="white", center=(250,280))
        if texts==5:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("After 1 bite, Bob knew he had made a masterpeice", color="white", center=(250,250))
        if texts==6:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob sold his creation across stores world-wide..", color="white", center=(250,250))
        if texts==7:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("World Health Officials noticed a major drop in health...", color="white", center=(250,250))
        if texts==8:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob's Burgers caused people to get sick...", color="white", center=(250,250))
        if texts==9:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("the other chefs were inventing a better dish...", color="white", center=(250,250))
        if texts==10:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("But Bob fed them so many bugers that they died...", color="white", center=(250,250))
        if texts>=11:
            level=1

    if level==1:
        screen.clear()
        screen.fill("green")
        screen.draw.text("Task: find the house of the BIG 3", color="white", topleft=(20,20))
        mainhouse.draw()
        mainhouse.x=random.randint(50,450)
        mainhouse.y=random.randint(50,450)
        for i in range(2):
            house.draw()
            house.x=random.randint(50, 450)
            house.y=random.randint(50,450)
            houses.append(house)   
        

        if troll==True:
            screen.clear()                 
            for i in range(3):
                if i==1:
                    wrong_house_anim.image="wrong_house1"
                    wrong_house_anim.draw()
                if i==2:
                    wrong_house_anim.image="wrong_house2"
                    wrong_house_anim.draw()
                if i==3:
                    wrong_house_anim.image="wrong_house3"
                    wrong_house_anim.draw()
            screen.draw.text("Nothing in this house :), click 'e' to leave ", color="white", topleft=(20,20))
               
    if level==2:
        screen.clear()        
        screen.blit("healthgamebg",(0,0))
        screen.draw.text("Task: find the cure's recepie", color="black", topleft=(20,20))
        computer.x=255
        computer.y=215
        nex_button.draw()
        nex_button.x=(450)
        nex_button.y=(50)
        paper_on_table.draw()
        paper_on_table.x=315
        paper_on_table.y=380
        computer.draw()
        if riddleactivate == True:
                    screen.clear()
                    screen.fill("black")
                    paper.draw()
                    paper.x=250
                    paper.y=250
                    screen.draw.text("The Riddle of the Three", color="black", topleft=(60,20))
                    screen.draw.text("_________________________", color="black", topleft=(60,25))
                    screen.draw.text("In the arctic,", color="black", topleft=(60,50))
                    screen.draw.text("Most of your needs you shall find,", color="black", topleft=(60,70))
                    screen.draw.text("The ingredients you must pick:", color="black", topleft=(60,90))
                    screen.draw.text("1) The vegetable that makes you go blind.", color="black", topleft=(60,110))
                    screen.draw.text("2) Squished to make sauce, Red like the sun,", color="black", topleft=(60,150))
                    screen.draw.text("3) Green leafs resembles a fan", color="black", topleft=(60,170))
                    screen.draw.text("4) Cut, Mince, don't burn", color="black", topleft=(60,190))
                    screen.draw.text("5) Place in a vessel, ", color="black", topleft=(60,210))
                    screen.draw.text("6) and let it wrestle, ", color="black", topleft=(60,230))
                    screen.draw.text("7) the toxins of the burger", color="black", topleft=(60,350))
        if drawcomputer==True:
            info_display_unit.draw()
            info_display_unit.x=250
            screen.draw.text("NEWS HEADLINES: BOB KILLS MILLIONS", color="black", topleft=(40,40))
            screen.draw.text("___________________________________________", color="black", topleft=(40,42))
            screen.draw.text("Bob's burgers strike again, this time a small", color="black", topleft=(40,60))
            screen.draw.text("town in Boston gets hit by burgers, nearly 235", color="black", topleft=(40,80))
            screen.draw.text("people are sickend by the Burger Syndrome", color="black", topleft=(40,100))
            salad.draw()
            salad.x=100
            salad.y=260
            screen.draw.text("Research on a cure by the BIG 3", color="black", topleft=(180,200))
            screen.draw.text("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_", color="black", topleft=(180,210))
            if saladinfo==True:
                screen.clear()
                screen.fill("cyan")
                screen.draw.text('"-A salad a day keeps the burger syndrome away"', color="black", topleft=(20,20))
                screen.draw.text("Our discoveries have shown us that eating #--@^$@! food", color="black", topleft=(20,60))
                screen.draw.text("is good, ^%&^@! food is good for you because of the #!$*_!($)", color="black", topleft=(20,80))
                screen.draw.text("there are many types of $&!@^*, but the most important part", color="black", topleft=(20,100))
                screen.draw.text("of all $!!$*&@ has to be the fact that it is %$@#*/!.", color="black", topleft=(20,120))
                screen.draw.text("Now I shall reveal the key to health", color="black", topleft=(20,140))
                screen.draw.text("Anyways, yesterday I discoverd that the key to health was:", color="black", topleft=(20,160))
                screen.draw.text("1) get some to*%!*&, P!#&tos, 0n1075, and some 6833Eg%", color="black", topleft=(20,200))
                screen.draw.text("2) make sure to !$!&5%3 the ingredients finely", color="black", topleft=(20,220))
                screen.draw.text("3) Place in a %#4l and drizzle some !393", color="black", topleft=(20,240))
                screen.draw.text("Update (3 years ago): bob is trying to exterminate us three", color="black", topleft=(20,280))
                screen.draw.text("in case he gets us and hacks our website i made a paper ", color="black", topleft=(20,300))
                screen.draw.text("document of the recipie", color="black", topleft=(20,320))
    if level==3:
        screen.clear() 
        screen.blit("grass",(0,0))
        main_character.draw()
        walmart.draw()
        costcos.draw()
        target_store.draw()
        bank.draw()
        screen.draw.text("Task: Find ingredients,(click 'f' for riddle, 'g' to close)", color="white", topleft=(20,20))
        screen.draw.text("arrow keys to move", color="black", topleft=(20,40))
        screen.draw.text('Cash: '+str(cash), color="black", topleft=(20,60))
        target_store.x=60
        target_store.y=450
        walmart.x=450
        walmart.y=450
        costcos.x=450
        costcos.y=60
        bank.x=250
        bank.y=450
        if stage=="bank":
            screen.clear()
            screen.fill('white')
            money_sack.x=random.randint(50,450)
            money_sack.y=random.randint(50,450)
            money_sack.draw()
            screen.draw.text("You have "+str(cash)+" USD", color="black", topleft=(20,20))
        if stage=="costcos":
            screen.clear()
            screen.fill("grey")
            screen.draw.text('Cash: '+str(cash), color="black", topleft=(20,60))
            shelves.draw()
            tomato.draw()
            carrot.draw()
            toothbrush.draw()
            shelves.x=250
            shelves.y=200
            toothbrush.x=180
            toothbrush.y=180
            carrot.y=180
            carrot.x=300
            tomato.x=60
            tomato.y=180
            screen.draw.text("50 USD", color='black',center=(60,230))
            screen.draw.text("30 USD", color="black", center=(180,230))
            screen.draw.text("50 USD", color="black", center=(300,230))
            if price_display_tomato==True and tomato_owned==True:
                tomato.x=900
                tomato.y=900
                inventory.append('tomato')
                tomato_owned=False
                move_tomato=True
            if toothbrush_owned==True:
                inventory.append("toothbrush")
                toothbrush_owned=False
            if carrot_owned==True:
                inventory.append("carrot")
                carrot_owned=False
        screen.draw.text("Inventory"+str(inventory), color="black", topleft=(20,80))    
        if stage=="target":
            screen.fill("green")
        if stage=="walmart":
            screen.fill("red")
        if riddleactivate == True:
            screen.clear()
            screen.fill("black")
            paper.draw()
            paper.x=250
            paper.y=250
            screen.draw.text("The Riddle of the Three", color="black", topleft=(60,20))
            screen.draw.text("_________________________", color="black", topleft=(60,25))
            screen.draw.text("In the arctic,", color="black", topleft=(60,50))
            screen.draw.text("Most of your needs you shall find,", color="black", topleft=(60,70))
            screen.draw.text("The ingredients you must pick:", color="black", topleft=(60,90))
            screen.draw.text("1) The vegetable that makes you go blind.", color="black", topleft=(60,110))
            screen.draw.text("2) Squished to make sauce, Red like the sun,", color="black", topleft=(60,150))
            screen.draw.text("3) Green leafs resembles a fan", color="black", topleft=(60,170))
            screen.draw.text("4) Cut, Mince, don't burn", color="black", topleft=(60,190))
            screen.draw.text("5) Place in a vessel, ", color="black", topleft=(60,210))
            screen.draw.text("6) and let it wrestle, ", color="black", topleft=(60,230))
            screen.draw.text("7) the toxins of the burger", color="black", topleft=(60,350))

def place_money():
    money_sack.x=random.randint(50,450)
    money_sack.y=random.randint(50,450)

                
    
def on_mouse_down(pos):
    global texts
    global price_display_tomato
    global level
    global drawcomputer
    global saladinfo
    global troll
    global riddleactivate
    global display_riddle
    global start_earning
    global cash
    global toothbrush_owned
    global carrot_owned
    global tomato_owned
    if computer.collidepoint(pos) and level==2:
        drawcomputer=True
    if salad.collidepoint(pos) and level==2:
        saladinfo=True
    if house.collidepoint(pos) and level==1:
        troll=True
    if mainhouse.collidepoint(pos) and level==1:
        level=2
    if paper_on_table.collidepoint(pos) and level==2:
        riddleactivate=True
        display_riddle=True
    if nex_button.collidepoint(pos) and display_riddle==True and level==2:
        level=3
        riddleactivate=False
    if tomato.collidepoint(pos) and level==3 and stage=="costcos":
        price_display_tomato=True
    if money_sack.collidepoint(pos) and level==3 and stage=="bank":
        cash=cash+10
    if tomato.collidepoint(pos) and level==3 and stage=="costcos" and cash>40:
        cash=cash-50
        tomato_owned=True
    if toothbrush.collidepoint(pos) and level==3 and stage=="costcos" and cash>20:
        toothbrush_owned=True
        cash=cash-30
    if carrot.collidepoint(pos) and level==3 and stage=="costcos" and cash>40:
        cash=cash-50
        carrot_owned=True



def update():
    global level
    global saladinfo
    global drawcomputer
    global troll
    global riddleactivate
    global price_display_tomato
    global stage
    if level==0:
        global texts
        if keyboard.space:
            texts=texts+0.25
    if level==1:
        if troll==True and level==1 and keyboard.e:
            troll=False
    if level==2:
        if saladinfo==True and level==2 and keyboard.e:
            saladinfo=False
        if drawcomputer==True and level==2 and keyboard.e:
            drawcomputer=False
        if riddleactivate==True and level==2 and keyboard.e:
            riddleactivate=False
    if level==3:
        if level==3 and riddleactivate==False and keyboard.f:
            riddleactivate=True
        if level==3 and riddleactivate==True and keyboard.g:
            riddleactivate=False
        if level==3 and riddleactivate==False and keyboard.right and main_character.x<500:
            main_character.x=main_character.x+2
            main_character.image="robot_right"
        if level==3 and riddleactivate==False and keyboard.left and main_character.x>0:
            main_character.x=main_character.x-2
            main_character.image="robot_left"
        if level==3 and riddleactivate==False and keyboard.up and main_character.y>0:
            main_character.y=main_character.y-2
            main_character.image="robot_idle"
        if level==3 and riddleactivate==False and keyboard.down and main_character.y<500:
            main_character.y=main_character.y+2
            main_character.image="robot_idle"
        if main_character.colliderect(costcos):
            stage="costcos"
        if main_character.colliderect(target_store):
            stage="target"
        if main_character.colliderect(bank):
            stage="bank"
        if main_character.colliderect(walmart):
            stage="walmart"
        if stage == "costcos" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
            price_display_tomato=False
        if stage == "walmart" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
        if stage == "target" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
        if stage=="bank" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
















pgzrun.go()