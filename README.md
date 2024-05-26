一个针对但不限于PET/CT静态、动态数据的工具库

### 功能1: dcm文件序列转换nifti文件，支持PET、CT模态。
作用：程序会将<文件夹路径>下所有的dcm序列都转化成nifti格式。其中nifti的命名由：{modality}#{body_part}.nii.gz，例如PT#WholeBody，或者CT#Head。

```
./dcm2nii.sh <文件夹路径>
```

### 功能2：对CT影像进行不同器官的ROI分割。
作用：将ct image划分成100+个不同器官的ROI区域，包含左心室，主动脉等；
下载训练好的模型权重文件lucida_large.pth到目录petcttools/lucida/lucida_large.pth位置。
百度云盘：
  - 链接：https://pan.baidu.com/s/1Bbds5aoGyWEQm1HpPOE0nQ 
  - 提取码：w7mo 
```
cd lucid
python3 bodyseg.py --ct <ct.nii.gz的路径> --output <输出的结果存放文件夹>
```

参考文献：

[1] Y. Chen et al., "PCNet: Prior Category Network for CT Universal Segmentation Model," in IEEE Transactions on Medical Imaging, doi: 10.1109/TMI.2024.3395349.
keywords: {Image segmentation;Biomedical imaging;Task analysis;Computational modeling;Computed tomography;Hidden Markov models;Anatomical structure;Computed Tomography;Universal Model;Segmentation;Prior Knowledge;Prompt},

### 功能3：将PETCT的CT image对齐到PET image中
作用：PETCT影像的PET image与CT在spacing，origin，direction上可能存在差异。运行下面指令之后，会将<ct.nii.gz的路径>按照<pet.nii.gz的路径>的尺寸进行对其。其中pet image可以是静态pet(shape like [z,w,h]),，也可以是dynamic image (shape like [z,w,h,time]).
```
python3 ctpetalign.py --ct <ct.nii.gz的路径> --pet <pet.nii.gz的路径>
```

运行之后，会在<ct.nii.gz的路径>目录下，生成一个*_petsize.nii.gz的新ct image文件。
