import imageio
import numpy as np

cbam_img = imageio.imread("cbam.png")
none_img = imageio.imread("none.png")
truth_img = imageio.imread("truth.png")
cbam_img = cbam_img[0:150,200:350]
none_img = none_img[0:150,200:350]
truth_img = truth_img[0:150,200:350]
img = np.concatenate((truth_img,cbam_img,none_img),axis=1)

imageio.imwrite("compare.png",img)