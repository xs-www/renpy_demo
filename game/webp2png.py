import os
from PIL import Image

def convert_and_resize_webp_to_png(folder_path, target_size=(1920, 1080)):
    # 确保路径存在
    if not os.path.exists(folder_path):
        print(f"路径 {folder_path} 不存在！")
        return

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                # 获取文件的完整路径
                webp_path = os.path.join(root, file)
                png_path = os.path.splitext(webp_path)[0] + ".png"

                # 如果对应的 PNG 文件已存在，则跳过
                if os.path.exists(png_path):
                    print(f"已存在：{png_path}，跳过转换。")
                    continue

                # 转换并调整大小
                try:
                    with Image.open(webp_path) as img:
                        # 调整大小
                        resized_img = img.resize(target_size, Image.ANTIALIAS)
                        # 保存为 PNG 格式
                        resized_img.save(png_path, "PNG")
                        print(f"转换成功：{webp_path} -> {png_path}，尺寸调整为 {target_size}")
                except Exception as e:
                    print(f"转换失败：{webp_path}，错误信息：{e}")

# 调用函数，传入相对路径和目标尺寸
convert_and_resize_webp_to_png("./images", target_size=(1920, 1080))