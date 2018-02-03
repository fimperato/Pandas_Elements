# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27  2018

@author: Francesco

"""

import numpy as np

## uso di numpy
print("## uso di numpy ################")
NUMBERS1 = np.array(range(1, 11), copy=True)
print(NUMBERS1)
ONES1 = np.ones([2, 4])
print(ONES1)
ONES1 = np.ones([2, 4], dtype=np.float)
print(ONES1)
ZEROS1 = np.zeros([2, 4], dtype=np.float64)
print(ZEROS1)
## per np.empty il contenuto dell'array non è necessariamente di zeri
EMPTY1 = np.empty([2, 4], dtype=np.float64)
print(EMPTY1)

## shape, ndim (che equivale a len(arraynome.shape) ), dtype
print("\r\n## shape, ndim, dtype (NUMBERS1) ################")
print(NUMBERS1.shape)
print(NUMBERS1.ndim)
print(NUMBERS1.dtype)
print("\r\n## shape, ndim, dtype (ONES1) ################")
print(ONES1.shape)
print(ONES1.ndim)
print(ONES1.dtype)
EYE1 = np.eye(4, k=1)
print(EYE1)
ARRAY_NUM_INTERVALLATO_GENERATO = np.arange(2, 6, 0.30)
print(ARRAY_NUM_INTERVALLATO_GENERATO)
IARRAY_NUM_INTERVALLATO_GENERATO = ARRAY_NUM_INTERVALLATO_GENERATO.astype(np.int)
print(IARRAY_NUM_INTERVALLATO_GENERATO)
#### la maggior parte delle operazioni numpy genera una vista, non una copia dell'array iniziale
#### per conservare i dati iniziali, generare una copia con:
IARRAY_COPY = IARRAY_NUM_INTERVALLATO_GENERATO.copy()

## trasposizione e alterazione array
print("\r\n## trasposizione e alterazione array ################")
ARR_VALS = np.array(["VAL01", "VAL02", "VAL03", "VAL04",
 "VAL05", "VAL06", "VAL07", "VAL08"])
print(ARR_VALS)
ARR_VALS_2D = ARR_VALS.reshape(2, 4) ## 2 dimensioni
print(ARR_VALS_2D)
ARR_VALS_3D = ARR_VALS.reshape(2, 2, 2) ## 3 dimensioni
print(ARR_VALS_3D)
print(ARR_VALS_3D[1][1][1])

#### trasposizione
print("\r\n#### trasposizione ")
print(ARR_VALS_3D.T)
print(ARR_VALS_3D.swapaxes(1,2))
print(ARR_VALS_3D.transpose(0,1,2))

## alterazione array numpy
print("\r\n## alterazione array numpy ################")
ARRAY_DIRTY = np.array([5, 4, 3, 2, -1, -0.1, 100])
CONDIZIONE_DIRTY = ARRAY_DIRTY < 0 ## array boolean da usare come indice boolean
#### set di tutti i valori dirty a zero:
print(ARRAY_DIRTY[CONDIZIONE_DIRTY])
ARRAY_DIRTY[CONDIZIONE_DIRTY] = 0
print(ARRAY_DIRTY)
#### operatori logici per le condizioni multiple: &, |, NOT
ARR_TEST1 = np.arange(-5,3,0.8)
print(ARR_TEST1)
ARR_TEST1_FLT_BOOL = (ARR_TEST1 <= -2.0) | (ARR_TEST1 >= 2.0)
print(ARR_TEST1_FLT_BOOL)
ARR_TEST1_FLT_BOOL = (ARR_TEST1 >= -1.0) & (ARR_TEST1 < 1.0)
print(ARR_TEST1_FLT_BOOL)
ARR_TEST1_FLT = ARR_TEST1[(ARR_TEST1 > -1.1) & (ARR_TEST1 < 1.0)]
print(ARR_TEST1_FLT)

## Slicing
print("\r\n## Slicing ################")
ARR_TEST1_SLICING = ARR_TEST1[ [1, 2, -1] ]
print(ARR_TEST1_SLICING)
### estrarre tutte le righe della colonna centrale
ARR_TEST2 = np.arange(5, 9, 0.2)
print(ARR_TEST2.size)
ARR_TEST2 = ARR_TEST2.reshape(5, 4)
print(ARR_TEST2)
ARR_ALL_ROW_COL2 = ARR_TEST2[ :, [2] ] ## primo modo: estraggo una matrice bidimensionale
print(ARR_ALL_ROW_COL2)
ARR_ALL_ROW_COL2 = ARR_TEST2[ :, 2 ] ## secondo modo: estraggo un array monodimensionale
print(ARR_ALL_ROW_COL2)
SIGNAL_NOISE1 = np.eye(4) + 0.01*np.random.random([4,4])
print(SIGNAL_NOISE1)
SIGNAL_NOISE1 = np.round(SIGNAL_NOISE1, 2)
print(SIGNAL_NOISE1)

## Funzioni universali: applicabili a tutti gli elementi di un array in una sola chiamata a funzione
print("\r\n## Funzioni universali ################")
ARR_TEST2 = np.arange(3,4.8,0.15)
print(ARR_TEST2)
ARR_TEST2 = ARR_TEST2.reshape(2,6)
ARR_TEST2 = ARR_TEST2*np.random.random([2,6])
print(ARR_TEST2)
DIMINUZIONE_CHECK = np.greater(ARR_TEST2[0], ARR_TEST2[1])
print(DIMINUZIONE_CHECK)

#### gestione nan
print("\r\n#### gestione nan ")
ARR_TEST3 = ARR_TEST2.copy()
ARR_TEST3[0,1] = np.nan
print(ARR_TEST3)
CONDITION_ISNAN3 = np.isnan(ARR_TEST3) 
print(CONDITION_ISNAN3)
ARR_TEST3[CONDITION_ISNAN3] = 0
print(ARR_TEST3)

#### where: verificare condizioni su coppie di array
print("\r\n#### gestione where ")
ARR_LABELS4 = np.array(["LAB1", "LAB2", "LAB3", "LAB4", "LAB5", "LAB6"])
ARR_TEST4 = ARR_TEST3.copy()
#ARR_TEST4 = np.vstack((ARR_LABELS4, ARR_TEST4))
print(ARR_TEST4)
ARR_REALLY_DIFF = np.where(np.abs(ARR_TEST4[0] - ARR_TEST4[1]) > 1.00, ARR_TEST4[1] - ARR_TEST4[0], 0)
print(ARR_REALLY_DIFF)
print(np.nonzero(ARR_REALLY_DIFF))
print(ARR_LABELS4[ np.nonzero(ARR_REALLY_DIFF) ])