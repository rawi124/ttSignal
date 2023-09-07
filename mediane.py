import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def median(lst):
    """
    une fonction qui calcule la mediane d'une liste
    """
    half = len(lst) // 2
    lst.sort()
    if not len(lst) % 2:
        return (lst[half - 1] + lst[half]) / 2.0
    return lst[half]

def arith_matrice(matrice):
    """
    une methode qui calcule la moyenne mediane pour chaque valeur de la matrice
    en ignornat les elements sur la bordure
    """
    n, i = len(matrice), 0
    copie, moyenne, tmp = [], [], []
    while i < n-1 :
        j = 0
        while j < n-1:
            if i-1 >= 0 and j-1 >= 0:
                moyenne.append(matrice[i-1][j-1])
            if i-1 >= 0 :
                moyenne.append(matrice[i-1][j])
            if i-1 >= 0and j+1 < n :
                moyenne.append(matrice[i-1][j+1])
            if j-1 >=0  :
                moyenne.append(matrice[i][j-1])
            if j+1 < n:
                moyenne.append(matrice[i][j+1])
            if i+1 < n and j-1 >= 0 :
                moyenne.append(matrice[i+1][j-1])
            if i+1 < n and j+1 < n :
                moyenne.append(matrice[i+1][j+1])
            if i+1 < n  :
                moyenne.append(matrice[i+1][j])
            moyenne.append(matrice[i][j])
            tmp.append(median(moyenne))
            moyenne = []
            j = j +1
        copie.append(tmp)
        tmp = []
        i = i+ 1
    return copie 
