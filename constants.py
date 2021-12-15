import sys


BLOCKS = {
	" " : None,
	"0" : "assets/blocks/yellow_block.png",
	"1" : "assets/blocks/purple_block.png",
	"2" : "assets/blocks/blue_block.png",
	"3" : "assets/blocks/green_block.png",
	"4" : "assets/blocks/aqua_block.png",
	"5" : "assets/blocks/red_block.png",
	"6" : "assets/blocks/hole.png"
}

tank_map = {
	"A" : "grey",
	"B" : "yellow",
	"C" : "blue",
	"D" : "green",
	"E" : "red",
	"F" : "black",
}


FIELDWIDTH = 22
FIELDHEIGHT = 16
IMAGEWIDTH = 50
IMAGEHEIGHT = 50
SCREEN_WIDTH = FIELDWIDTH*IMAGEWIDTH
SCREEN_HEIGHT = FIELDHEIGHT*IMAGEHEIGHT

TANKWIDTH = 50
TANKHEIGHT = 40