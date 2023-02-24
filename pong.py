import pygame
import random
pygame.init()

# Colors
white = (255,255,255)
red = (255, 0, 0)
orange=(255,165,0)
yellow=(255,255,0)
green=(0,255,0)
blue=(0,0,255)
pink=()
brown=()
purple=()
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    return screen_text

def set_image(name,size_x,size_y):
    img=pygame.image.load(name)
    img=pygame.transform.scale(img,(size_x,size_y)).convert_alpha()
    gameWindow.blit(img,(0,0))

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Play TENNIS", black, 340, 200)
        text_screen("Press Space Bar To Play", black, 232, 290)

        pygame.draw.rect(gameWindow,blue,[343,408,230,45])
        pygame.draw.rect(gameWindow,white,[345,410,225,40])
        text_screen("Game Rules", red, 345, 410)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enteries()
                    '''score1=0
                    score2=0
                    gameloop(score1,score2,a,p2)'''
                    
            if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if x>345 and x<570 and y>410 and y<450:
                        rules()
                        
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    quit()

def rules():
    exit_game = False
    while not exit_game:
        gameWindow.fill(green)
        pygame.draw.rect(gameWindow,black,[0,100,900,1])
        pygame.draw.rect(gameWindow,black,[0,500,900,1])
        pygame.draw.rect(gameWindow,black,[225,100,1,400])
        pygame.draw.rect(gameWindow,black,[675,100,1,400])
        pygame.draw.rect(gameWindow,black,[450,100,2,400])
        pygame.draw.rect(gameWindow,black,[225,300,450,1])

        pygame.draw.rect(gameWindow,blue,[748,518,104,44])
        pygame.draw.rect(gameWindow,white,[750,520,100,40])
        text_screen("Back", red, 750, 520)
        pygame.draw.rect(gameWindow,black,[0,225,10,150])
        pygame.draw.rect(gameWindow,black,[890,225,10,150])
        pygame.draw.circle(gameWindow,white,(450,300),10)
        text_screen("Use 'W' & 'S' to move left stick up & down", yellow, 50, 10)
        text_screen("Use '8' & '2' to move right stick up & down", yellow, 50, 50)
        text_screen("First one to score 5 points win.", yellow, 50, 510)
        pygame.draw.circle(gameWindow,blue,(25,25),7)
        pygame.draw.circle(gameWindow,blue,(25,65),7)
        pygame.draw.circle(gameWindow,blue,(25,525),7)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if x>750 and x<850 and y>520 and y<560:
                        welcome()
            
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    quit()

