import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

def read_data(path):
    image_data = nib.load(path).get_fdata()
    return image_data

#  单张显示
def show_img(ori_img):
    plt.imshow(ori_img[:, :, 60], cmap='gray')
    plt.show()


img_path = r'D:\2020SIT1\2020Autumn\ADNI_dataset\ADNI1_Annual_2_Yr_3T\ADNI\002_S_1261\MPR____N3__Scaled\2008-05-27_18_41_16.0\S60591\ADNI_002_S_1261_MR_MPR____N3__Scaled_Br_20081224110926692_S60591_I132220.nii'
# data = read_data(path)
# show_img(data)
image_data = nib.load(img_path).get_fdata()
print(image_data.shape)
x, y, z = image_data.shape
print(np.max(image_data), np.min(image_data))

for _ in range(z):
    print(_)
    plt.imshow(image_data[:, :, _], cmap='gray')
    plt.show()


