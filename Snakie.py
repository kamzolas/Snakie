import pygame
import time
import random
import tkMessageBox

pygame.init()

eat_sound= pygame.mixer.Sound("bloop3.wav")
click_sound= pygame.mixer.Sound("click1.wav")
new_level= pygame.mixer.Sound("beep2.wav")
sound_list=[0.8,0.2,0.4]
click_sound.set_volume(sound_list[0])
new_level.set_volume(sound_list[1])
eat_sound.set_volume(sound_list[2])

sound = "on"

sound_on_img= pygame.image.load('sound_on.png')
sound_off_img= pygame.image.load('sound_off.png')
mute_icon = pygame.image.load('mute.png')
unmute_icon = pygame.image.load('unmute.png')

white=(255,255,255)
black=(0,0,0)
light_red = (255,0,0)
red=(204,0,0)
light_green=(0,255,0)
green=(0,204,0)
dark_green=(0,130,0)
light_blue=(0,0,255)
blue=(0, 0, 204)
light_yellow = (255,255,0)
yellow = (230,230,0)
gray=(184,184,184)
orange=(255, 102, 0)
purple=(102,0,51)

colors_list=[black,orange,gray,red,green,dark_green,blue,yellow,light_red,light_green,light_blue,light_yellow,purple]
message_list=["Game Developer: Kamzolas Yannis", "The rules are simple! Just eat the fruits...", "To Pause press P", "To turn on/off the sound press M"]

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakie')


apple = pygame.image.load('fruit0.jpg')
high_score_img = pygame.image.load('HighScore.png')
pause_img = pygame.image.load('pause_img.png')
start_img = pygame.image.load('start.png')
finish_img = pygame.image.load('finish.png')
info_img= pygame.image.load('info.png')



predator_list=[[pygame.image.load('owl1.png'),pygame.image.load('owl2.png')],[pygame.image.load('eagle1.png'),pygame.image.load('eagle2.png')],[pygame.image.load('cat.jpg'),pygame.image.load('cat.jpg')]]
porportions_list=[[(120,65),(140,51)],[(85,95),(80,121)],[(150,52),((150,52))]]
fruit_image_list=[pygame.image.load('fruit0.jpg'),pygame.image.load('fruit1.png'),pygame.image.load('fruit2.png'),pygame.image.load('fruit3.png'),pygame.image.load('fruit4.png'),pygame.image.load('fruit5.png'),pygame.image.load('fruit6.png'),pygame.image.load('fruit7.png')]
snake_image_list=[pygame.image.load('snake_background.jpg'),pygame.image.load('snake1.jpg'),pygame.image.load('snake2.png'),pygame.image.load('snake3.png'),pygame.image.load('snake4.jpg'),pygame.image.load('snake5.jpg')]
chose_snake_list=[pygame.image.load('right_img.png'),pygame.image.load('left_img.png'),pygame.image.load('random_snake.png')]
snakeheads=[pygame.image.load('snakehead1.png'),pygame.image.load('snakehead2.png'),pygame.image.load('snakehead3.png'),pygame.image.load('snakehead4.png'),pygame.image.load('snakehead5.png'),pygame.image.load('snakehead6.png'),pygame.image.load('snakehead7.png'),pygame.image.load('snakehead8.png')]
snake_names=["Indigo Eastern Rat Snake", "Leucistic Texas Rat Snake","Honduran Milksnake","Emerald Tree Boa","Iridescent Shieldtail","Amelanistic Python","Brazilian Rainbow Boa","Eastern Coral Snake"]
snake_info={0:"The longest in America, carnivorous in habits, he has been known to beat his prey against other objects in a frenzied fashion to kill it. He will even eat other snakes such as the Texas Rattlesnake.",
            1:"A lovely lady in white. She gets her coloring and the 'leucistic' element of her name from a condition that results in a lack of all pigmentation. Texas Rat Snakes are (obviously) found in Texas as well as in Arizona and Louisiana. They are non venomous so a bite will give you little more than a sore leg.",
            2:"Lampropeltis triangulum hondurensis, is found in Honduras and Nicaragua. They are constrictors, but look a lot like coral snakes which herpetologists believe is an example of Batesian Mimicry.",
            3:"One of the most vivid. They are found in South America and the Amazon. Even though it looks like it is closely related to the Green Tree Python and sleeps the same way, they are only distant relatives. One thing that the Emerald has, is very large front teeth.",
            4:"It has to be one of the most beautiful snakes in the world, but it's not well known. Only three specimens are thought to have ever been caught and little is known of how it behaves in the wild.",
            5:"Is found in New Guinea, Indonesia and parts of Australia. It, along with the Emerald Tree Boa, have a unique way of sleeping. They loop one or two coils along a branch, saddle style and place their head in the middle. If it is in Indonesia, it is a python, if it is in South America, a boa.",
            6:"The underlying color is either brown, orange as we see here or a mix of the two. It is found in Central and South America and all the way through the Amazon basin. It is medium sized compared to other snakes and it likes the rivers and drainage areas, living for up to 20 years.",
            7:"Very venomous, but on the good side, there are only about 15 to 20 recorded bites a year. On the bad side they are deadly and soon there will be no more antivenin for it. Current stock is due to expire at the end of this year."
            }

