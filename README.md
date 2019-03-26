# Rubik-s-Cube-OpenGL
A graphical Rubik's Cube Solver with python and OpenGL

[Installation]

  - make sure you have python3+ installed
  - go to repo (with terminal/cmd)
  - type: 'pip install -r requirements.txt'
  - to run it: 'python main.py'


[How to use it]

First, note that you can customize the starting point
(now you still have to go in the 'main.py' code and change the values at the top).
There are several keyboard inputs available:
  - J & L: rotate the camera left & right
  - I & K: rotate the camera up & down
  - S: scrambles the cube (D for at once)
  - F: solves the cube (G for at once)
  - P: clear the terminal/cmd screen
  - W: quit

  - Y: complete the white cross (W for at once)
  - X: complete the white corners (E for at once)
  - C: complete the side edges (R for at once)
  - V: complete the bottom cross (T for at once)
  - B: complete the bottom corners (Z for at once)
  - N: complete the Rubik'y Cube (U for at once)

The mouse button scrolling will zoom in/out.
Note that the camera rotation is done with basic OpenGL functions, so that you will have weird (they're actually normal, you will get used to :-) ) results.


[What I want to implement]

  - fix a bug (rarely occurs) which makes the program 'freeze' (it's not really freeezing, it's running an infinite while loop)
  - more than 3x3 Cube (2x2, 4x4, etc.)
  - BLD Solving
  - More complex (and fast) methods for RC solving
