"""
tp sur le filtrage lineaire
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from numpy.random import randn


def calcul_variance(im_origine, im_filtre):
    """
    retourne la variance entre les deux images
    """
    data_or = np.squeeze(im_origine)
    data_fi = np.squeeze(im_filtre)
    dim_n,dim_m = data_or.shape
    variance = 0
    for i in range(dim_n):
        for j in range(dim_m):
            variance += (data_or[i][j] - data_fi[i][j])**2
    return variance/(dim_n*dim_m)


if __name__ == '__main__':
    fig = plt.figure()

    im = cv.imread('photophore.tif', cv.IMREAD_GRAYSCALE)
    # on construit l image bruite a partir de l image im avec le bruit gaussien et
    ecart_type = 6  # et est l ecart type

    imb = im + ecart_type*randn(im.shape[0], im.shape[1])
    flt1, flt2 = np.ones((3, 3)) / 9, np.ones((5, 5)) / 25
    # print("filtre 1 :" ,flt1,"\nfiltre 2 :", flt2)

    x, y = np.meshgrid(range(-1, 2), range(-1, 2))  # (3, 3)
    x1, y1 = np.meshgrid(range(-1, 4), range(-1, 4))  # (5, 5)

    fgauss1 = np.exp(-(x*x + y*y) / (2*ecart_type*ecart_type))
    # le parametre et est l ecart type (sigma)
    fgauss1 = fgauss1/sum(sum(fgauss1))

    fgauss2 = np.exp(-(x1*x1 + y1*y1) / (2*ecart_type*ecart_type))
    # le parametre et est l ecart type (sigma)
    fgauss2 = fgauss2/sum(sum(fgauss2))

    imf1 = cv.filter2D(imb, -1, flt1, borderType=cv.BORDER_CONSTANT)
    imf2 = cv.filter2D(imb, -1, flt2, borderType=cv.BORDER_CONSTANT)
    imf3 = cv.filter2D(imb, -1, fgauss1, borderType=cv.BORDER_CONSTANT)
    imf4 = cv.filter2D(imb, -1, fgauss2, borderType=cv.BORDER_CONSTANT)

    lignes, colonnes = 2, 2
    # on affiche l image d origine
    fig.add_subplot(lignes, colonnes, 1)
    plt.imshow(imb, cmap='gray')
    plt.axis('off')
    plt.title("image d origine bruitee")

    fig.add_subplot(lignes, colonnes, 2)
    # on affiche l image avec le filtre (3, 3)
    plt.imshow(imf1, cmap='gray')
    plt.axis('off')
    plt.title("image debruitee avec fgauss1")

    # on affiche l image avec le filtre (5, 5)
    fig.add_subplot(lignes, colonnes, 3)
    plt.imshow(imf2, cmap='gray')
    plt.axis('off')
    plt.title("image debruitee avec fgauss2")

    print("calcul de la variance")
    print("variance avec filtre moyen 3,3 ", calcul_variance(im, imf1))
    print("variance avec filtre moyen 5,5 ", calcul_variance(im, imf2))
    print("variance avec filtre gaussien 3,3 ", calcul_variance(im, imf3))
    print("variance avec filtre gaussien 5,5 ", calcul_variance(im, imf4))

    plt.show()
