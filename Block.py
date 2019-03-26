# Block Class
from little_opengl import *

'''
This module contains the 'Block' Class

The Block Class has the 3D Cube of a Rubik's Cube in it.
It has color attributes, 3D coordinates, and specific values.

There are many functions to handle the Cube (e.g. rotate it, move it, etc.)

'''




class Block:
	def __init__(self, x, y, z, color_list, gap=.1, cube_size=2, values=[]):
		# positions
		self.x, self.y, self.z = x, y, z

		# vertices
		self.vertices = set_vertices(self.x, self.y, self.z)
		# gap between cubes & size of a cube
		self.gap = gap
		self.cube_size = cube_size

		# colors
		self.color_list = color_list[:]

		# opengl cube object
		self.Cube = lambda : Cube(self.vertices, self.color_list)

		# color_functions
		self.get_top = lambda : self.color_list[0]
		self.get_bottom = lambda : self.color_list[1]

		self.get_left = lambda : self.color_list[2]
		self.get_right = lambda : self.color_list[3]

		self.get_front = lambda : self.color_list[4]
		self.get_back = lambda : self.color_list[5]

		# values for cube-solving
		self.values = values

	def move(self, x, y, z):
		# set new values
		self.x += x
		self.y += y
		self.z += z

		# set new verices
		self.vertices = set_vertices(self.x, self.y, self.z)

	def switch_colors(self, new_color_list):
		# make a color-list backup
		old_color_list = self.color_list[:]
		# update color-list
		self.color_list = new_color_list
		# return old color-lsit
		return old_color_list

	def rotate_by_colors(self, direction, rotations=1):
		# there can be null rotations, in debugging-loop
		if rotations == 0: return

		# how it works: manually re-arrange the colors on the cubes face, according to the rotation axis

		if direction == 'x':
			for i in range(rotations):
				top,bottom,right,left,front,back = self.color_list # back, top, bottom, left, right, front = self.color_list
				self.color_list = [top, bottom, front, back, left, right]

		elif direction == 'y':
			for i in range(rotations):
				top,bottom,right,left,front,back = self.color_list # back, top, bottom, left, right, front = self.color_list
				self.color_list = [front, back, right, left, bottom, top]


		elif direction == 'z':
			for i in range(rotations):
				top,bottom,right,left,front,back = self.color_list # back, top, bottom, left, right, front = self.color_list
				self.color_list = [left, right, top, bottom, front, back]

		else: raise NameError('Wrong direction argument {}. direction can be "x", "y" or "z"'.format(direction))

	def traduction(self):
		# for the self.values, traduction from opengl-rgb to integer values (to simplify the algorithms)
		# cannot do a dictionnary, since lists are not hashable
		return []

		for color in self.color_list:
			if color == white:
				traduction.append(0)
			if color == yellow:
				traduction.append(1)
			if color == red:
				traduction.append(2)
			if color == orange:
				traduction.append(3)
			if color == green:
				traduction.append(4)
			if color == blue:
				traduction.append(5)
			if color == mask:
				traduction.append(-1)

		return traduction

	@staticmethod
	def translate(color):
		# for the self.values, traduction from opengl-rgb to integer values (to simplify the algorithms)
		# cannot do a dictionnary, since lists are not hashable

		if color == white:
			return 0
		if color == yellow:
			return 1
		if color == red:
			return 2
		if color == orange:
			return 3
		if color == green:
			return 4
		if color == blue:
			return 5
		if color == mask:
			return -1

	def set_top(self, color):
		self.color_list[0] = color

	def set_bottom(self, color):
		self.color_list[1] = color

	def set_left(self, color):
		self.color_list[2] = color

	def set_right(self, color):
		self.color_list[3] = color

	def set_front(self, color):
		self.color_list[4] = color

	def set_back(self, color):
		self.color_list[5] = color


