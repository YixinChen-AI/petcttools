#!/bin/bash

# 假设你的主文件夹名为normal
main_folder=$1
echo "deal with $main_folder"

# 检查DICOM文件夹的模态类型和检查部位
check_dicom_info() {
    local folder_path=$1
    # 查找文件夹中的第一个DICOM文件
    local dicom_file=$(find "$folder_path" -type f -name "*.dcm" | head -n 1)
    # 读取Modality和Body Part Examined字段
    if [ -f "$dicom_file" ]; then
        modality=$(dcmdump "$dicom_file" | grep "(0008,0060)" | cut -d'[' -f2 | cut -d']' -f1)
        body_part=$(dcmdump "$dicom_file" | grep "(0018,0015)" | cut -d'[' -f2 | cut -d']' -f1)
        echo "$modality#$body_part"
    else
        echo "Unknown#Unknown"
    fi
}

# 遍历normal文件夹中的每个子文件夹（即每个案例）
for case_folder in "$main_folder"/*; do
    if [ -d "$case_folder" ]; then
        # 遍历每个案例中的扫描文件夹
        for scan_folder in "$case_folder"/*; do
            if [ -d "$scan_folder" ]; then
                # 获取扫描文件夹的名称
                scan_name=$(basename "$scan_folder")
                # 检查模态类型和检查部位
                dicom_info=$(check_dicom_info "$scan_folder")
                modality=$(echo "$dicom_info" | cut -d'#' -f1)
                body_part=$(echo "$dicom_info" | cut -d'#' -f2)
                # 设置文件名前缀
                prefix="${modality}#${body_part}#"
                echo $case_folder
                # 使用dcm2niix进行转换，并将输出文件保存在案例文件夹下
                dcm2niix -z y -m y -o "$case_folder" -f "${prefix}${scan_name}" "$scan_folder"
                for output_file in "$case_folder/${prefix}${scan_name}"*.nii.gz; do
                    if [[ "$output_file" == *"CT"* ]]; then
                        mv "$output_file" "$case_folder/ct.nii.gz"
                    fi
                done
            fi
        done
    fi
done
