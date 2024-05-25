一个针对但不限于PET/CT静态、动态数据的工具库
功能：
1. dcm文件序列转换nifti文件，支持PET、CT模态。
```
./dcm2nii.sh <文件夹路径>
```
程序会将<文件夹路径>下所有的dcm序列都转化成nifti格式。其中nifti的命名由：{modality}#{body_part}.nii.gz，例如PT#WholeBody，或者CT#Head。

2. 
