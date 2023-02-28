#import libraries
import pygame 
from pygame.locals import *
import random

#set widow size
size = width, height = (600, 600)

#define road width in screen
road_w = int(width/1.6)
roadmark_w = int(width/60)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame .init()
running = True
screen = pygame.display.set_mode((size))
#set title
pygame.display.set_caption("Formula Josh")
#set background color
screen.fill((60, 220, 0))

#apply changes
pygame.display.update()

#player car
car = pygame.image.load("car.png")
car_location = car.get_rect()
car_location.center = right_lane, height*0.8

#cpu car
cpu_car = pygame.image.load("cpu_car.png")
cpu_car_location = cpu_car.get_rect()
cpu_car_location.center = left_lane, height*0.2

counter = 1
#game loop
while running:
    #incread difficulty
    if counter == 1024:
        speed += 1
        counter = 1
    #animate cpu_car
    cpu_car_location[1] += speed
    if cpu_car_location[1] > height:
        # cpu_car_location[1] = height*-1
        if random.randint(0,1) == 0:
            cpu_car_location.center = right_lane, height*-1
        else:
            cpu_car_location.center = left_lane, height*-1
    
    #end game
    if car_location[0] == cpu_car_location[0] and cpu_car_location[1] == car_location [1] -128:
        print("GAME OVER. YOU LOSE!!!")
        break

    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running =False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location = car_location.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_location = car_location.move([int(road_w/2), 0])
    #draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2-roadmark_w/2, 0, roadmark_w, height))
    pygame.draw.rect(screen,(255, 255, 255),(width/2-road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(screen,(255, 255, 255),(width/2+road_w/2 - roadmark_w*3, 0, roadmark_w, height))            
    screen.blit(car, car_location)
    screen.blit(cpu_car, cpu_car_location)
    pygame.display.update()

pygame.quit()