def enteries():
    a=""
    p2=""
    l1=300
    l2=300
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        #set_image("snakes2.png",150,150)
        text_screen("ENTER NAMES", black, 300, 100)
        text_screen("(only in small letters)", black, 260, 150)
        text_screen("Player 1 :", black, 10, 250)
        text_screen("Player 2 :", black, 10, 300)
        pygame.draw.rect(gameWindow,white,[200,250,l1,40])
        pygame.draw.rect(gameWindow,white,[200,300,l2,40])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if x>200 and x<500 and y>250 and y<290:
                   if '|' not in a: 
                       a=a+"|"
                else:
                    if len(a)>0:
                        a=a[0:len(a)-1]
                if x>200 and x<500 and y>300 and y<340:
                    if '|' not in p2:
                        p2=p2+"|"
                else:
                    if len(p2)>0:
                        p2=p2[0:len(p2)-1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if '|' in a:
                        if len(a)>1:
                            a=a[0:len(a)-2]+"|"
                    if '|' in p2:
                        if len(p2)>1:
                            p2=p2[0:len(p2)-2]+"|"
                if '|' in a:
                    b=pygame.key.name(event.key)
                    try:
                        c=pygame.key.key_code(b)
                    except ValueError:
                        c=0
                    if c>31 and c<127:
                        if ts1.get_width()<300:
                            a=a[0:len(a)-1]+chr(int(c))+'|'
                if '|' in p2:
                    d=pygame.key.name(event.key)
                    try:
                        e=pygame.key.key_code(d)
                    except ValueError:
                        e=0
                    if e>31 and e<127:
                        if ts2.get_width()<300:
                            p2=p2[0:len(p2)-1]+chr(int(e))+'|'
                if event.key == pygame.K_RETURN:
                    score1=0
                    score2=0
                    gameloop(score1,score2,a,p2,ts1,ts2)
                    
        ts1=text_screen(a,black,200,250)
        ts2=text_screen(p2,black,200,300)
        if ts1.get_width()>300:
            l1=int(ts1.get_width())+1
        else:
            l1=300
        if ts2.get_width()>300:
            l2=int(ts2.get_width())+1
        else:
            l2=300
        text_screen("press Enter to start",black,250,400)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
                
def gameloop(score1,score2,a,p2,ts1,ts2):
    exit_game = False
    game_over = False
    t1_y = screen_height/2-75
    t2_y = screen_height/2-75
    ball_x=screen_width/2
    ball_y=screen_height/2
    vel=[5,-5]
    velocity_x =0
    velocity_y =0
    vel_t1=0
    vel_t2=0
    v=[0,0]
    tick=50
    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            if score1==5:
                text_screen("Player 1 WINS :)", blue, 330, 200)
            elif score2==5:
                text_screen("Player 2 WINS :)", blue, 330, 200)
            else:
                text_screen("Game exited", blue, 330, 200)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if x>50 and x<470 and y>510 and y<560:
                        game_over=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if t1_y>100 and (velocity_x!=0 and velocity_y!=0):
                            vel_t1=-5

                    if event.key == pygame.K_s:
                        if t1_y<350 and (velocity_x!=0 and velocity_y!=0):
                            vel_t1=+5

                    if event.key == pygame.K_KP_8:
                        if t2_y>100 and (velocity_x!=0 and velocity_y!=0):
                            vel_t2=-5

                    if event.key == pygame.K_KP_2:
                        if t2_y<350 and (velocity_x!=0 and velocity_y!=0):
                            vel_t2=+5

                    if event.key == pygame.K_RETURN:
                        if v[0]==0 and v[1]==0 and velocity_x==0 and velocity_y==0:
                            velocity_x = vel[random.randint(0,1)]
                            velocity_y = vel[random.randint(0,1)]
                            v[0]=velocity_x
                            v[1]=velocity_y
                        elif v[0]!=0 and v[1]!=0 and velocity_x==0 and velocity_y==0:
                            velocity_x=v[0]
                            velocity_y=v[1]

                    if event.key == pygame.K_SPACE:
                        if velocity_x!=0 and velocity_y!=0:
                            v[0]=velocity_x
                            v[1]=velocity_y
                            velocity_x=0
                            velocity_y=0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        vel_t1=0

                    if event.key == pygame.K_s:
                        vel_t1=0

                    if event.key == pygame.K_KP_8:
                        vel_t2=0

                    if event.key == pygame.K_KP_2:
                        vel_t2=0

            gameWindow.fill(green)
            pygame.draw.rect(gameWindow,black,[0,100,900,1])
            pygame.draw.rect(gameWindow,black,[0,500,900,1])
            pygame.draw.rect(gameWindow,black,[225,100,1,400])
            pygame.draw.rect(gameWindow,black,[675,100,1,400])
            pygame.draw.rect(gameWindow,black,[450,100,2,400])
            pygame.draw.rect(gameWindow,black,[225,300,450,1])

            pygame.draw.rect(gameWindow,blue,[48,508,204,44])
            pygame.draw.rect(gameWindow,white,[50,510,200,40])
            text_screen("End Game", red, 50, 510)
            
            pygame.draw.rect(gameWindow,yellow,[3,45,int(ts1.get_width())+50,50])
            pygame.draw.rect(gameWindow,yellow,[895-(int(ts2.get_width())+50),502,int(ts2.get_width())+50,50])
            if '|' in a:
                a=a[0:len(a)-1]
                if len(a)>0:
                    text_screen(a + ": "+str(score1), red, 5, 50)
                else:
                    pygame.draw.rect(gameWindow,yellow,[3,45,200,50])
                    text_screen("Player 1:" + str(score1), red, 5, 50)
            else:
                if len(a)>0:
                    text_screen(a + ": "+str(score1), red, 5, 50)
                else:
                    pygame.draw.rect(gameWindow,yellow,[3,45,200,50])
                    text_screen("Player 1:" + str(score1), red, 5, 50)
            if '|' in p2:
                p2=p2[0:len(p2)-1]
                if len(p2)>0:
                    text_screen(p2 + ": "+str(score2), red, 895-(int(ts2.get_width())+50), 505)
                else:
                    pygame.draw.rect(gameWindow,yellow,[695,502,200,50])
                    text_screen("Player 2:" + str(score2), red, 700, 505)
            else:
                if len(p2)>0:
                    text_screen(p2 + ": "+str(score2), red, 895-(int(ts2.get_width())+50), 505)
                else:
                    pygame.draw.rect(gameWindow,yellow,[695,502,200,50])
                    text_screen("Player 2:" + str(score2), red, 700, 505)

            if velocity_x==0 and velocity_y==0:
                vel_t1=0
                vel_t2=0
                if v[0]==0 and v[1]==0:
                    text_screen("Press Enter To Start", blue, 250, 5)
                else:
                    text_screen("Game paused", black, 300, 100)
                    text_screen("Press Enter To Continue", black, 230, 5)
            else:
                text_screen("Press Space To Pause", black, 250, 5)

            t1_y=t1_y+vel_t1
            t2_y=t2_y+vel_t2
                
            ball_x+=velocity_x
            ball_y+=velocity_y
            if t1_y<=100 or t1_y>=350:
                vel_t1=0
            if t2_y<=100 or t2_y>=350:
                vel_t2=0

            if (ball_x==15 and ball_y>t1_y-7 and ball_y<t1_y+157) or (ball_x==885 and ball_y>t2_y-6 and ball_y<t2_y+156) and (velocity_x!=0 and velocity_y!=0):
                velocity_x = velocity_x*(-1)
                tick+=5
            if (ball_x==20 and ball_y>t1_y-7 and ball_y<t1_y+157) and (velocity_x!=0 and velocity_y!=0):
                if velocity_x<0:
                    velocity_x = velocity_x*(-1)
                    tick+=5
            if (ball_x==880 and ball_y>t2_y-7 and ball_y<t2_y+157) and (velocity_x!=0 and velocity_y!=0):
                if velocity_x>0:
                    velocity_x = velocity_x*(-1)
                    tick+=5
                
            """
                velocity_x+=velocity_x/abs(velocity_x)*0.5
                velocity_y+=velocity_y/abs(velocity_y)*0.5"""

            if ball_y==110 or ball_y==490:
                velocity_y = velocity_y*(-1)

            pygame.draw.circle(gameWindow,white,(ball_x,ball_y),10)
            pygame.draw.rect(gameWindow,black,[0,t1_y,10,150])
            pygame.draw.rect(gameWindow,black,[890,t2_y,10,150])
                
            if ball_x==10:
                score2+=1
                gameloop(score1,score2,a,p2,ts1,ts2)
                
            if ball_x==890:
                score1+=1
                gameloop(score1,score2,a,p2,ts1,ts2)
                
            if score1==5 or score2==5:
                game_over=True
                    
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()
    quit()
welcome()
