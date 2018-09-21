import pygame
import math
import random
import time

# initialize the pygame module

pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Game Over', False, (0, 0, 0))


#pygame.display.set_caption("minimal program")

# define the height and width of the screen 
width = 400
height = 400
 
# create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((height, width))
# set the background to white
screen.fill((255, 255, 255))

# define a variable to control the main loop
running = True

# moving ball function
def moving_ball(current_pos, move):
	# both current_pos and move are 2 element tuple; 
	# move is the next movement of x and y
	mx, my = move
	x, y = current_pos
	if x + mx >= height or x + mx <= 0:
		mx = -mx
	if y + my >= width or y + my <= 0:
		my = -my
	move = (mx, my)
	next_place = (x + mx, y + my)
	pygame.draw.circle(screen, (255, 0, 0), next_place, ball_size)
	#m ,b = line(next_place, current_pos)
	return (next_place, move)

def player(current_pos, v):
	# current_pos is a 2 elements tuple; v is the speed
	x, y = current_pos
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and x - v - player_size / 2 >= 0:
		x -= v
	if keys[pygame.K_RIGHT] and x + v + player_size / 2 <= height:
		x += v
	if keys[pygame.K_UP] and y - v - player_size / 2 >= 0:
		y -= v
	if keys[pygame.K_DOWN] and y + v + player_size / 2 <= width:
		y += v
	
	pygame.draw.circle(screen, (0, 0, 0), (x, y), player_size)
	return (x, y)

# define the origin
origin = (height // 2, width // 2)

# initialize all values
v = 5
player_x, player_y = origin

next_place1 = (100, 150)
next_place2 = (100, 150)
next_place3 = (100, 150)
next_place4 = (100, 150)
next_place5 = (100, 150)
move1 = (random.randrange(-10, 10), random.randrange(-10, 10))
move2 = (random.randrange(-10, 10), random.randrange(-10, 10))
move3 = (random.randrange(-10, 10), random.randrange(-10, 10))
move4 = (random.randrange(-10, 10), random.randrange(-10, 10))
move5 = (random.randrange(-10, 10), random.randrange(-10, 10))

player_size = 2
ball_size = 10

start_time = time.time()
# main loop
while running:
	pygame.time.delay(40)
	screen.fill((255, 255, 255))
	
	# draw player and ball on the screen
	player_x, player_y = player((player_x, player_y), v)
	next_place1, move1 = moving_ball(next_place1, move1)
	next_place2, move2 = moving_ball(next_place2, move2)
	next_place3, move3 = moving_ball(next_place3, move3)
	next_place4, move4 = moving_ball(next_place4, move4)
	next_place5, move5 = moving_ball(next_place5, move5)
	
	# display survival time on the screen
	elapsed_time = time.time() - start_time
	new = "".join(str(elapsed_time).split(".")[0])
	texttime = myfont.render(new, False, (0, 0, 0))
	screen.blit(texttime,(180,0))
	pygame.display.update()
	
	if (math.sqrt((player_x - next_place1[0]) ** 2 + (player_y - next_place1[1]) ** 2) <= ball_size or
	math.sqrt((player_x - next_place2[0]) ** 2 + (player_y - next_place2[1]) ** 2) <= ball_size or
	math.sqrt((player_x - next_place3[0]) ** 2 + (player_y - next_place3[1]) ** 2) <= ball_size or
	math.sqrt((player_x - next_place4[0]) ** 2 + (player_y - next_place4[1]) ** 2) <= ball_size or
	math.sqrt((player_x - next_place5[0]) ** 2 + (player_y - next_place5[1]) ** 2) <= ball_size):
		pygame.display.update()
		screen.blit(textsurface,(120,180))
		pygame.display.update()
		pygame.time.delay(3000)
		pygame.event.post(pygame.event.Event(pygame.QUIT))
	
	# event handling, gets all event from the eventqueue
	for event in pygame.event.get():
		# only do something if the event is of type QUIT
		if event.type == pygame.QUIT:
			# change the value to False, to exit the main loop
			running = False
	
	