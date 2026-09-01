import pygame
from pygame.locals import *
pygame.init()

width = 1100
height = 1000

window = pygame.display.set_mode((width,height))

#clock = pygame.time.clock()
#timeTracker = clock.tick(60)

white = 255,255,255
yellow = 255,255,0
grey = 80,80,80
red = 200,0,0

window.fill((0,0,120))
ground = pygame.draw.rect(window,'green',(0,600,1100,400))

sun = pygame.draw.circle(window,yellow,(950,200), 50,0)
road = pygame.draw.polygon(window,grey, ((500,600), (350,600), (150,1000), (1100,1000)))

traffic_light = pygame.image.load('traffic_light1.png')
traffic_light = pygame.transform.scale(traffic_light,(300,500))

traffic_light_red = pygame.image.load('images/traffic lights - RED.png')
traffic_light_red = pygame.transform.scale(traffic_light_red,(150,500))

traffic_light_green = pygame.image.load('images/traffic lights - GREEN.png')
traffic_light_green = pygame.transform.scale(traffic_light_green,(150,500))

traffic_light_yellow = pygame.image.load('images/traffic lights - YELLOW.png')
traffic_light_yellow = pygame.transform.scale(traffic_light_yellow,(150,500))

                                 
white_car_back = pygame.image.load('white_car_back_v2.png')
white_car_back = pygame.transform.scale(white_car_back, (330,300))

#line1 = pygame.draw.rect

#from PIL import Image
#img = Image.open('white_car_back.png')
#img = img.convert('RGBA')
#data = img.getdata()
#print(data)

all_colours = []

count_all_pixels = 0
#for d in data:
#   count_all_pixels += 1
#   if d not in all_colours:
#       all_colours.append(d)
#       print(d)
       
print(f" /n all_colours = {all_colours}")
print(f" /n Len of all_colours = {len(all_colours)}")
print(f" /n count_all_pixels = {count_all_pixels}")

#newdata = list()
#for d in data:
    #if d[0] == 179 and d[1] == 255 and d[2] == 128:
#    if d[0] > 159 and d[0] < 199 and d[1] > 235 and d[1] < 275 and d[2] > 108 and d[2] < 148:

#        newdata.append((255,255,255,0))
#else:
 #       newdata.append(d)
#img.putdata(newdata)
#img.save('white_car_back_v2.png','PNG')



counter =0 
while True:
    if counter < 300:
        window.blit(traffic_light_red,(800,300))
    elif counter < 600:
        window.blit(traffic_light_yellow,(800,300))
    elif counter < 900:
        window.blit(traffic_light_green,(800,300))
        
    window.blit(white_car_back,(350,600))
    pygame.display.update()
    counter += 1
