import SimpleITK as sitk
import os,sys
import numpy as np

def save_image(image, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    sitk.WriteImage(image, file_path)
def rename_file(old_name, new_name):
    # 确保旧文件名的文件确实存在
    if os.path.exists(old_name):
        # 重命名文件
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    else:
        print(f"The file {old_name} does not exist.")

def resample_image(input_image, reference_image):
    # 创建一个重采样过滤器
    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(reference_image)
    
    # 设置插值方法，通常使用线性插值
    resampler.SetInterpolator(sitk.sitkLinear)
    
    # 设置输出使用参考图像的spacing, origin和direction
    resampler.SetOutputSpacing(reference_image.GetSpacing())
    resampler.SetOutputOrigin(reference_image.GetOrigin())
    resampler.SetOutputDirection(reference_image.GetDirection())
    
    # 设置输出图像的size
    resampler.SetSize(reference_image.GetSize())
    resampler.SetDefaultPixelValue(-3024)
    
    # 执行重采样
    return resampler.Execute(input_image)

parser = argparse.ArgumentParser(description="align ct image (nifti) to pet image (nifti)")
parser.add_argument("--ct", type=str, help="the nii.gz path for ct.nii.gz")
parser.add_argument("--pet", type=str, help="the nii.gz path for ct.nii.gz")
args = parser.parse_args()

print(f"CT Path: {args.ct}")
print(f"pet Path: {args.pet}")
print("new CT Path: {}".format(args.ct.replace(".nii.gz","_petsize.nii.gz")))

ctniipath = args.ct
petnii = args.pet
ctnii = sitk.ReadImage(ctniipath)
petnii = sitk.ReadImage(petnii)

print(ctnii.GetSpacing(),petnii.GetSpacing())
if len(petnii.GetSpacing()) == 4:
    print("dynamic pet. remove last dimension")
    ctnii = resample_image(ctnii,petnii[:,:,:,0])
elif len(petnii.GetSpacing()) == 3:
    ctnii = resample_image(ctnii,petnii)
print("new ct spacing:",ctnii.GetSpacing())
ctarr = sitk.GetArrayFromImage(ctnii)
petarr = sitk.GetArrayFromImage(petnii)
print("new ct shape and pet shape",ctarr.shape,petarr.shape)
# rename_file(ctniipath,ctniipath.replace("ct.nii.gz","ctori.nii.gz"))
sitk.WriteImage(ctnii,args.ct.replace(".nii.gz","_petsize.nii.gz"))
print("new ct image have been written:",args.ct.replace(".nii.gz","_petsize.nii.gz"))
