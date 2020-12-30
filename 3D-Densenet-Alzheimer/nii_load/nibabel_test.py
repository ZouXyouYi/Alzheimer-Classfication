
import nibabel as nib
from matplotlib import pylab as plt
from nibabel.viewers import OrthoSlicer3D




img_path = r'D:\2020SIT1\2020Autumn\ADNI_dataset\ADNI1_Annual_2_Yr_3T\ADNI\002_S_1261\MPR____N3__Scaled\2008-05-27_18_41_16.0\S60591\ADNI_002_S_1261_MR_MPR____N3__Scaled_Br_20081224110926692_S60591_I132220.nii'

image = nib.load(img_path)
print(image)
width, height, queue = image.dataobj.shape

OrthoSlicer3D(image.dataobj).show()

num = 1
for i in range(0, queue, 8): #也可以取10等
    img_arr = image.dataobj[:,:,i]
    print(img_arr.shape)
    plt.subplot(5, 4, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1
plt.show()