snake_colors=((black,black,black),(gray,gray,gray),(red,black,orange),(green,light_yellow,green),(blue,light_blue,black),(light_yellow,gray,light_yellow),(orange,orange,black),(black,purple,light_yellow))

Head=0

Level_list=[pygame.image.load('easy.png'),pygame.image.load('medium.png'),pygame.image.load('hard.png')]
Level=1##hard=1 medium=3 easy=5

clock= pygame.time.Clock()

block_size = 10
appleLength=30

FPS = 30 

smallfont = pygame.font.SysFont("comicsansms", 20)
mediumfont = pygame.font.SysFont("comicsansms", 25)
largefont = pygame.font.SysFont("comicsansms", 57)
tinyfont= pygame.font.SysFont("Arial", 15)

previous = "right"


def snake_cartoon_draw(startpoint):
        pygame.draw.circle(gameDisplay, snake_colors[Head][2],(startpoint[0]-10,startpoint[1]+10+1),int(block_size/2))
        pygame.draw.lines(gameDisplay, snake_colors[Head][0], False, [[startpoint[0]-10,startpoint[1]+10],[startpoint[0]+5,startpoint[1]+10],[startpoint[0]+5,startpoint[1]-10],[startpoint[0]+30,startpoint[1]-10],[startpoint[0]+30,startpoint[1]+20],[startpoint[0]+60,startpoint[1]+20],[startpoint[0]+60,startpoint[1]-20],[startpoint[0]+90,startpoint[1]-20],[startpoint[0]+90,startpoint[1]],[startpoint[0]+120,startpoint[1]]], block_size)#####
        
        pygame.draw.line(gameDisplay, snake_colors[Head][1], ([startpoint[0]+18,startpoint[1]-10-4]), [startpoint[0]+18,startpoint[1]-10+5],10)
        pygame.draw.line(gameDisplay, snake_colors[Head][2], ([startpoint[0]+18,startpoint[1]-10-4]), [startpoint[0]+18,startpoint[1]-10+5],2)

        pygame.draw.line(gameDisplay, snake_colors[Head][1], ([startpoint[0]+45,startpoint[1]-10-3+29]), [startpoint[0]+45,startpoint[1]-10+35],14)
        pygame.draw.line(gameDisplay, snake_colors[Head][2], ([startpoint[0]+46,startpoint[1]-10-3+29]), [startpoint[0]+46,startpoint[1]-10+35],3)


        pygame.draw.line(gameDisplay, snake_colors[Head][1], (startpoint[0]+120-10, startpoint[1]-block_size/2+1), (startpoint[0]+120-10,startpoint[1]-block_size/2+10) ,12)
        pygame.draw.line(gameDisplay, snake_colors[Head][2], (startpoint[0]+120-10, startpoint[1]-block_size/2+1), (startpoint[0]+120-10,startpoint[1]-block_size/2+10) ,4)

        gameDisplay.blit(snakeheads[Head],(startpoint[0]+120,startpoint[1]-block_size/2+1))
        


