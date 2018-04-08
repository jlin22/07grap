from display import *
from draw import *
from parser import *
from matrix import *
import math
'''
screen = new_screen()
color = [ 0, 255, 0 ]
edges = []'''
#add_polygon(edges, 100, 100, 0, 400, 400, 0, 400, 100 ,0)
#add_box(edges, 100, 400, 100, 300, 300, 300)
'''points = generate_sphere(250, 250, 250, 200, 10)
for x in range(21):
	print("index" + str(x) + str(points[x]))'''
'''add_sphere(edges, 250, 250, 250, 100, 12)
draw_polygons(edges, screen, color)
save_ppm(screen, 'img.ppm')
#draw_lines(edges, screen, color)
#save_ppm(screen, 'img.ppm')
'''
screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )