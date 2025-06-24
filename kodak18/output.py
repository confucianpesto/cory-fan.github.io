import imageio
import numpy as np

cbam_img = imageio.imread("cbam.png")
none_img = imageio.imread("none.png")
truth_img = imageio.imread("truth.png")
cbam_img = cbam_img[420:570,330:430]
none_img = none_img[420:570,330:430]
truth_img = truth_img[420:570,330:430]
img = np.concatenate((truth_img,cbam_img,none_img),axis=1)

imageio.imwrite("compare.png",img)