"""
detection de contour
"""
import cv2 as cv
from matplotlib import pyplot as plt
from numpy.random import randn

from fct_contour import contour_laplacien

if __name__ == '__main__':
    im_src = cv.imread('photophore.tif')
    SEUILH = 30
    SEUILB = 0.7*SEUILH

    ET = 3

    im_lap = im_src + ET * \
        randn(im_src.shape[0], im_src.shape[1], im_src.shape[2])

    ref_canny = cv.Canny(im_src, SEUILB, SEUILH)
    ref_lapla = contour_laplacien(im_lap, 3000)

    fig = plt.figure()

    lignes, colonnes = 1, 2
    fig.add_subplot(lignes, colonnes, 1)
    plt.imshow(ref_canny, cmap='gray')
    plt.axis('off')
    plt.title("detection avec canny ")

    fig.add_subplot(lignes, colonnes, 2)
    plt.imshow(ref_lapla, cmap='gray')
    plt.axis('off')
    plt.title("detection avec laplacien")

    plt.show()