def game_intro():

    intro = True
    gameDisplay.fill(white)

    random_snake=random.randrange(0,len(snake_image_list))
    gameDisplay.blit(snake_image_list[random_snake] ,(int(display_width* 3/5), 270))
    message_to_screen("Welcome to Snakie", dark_green, -150, "large")
    message_to_screen("The rules are simple: Just eat the fruits", black, -90, "small", 0)  

    h_score,date =read_high_score_file()
    text= smallfont.render("Highest Score: " + str(int(h_score)), True, black)
    gameDisplay.blit(text, [600,0])
    text= smallfont.render("Date: " + str(date), True, black)
    gameDisplay.blit(text, [600,25])

    snake_cartoon_draw([200,300])
    box(white,white, 230,330,30,20 ,snake_names[Head], black, size = "small")

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    mute()
                if event.key == pygame.K_SPACE:
                        gameOver = False
                        GameLoop()
                   
        icons()
        pygame.display.update()


def mute():
    pygame.mixer.Sound.play(click_sound)
    global sound
    if sound == "on":
        sound = "off"
    else:
        sound = "on"

    pygame.display.update()


    

def play_sound(place):
    global sound
    if sound == "on":
        pygame.mixer.Sound.play(place)
    

def message_to_screen(msg, color, displace=0, size = "small", displaceX=0):
    if size == "small":
        screen_text = smallfont.render(msg,True, color)
    if size == "medium":
        screen_text = mediumfont.render(msg,True, color)
    if size == "large":
        screen_text = largefont.render(msg,True, color)
    if size == "tiny":
        screen_text = tinyfont.render(msg,True, color)
    
    textRect = screen_text.get_rect()
    textRect.center = (display_width/2) + displaceX, (display_height/2) + displace
    gameDisplay.blit(screen_text, textRect)



def read_high_score_file():
    f= open('highest_score.txt','r')
    h_score= int(f.readline())
    date=f.readline()
    f.close()
    return h_score,date
    


