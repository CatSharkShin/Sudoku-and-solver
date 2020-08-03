import pygame, sys
from pygame.locals import *

windowwidth = 60*9
windowheight = 60*9
cellw = windowwidth//9
cellh = windowheight//9
global cellx,celly,rx,ry
gridwidth = 4
gridcolor = (0,0,0)
backgroundcolor = (190,190,190)
clicked = (250,250,250)
sudoku = [
		[2,3,4,7,5,0,9,0,0],
		[7,0,0,4,0,0,0,0,3],
		[1,0,0,0,0,0,0,4,5],
		[6,9,0,0,7,8,0,0,4],
		[0,7,1,0,0,0,8,5,0],
		[4,0,8,3,0,5,0,7,0],
		[8,4,0,0,0,3,0,0,7],
		[9,6,0,1,0,0,0,0,8],
		[5,0,0,7,0,2,9,0,0]
]
selected = (-1,-1)

def main():
	global DISPLAY
	pygame.init()
	DISPLAY = pygame.display.set_mode((windowwidth,windowheight)) 
	pygame.display.set_caption('Sudoku')
	DISPLAY.fill(backgroundcolor)
	drawGrid()
	while True: 
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	        if event.type == pygame.MOUSEBUTTONUP:
	        	select()
	        	fill()
	        	drawGrid()
	        if event.type == KEYDOWN:
	        	if selected != (-1,-1) and event.unicode.isnumeric():
	        		print(event.unicode)
	    pygame.display.update()

def ceildiv(a, b):
    return -(-a // b)

def drawGrid():
	for x in range(cellw,windowwidth,cellw):
		pygame.draw.line(DISPLAY,gridcolor,(x,0),(x,windowheight),gridwidth)

	for y in range(cellh,windowheight,cellh):
		pygame.draw.line(DISPLAY,gridcolor,(0,y),(windowwidth,y),gridwidth)

def fill():
	DISPLAY.fill((backgroundcolor))
	print(selected)
	print("filling")
	rx = 0 + selected[0]*cellw
	ry = 0 + selected[1]*cellh
	pygame.draw.rect(DISPLAY,clicked,(rx,ry,cellw,cellh))

def select():
	global selected
	mpos = pygame.mouse.get_pos()
	cellx = mpos[0]//cellw
	celly = mpos[1]//cellh
	selected = (cellx,celly)
if __name__=='__main__':
	main()