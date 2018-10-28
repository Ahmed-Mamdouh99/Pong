import sys, pygame, time
from gui.ball import Ball
from gui.pausemenu import Pausetext
from gui.scoreboard import Scoreboard
from gui.frame import Frame
from gui.paddle import Paddle


BLACK = 0, 0, 0


def move_ball(frect, lpad, rpad, ball, score):
    left = ball.rect.left
    right = ball.rect.right
    up = ball.rect.top
    down = ball.rect.bottom
    x = ball.speed[0]
    y = ball.speed[1]
    #Checking horizontal collisions
    #Left side
    if x < 0 and left <= lpad.right:
        if ball.rect.colliderect(lpad): #Left paddle
            ball.speed[0] *= -1
        elif left <= frect.left: #Left wall
            ball.speed[0] *= -1
            score = score[0], score[1] + 1
    #Right side
    if x > 0 and right >= rpad.left:
        if ball.rect.colliderect(rpad): #Right paddle
            ball.speed[0] *= -1
        elif right >= frect.right: #Right wall
            ball.speed[0] *= -1
            score = score[0] + 1, score[1]
    #Checking vertical collisions
    #Top
    if y < 0 and up <= frect.top:
        ball.speed[1] *= -1
    #Bottom
    elif y > 0 and down >= frect.bottom:
        ball.speed[1] *= -1
    #Move the ball's rectangle
    ball.move()
    return score


def pause_game(screen, clock):
    pause = Pausetext()
    while 1:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Close the game
                sys.exit()
            keys = pygame.key.get_pressed()
            #Resume
            if keys[pygame.K_ESCAPE]:
                return
        screen.fill(BLACK)
        screen.blit(pause.surface, [0, 0])
        pygame.display.flip()


def game_loop(screen, frame, lpad, rpad, ball, scoreboard):
    clock = pygame.time.Clock()
    done = False
    score = 0, 0
    start_time = int(time.time())
    #Game loop
    while not done:
        #Check for winner
        if 10 in score:
            if score[0] == 1:
                print('Left side wins')
            else:
                print('Right side wins')
            done = True
        #Change ball speed
        elapsed_time = int(time.time() - start_time) + 1
        if elapsed_time % 10 == 0:
            start_time = time.time()
            ball.speed = [(ball.speed[0] + 1), (ball.speed[1] + 1)]
        clock.tick(120)#Setting refresh rate
        for event in pygame.event.get():#Handing events
            if event.type == pygame.QUIT: #Close the game
                return
            keys = pygame.key.get_pressed()
            #Left pad
            if keys[lpad.up]:
                lpad.direc = -1
            elif keys[lpad.dwn]:
                lpad.direc = 1
            else:
                lpad.direc = 0
            #Right pad
            if keys[rpad.up]:
                rpad.direc = -1
            elif keys[rpad.dwn]:
                rpad.direc = 1
            else:
                rpad.direc = 0
            #Pause
            if keys[pygame.K_ESCAPE]:
                pause_game(screen, clock)
        #Moving the ball and updating scoreboard
        score = move_ball(frame.rect, lpad.rect, rpad.rect, ball, score)
        scoreboard.update(score)
        #Moving the paddles
        lpad.move(frame.rect)
        rpad.move(frame.rect)
        #Redrawing the screen
        screen.fill(BLACK)
        shapes = (frame, lpad, rpad, ball, scoreboard)
        for x in shapes:
            screen.blit(x.surface, x.rect)
        pygame.display.flip()


def main():
    ball_speed = 3
    paddle_speed = 5
    #Starting pygame
    pygame.init()
    #Setting screen
    size = width, height = 1360, 768
    screen = pygame.display.set_mode(size)
    #Making the frame
    frame = Frame(dimensions=size)
    #Making the left paddle and setting its speed
    lpad = Paddle(pos=[0, height // 2], up=pygame.K_w, dwn=pygame.K_s, speed=paddle_speed)
    #Making the right paddle and setting its speed
    rpad = Paddle(pos=[width-20, height // 2], speed=paddle_speed)
    #Making the ball and setting its speed
    ball = Ball(pos=[width // 2, height // 2], speed=[ball_speed,ball_speed])
    #Making the scoreboard
    scoreboard = Scoreboard((0, 0), pos=[width //2 ,0])
    #Starting game loop
    game_loop(screen, frame, lpad, rpad, ball, scoreboard)
    #Quitting the game
    pygame.quit()

if __name__ == '__main__':
    main()