def icons(state="Start",random_snake=0):
    box(green,light_green, 100,400,120,50 ,"Play", white, size = "small")
    box(blue,light_blue, 300,400,120,50 ,"Settings", white, size = "small")
    box(yellow,light_yellow, 100,500,120,50 ,"High Score", white, size = "small")
    box(red,light_red, 300,500,120,50 ,"Quit", white, size = "small")


    cur = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global sound
    global sound_list
    global Level
    global Head

    if state == "High_Score":
        gameDisplay.blit(info_img ,(310,230))
        if 310<cur[0]<335 and 230<cur[1]<255 and click[0]==1:#####Prints the info for the snake
            tkMessageBox.showinfo(title=snake_names[Head], message=snake_info[Head])
        
    
    if state == "Settings":
        box(white,white, 130,178,120,50 ,"   Fruit Eat:", dark_green, size = "small")
        box(white,white, 130,145,120,50 ," High Score:", dark_green, size = "small")
        box(white,white, 130,112,120,50 ,"Mouse Click:", dark_green, size = "small")
        box(white,white, 90,80,120,50 ,"Sound:", dark_green, size = "medium")

        gameDisplay.blit(info_img ,(770,90))
        if 770<cur[0]<795 and 90<cur[1]<115 and click[0]==1:#####Prints the info for the snake
            tkMessageBox.showinfo(title=snake_names[Head], message=snake_info[Head])
 
        pygame.draw.rect(gameDisplay,white, (600,50,160,100))
        for g in range(8):
                if g==Head:
                        pygame.draw.circle(gameDisplay, gray,(637+12*g,110), int(block_size/2))
                elif 637+12*g -int(block_size/2)<cur[0]<637+12*g +int(block_size/2) and 110 - int(block_size/2)<cur[1]<110+int(block_size/2):
                        pygame.draw.circle(gameDisplay, gray,(637+12*g,110), int(block_size/2))
                        if click[0]==1:
                                Head=g
                else:
                        pygame.draw.circle(gameDisplay, gray,(637+12*g,110), int(block_size/3-1))

        box(white,white, 90,230,120,50 ,"Difficulty:", dark_green, size = "medium")
        pygame.draw.rect(gameDisplay,white, (80,280,350,100))
        if 90 <cur[0]< 90+80   and 290 <cur[1]< 290+80:
            gameDisplay.blit(Level_list[0], (80,280))
            if click[0]==1:
                play_sound(click_sound)
                Level=5
        else:
            gameDisplay.blit(pygame.transform.scale(Level_list[0], (80, 80)), (90,290))####
        if 210 <cur[0]< 210+80   and 290 <cur[1]< 290+80:
            gameDisplay.blit(Level_list[1], (200,280))
            if click[0]==1:
                play_sound(click_sound)
                Level=3
        else:
            gameDisplay.blit(pygame.transform.scale(Level_list[1], (80, 80)), (210,290))####
        if 330 <cur[0]< 330+80   and 290 <cur[1]< 290+80:
            gameDisplay.blit(Level_list[2], (320,280))
            if click[0]==1:
                play_sound(click_sound)
                Level=1
        else:
            gameDisplay.blit(pygame.transform.scale(Level_list[2], (80, 80)), (330,290))####

        l=snake_image_list[random_snake].get_rect()
        pygame.draw.rect(gameDisplay,white, (int(display_width* 3/5), 270,420,display_height-270))
        if Level==5:
            gameDisplay.blit(Level_list[0], (80,280))
            gameDisplay.blit(pygame.transform.scale(snake_image_list[random_snake], (int((l[2]-l[0])*0.6), int((l[3]-l[1])*0.6))), (int(display_width* 3/5)+100, 330))
        elif Level==3:
            gameDisplay.blit(Level_list[1], (200,280))
            gameDisplay.blit(pygame.transform.scale(snake_image_list[random_snake], (int((l[2]-l[0])*0.8), int((l[3]-l[1])*0.8))), (int(display_width* 3/5)+50, 300))
        else:
            gameDisplay.blit(Level_list[2], (320,280))
            gameDisplay.blit(snake_image_list[random_snake] ,(int(display_width* 3/5), 270))
            


        box(white,white, 482,80,120,50 ,"Snake:", dark_green, size = "medium")

        pygame.draw.rect(gameDisplay,white, (565,125,420,100))
        gameDisplay.blit(pygame.transform.scale(chose_snake_list[1], (40, 40)), (600,130))
        gameDisplay.blit(pygame.transform.scale(chose_snake_list[2], (40, 40)), (660,130))
        gameDisplay.blit(pygame.transform.scale(chose_snake_list[0], (40, 40)), (720,120))

        if 600 <cur[0]< 600+40   and 130 <cur[1]< 130+30:
            gameDisplay.blit(chose_snake_list[1],(595,125))
            if click[0]==1:
                play_sound(click_sound)
                Head-=1
                time.sleep(0.1)
        elif 660 <cur[0]< 660+40   and 130 <cur[1]< 130+30:
            gameDisplay.blit(chose_snake_list[2],(655,125))
            if click[0]==1:
                play_sound(click_sound)
                Head=random.randrange(0,len(snakeheads))
        elif 720 <cur[0]< 720+40   and 120 <cur[1]< 120+30:
            gameDisplay.blit(chose_snake_list[0],(715,115))
            if click[0]==1:
                play_sound(click_sound)
                Head+=1
                time.sleep(0.1)
        
        if Head<0:
            Head=len(snakeheads)-1
        elif Head>len(snakeheads)-1:
            Head=0


        startpoint=[620,70]
        snake_cartoon_draw(startpoint)
        box(white,white, 490,180,350,40 ,snake_names[Head], black, size = "small")
        

        if sound=="on":
            gameDisplay.blit(sound_on_img, (200,95))
        else:
            gameDisplay.blit(sound_off_img, (200,95))


        if 250 > cur[0] > 200 and 115 > cur[1] > 95 and click[0]==1:
            pygame.mixer.Sound.play(click_sound)
            time.sleep(0.1)
            if sound=="on":
                sound="off"
            else:
                sound="on"
        
        global new_level
        global eat_sound
        for j in range(3):
            if  260+5*13 <cur[0]< 260+5*13+50 and 130 +j*31 <cur[1]< 130+j*31+20 and click[0]==1:
                time.sleep(0.1)
                if sound_list[j]==0 and sound=="on":
                    sound_list[j]=0.6
                    click_sound.set_volume(0.6)
                    play_sound(click_sound)
                else:
                    sound_list[j]=0
                    if j==0:
                        click_sound.set_volume(0)
                    elif j==1:
                        new_level.set_volume(0)
                    else:
                        eat_sound.set_volume(0)

        for i in range(5):
            for j in range(3):
                if  260 + i*13 < cur[0] < 260 + i*13 +10 and 130 +j*31 < cur[1] < 130 +j*31 +20 and click[0]==1:
                    #global sound_list
                    sound_list[j]=(i+1)*1.0/5.0
                    if j==0:
                        #global click_sound
                        click_sound.set_volume(sound_list[0])
                        play_sound(click_sound)
                        
                    elif j==1:
                        #global new_level
                        new_level.set_volume(sound_list[1])
                        play_sound(new_level)
                    else:
                        #global eat_sound
                        eat_sound.set_volume(sound_list[2])
                        play_sound(eat_sound)


        for j in range(3):    
            for i in range(260,260+5*13,13):                
                if i < 260+sound_list[j]*5*13:
                    if  i < cur[0] <i+10 and 130+j*31 < cur[1] <130+j*31 +20:
                        pygame.draw.rect(gameDisplay,black, (i,130+j*31-2,10,20+4))
                    else:
                        pygame.draw.rect(gameDisplay,white, (i,130+j*31-2,10,2))
                        pygame.draw.rect(gameDisplay,white, (i,130+j*31+20,10,2))
                        pygame.draw.rect(gameDisplay,black, (i,130+j*31,10,20))
                else:
                    if  i < cur[0] <i+10 and 130+j*31 < cur[1] <130+j*31 +20:
                        pygame.draw.rect(gameDisplay,gray, (i,130+j*31-2,10,20+4))
                    else:
                        pygame.draw.rect(gameDisplay,white, (i,130+j*31-2,10,2))
                        pygame.draw.rect(gameDisplay,white, (i,130+j*31+20,10,2))
                        pygame.draw.rect(gameDisplay,gray, (i,130+j*31,10,20))
            if sound_list[j]==0 or sound=="off":
                gameDisplay.blit(sound_off_img, (i+16,130+j*31))
            else:
                gameDisplay.blit(sound_on_img, (i+16,130+j*31))
    else:            
        
        if sound == "on":
            gameDisplay.blit(unmute_icon, (2,568))
        else:
            gameDisplay.blit(mute_icon, (2,568))
        
        



    if 220 > cur[0] > 100 and 450 > cur[1] > 400 and click[0]==1:
        GameLoop()
    elif 420 > cur[0] > 300 and 450 > cur[1] > 400 and click[0]==1:
        if state != "Settings":
            Settings()
    elif 220 > cur[0] > 100 and 550 > cur[1] > 500 and click[0]==1:
        if state != "High_Score":
            High_Score()
    elif 420 > cur[0] > 300 and 550 > cur[1] > 500 and click[0]==1:
        pygame.quit()
        quit()


    
    

