#!/usr/bin/python

# First execute: easy_install Image

import math;
import random;
from PIL import Image;

im = Image.open("/Users/Bookman/Pictures/29411.jpg");
mat = im.getdata();
im.show();

class pulse_couple_nn:
	dim_x = 0;
	dim_y = 0;
	feed = [];
	couple = [];
	
	