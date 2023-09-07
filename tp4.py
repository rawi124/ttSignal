# -*- coding: utf-8 -*-
"""
tp sur la segmentation
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from numpy.random import randn


def variance_locale(img, mask):
    """
    calcule la variance locale de l'image en parametre
    """
    l, c = img.shape
    res = np.ones((l, c))
    m = np.floor(mask / 2.)
    m = int(m)
    for i in range(m, l-m):
        for j in range(m, c-m):
            a = img[i-m:i+m, j-m:j+m]
            v = a.var()
            res[i, j] = v
    return res


def solve(m1, m2, std1, std2):
    """
    calcule le seuil optimal
    """
    a = 1/(2*std1**2) - 1/(2*std2**2)
    b = m2/(std2**2) - m1/(std1**2)
    c = m1**2 / (2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
    return np.roots([a, b, c])


if __name__ == '__main__':
    msk_lap = np.array([[-1, 0, 2, 0, -1], [-4, 0, 8, 0, -4],
                       [-6, 0, 12, 0, -6], [-4, 0, 8, 0, -4], [-1, 0, 2, 0, -1]])
    im_src_1 = cv.imread('texture1.tif', cv.IMREAD_GRAYSCALE)
    im_src_2 = cv.imread('texture2.tif', cv.IMREAD_GRAYSCALE)
    im_src_3 = cv.imread('texture3.tif', cv.IMREAD_GRAYSCALE)

    im_src_1 = cv.filter2D(im_src_1, -1, msk_lap,
                           borderType=cv.BORDER_CONSTANT)
    im_src_2 = cv.filter2D(im_src_2, -1, msk_lap,
                           borderType=cv.BORDER_CONSTANT)
    img = cv.filter2D(im_src_3, -1, msk_lap, borderType=cv.BORDER_CONSTANT)

    fig = plt.figure()
    lignes, colonnes = 1, 1

    var_1, var_2, img = variance_locale(im_src_1, 5), variance_locale(
        im_src_2, 5), variance_locale(img, 5)

    m1 = var_1.mean()
    ec1 = np.sqrt(var_1.var())
    m2 = var_2.mean()
    ec2 = np.sqrt(var_2.var())

    seuil = solve(m1, m2, ec1, ec2)
    print(seuil)
    seuil = min(filter(lambda x: x > 0, seuil))

    imb = img > seuil

    fig.add_subplot(lignes, colonnes, 1)
    plt.imshow(imb)
    plt.axis('off')
    plt.title("segmentation supervisée")

    plt.show()