def box(color, highlighted_color, cornerX, cornerY, length, width, msg, msg_color, size = "small"):
    pygame.draw.rect(gameDisplay,color, (cornerX, cornerY, length, width))
    cur = pygame.mouse.get_pos()
    if cornerX+ length > cur[0] > cornerX and cornerY +width > cur[1] > cornerY:
        pygame.draw.rect(gameDisplay,highlighted_color, (cornerX, cornerY, length, width))       
  
    if size == "small":
        screen_text = smallfont.render(msg,True, msg_color)
    if size == "medium":
        screen_text = mediumfont.render(msg,True, msg_color)
    if size == "large":
        screen_text = largefont.render(msg,True, msg_color)

    
    textRect = screen_text.get_rect()
    textRect.center = (cornerX+length/2), (cornerY+width/2)
    gameDisplay.blit(screen_text, textRect)

def Settings():
    play_sound(click_sound)
    control=True
    gameDisplay.fill(white)
    random_snake=random.randrange(0,len(snake_image_list))
    random_color=random.randrange(0,len(colors_list))
    message_to_screen("Settings", dark_green, -250, "large")
    message_to_screen(message_list[0], yellow, 280, "small", -140)

    i=0
    left=True
    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    mute()
                if event.key == pygame.K_SPACE:
                        gameOver = False
                        GameLoop()
            
        icons("Settings",random_snake)
        box(light_blue,light_blue, 300,400,120,50 ,"Settings", white, size = "small")
        pygame.draw.rect(gameDisplay, white, [0, display_height-30,display_width*0.7, 30])
        message_to_screen(message_list[0], colors_list[random_color], 280, "small", -60 -int(i))
        if i<0:
            left=True
        elif i>170:
            left=False
        if left:
            i+=0.1
        else:
            i-=0.1
        pygame.display.update()
        


    
