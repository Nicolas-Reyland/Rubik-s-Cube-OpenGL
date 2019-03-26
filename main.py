# Rubik's Cube with OpenGL
import pygame as pg
# open_gl(u) & color-related functions
from little_opengl import *
# algorithms to slove the Cube
from algorithm import *
# matrix handling & co.
from matrix import *
# random for scrambling, time for chronometer
import random, time
# os for terminal stdout clear
import os
os.system('clear') # to woosh the pygame text out of the screen

# --- variables ---
cube_size = 3

start_with_scrambled = True
# if one is False (from here), all the following we be interpreted as False too
start_with_white_cross = False
start_with_corners = True
start_with_belgium_crown = True
start_with_bottom_cross = True
start_with_bottom_full = True

# --- the cube_list creator function ---
def create_RC():

	initial_color_list=[white, yellow, green, blue, red, orange]

	# initialize cube_list
	cube_list = [block for block in create_rubiks_cube_matrix(custom_color_list=initial_color_list[:], gap=.05)]

	# set_all coors to defalut mask color
	set_all_colors(cube_list, mask)

	# create new color matrix
	color_matrix = create_color_matrix(cube_size, initial_color_list[:])

	# set this matrix to the cubes
	set_color_matrix_to_cubes(color_matrix, cube_list)

	return cube_list

# initialize the cube_list
cube_list = create_RC()

