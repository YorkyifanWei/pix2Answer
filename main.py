# 导入view模块，用于界面显示
import view
# 从PIL导入Image类，用于图像处理
from PIL import Image
# 导入tkinter模块，用于创建GUI应用程序
import tkinter as tk
# 从pix2tex的CLI导入LatexOCR类，用于OCR识别数学公式
from pix2tex.cli import LatexOCR
# 导入module模块，用于公式转换和图像生成
import module


def process_image(image_path, callback):
    """
    处理图像，将其转换为LaTeX代码并进行进一步处理。

    参数:
    image_path (str): 图像文件的路径。
    callback (function): 处理完成后的回调函数，接收LaTeX输入、输出及生成的图像作为参数。

    返回:
    无
    """
    # 打印处理开始信息

    # # 示例处理逻辑
    # print("Processing image:", image_path)

    # 打开图像文件
    img = Image.open(image_path)
    # 初始化OCR对象，用于识别图像中的LaTeX代码
    latex_ocr = LatexOCR()
    # 使用OCR识别图像中的LaTeX代码
    latex_input = latex_ocr(img)

    # # 打印识别得到的LaTeX输入
    # print("Latex input:", latex_input)

    # 使用module模块中的函数处理LaTeX输入，得到LaTeX输出
    latex_output = module.pix2answer(latex_input)

    # # 打印处理后的LaTeX输出
    # print("Latex output:", latex_output)

    # 根据LaTeX输出生成对应的图像
    external_image = module.answer2pix(latex_output)
    # 调用回调函数，传入LaTeX输入、输出及生成的图像
    # 通过回调函数通知view.py处理完成
    callback(latex_input, latex_output, external_image)

# 示例调用，实际中应由view.py调用
# process_image("path/to/image.jpg", update_view_callback)


def main():
    """
    主函数，创建GUI应用程序的入口。
    """
    # 创建根窗口
    root = tk.Tk()
    # 初始化界面视图
    app = view.LatexViewer(root)
    # 运行主事件循环
    root.mainloop()


if __name__ == "__main__":
    main()