def High_Score():
    play_sound(click_sound)    
    intro = True
    gameDisplay.fill(white)
    random_snake=random.randrange(0,len(snake_image_list))
    random_color=random.randrange(0,len(colors_list))
    gameDisplay.blit(snake_image_list[random_snake] ,(int(display_width* 3/5), 270))
    message_to_screen("Highest Score", dark_green, -250, "large")
    h_score,date =read_high_score_file()


    message_to_screen(str(int(h_score)) +" points, " + str(date), black, -170, "medium")    

    startpoint=[150,250]
    snake_cartoon_draw(startpoint)
    box(white,white, 200,280,30,20 ,snake_names[Head], black, size = "small")
    
    i=0
    left=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    mute()
                if event.key == pygame.K_SPACE:
                        gameOver = False
                        GameLoop()
                    
        icons("High_Score")
        box(light_yellow,light_yellow, 100,500,120,50 ,"High Score", white, size = "small")
        pygame.draw.rect(gameDisplay, white, [37, display_height-30,display_width*0.6, 30])
        message_to_screen(message_list[0], colors_list[random_color], 280, "small", -60 -int(i))
        if i<0:
            left=True
        elif i>130:
            left=False
        if left:
            i+=0.1
        else:
            i-=0.1
            
        pygame.display.update()
    
   

def pause():
    play_sound(click_sound)
    paused = True
    gameDisplay.blit(pause_img, (15,int(display_height/4)))

    i=int(display_width * 3.0/5.0)-20
    color=random.randrange(0,len(colors_list))
    left=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_m:
                    mute()
                    global sound
                    if sound == "on":
                        gameDisplay.blit(unmute_icon, (2,568))
                    else:
                        gameDisplay.blit(mute_icon, (2,568))
                else:    
                    paused = False
            
        
        pygame.draw.rect(gameDisplay, white, [0, 300,display_width, 50])
        box(white, white, i, 320, 300, 30, "Press Q to quit or Any Key to continue", colors_list[color], size = "small")
        if left:
            i-=5###
        else:
            i+=5
        if i<100:
            left=False
        elif i> int(display_width * 3.0/5.0) -50:
            left=True
        pygame.display.update()
        clock.tick(5)



h_score,date =read_high_score_file()
first = h_score

def score(score):
    text= smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [2,40])
    level=round(score/10)+1
    text= smallfont.render("Level: " + str(int(level)), True, black)
    gameDisplay.blit(text, [2,0])

    score=int(score)
    if score == first + 1:
        play_sound(new_level)
        global message_list
        del message_list[0]
        message_list.append("New high score")

    h_s,date =read_high_score_file()
    if score >  h_s:
        f= open('highest_score.txt','w')
        f.write(str(score)+'\n'+ str(time.strftime("%d/%m/%Y")))
        f.close()
        

    s,date =read_high_score_file()
    text= smallfont.render("Highest Score: " + str(s), True, black)
    gameDisplay.blit(text, [600, 0])
    text= smallfont.render("Date: " + str(date), True, black)
    gameDisplay.blit(text, [600,25])


    

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width- appleLength)/10.0)*10.0
    randAppleY = round(random.randrange(70, display_height- appleLength -70)/10.0)*10.0

    return randAppleX, randAppleY


def snake(block_size, snakeList):

    if previous == "right":
        head = snakeheads[Head]
    if previous == "left":
        head = pygame.transform.rotate(snakeheads[Head],180)
    if previous == "up":
        head = pygame.transform.rotate(snakeheads[Head],90)
    if previous == "down":
        head = pygame.transform.rotate(snakeheads[Head],270)


    global sound
    if sound == "on":
        gameDisplay.blit(unmute_icon, (2,568))
    else:
        gameDisplay.blit(mute_icon, (2,568))    

    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))

    k=1
    for XnY in snakeList[:-1]:
        if k%7==0 or k%9==0:
            pygame.draw.rect(gameDisplay, snake_colors[Head][1], [XnY[0],XnY[1], block_size,block_size])
        elif k%8==0:
            pygame.draw.rect(gameDisplay, snake_colors[Head][2], [XnY[0],XnY[1], block_size,block_size])
        else:
            pygame.draw.rect(gameDisplay, snake_colors[Head][0], [XnY[0],XnY[1], block_size,block_size])
        k+=1
    #########


    
