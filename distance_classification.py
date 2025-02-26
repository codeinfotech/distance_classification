import cv2
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

img_ST = cv2.imread('Dr_Shashi_Tharoor.jpg')
img_ST = cv2.cvtColor(img_ST, cv2.COLOR_BGR2RGB)
img_PF = cv2.imread('Plaksha_Faculty.jpg')
img_PF = cv2.cvtColor(img_PF, cv2.COLOR_BGR2RGB)

plt.figure() 
plt.imshow(img_ST)
plt.axis('off') 
plt.savefig('img_ST.png', bbox_inches='tight')

plt.figure() 
plt.imshow(img_PF)
plt.axis('off')  
plt.savefig('img_PF.png', bbox_inches='tight')