from PIL import Image
from pix2tex.cli import LatexOCR

from sympy import symbols, Eq, solve, latex
from sympy.parsing.latex import parse_latex

import module

img = Image.open("D:/CodeProjects/Python/projects/pix2Answer/test.png")
latex_ocr = LatexOCR()
latex_input = latex_ocr(img)

answer = module.pix2answer(latex_input)

# print(answer)

# expr = parse_latex(latex_input)
# integral_result = expr.doit()
# latex_result = latex(integral_result)
#
# print(latex_result)
