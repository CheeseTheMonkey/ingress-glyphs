==============
Ingress Glyphs
==============

I wanted an easy programatical way to represent ingress glyphs so I whipped up a basic python script.

The Calibration Grid has eleven vertices, numbered 0 through 10, top to bottom, left to right.

So a glyph can be represented as a dictionary with keys "name" and "vertices", vertices being a list of the vertices on the calibration grid that the glyph connects
