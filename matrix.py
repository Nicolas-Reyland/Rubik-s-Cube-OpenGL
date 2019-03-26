# Matrix
from Block import Block
from little_opengl import rgb_color, rgb_to_opengl

default_color_list = [rgb_to_opengl(rgb_color[x]) for x in ['white', 'yellow', 'green', 'blue', 'red']] + [rgb_to_opengl((255,169,0))]

'''
This module contains all the mathematical operations (beside solving-algorithms),
a lot of matrix-handling and a lot of color-handling (which is matrix-handling too,
but big enough to mention)

'''

# ----- Rubik's Cube Matrix -----

# --- RC Faces, Croners & Edges ---
def get_RC_face_indexs(name='all'):

	top = [6,7,8, 15,16,17, 24,25,26]
	bottom = [0,1,2, 9,10,11, 18,19,20]
	left = [0,3,6, 9,12,15, 18,21,24]
	right = [2,5,8, 11,14,17, 20,23,26]
	front = [0,1,2, 3,4,5, 6,7,8]
	back = [18,19,20, 21,22,23, 24,25,26]
	horizontal = [3,4,5, 12,13,14, 21,22,23]
	vertical = [9,10,11, 12,13,14, 15,16,17]

	if name != 'all':
		if name == 'top': return top
		if name == 'bottom': return bottom
		if name == 'left': return left
		if name == 'right': return right
		if name == 'front': return front
		if name == 'back': return back
		if name == 'horizontal': return horizontal
		if name == 'vertical': return vertical
		else: raise NameError('There is no {} face'.format(name))

	return [top,bottom,left,right,front,back]

def get_corners_from_face(face):
	return [face[0], face[2], face[-1], face[-3]]

def get_edges_from_face(face):
	return [face[1], face[-4], face[-2], face[3]]


# --- RC Matrix Initializer ---
def create_rubiks_cube_matrix(matrix_size=3, gap=.5, cube_size=2, custom_color_list=default_color_list):

	matrix = []

	# lambda function to set the right vertices to the cube
	norm = lambda xyz : (xyz - 1) * (gap + cube_size)

	for x in range(matrix_size):
		for y in range(matrix_size):
			for z in range(matrix_size):
				block = Block(norm(x), norm(y), norm(z), custom_color_list, gap=gap, cube_size=cube_size)
				matrix.append(block)

	return matrix

# --- get RC color-matrix ---

def get_value_matrix(cube_list):

	matrix = []
	matrix.append([Block.translate(cube_list[i].color_list[0]) for i in get_RC_face_indexs('top')])
	matrix.append([Block.translate(cube_list[i].color_list[1]) for i in get_RC_face_indexs('bottom')])
	matrix.append([Block.translate(cube_list[i].color_list[5]) for i in get_RC_face_indexs('left')])
	matrix.append([Block.translate(cube_list[i].color_list[4]) for i in get_RC_face_indexs('right')])
	matrix.append([Block.translate(cube_list[i].color_list[2]) for i in get_RC_face_indexs('front')])
	matrix.append([Block.translate(cube_list[i].color_list[3]) for i in get_RC_face_indexs('back')])

	return matrix



# ----- Color Matrix -----

# --- Color Matrix Initializer ---
def create_color_matrix(cube_size, color_list):

	# empty list
	matrix = []
	# iterate through all cube-faces (there are always 6)
	for a in range(6):
		# create a new list for the cube_size**2 - sized array
		line = []
		# fill it
		for b in range(cube_size**2):
			# one color per face
			line.append(color_list[a])
		# add if to the matrix
		matrix.append(line)

	# return the filled matrix
	return matrix

# --- Apply the colors to the Cubes ---
def set_color_matrix_to_cubes(color_matrix, cube_list):
	for i, face in enumerate(color_matrix):
		for color in face:

			# make the selected_cube_index variable (the adj)

			# choose the right combinasion of blocks to color, and which face (of the blocks)
			if i == 0:
				selected_cube_index = [6,7,8, 15,16,17, 24,25,26] # t
				color_index = i
			elif i == 1:
				selected_cube_index = [0,1,2, 9,10,11, 18,19,20] # bo
				color_index = i
			elif i == 2:
				selected_cube_index = [0,3,6, 9,12,15, 18,21,24] # l
				color_index = 5
			elif i == 3:
				selected_cube_index = [2,5,8, 11,14,17, 20,23,26] # r
				color_index = 4
			elif i == 4:
				selected_cube_index = [0,1,2,3,4,5,6,7,8] # f
				color_index = 2
			elif i == 5:
				selected_cube_index = [18,19,20,21,22,23,24,25,26] # ba
				color_index = 3

			# apply the color to the cube
			for index in selected_cube_index:
				cube_list[index].color_list[color_index] = color

def set_all_colors(cube_list, color):
	for cube in cube_list:
		cube.color_list = [color for _ in range(6)]




