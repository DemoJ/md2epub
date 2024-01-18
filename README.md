## 使用场景
想要将多个md文档（且文档中全是本地图片）打包成epub电子书文件时，搜索一圈发现没有可现成使用的工具，遂自己写了这个脚本实现
## 使用方法
1. md文档目录结构如下：files文件夹下是所有md文档及md文档中引用的图片文件夹images
    - files
        - images
        - file1.md
        - file2.md
2. 安装pandoc并将其添加到系统的PATH环境变量中：
    - 访问pandoc官方网站下载并安装适用于您的操作系统的pandoc。
    - 安装完成后，将pandoc所在的路径添加到系统的PATH环境变量中。这样pypandoc就能够找到并使用pandoc进行转换操作。
3. 在终端中安装pypandoc：pip install pypandoc==1.12
4. 将脚本中`input_folder = r"C:\Users\dy003\Desktop\files" `修改为对应md文档及图片所在的文件夹路径
5. 将脚本中`pypandoc.convert_text(combined_content, 'epub', format='md', outputfile=output_file, extra_args=['--embed-resources',f'--resource-path={temp_folder}', '--metadata', 'title=book title'])`的「book title」修改为电子书名称
6. 脚本运行完成后，epub电子书将生成在与脚本同级的目录下