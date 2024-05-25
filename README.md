一个针对但不限于PET/CT静态、动态数据的工具库

### 功能1: dcm文件序列转换nifti文件，支持PET、CT模态。
```
./dcm2nii.sh <文件夹路径>
```
程序会将<文件夹路径>下所有的dcm序列都转化成nifti格式。其中nifti的命名由：{modality}#{body_part}.nii.gz，例如PT#WholeBody，或者CT#Head。

### 功能2：对CT影像进行不同器官的ROI分割。
下载训练好的模型权重文件lucida_large.pth到目录petcttools/lucida/lucida_large.pth位置。
百度云盘：
  - 链接：https://pan.baidu.com/s/1Bbds5aoGyWEQm1HpPOE0nQ 
  - 提取码：w7mo 
```
cd lucid
python3 bodyseg.py --ct <ct.nii.gz的路径> --output <输出的结果存放文件夹>
```
