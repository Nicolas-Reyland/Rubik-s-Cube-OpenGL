# Algorithms & Co.
import time # time for chronometer
from random import choice
from matrix import *

# ----- Functions -----
# Perform a move by given letter
def RCMove(Cubes, move_name):
	# since it's a command-line called program, this doesn't hurt
	if move_name == '' or move_name == ' ': return
	if ' ' in move_name:
		for move in move_name.split():
			RCMove(Cubes, move)
		return

	if move_name[0] == '2':
		move_name = move_name[1:]
		RCMove(Cubes, move_name)

	top, bottom, left, right, front, back = get_RC_face_indexs(name='all')

	if move_name == 'R': # right, to the top

		side_cubes = get_RC_face_indexs('right')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'z', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Ri': # right, to the bottom

		side_cubes = get_RC_face_indexs('right')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'z', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Li': # left, to the top

		side_cubes = get_RC_face_indexs('left')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'z', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'L': # left, to the bottom

		side_cubes = get_RC_face_indexs('left')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'z', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'D': # bottom, to the right

		side_cubes = get_RC_face_indexs('bottom')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'x', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Di': # bottom, to the left

		side_cubes = get_RC_face_indexs('bottom')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'x', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Fi': # front, to the right

		side_cubes = get_RC_face_indexs('front')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'y', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'F': # front, to the left

		side_cubes = get_RC_face_indexs('front')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'y', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'B': # back, to the left

		side_cubes = get_RC_face_indexs('back')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'y', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Bi': # back, to the right

		side_cubes = get_RC_face_indexs('back')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'y', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Ui': # top, to the left # c normal pr U et Ui

		side_cubes = get_RC_face_indexs('top')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'x', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'U': # top, to the right

		side_cubes = get_RC_face_indexs('top')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'x', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'M': # middle, horizontal, right

		side_cubes = get_RC_face_indexs('horizontal')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'x', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Mi': # middle, horizontal, left

		side_cubes = get_RC_face_indexs('horizontal')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'x', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'X': # middle, horizontal, left

		RCMove(Cubes, 'Ui')
		RCMove(Cubes, 'M')
		RCMove(Cubes, 'D')

	elif move_name == 'Xi': # middle, horizontal, left

		RCMove(Cubes, 'U')
		RCMove(Cubes, 'Mi')
		RCMove(Cubes, 'Di')

	elif move_name == 'V': # middle, vertical, up

		side_cubes = get_RC_face_indexs('vertical')
		side_cubes_corners = get_corners_from_face(side_cubes)
		side_cubes_edges = get_edges_from_face(side_cubes)

		adv_move(Cubes, 'y', 1, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Vi': # middle, vertical, down

		side_cubes = get_RC_face_indexs('vertical')
		side_cubes_corners = get_corners_from_face(side_cubes)[::-1]
		side_cubes_edges = get_edges_from_face(side_cubes)[::-1]

		adv_move(Cubes, 'y', 3, side_cubes, side_cubes_corners, side_cubes_edges)

	elif move_name == 'Y': # middle, vertical, up

		RCMove(Cubes, 'Fi')
		RCMove(Cubes, 'V')
		RCMove(Cubes, 'B')

	elif move_name == 'Yi': # middle, vertical, down

		RCMove(Cubes, 'F')
		RCMove(Cubes, 'Vi')
		RCMove(Cubes, 'Bi')

	else:
		print('Unvalid Move name {}'.format(move_name))

# used in RCMove to rotate and move the color-lists
def adv_move(Cubes, rotation_direction, rotation_iterations, side_cubes, side_cubes_corners, side_cubes_edges):

		# iterate through all cubes and rotate them accordingly
		for index in side_cubes:
			# first rotate color_list
			Cubes[index].rotate_by_colors(rotation_direction, rotation_iterations)

		# - do the corners -
		# store the color_list of the last corner
		last_color_list = Cubes[side_cubes_corners[-1]].color_list
		# iterate through all corners
		for corner in side_cubes_corners:
			# change the color_list, and get the old one in return
			last_color_list = Cubes[corner].switch_colors(last_color_list)


		# - do the edges -
		# store the color_list of the last edge
		last_color_list = Cubes[side_cubes_edges[-1]].color_list
		# iterate through all corners
		for edge in side_cubes_edges:
			# change the color_list, and get the old one in return
			last_color_list = Cubes[edge].switch_colors(last_color_list)

# For easier algorithm execution
def RCMoveQueue(Cubes, move_list):
	# iterate through all move and do it
	for move in move_list:
		RCMove(Cubes, move)

# Scramble the Cube
def Scramble(Cubes, iterations=100):

	for _ in range(iterations):
		# choose a random move
		move = choice(['R','Ri','L', 'Li', 'B', 'Bi', 'D', 'Di', 'F', 'Fi', 'U', 'Ui'])
		# execute the move
		RCMove(Cubes, move)
		# yield it (not for reverse scrambling ! ... 0_0 )
		yield move

# Reverse move-log
reverse_move_log = lambda Cubes, move_log : RCMoveQueue(Cubes, list(map(lambda x: x+'i' if 'i' not in x else x[:-1], move_log))[::-1])

# ----- Solving Algorithms -----
def SimpleSolve(Cubes):

	moves = SSWhiteCross(Cubes)

	moves.extend(SSFillTopCorners(Cubes))

	moves.extend(SSBelgiumCrown(Cubes))

	moves.extend(SSBottomCross(Cubes))

	moves.extend(SSFillBottomCorners(Cubes))

	moves.extend(SSFinish(Cubes))

	return moves

def match_edges_with_centers(Cubes):
	# turn the top, untill the colors of the top's edges match with the centers
	global move_log

	get_edges = lambda face : [face[i] for i in range(1,8,2)]
	get_up_crown = lambda matrix : [get_edges(matrix[2])[2], get_edges(matrix[3])[2], get_edges(matrix[4])[3], get_edges(matrix[5])[3]]
	matrix = get_value_matrix(Cubes)

	cnt = 0
	while get_up_crown(matrix)[2] != 2:
		cnt += 1

		# turn top
		move = 'U'
		RCMove(Cubes, move)
		move_log.append(move)

		# update matrix
		matrix = get_value_matrix(Cubes)

	# it moves 3 times in 'U', so 1 'Ui' is more beautiful
	if cnt == 3:
		del move_log[-3:]
		move_log.append('Ui')

def SSWhiteCross(Cubes):
	'''
	while not-white-face-edges-finished:
		for face in rubiks-cube-faces:
			if at the bottom:
				while at same position, on the top it is white:
					turn bottom
				turn 2 times the face, so it will be at the top
			if anywhere else (except the top):
				turn the white-face to do it at the bottom
				break (only for-loop)

	re-arrange the colors to match

	'''

	matrix = get_value_matrix(Cubes)
	get_edges = lambda face : [face[i] for i in range(1,8,2)]

	global move_log
	move_log = []

	finished = get_edges(matrix[0]) == [0 for _ in range(len(get_edges(matrix[0])))]

	while not finished:

		# update matrix
		matrix = get_value_matrix(Cubes)

		face = matrix[1]

		if 0 in get_edges(face): # bottom face

			# is the edge at 180° free ?
			top_is_free = get_edges(face).index(0) in [i for i,color in enumerate(get_edges(matrix[0])) if color != 0]

			# while the top-face at this index is not free (non-top-color)
			while not top_is_free: # can surely do this while loop with single math operation

				# turn the bottom (Down)
				move = 'D'
				RCMove(Cubes, move)
				move_log.append(move)

				# get the new matrix value
				matrix = get_value_matrix(Cubes)

				# update the while-condition
				face = matrix[1]
				top_is_free = get_edges(face).index(0) in [i for i,color in enumerate(get_edges(matrix[0])) if color != 0]

			# where is the white color (index)
			zero_index = get_edges(face).index(0)

			# switch, to know how to turn the Cube
			if zero_index == 0:
				move = '2F'
			elif zero_index == 1: # back ?
				move = '2L'
			elif zero_index == 2:
				move = '2R'
			elif zero_index == 3:
				move = '2B'

			move_log.append(move)

			RCMove(Cubes, move)

			matrix = get_value_matrix(Cubes)

		else:

			for i,face in enumerate(matrix[2:]):
				# always front(from face) sight

				# edges on the current face
				edges = get_edges(face)


				# --- Left & Right ---

				if i == 0: # left, green
					# start: down-right
					top1, top2 = 0, 3
					r, l = 0, 3
					move1, move2 = 'F', 'Bi'

				if i == 1: # right, blue
					# start: down-left
					top1, top2 = 0, 3
					r, l = 0, 3
					move1, move2 = 'Fi', 'B'

				if i == 2: # front, red
					# start: down-left
					top1, top2 = 2, 1
					r, l = 2, 1
					move1, move2 = 'Ri', 'Li'

				if i == 3: # back, orange
					# start: down-right
					top1, top2 = 2, 1
					r, l = 2, 1
					move1, move2 = 'Ri', 'L'

				# right edge is 0
				if edges[r] == 0: # far-left - near-right

					if get_edges(matrix[0])[top1] != 0:

						move = move1
						RCMove(Cubes, move)
						move_log.append(move)
						break

					else:
						move = 'U'
						RCMove(Cubes, move)
						move_log.append(move)
						break

				# left edge is 0
				elif edges[l] == 0: # far-left - near-right

					if get_edges(matrix[0])[top2] != 0:

						move = move2
						RCMove(Cubes, move)
						move_log.append(move)
						break

					else:
						move = 'U'
						RCMove(Cubes, move)
						move_log.append(move)
						break


				# --- Up & Down ---

				if i == 0: # left, green
					# start: down-right
					top3 = 1
					u, d = 2, 1
					move3 = 'L' # could use 'Li' as well

				if i == 1: # right, blue
					# start: down-left
					top3 = 2
					u, d = 2, 1
					move3 = 'R' # could use 'Ri' as well (goes on...)

				if i == 2: # front, red
					# start: down-left
					top3 = 0
					u, d = 3, 0
					move3 = 'F'

				if i == 3: # back, orange
					# start: down-right
					top3 = 3
					u, d = 3, 0
					move3 = 'B'

				# right edge is 0
				if edges[u] == 0:

					# don't need to check, coz it's already at the top

					move = move3
					RCMove(Cubes, move)
					move_log.append(move)
					break

				# left edge is 0
				elif edges[d] == 0:

					if get_edges(matrix[0])[top3] != 0:

						move = move3
						RCMove(Cubes, move)
						move_log.append(move)
						break

					else:
						move = 'U'
						RCMove(Cubes, move)
						move_log.append(move)
						break

		finished = get_edges(matrix[0]) == [0 for _ in range(len(get_edges(matrix[0])))]


	get_up_crown = lambda matrix : [get_edges(matrix[2])[2], get_edges(matrix[3])[2], get_edges(matrix[4])[3], get_edges(matrix[5])[3]]

	right_order = [4, 5, 2, 3] # vert bleu rouge orange

	match_edges_with_centers(Cubes)

	matrix = get_value_matrix(Cubes)

	while get_up_crown(matrix) != right_order:

		if get_up_crown(matrix)[0] == 5 and get_up_crown(matrix)[1] == 4:
			moves = ['2R', '2L', '2D', '2R', '2L']

		elif get_up_crown(matrix)[0] == 4:
			moves = ['2R', '2B', 'Di', '2R', '2D', '2B']

		elif get_up_crown(matrix)[0] == 5:
			moves = ['2L', '2B', 'D', '2L', '2D', '2B']

		elif get_up_crown(matrix)[3] == 4:
			moves = ['2L', '2D', '2R', 'D', '2B', 'D', '2L']

		elif get_up_crown(matrix)[3] == 5:
			moves = ['2R', '2D', '2L', 'Di', '2B', 'Di', '2R']

		# execute the moves and log them
		RCMoveQueue(Cubes, moves)
		move_log.extend(moves)

		# update matrix
		matrix = get_value_matrix(Cubes)

	return move_log


def SSFillTopCorners(Cubes):
	'''
	basically the same thing than SSWhiteCross,
	but this time I will immediately
	move the corners to the right corner (color-match)

	'''
	
	matrix = get_value_matrix(Cubes)
	get_corners = lambda face : [face[i] for i in [0,2,6,8]]

	global move_log
	move_log = []

	finished = False

	while not finished:

		# --- up face (only when all corners are white) ---

		if get_corners(matrix[0]) == [0 for _ in range(4)]:

			face = matrix[0]

			match_edges_with_centers(Cubes)
			matrix = get_value_matrix(Cubes)

			# iterate through every corner
			for x,corner in enumerate(get_corners(face)):
				if corner == 0:
					moves = None

					# if the corner is wrong, change it
					if x == 0 and matrix[2][2] != 4:#matrix[2][5]: # if it's not the same color as the edge next to it, move it
						#print(matrix[0], matrix[2], matrix[2][2], matrix[2][5])
						#print('moving wrong white-green-red corner')
						moves = ['Fi', 'Di', 'F']

					if x == 1 and matrix[3][2] != 5:#matrix[3][5]:
						#print(matrix[0], matrix[3], matrix[3][2], matrix[3][5])
						#print('moving wrong white-blue-red corner')
						moves = ['F', 'D', 'Fi']

					if x == 2 and matrix[2][8] != 4:#matrix[2][7]:
						#print(matrix[0], matrix[2], matrix[2][6], matrix[2][7])
						#print('moving wrong white-green-orange corner')
						moves = ['B', 'D', 'Bi']

					if x == 3 and matrix[3][8] != 5:#matrix[2][7]:
						#print(matrix[0], matrix[2], matrix[2][8], matrix[2][7])
						#print('moving wrong white-blue-orange corner')
						moves = ['Bi', 'Di', 'B']

					if moves:
						RCMoveQueue(Cubes, moves)
						move_log.extend(moves)

						#return move_log

					finished = True


		# --- bottom face (only if there are already corners at the top) ---

		if 0 in get_corners(matrix[1]) and get_corners(matrix[0]).count(0) > 1: # normally, we don't need the get_corners, coz the white cross is made

			face = matrix[1] # red-sight start: near-left - far-right (1 right)

			# get all corners
			corners = get_corners(face)

			# get first 0 index
			zero_index = corners.index(0)

			# find the right moves
			# order like the corners at the bottom face
			if zero_index == 0: # green
				moves = ['L', '2D', 'Li', 'Di', 'L', 'D', 'Li', '2D', 'Fi', 'Di', 'F']
			elif zero_index == 1: # red (right side, always)
				moves = ['F', '2D', 'Fi', 'Di', 'F', 'D', 'Fi', '2D', 'Ri', 'Di', 'R'] # origninal version
			elif zero_index == 2: # orange
				moves = ['B', '2D', 'Bi', 'Di', 'B', 'D', 'Bi', '2D', 'Li', 'Di', 'L']
			elif zero_index == 3: # blue
				moves = ['R', '2D', 'Ri', 'Di', 'R', 'D', 'Ri', '2D', 'Bi', 'Di', 'B']

			# execute the moves & add them to log
			RCMoveQueue(Cubes, moves)
			move_log.extend(moves)


		# --- side faces ---

		else:

			for i,face in enumerate(matrix[2:]):

				corners = get_corners(face)

				# --- Down-Left & Down-Right ---

				if i == 0: # left, green
					# start: down-right (1 up)
					color1, color2 = 0, 6 # bottom start: red-green - blue-orange (long red, first)
					r, l = 0, 2
					move1, move2 = ['L', 'D', 'Li'], ['Li', 'Di', 'L']
					face_color = 5

				if i == 1: # right, blue
					# start: down-left (1 up)
					color1, color2 = 8, 2
					r, l = 2, 0
					move1, move2 = ['R', 'D', 'Ri'], ['Ri', 'Di', 'R']
					face_color = 5

				if i == 2: # front, red
					# start: down-left (right)
					color1, color2 = 2, 0
					r, l = 1, 0
					move1, move2 = ['F', 'D', 'Fi'], ['Fi', 'Di', 'F']
					face_color = 7

				if i == 3: # back, orange
					# start: down-right (left)
					color1, color2 = 6, 8
					r, l = 0, 1
					move1, move2 = ['B', 'D', 'Bi'], ['Bi', 'Di', 'B']
					face_color = 7

				if corners[r] == 0:

					if face[face_color] == matrix[1][color1]:

						moves = move1

						RCMoveQueue(Cubes, moves)
						move_log.extend(moves)

						break

					else:
						move = 'U'
						RCMove(Cubes, move)
						move_log.append(move)

						break

				elif corners[l] == 0:

					if face[face_color] == matrix[1][color2]:

						moves = move2

						RCMoveQueue(Cubes, moves)
						move_log.extend(moves)

						break

					else:
						move = 'U'
						RCMove(Cubes, move)
						move_log.append(move)

						break


				# --- Up-Left & Up-Right ---

				if i == 0: # left, green
					# start: down-right (1 up)
					r, l = 1, 3
					move1, move2 = ['L', '2D', 'Li'], ['Li', '2D', 'L']

				if i == 1: # right, blue
					# start: down-left (1 up)
					r, l = 1, 3
					move1, move2 = ['R', '2D', 'Ri'], ['Ri', '2D', 'R']

				if i == 2: # front, red
					# start: down-left (1 right)
					r, l = 3, 2
					move1, move2 = ['F', '2D', 'Fi'], ['Fi', '2D', 'F']

				if i == 3: # back, orange
					# start: down-right (1 left)
					r, l = 2, 3
					move1, move2 = ['B', '2D', 'Bi'], ['Bi', '2D', 'B']

				if corners[r] == 0:

					moves = move1

					RCMoveQueue(Cubes, moves)
					move_log.extend(moves)

				elif corners[l] == 0:

					moves = move2

					RCMoveQueue(Cubes, moves)
					move_log.extend(moves)

		# update matrix
		matrix = get_value_matrix(Cubes)

	match_edges_with_centers(Cubes)

	return move_log


def SSBelgiumCrown(Cubes):
	'''
	while not completed:
		put in every edge it can (in the right spot),
		then check for wrong edges

	'''
	
	matrix = get_value_matrix(Cubes)
	get_edges = lambda face : [face[i] for i in range(1,8,2)]

	global move_log
	move_log = []

	finished = False

	while not finished:

		# --- put them into the right position ---

		for i in range(4):

			matrix = get_value_matrix(Cubes)

			face = matrix[i+2]

			if i == 0:
				base = 3
				r, l = (4, 3), (5, 3)
				down_index = 3
				action_right, action_left = ['Di', 'Fi', 'D', 'F', 'D', 'L', 'Di', 'Li'], ['D', 'B', 'Di', 'Bi', 'Di', 'Li', 'D', 'L']
			if i == 1:
				base = 3
				r, l = (5, 5), (4, 5)
				down_index = 5
				action_right, action_left = ['Di', 'Bi', 'D', 'B', 'D', 'R', 'Di', 'Ri'], ['D', 'F', 'Di', 'Fi', 'Di', 'Ri', 'D', 'R']
			if i == 2:
				base = 1
				r, l = (3, 5), (2, 5)
				down_index = 1
				# original
				action_right, action_left = ['Di', 'Ri', 'D', 'R', 'D', 'F', 'Di', 'Fi'], ['D', 'L', 'Di', 'Li', 'Di', 'Fi', 'D', 'F']
			if i == 3:
				base = 1
				r, l = (2, 7), (3, 7)
				down_index = 7
				action_right, action_left = ['Di', 'Li', 'D', 'L', 'D', 'B', 'Di', 'Bi'], ['D', 'R', 'Di', 'Ri', 'Di', 'Bi', 'D', 'B']

			if face[base] == face[4] and matrix[1][down_index] == matrix[r[0]][4]:

				RCMoveQueue(Cubes, action_right)
				move_log.extend(action_right)

				break

			if face[base] == face[4] and matrix[1][down_index] == matrix[l[0]][4]:

				RCMoveQueue(Cubes, action_left)
				move_log.extend(action_left)

				break

		else:

			move = 'D'
			RCMove(Cubes, move)
			move_log.append(move)

			for i in range(4):

				matrix = get_value_matrix(Cubes)

				face = matrix[i+2]

				if i == 0:
					r, l = 1, 7
					fr, fl = (4, 3), (5, 3)
					action_right, action_left = ['Di', 'Fi', 'D', 'F', 'D', 'L', 'Di', 'Li'], ['D', 'B', 'Di', 'Bi', 'Di', 'Li', 'D', 'L']
				if i == 1:
					r, l = 7, 1
					fr, fl = (5, 5), (4, 5)
					action_right, action_left = ['Di', 'Bi', 'D', 'B', 'D', 'R', 'Di', 'Ri'], ['D', 'F', 'Di', 'Fi', 'Di', 'Ri', 'D', 'R']
				if i == 2:
					r, l = 5, 3
					fr, fl = (3, 5), (2, 5)
					# original
					action_right, action_left = ['Di', 'Ri', 'D', 'R', 'D', 'F', 'Di', 'Fi'], ['D', 'L', 'Di', 'Li', 'Di', 'Fi', 'D', 'F']
				if i == 3:
					r, l = 3, 5
					fr, fl = (2, 7), (3, 7)
					action_right, action_left = ['Di', 'Li', 'D', 'L', 'D', 'B', 'Di', 'Bi'], ['D', 'R', 'Di', 'Ri', 'Di', 'Bi', 'D', 'B']

				if face[4] != face[r] != 1 != matrix[fr[0]][fr[1]]:

					RCMoveQueue(Cubes, action_right)
					move_log.extend(action_right)

					break

				elif face[4] != face[l] != 1 != matrix[fl[0]][fl[1]]:

					RCMoveQueue(Cubes, action_left)
					move_log.extend(action_left)

					break

		# --- testing if it's over ---

		counter = 0

		for i in range(4):

			matrix = get_value_matrix(Cubes)

			face = matrix[i+2]

			if i == 0:
				r, l = 1, 7
			if i == 1:
				r, l = 7, 1
			if i == 2:
				r, l = 5, 3
			if i == 3:
				r, l = 3, 5

			if face[4] == face[r] == face[l]:

				counter += 1

		# if counter is 4, all 4 faces are complete
		finished = counter == 4

	return move_log

def SSBottomCross(Cubes):
	# basic analysiation of the face,
	# then doing the algorithm,
	# untill the bottom-cross is completed
	algorithm = ['F', 'L', 'D', 'Li', 'Di', 'Fi']
	get_edges = lambda face : [face[i] for i in range(1,8,2)]
	one_hot_color = lambda face, color_value : [1 if color == color_value else 0 for color in face]

	matrix = get_value_matrix(Cubes)

	color = matrix[1][4] # bottom color (centre)
	move_log = []

	# get bottom face edges & convert it to one_hot values (see ML terminology)
	face = get_edges(one_hot_color(matrix[1], color))

	# if there's only a dot, do the algorithm
	if face.count(1) == 0:
		RCMoveQueue(Cubes, algorithm)
		move_log.extend(algorithm)

	# update face
	face = get_edges(one_hot_color(get_value_matrix(Cubes)[1], color))

	# if there's a line or an 'L' (right angle shape)
	if face.count(1) == 2:

		# check for index-sum (simplest way to see what figure the bottom face represents)
		if sum([i for i,c in enumerate(face) if c == 1]) != 3: # 'L'

			# rotate to reach the right position
			while face != [1,1,0,0]:

				# move
				move = 'D'
				RCMove(Cubes, move)
				move_log.append(move)

				# update
				face = get_edges(one_hot_color(get_value_matrix(Cubes)[1], color))
			
			# do the moves
			RCMoveQueue(Cubes, algorithm)
			move_log.extend(algorithm)

			# update face
			face = get_edges(one_hot_color(get_value_matrix(Cubes)[1], color))

		if [1]*4 != face != [0,1,1,0]: # if not completed + not a horizontal line, rotate once

			move = 'D'
			RCMove(Cubes, move)
			move_log.append(move)

		# update face
		face = get_edges(one_hot_color(get_value_matrix(Cubes)[1], color))

		if face == [0,1,1,0]:

			# do the moves
			RCMoveQueue(Cubes, algorithm)
			move_log.extend(algorithm)

	return move_log


def SSFillBottomCorners(Cubes): # There are some bugs, apparently
	# fill the yellow face (don't care about the sides yet) with one algorithm

	algorithm = ['Ri', 'Di', 'R', 'Di', 'Ri', '2D', 'R']

	get_corners = lambda face : [face[i] for i in [0,2,6,8]]
	one_hot_color = lambda face, color_value : [1 if color == color_value else 0 for color in face]

	matrix = get_value_matrix(Cubes)

	color = matrix[1][4] # bottom color (centre)
	move_log = []

	face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

	finished = face == [1]*4

	while not finished:

		# only a cross, no corner
		if face.count(color) == 0:

			# apply the algorithm once
			RCMoveQueue(Cubes, algorithm)
			move_log.extend(algorithm)

		# fish-looking face
		if face.count(color) == 1:

			while face[0] != 1:

				# turn once
				move = 'D'
				RCMove(Cubes, move)
				move_log.append(move)

				# update
				face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

			RCMoveQueue(Cubes, algorithm)
			move_log.extend(algorithm)

			# update
			face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

		elif face.count(1) == 2:

			# the sum of the indexs of 1s in the face can easily give the shape on the face
			if sum([i for i,c in enumerate(face) if c == 1]) == 3: # fat-diagonal

				if face[1] == 0: # turn it to make it in the right position

					move = 'D'
					RCMove(Cubes, move)
					move_log.append(move)

				# update
				face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

				RCMoveQueue(Cubes, algorithm)
				move_log.extend(algorithm)

				# update
				face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

			else: # helmet-looking figure

				# turn it for the right position
				while face != [1,1,0,0]:

					# turn once
					move = 'D'
					RCMove(Cubes, move)
					move_log.append(move)

					# update
					face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

				RCMoveQueue(Cubes, algorithm)
				move_log.extend(algorithm)

		face = get_corners(one_hot_color(get_value_matrix(Cubes)[1], color))

		finished = face == [1]*4

	return move_log

def SSFinish(Cubes):
	# finish the cube, with known algorithm to match the side- and middle colors

	get_middles = lambda matrix : [matrix[2][3], matrix[3][3], matrix[4][1], matrix[5][1]]
	right_middle_order = lambda matrix : [matrix[2][4], matrix[3][4], matrix[4][4], matrix[5][4]]
	get_sides = lambda matrix : [[matrix[2][0], matrix[2][6]], [matrix[3][0], matrix[3][6]], [matrix[4][2], matrix[4][0]], [matrix[5][0], matrix[5][2]]]

	double_back_algorithm = ['Li', 'F', 'Li', '2B', 'L', 'Fi', 'Li', '2B', '2L']
	left_escalator_algorithm = ['Ri', 'Di', 'R', 'D', 'L', 'D', 'Li', 'Di', 'Di', 'Ri', 'D', 'R', 'D', 'L', 'Di', 'Li']
	right_escalator_algorithm = ['L', 'D', 'Li', 'Di', 'Ri', 'Di', 'R', 'D', 'D', 'L', 'Di', 'Li', 'Di', 'Ri', 'D', 'R']

	matrix = get_value_matrix(Cubes)
	move_log = []

	finished = all([all([x == f[4] for x in f]) for f in matrix])

	while not finished:

		# setting up if the sides are messy
		if not all([a == b for a,b in get_sides(matrix)]):

			for i,(a,b) in enumerate(get_sides(matrix)):

				if a == b:

					move = '2D'
					RCMove(Cubes, move)
					move_log.append(move)

					if i == 0:
						move = 'D'
					if i == 1:
						move = 'Di'
					if i == 3:
						move = '2D'

					if i != 2:
						RCMove(Cubes, move)
						move_log.append(move)

					# spot found, break
					break

			# do the 2B-algorithm (if there was no spot found, do it anyway)
			RCMoveQueue(Cubes, double_back_algorithm)
			move_log.extend(double_back_algorithm)

			matrix = get_value_matrix(Cubes)

		# setting up the sexy move position
		elif any([a == b for a,b in get_sides(matrix)]):# and not all([a == b for a,b in get_sides(matrix)]):

			# find the right spot fot the escalator_algorithm
			for i in range(4): # could do a while too

				if get_sides(matrix)[i][0] == get_middles(matrix)[i]:# == get_sides(matrix)[i][1]: # red face

					if i == 0:
						move = 'D'
					if i == 1:
						move = 'Di'
					if i == 3:
						move = '2D'

					if i != 2:
						RCMove(Cubes, move)
						move_log.append(move)

					break

			else:

				# if 2x opposite ...

				RCMoveQueue(Cubes, left_escalator_algorithm)
				move_log.extend(left_escalator_algorithm)

		matrix = get_value_matrix(Cubes)

		if all([a == b for a,b in get_sides(matrix)]): # get_middles(matrix) != right_middle_order(matrix) and 

			if get_middles(matrix)[0] == get_sides(matrix)[1][0]:

				RCMoveQueue(Cubes, left_escalator_algorithm)
				move_log.extend(left_escalator_algorithm)

			elif get_middles(matrix)[1] == get_sides(matrix)[0][0]:

				RCMoveQueue(Cubes, right_escalator_algorithm)
				move_log.extend(right_escalator_algorithm)

		matrix = get_value_matrix(Cubes)

		# check for no good middle
		if all(get_middles(matrix)[i] != get_sides(matrix)[i][0] for i in range(4)):

			RCMoveQueue(Cubes, left_escalator_algorithm)
			move_log.extend(left_escalator_algorithm)

		# match edges with center (bottom)
		for i in range(4):

			RCMove(Cubes, 'D')

			matrix = get_value_matrix(Cubes)

			if all([all([x == f[4] for x in f]) for f in matrix]):

				if i == 1:
					move_log.append('D')
				elif i == 2:
					move_log.append('2D')
				elif i == 3:
					move_log.append('Di')

				return move_log # note this move_log is not complete (the moves it just did)


		matrix = get_value_matrix(Cubes)

		finished = all([all([x == f[4] for x in f]) for f in matrix])

	return move_log

def BLD():
	pass


