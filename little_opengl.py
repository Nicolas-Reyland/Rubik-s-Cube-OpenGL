# OpenGL functions, variables & constants
# basic functions
from OpenGL.GL import *
# more advanced functions
from OpenGL.GLU import *
# rgb colors for surfaces
from pixel import rgb_color


# --- Rubik's Cube colors ---
# opengl rgb values are between 0 and 1
rgb_to_opengl = lambda rgb : [value / 255 for value in rgb]

white = rgb_to_opengl(rgb_color['white'])
yellow = rgb_to_opengl(rgb_color['light_yellow'])

red = rgb_to_opengl(rgb_color['red'])
orange = rgb_to_opengl((250,164,0)) # normal orange is (255,269,0)

green = rgb_to_opengl(rgb_color['green'])
blue = rgb_to_opengl(rgb_color['blue'])

# inside color, will be black, but is set to pink for debugging
mask = rgb_to_opengl((15,15,15))

colors = [white, yellow, red, orange, green, blue]



vertices = ((1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, 1),(1, 1, 1),(-1, -1, 1),(-1, 1, 1)) # can be understood as nodes too
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
'''surfaces = ((0,1,2,3),
			(3,2,7,6),
			(6,7,5,4),
			(4,5,1,0),
			(1,5,7,2),
			(4,0,3,6)
	)
'''
surfaces = ((1,5,7,2), # top
			(4,0,3,6), # bottom
			(3,2,7,6), # right
			(4,5,1,0), # left
			(6,7,5,4), # front
			(0,1,2,3)  # back
	)

# vertices
def set_vertices(x_change, y_change, z_change):

	new_vertices = []

	for vert in vertices: # pre-defined vertices

		new_x = vert[0] + x_change
		new_y = vert[1] + y_change
		new_z = vert[2] + z_change

		new_vertices.append([new_x, new_y, new_z])

	return new_vertices






def Cube(vertices, color_list):
	glBegin(GL_QUADS)
	for x, surface in enumerate(surfaces):
		for vertex in surface:
			glColor3fv(color_list[x]) # rgb but from 0 to 1
			glVertex3fv(vertices[vertex])
	glEnd()
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()