def GameLoop():
    play_sound(click_sound)
    rolling_message=display_width
    message=random.randrange(0,len(message_list))
    color=random.randrange(0,len(colors_list))
    color1=random.randrange(0,len(colors_list))

    predator=False
    predator_image=0
    
    global previous
    gameExit= False
    gameOver= False

    pygame.mouse.set_visible(False)

    lead_x=display_width/2
    lead_y=display_height/2

    lead_x_change=0
    lead_y_change=0

    snakeList=[]
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    chose_fruit=random.randrange(0,len(fruit_image_list))

    PredatorX,PredatorY=0,0

    time=int(display_width/2)

    left=True
    m=-100
    while not gameExit: # while gameExit = False

        if gameOver == True:
            pygame.mouse.set_visible(True)
            gameDisplay.fill(white)
            random_snake=random.randrange(0,len(snake_image_list))
            gameDisplay.blit(snake_image_list[random_snake] ,(int(display_width* 3/5), 270))

            if Level==3:
                t_score=(snakeLength-1)*1.0/2
            else:
                t_score=(snakeLength-1)*1.0/Level 
            
            message_to_screen("Game Over!", red, -145, "large")
            message_to_screen("Total Score= " + str(t_score), black, displace=-80, size = "medium")
            message_to_screen("Level= " + str(int(round(t_score/10)+1)), black, displace=-45, size = "medium")



            if snakeLength > first +1:
                gameDisplay.blit(high_score_img, (0,0))

            high_score,date =read_high_score_file()
            text= smallfont.render("Highest Score: " + str(high_score), True, black)
            gameDisplay.blit(text, [600, 0])
            text= smallfont.render("Date: " + str(date), True, black)
            gameDisplay.blit(text, [600,25])

            snake_cartoon_draw([120,320])
            box(white,white, 150,350,30,20 ,snake_names[Head], black, size = "small")

            i=0
            left=True
            random_color=random.randrange(0,len(colors_list))
            pygame.display.update()
        
        while gameOver ==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        mute()
                    if event.key == pygame.K_SPACE:
                        gameOver = False
                        GameLoop()
                    
            icons()
            pygame.draw.rect(gameDisplay, white, [37, display_height-30,display_width*0.6, 30])
            message_to_screen("Highest Score: "+ str(high_score) +" (Date: "+ str(date)+")", colors_list[random_color], 280, "small", -70 -int(i)) ##-140
            if i<0:
                left=True
            elif i>115:
                left=False
            if left:
                i+=0.1
            else:
                i-=0.1
            pygame.display.update()
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_LEFT and previous != "right":
                    previous="left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and previous != "left":
                    previous="right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP and previous != "down":
                    previous = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and previous != "up":
                    previous = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_m:
                    mute()
        


        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver = True
        
        lead_x+= lead_x_change
        lead_y+= lead_y_change 
        gameDisplay.fill(white)
        gameDisplay.blit(fruit_image_list[chose_fruit], (randAppleX,randAppleY))

        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_size, snakeList)

        if len(snakeList) >snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver=True

        
        message_to_screen(message_list[message], colors_list[color], 280, "small", rolling_message)
        rolling_message-=2
        if rolling_message==-600:
            rolling_message = display_width
            message=random.randrange(0,len(message_list))
            color=random.randrange(0,len(colors_list))
        snake(block_size, snakeList)

        ######## predator
        if snakeLength % 10 ==3 and predator==False:#######
                predator_image=0 ###0 for left, 1 for right
                random_predator=random.randrange(3)###0for owl, 1 for eagle,2 for cat
                PredatorX, PredatorY = randAppleGen()
                while abs(PredatorY-lead_y)<100 or PredatorX>display_width-150 or (abs(PredatorY-randAppleY)<200 and abs(PredatorX-randAppleX)<200):
                        PredatorX, PredatorY = randAppleGen()
                if random_predator==0 or random_predator==1:
                        PredatorX=display_width
                predator=True

        if predator:
                gameDisplay.blit(predator_list[random_predator][predator_image], (PredatorX, PredatorY))
                if PredatorX<=lead_x<=PredatorX+porportions_list[random_predator][predator_image][0] and PredatorY<=lead_y<=PredatorY+porportions_list[random_predator][predator_image][1]:
                        gameOver=True
                        predator = False

                if  2<snakeLength%10<8:
                        if random_predator==0 or random_predator==1:
                                if lead_x>PredatorX:
                                        PredatorX+=3
                                        predator_image=1
                                elif lead_x<PredatorX:
                                        PredatorX-=3
                                        predator_image=0
                                if lead_y>PredatorY:
                                        PredatorY+=3
                                elif lead_y<PredatorY:
                                        PredatorY-=3
                else:
                        if random_predator==2:
                                PredatorX+=display_width
                                
                        predator_image=1
                        PredatorX+=3        
                        if lead_y>PredatorY:
                                PredatorY+=3
                        elif lead_y<PredatorY:
                                PredatorY-=3
                        if PredatorX>display_width:
                                predator=False
                        

        #######
        if Level==1 or Level==3:
                center=display_width/4+int(time)
                if time>255:
                        pygame.draw.rect(gameDisplay,green, (display_width/4, display_height-40,time, block_size/2))
                        for b in range(10):
                                pygame.draw.circle(gameDisplay, green,(center+random.randrange(-5,15),display_height-40+random.randrange(-10,10)),random.randrange(1,5))
                elif time<100:
                        pygame.draw.rect(gameDisplay,red, (display_width/4, display_height-40,time, block_size/2))
                        for b in range(10):
                                pygame.draw.circle(gameDisplay, red,(center+random.randrange(-5,15),display_height-40+random.randrange(-10,10)),random.randrange(1,5))
                        play_sound(new_level)
                else:
                        pygame.draw.rect(gameDisplay,(255,time,0), (display_width/4, display_height-40,time, block_size/2))
                        for b in range(10):
                                pygame.draw.circle(gameDisplay, (255,time,0),(center+random.randrange(-5,15),display_height-40+random.randrange(-10,10)),random.randrange(1,5) )
                if Level==1:
                        time-=1
                else:
                        time-=0.5
                if time==0:
                        gameOver=True##########

        ########

        if Level==3:
            score((snakeLength-1)*1.0/2)
        else:
            score((snakeLength-1)*1.0/Level)          


        if m>100 or m<-170:
            left= not left
            color1=random.randrange(0,len(colors_list))
        if left:
            m+=1
        else:
            m-=1
        
        message_to_screen(snake_names[Head], colors_list[color1], -250, "small", m)
        
        pygame.draw.rect(gameDisplay,yellow, (int(display_width/2 - 1.5*first), 8, 2*first, block_size))
        pygame.draw.rect(gameDisplay,red, (int(display_width/2 - 1.5*first), 8, 2*snakeLength -1, block_size))
        gameDisplay.blit(start_img, (int(display_width/2 - 1.5*first)-100,0))
        gameDisplay.blit(finish_img, (int(display_width/2 - 1.5*first)+2*first,0))
                
        pygame.display.update()

        if lead_x>=randAppleX and lead_x<randAppleX + appleLength and lead_y>=randAppleY and lead_y<randAppleY + appleLength:
            play_sound(eat_sound)
            if Level==1:
                    time+=80
            elif Level==3:
                    time+=40
            if time>3.0 * display_width/4.0 -20:
                    time=int(3.0 * display_width/4.0 -20)

            randAppleX, randAppleY = randAppleGen()
            while (abs(PredatorY-randAppleY)<200 and abs(PredatorX-randAppleX)<200):
                    randAppleX, randAppleY = randAppleGen()
            chose_fruit=random.randrange(0,len(fruit_image_list))
            snakeLength+=1
            
        clock.tick(FPS+ int(len(snakeList)/Level)-Level)
        
game_intro()
GameLoop()

pygame.quit()
quit()
