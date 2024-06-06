# 导入必要的库，用于图像处理和数学公式转换
import io
import os
from tempfile import NamedTemporaryFile

from latex2sympy2 import latex2latex
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from PIL import Image, ImageTk


def pix2answer(pix):
    """
    将像素值转换为LaTeX公式。

    参数:
    pix -- 字符串形式的像素值

    返回:
    answer -- 经过处理的LaTeX公式字符串
    """
    answer = latex2latex(pix)
    return answer


def answer2pix(answer):
    """
    将数学公式转换为图像像素。

    参数:
    answer -- LaTeX公式字符串

    返回:
    tk_image -- Tkinter兼容的图像对象
    """
    # 创建一个不带边框的空白图形
    fig = Figure()
    ax = fig.add_axes((0, 0, 1, 1), frameon=False, aspect=1)
    # 设置文本属性
    fontsize = 16
    color = "black"
    ax.text(0.5, 0.5, answer, fontsize=fontsize, color=color, ha="center", va="center",
            transform=ax.transAxes, usetex=True)

    # 使用临时文件保存图像
    # 使用with语句确保文件自动关闭
    with NamedTemporaryFile(dir=os.path.join(os.getcwd()), suffix=".png", delete=False) as temp_file:
        # 更新图形并保存为PNG图像
        plt.draw()
        plt.savefig(temp_file.name, format="png", dpi=300, bbox_inches="tight")

        # 打开图像文件并转换为Tkinter兼容的格式
        # 打开图像并立即关闭
        image = Image.open(temp_file.name)
        image.load()  # 确保图像数据完全加载
        # 立即转换为Tkinter兼容的图像格式，然后关闭原始PIL图像
        tk_image = ImageTk.PhotoImage(image=image)
        image.close()  # 显式关闭图像
        print("Image saved to", temp_file.name)

    # 尝试删除文件，此时临时文件应该已经关闭
    try:
        os.remove(temp_file.name)
    except OSError as e:
        print(f"Error: {e.strerror}. Unable to delete temporary file: {temp_file.name}")

    return tk_image