# ----- Graphics -----
def main():

	# start looking-at position : x, y, z (it is a movement, u start at (0,0,0))
	glTranslatef(0,0,-15)

	# the camera rotation values
	camera_rot_x = 0
	camera_rot_y = 0

	# constants
	game_speed = 2
	direction_speed = .5

	cnt = 0 # iteration-counter
	scramble = 0 # while cnt <= scramble, do scramble

	# inmove is True if there are moves on the RC that are being executed
	inmove = False
	# how many moves per frame (10ms between every frame)
	move_every_n_frame = 1

	# if u want the cube to be scrambled first
	if start_with_scrambled:
		# how many iterations
		iterations = 100
		# the tmp is a list having 'iterations' random moves
		tmp = list([random.choice(['R','Ri','L', 'Li', 'B', 'Bi', 'D', 'Di', 'F', 'Fi', 'U', 'Ui']) for _ in range(iterations)])
		# execute every move from tmp
		for move in tmp: RCMove(cube_list, move)
		# delete the tmp
		del tmp

		# nested ifs, to pre-do actions on the RC
		if start_with_white_cross:
			SSWhiteCross(cube_list)

			if start_with_corners:
				SSFillTopCorners(cube_list)

				if start_with_belgium_crown:
					SSBelgiumCrown(cube_list)

					if start_with_bottom_cross:
						SSBottomCross(cube_list)

						if start_with_bottom_full:
							SSFillBottomCorners(cube_list)

	# main loop
	while True:

		cnt += 1 # increment iteration-counter by 1

		# scramble the cube
		if cnt <= scramble and not inmove:
			# create a random move
			move = random.choice(['R','Ri','L', 'Li', 'B', 'Bi', 'D', 'Di', 'F', 'Fi', 'U', 'Ui'])
			# execute the move
			RCMove(cube_list, move)
			# scramble_id--
			scramble -= 1

		# if there are moves being executed, and the frame is 'move-enabled', execute one move
		if inmove and cnt % move_every_n_frame == 0:
			# see if the next index is going to throw an IndexError, stop inmove
			if move_index + 1 >= len(moves):
				# toggle the inmove to False
				inmove = False

			# execute the current move
			RCMove(cube_list, moves[move_index])
			# increment the move_index
			move_index += 1

		# go through pg.events
		for event in pg.event.get():
			# if the window cross has been clicked, quit everything
			if event.type == pg.QUIT:
				# terminate pygame
				pg.quit()
				# terminate the program
				quit()

			# if the event-type is a key-pressed
			if event.type == pg.KEYDOWN:
				# 'q' terminates the program
				if event.key == pg.K_q:
					pg.quit()
					quit()

				# camera rotation
				if event.key == pg.K_j:
					camera_rot_x = -direction_speed

				if event.key == pg.K_l:
					camera_rot_x = direction_speed

				if event.key == pg.K_i:
					camera_rot_y = direction_speed

				if event.key == pg.K_k:
					camera_rot_y = -direction_speed


				# RCMove input
				if event.key == pg.K_SPACE:
					# get an input and execute it
					RCMove(cube_list, input('Move: '))

				# --- RC Solving ---

				# Simple Solving - slow solve
				if event.key == pg.K_f:
					# get the move-list
					moves = SimpleSolve(cube_list)

					# if moves != [], do :
					if moves:
						# reverse all moves (they have already been made in the function)
						reverse_move_log(cube_list, moves)

						# initialize the variables to go through all move in 'moves'
						move_index = 0
						inmove = True

				if event.key == pg.K_g:

					# get current time
					t1 = time.perf_counter()

					# solve the cube
					SimpleSolve(cube_list)

					# get current time
					t2 = time.perf_counter()

					# print the time taken for solving the cube, and print it out
					print('Cube solved in {} sec'.format(t2 - t1))

				# do the same thing as previous for the rest

				# White Cross - slow solve
				if event.key == pg.K_y:
					moves = SSWhiteCross(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove = True
				# White Cross - fast solve
				if event.key == pg.K_w:
					SSWhiteCross(cube_list)

				# Corners - slow solve
				if event.key == pg.K_x:
					moves = SSFillTopCorners(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove = True
				# Corners - fast solve
				if event.key == pg.K_e:
					SSFillTopCorners(cube_list)

				# Belgium Crown - slow solve
				if event.key == pg.K_c:
					moves = SSBelgiumCrown(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove = True
				# Belgium Crown - fast solve
				if event.key == pg.K_r:
					SSBelgiumCrown(cube_list)

				# Bottom Cross - slow solve
				if event.key == pg.K_v:
					moves = SSBottomCross(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove = True
				# Bottom Cross - fast solve
				if event.key == pg.K_t:
					SSBottomCross(cube_list)

				# Bottom Corners - slow solve
				if event.key == pg.K_b:
					moves = SSFillBottomCorners(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove = True
				# Bottom Corners - fast solve
				if event.key == pg.K_z:
					SSFillBottomCorners(cube_list)

				# Bottom Finish - slow solve
				if event.key == pg.K_n:
					moves = SSFinish(cube_list)
					if moves:
						reverse_move_log(cube_list, moves)
						move_index = 0
						inmove= True
				# Bottom Finish- fast solve
				if event.key == pg.K_u:
					SSFinish(cube_list)


				# --- Anything else ---

				# Shuffle - slow
				if event.key == pg.K_s:
					scramble = cnt + 50
				# Shuffle - fast
				if event.key == pg.K_d:
					# create a random-moves-list, execute every move in it, delete it
					tmp = list(Scramble(cube_list))
					for _ in tmp: RCMove(cube_list, _)
					del tmp

				# terminal screen clear
				if event.key == pg.K_p:
					os.system('clear')

			# Moving, etc.
			if event.type == pg.KEYUP:
				# camera
				if event.key == pg.K_j or event.key == pg.K_l:
					camera_rot_x = 0
				if event.key == pg.K_i or event.key == pg.K_k:
					camera_rot_y = 0

			# the mouse-button-scrolling
			if event.type == pg.MOUSEBUTTONDOWN: # mouse-wheel

				if event.button == 4: # forward
					glTranslatef(0,0,direction_speed)
				if event.button == 5: # backwards
					glTranslatef(0,0,-direction_speed)

		# rotating camera
		glRotatef(10, camera_rot_y, camera_rot_x, 0)

		# clear frame : specify what we wanna clear
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		# generate the 3D opengl object of the cube for every cube in the cube_list
		for cube in cube_list:
			cube.Cube()

		# update the display
		pg.display.flip()

		# wait for 10 ms
		pg.time.wait(10) # ms

# --- Starting the loop ---

# init 3D graphics
pg.init()
display = (800, 800)

# must tell pygame that we will use opengl
pg.display.set_mode(display, pg.DOUBLEBUF|pg.OPENGL)

# enable strong colors (non-tranparent)
glEnable(GL_DEPTH_TEST)

# perspective: field-of-view, aspect-ratio (width/height), mc-sort-of-chink-loading-when-far-or-near (both last one, 1. near, 2. far)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)

# start main loop
main()
