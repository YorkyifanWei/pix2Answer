import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import main


class LatexViewer:
    """
    LaTeX查看器类，用于显示和处理 LaTeX 公式。

    Attributes:
        master: tkinter 主窗口对象。
        image_path: 选择的图像文件路径。
        latex_input: 输入的 LaTeX 公式。
        latex_output: 处理后的 LaTeX 公式。
        external_image: 处理后的外部图像。
        process_image_callback: 图像处理回调函数。
    """
    def __init__(self, master):
        """
        初始化 LaTeX 查看器。

        参数:
            master: tkinter 主窗口对象。
        """
        self.restart_button = None
        self.show_image_button = None
        self.display_result_button = None
        self.display_formula_button = None
        self.choose_image_button = None
        self.master = master
        self.master.title("Pix2Answer")
        self.master.geometry("600x800")
        self.create_widgets()
        self.image_path = ""
        self.latex_input = ""
        self.latex_output = ""
        self.external_image = None
        self.process_image_callback = None

    def create_widgets(self):
        """
        创建界面组件。
        """
        self.choose_image_button = tk.Button(self.master, text="上传图片", command=self.open_file_dialog)
        self.choose_image_button.pack()

        self.display_formula_button = tk.Button(self.master, text="显示原始公式",
                                                command=self.show_latex_input, state=tk.DISABLED)
        self.display_formula_button.pack(side="left", expand=False, padx=3, pady=1)

        self.display_result_button = tk.Button(self.master, text="显示计算结果",
                                               command=self.show_latex_output, state=tk.DISABLED)
        self.display_result_button.pack(side="right", expand=False, padx=3, pady=1)

        self.show_image_button = tk.Button(self.master, text="显示结果图片",
                                           command=self.show_external_image, state=tk.DISABLED)
        self.show_image_button.pack(side="right", expand=False, padx=3, pady=1)

        self.restart_button = tk.Button(self.master, text="Return to start",
                                        command=self.restart_app)
        self.restart_button.pack(side="bottom", padx=10, pady=10, anchor="se")

    def open_file_dialog(self):
        """
        打开文件选择对话框，并显示所选图像。
        """
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((300, 300))  # 缩放图片
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.master, image=photo)
            label.image = photo
            label.pack(pady=2)
            self.process_image_callback = lambda latex_in, latex_out, external_image: (
                self.on_image_processed(latex_in, latex_out, external_image))
            main.process_image(self.image_path, self.process_image_callback)

    def on_image_processed(self, latex_input, latex_output, external_image):
        """
        处理图像完成后调用的函数，用于更新界面状态。

        参数:
            latex_input: 输入的 LaTeX 公式。
            latex_output: 处理后的 LaTeX 公式。
            external_image: 处理后的外部图像。
        """
        self.latex_input = latex_input
        self.latex_output = latex_output
        self.external_image = external_image
        self.update_ui_state(True)

    def update_ui_state(self, enable=True):
        """
        更新界面组件的状态（启用或禁用）。

        参数:
            enable: 是否启用组件，默认为 True。
        """
        state = tk.NORMAL if enable else tk.DISABLED
        self.display_formula_button.config(state=state)
        self.display_result_button.config(state=state)
        self.show_image_button.config(state=state)

    def show_latex_input(self):
        """
        显示输入的 LaTeX 公式。
        """
        if self.latex_input:
            label = tk.Label(self.master, text=self.latex_input)
            label.pack()

    def show_latex_output(self):
        """
        显示处理后的 LaTeX 公式。
        """
        if self.latex_output:
            label = tk.Label(self.master, text=self.latex_output)
            label.pack()

    def show_external_image(self):
        """
        显示处理后的外部图像。
        """
        if self.external_image:
            label = tk.Label(self.master, image=self.external_image)
            label.image = self.external_image
            label.pack()

    def restart_app(self):
        """
        重启应用程序。
        """
        self.master.destroy()
        import main
        main.main()


if __name__ == "__main__":
    root = tk.Tk()
    app = LatexViewer(root)
    root.mainloop()
