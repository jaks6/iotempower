# main.py script for ulno's version of wemos shields
#
# TODO: build reset function when lower button
# is pressed when starting up
#
import machine
machine.freq(160000000)
import ulno_shield01
if ulno_shield01.present:
	from ulno_shield01 import d3,d4,d5,d6,d7,left_button,right_button,lower_button,red,yellow,blue,display
