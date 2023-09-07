# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def variance_locale(img, mask):
    """
    calcule la variance locale de l image img en entree
    """
    ligne, colone = img.shape
    unitaire = np.ones((ligne, colone))
    maxi = np.floor(mask / 2.)
    maxi = int(maxi)
    for i in range(maxi, ligne-maxi):
        for j in range(maxi, colone-maxi):
            tmp = img[i-maxi:i+maxi, j-maxi:j+maxi]
            v_tmp = tmp.var()
            unitaire[i, j] = v_tmp
    return unitaire
def solve(m_1, m_2, std_1, std_2):
    """
    calcule le seuil optimal
    """
    tmp_1 = 1/(2*std_1**2) - 1/(2*std_2**2)
    tmp_2 = m_2/(std_2**2) - m_1/(std_1**2)
    tmp_3 = m_1**2 /(2*std_1**2) - m_2**2 / (2*std_2**2) - np.log(std_2/std_1)
    return np.roots([tmp_1, tmp_2, tmp_3])
if __name__ == '__main__':
	"""
    IM = cv.imread('texture3.tif', cv.IMREAD_GRAYSCALE)
    MSK = np.array([[-1, 0, 2, 0, -1],
                    [-4, 0, 8, 0, -4],
                    [-6, 0, 12, 0, -6],
                    [-4, 0, 8, 0, -4], 
                    [-1, 0, 2, 0, -1]])
    IM_MSK = cv.filter2D(IM, -1, MSK, borderType=cv.BORDER_CONSTANT)
    FIG = plt.figure()
    LIGNES, COLONNES = 2, 2
    FIG.add_subplot(LIGNES, COLONNES, 1)
    plt.imshow(IM, cmap='gray')
    plt.axis('off')
    plt.title("avant mask")
    FIG.add_subplot(LIGNES, COLONNES, 2)
    plt.imshow(IM_MSK, cmap='gray')
    plt.axis('off')
    plt.title("apres mask ")
    plt.show()
    """	
	msk_lap = np.array([[-1,0,2,0,-1],[-4,0,8,0,-4],[-6,0,12,0,-6],[-4,0,8,0,-4],[-1,0,2,0,-1]])
	im_src_1 = cv.imread('texture1.tif', cv.IMREAD_GRAYSCALE)
	im_src_2 = cv.imread('texture2.tif', cv.IMREAD_GRAYSCALE)
	
	im_src_1 = cv.filter2D(im_src_1, -1, msk_lap, borderType=cv.BORDER_CONSTANT)
	im_src_2 = cv.filter2D(im_src_2, -1, msk_lap, borderType=cv.BORDER_CONSTANT)
	
	fig = plt.figure()
	lignes, colonnes = 2, 2
	fig.add_subplot(lignes, colonnes, 1)
	plt.imshow(im_src_1, cmap='gray')
	plt.axis('off')
	plt.title("texture 1")
	
	
	fig.add_subplot(lignes, colonnes, 2)
	plt.imshow(im_src_2, cmap='gray')
	plt.axis('off')
	plt.title("texture 2")
	
	var_1, var_2 = variance_locale(im_src_1, 5), variance_locale(im_src_2, 5)
	
	fig.add_subplot(lignes, colonnes, 3)
	plt.hist(var_1.ravel(), 100)
	plt.title("histogramme de texture 1")
	
	
	fig.add_subplot(lignes, colonnes, 4)
	plt.hist(var_2.ravel(), 100)
	plt.title("histogramme de texture 2")
	#conclusions sur les histogrammes : histo 1 ya plus de blanc que de noir 
	#histo 2 ya  plus  de noir que de blanc
	plt.show() 
	
