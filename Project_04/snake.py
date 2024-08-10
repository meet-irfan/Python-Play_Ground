import pygame
import time
import random

pygame.init()

black = (51,255,255)
white = (255,153,51)
green = (0,0,0)
red = (153, 0, 153)
yellow = (51,0,0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri",25)
score_font = pygame.font.SysFont("comicsans",34)
# print(pygame.font.get_fonts())

def my_score(score):
    value = score_font.render("Score: "+str(score),True,yellow)
    dis.blit(value, [0,0])

def message(msg,color):
    mssg = font_style.render(msg,True,color)
    dis.blit(mssg,[0,dis_height/2])


def my_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_block,snake_block])



def main_game():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list =[]
    length_snake = 1

    foodx = round(random.randrange(0,dis_width- snake_block)/10.0)*10.0
    foody = round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("  Sorry Bro: ------ You lost!  Press P to Play And  Q to Quit",red)


            my_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis,red, [foodx,foody,snake_block,snake_block] )
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_list.append(snake_size)
        if len(snake_list) > length_snake:
            del snake_list[0]

        my_snake(snake_block,snake_list)
        my_score(length_snake - 1)

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height-snake_block) / 10.0) * 10.0
            length_snake +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main_game()

