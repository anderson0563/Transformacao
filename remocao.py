import cv2
import numpy as np
from PIL import Image

img = cv2.imread("imagem.png")
cv2.imshow('color image', img)

pts1 = np.float32([[52,440], [10, 908], [810,20], [829,985]])
pts3 = np.float32([[810,20], [829,985], [1480, 341], [1532, 909]])
pts2 = np.float32([[0,0], [0,300], [500, 0], [500, 300]])
 
M = cv2.getPerspectiveTransform(pts1, pts2)
dst1 = cv2.warpPerspective(img, M, (500,300))
cv2.imwrite("imagem1.png", dst1)

cv2.imshow('color image', dst1)
cv2.waitKey(0)

M2 = cv2.getPerspectiveTransform(pts3, pts2)
dst2 = cv2.warpPerspective(img, M2, (500,300))

cv2.imwrite("imagem2.png", dst2)

cv2.imshow('color image', dst2)
cv2.waitKey(0)

final = cv2.hconcat([dst1, dst2])
cv2.imwrite("imagemfinal.png", final)

cv2.imshow('color image', final)
cv2.waitKey(0)