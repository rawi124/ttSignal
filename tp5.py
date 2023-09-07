"""
tp sur filtrage de la moyenne
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from numpy.fft import fft2, ifft2, fftshift
import mediane as md


def mc(img1, img2, border_size):
    """
    ttt
    """
    x1, y1 = img1.shape
    x2, y2 = img2.shape

    if (x1, y1) != (x2, y2):
        print("Images de tailles differentes !")

    ext1 = img1[border_size:x1-border_size, border_size:y1-border_size]
    ext2 = img2[border_size:x1-border_size, border_size:y1-border_size]
    r = np.mean((ext1 - ext2) ** 2)
    return r


if __name__ == '__main__':
    im = cv.imread('photophore.tif', 0)
    im1 = cv.imread('ph_gauss.tif', 0)
    im2 = cv.imread('ph_pulse.tif', 0)
    filtre = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9
    imm1 = cv.filter2D(im1, -1, filtre, borderType=cv.BORDER_CONSTANT)
    imm2 = cv.filter2D(im2, -1, filtre, borderType=cv.BORDER_CONSTANT)
    fig = plt.figure()
    lignes, colonnes = 2, 2
    fig.add_subplot(lignes, colonnes, 1)
    plt.imshow(im1, cmap='gray')
    plt.axis('off')
    plt.title("ph_gauss")
    fig.add_subplot(lignes, colonnes, 2)
    plt.imshow(imm1, cmap='gray')
    plt.axis('off')
    plt.title("ph_gauss filtré")
    fig.add_subplot(lignes, colonnes, 3)
    plt.imshow(im2, cmap='gray')
    plt.axis('off')
    plt.title("ph_pulse")
    fig.add_subplot(lignes, colonnes, 4)
    plt.imshow(imm2, cmap='gray')
    plt.axis('off')
    plt.title("ph_pulse filtré")
    plt.show()
