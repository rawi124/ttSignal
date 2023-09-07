# -*- coding: utf-8 -*-
"""
tp sur la transformation de fourier
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from numpy.fft import fft2, ifft2, fftshift

image_size = 256

fig, axarr = plt.subplots(1, 2)        # 2 figures sur 1 ligne et 2 colonnes
axA = plt.axes([0.2, 0.05, 0.6, 0.03])  # [gauche, bas, largeur, hauteur]
axB = plt.axes([0.2, 0.08, 0.6, 0.03])  # en dimensions normalisées
s_A = Slider(axA, 'A', 0, image_size)
s_B = Slider(axB, 'B', 0, image_size)
l1 = axarr[0].imshow(np.ones((image_size, image_size)),
                     cmap='gray', interpolation='none')
l2 = axarr[1].imshow(np.ones((image_size, image_size)),
                     cmap='gray', interpolation='none')


x, y = np.meshgrid(range(0, 256), range(0, 256))
i1 = 128*(np.sin(2*np.pi*(20*x/256 + 20*y/256)) + 1)
i2 = 128*(np.sin(2*np.pi*(145*x/256 + 145*y/256)) + 1)
# i = i1 + i2


# convertir au meme type pour pouvoir effectuer l'addition

# perturber l image


i = 128*np.sin(2*np.pi*(50*x/256 + 10*y/256))  # perturbation
fi = fft2(i)  # transformé de fourier
fi = fftshift(fi)
fi = abs(fi)


im = cv.imread('photophore.tif', 0)  # charger l image a perturber
im = np.array(im, float)
i = np.array(i, float)
im2 = im + i

im2 = fft2(im2)
im2 = fftshift(im2)

im2[119][79] = 0
im2[139][179] = 0

im2 = fftshift(im2)
im2 = ifft2(im2)  # transformé de fourier inverse
im2 = abs(im2)


l1.set_data(im)
l1.autoscale()

l2.set_data(im2)
l2.autoscale()


def update():
    # i doit contenir une image de sinus
    # m_fi est l'image module de sa transformée de Fourier recentrée en 0
    # les valeurs des slider sont récupérés au travers de l'attribut val
    # ex : A = s_A.val
    l1.set_data(i)
    l2.set_data(m_fi)
    l1.autoscale()
    l2.autoscale()
    fig.canvas.draw_idle()


s_A.on_changed(update)
s_B.on_changed(update)

plt.show()
