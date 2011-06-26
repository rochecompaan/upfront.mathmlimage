============
Introduction
============

Easily convert MathML to an image in PNG format.

>>> from upfront.mathmlimage import convert
>>> mathml = "<math title="E = mc^2"><mi>E</mi><mo>=</mo><mi>m</mi><msup><mi>c</mi><mn>2</mn></msup></math>"
>>> image_data = convert(mathml)
>>> f = open('emc2.png')
>>> f.write(image_data)
>>> f.close()

This package uses SVGMath written by Nikolai Grigoriev
(http://grigoriev.ru/svgmath/) to convert MathML to SVG and
ImageMagick's "convert" command to convert SVG to PNG.
