import os
import shutil
import pypandoc

input_folder = r"C:\Users\dy003\Desktop\input"
output_file = "output.epub"
temp_folder = r"C:\Users\dy003\Desktop\temp"

# 创建临时文件夹
os.makedirs(temp_folder, exist_ok=True)

# 遍历输入文件夹中的文件
file_list = []
for file_name in os.listdir(input_folder):
    if file_name.endswith('.md'):
        # 构建输入文件的完整路径
        input_path = os.path.join(input_folder, file_name)

        # 读取Markdown文件的内容
        with open(input_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # 将Markdown内容添加到文件列表中
        file_list.append(file_content)

        # 复制Markdown文件所在路径下的images文件夹到临时文件夹中
        image_folder = os.path.join(os.path.dirname(input_path), 'images')
        temp_image_folder = os.path.join(temp_folder, 'images')
        if os.path.exists(image_folder):
            shutil.rmtree(temp_image_folder, ignore_errors=True)  # 删除目标文件夹
            shutil.copytree(image_folder, temp_image_folder, ignore_dangling_symlinks=True)

# 将文件列表中的Markdown内容合并为一个字符串
combined_content = '\n'.join(file_list)

# 将Markdown内容转换为EPUB，指定临时文件夹作为图片根路径
pypandoc.convert_text(combined_content, 'epub', format='md', outputfile=output_file, extra_args=['--embed-resources',f'--resource-path={temp_folder}', '--metadata', 'title=财富自由之路by李笑来'])

# 删除临时文件夹
shutil.rmtree(temp_folder)