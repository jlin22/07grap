from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script', polygons, edges, transform, screen, color )	
'''
add_box(edges, 200, 200, 200, 100, 100, 100)
add_sphere(edges, 250, 250, 250, 50, 10)
add_torus(edges, 250, 250, 250, 50, 75, 10)
draw_polygons(edges, screen, color)
save_ppm(screen, 'img.ppm')
'''