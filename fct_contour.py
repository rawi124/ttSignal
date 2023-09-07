import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from numpy.random import randn

def contour_laplacien(im_src, seuil):
	"""
	im_src :image source
	retourne : une image avec un contour
	"""
	gx = np.zeros((3,3))
	gx[0][0] = 1
	gx[0][2] = -1
	gx[1][0] = 1
	gx[1][2] = -1
	gx[2][0] = 1
	gx[2][2] = -1
	
	gy = gx.T

	seuil_haut, seuil_bas  = seuil, seuil*0.7
	flt_1 = np.zeros((3, 3))#initialise une matrice 3*3 a zero
	flt_1[1][1], flt_1[0][1], flt_1[1][0], flt_1[1][2], flt_1[2][1] = -4, 1, 1, 1, 1 #effectue le masquage
	pos = cv.filter2D(im_src, -1, flt_1, borderType=cv.BORDER_CONSTANT)
	
	im_lap1 = pos[0:255,0:255]
	im_lap1 = np.insert(im_lap1, -1, np.array([[0, 0, 0]]*(pos.shape[0]-1)), axis=0)
	im_lap1 = np.insert(im_lap1, -1, np.array([[0, 0, 0]]*(pos.shape[1])), axis=1)
	
	im_lap2 = pos[1:256,0:255]
	im_lap2 = np.insert(im_lap2, -1, np.array([[0, 0, 0]]*(pos.shape[0]-1)), axis=0)
	im_lap2 = np.insert(im_lap2, -1, np.array([[0, 0, 0]]*(pos.shape[1])), axis=1)
	
	im_lap3 = pos[0:255,1:256]
	im_lap3 = np.insert(im_lap3, -1, np.array([[0, 0, 0]]*(pos.shape[0]-1)), axis=0)
	im_lap3 = np.insert(im_lap3, -1, np.array([[0, 0, 0]]*(pos.shape[1])), axis=1)
	
	
	
	#calcule norme de gradient
	ngrad = cv.filter2D(im_src, -1, gx, borderType=cv.BORDER_CONSTANT)**2 + cv.filter2D(im_src, -1, gy, borderType=cv.BORDER_CONSTANT)**2
	
	cont =  (((im_lap1*im_lap3) < seuil_bas) | ((im_lap2*im_lap3) < seuil_bas)) & (ngrad > seuil_haut)
	
	return cont*175
	
