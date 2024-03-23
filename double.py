from manim import *
import math
import numpy as np
from scipy.stats import norm


def make_box(label, bits, height=3, width=5, 
             color=WHITE, label_scale=1.25, 
             label_shift=.5, bits_scale=1.25, bits_shift=.5,):
    box = Rectangle(
        width=width,
        height=height,
        color=color
    )
    label = Tex(label).scale(label_scale).shift(UP*label_shift)
    bits = Tex(f"{bits} Bits").scale(bits_scale).shift(DOWN*bits_shift)
    return VGroup(box, label, bits)

class DoubleQuantization(Scene):
    def construct(self):


        all_objs = VGroup()
        og_weight = make_box("Weights", 16)

        self.play(FadeIn(og_weight))
        self.wait(2)
        self.play(og_weight.animate.scale(.5))
        self.play(og_weight.animate.shift(UP*3))
        all_objs.add(og_weight)


        self.wait(2)


        dot1 = Dot(og_weight.get_bottom(), fill_opacity=0)
        dot2 = Dot(og_weight.get_bottom(), fill_opacity=0)

        dot1.shift(DOWN*1.5+LEFT*1.5)
        dot2.shift(DOWN*1.5+RIGHT*1.5)

        line1 = Line(og_weight.get_bottom(), dot1.get_corner(UR))
        line2 = Line(og_weight.get_bottom(), dot2.get_corner(UL))

        self.play(Create(line1), Create(line2))
        all_objs.add(line1, line2)
        
        q_weights = make_box("Quantized Weights", 4, width=6).scale(.4).move_to(dot1, UP+RIGHT)
        const1 = make_box("Normalization Constant", 0.5, width=7).scale(.4).move_to(dot2, UP+LEFT)

        self.play(FadeIn(q_weights, const1))
        all_objs.add(q_weights, const1)


        self.wait(2)


        self.play(all_objs.animate.shift(LEFT*1.75))


        self.wait(1)


        dot3 = Dot(const1.get_bottom(), fill_opacity=0)
        dot4 = Dot(const1.get_bottom(), fill_opacity=0)

        dot3.shift(DOWN*1.5+LEFT*1.5)
        dot4.shift(DOWN*1.5+RIGHT*1.5)

        line3 = Line(const1.get_bottom(), dot3.get_corner(UR))
        line4 = Line(const1.get_bottom(), dot4.get_corner(UL))

        self.play(Create(line3), Create(line4))
        all_objs.add(line3, line4)
        
        q_const = make_box("Quantized Constant", 0.125, width=6).scale(.4).move_to(dot3, UP+RIGHT)
        const2 = make_box("Normalization Constant 2", 0.002, width=8).scale(.4).move_to(dot4, UP+LEFT)

        self.play(FadeIn(q_const, const2))
        all_objs.add(q_const, const2)
        # self.play(all_objs.animate.scale(.75))

        self.wait(2)
        self.play(FadeOut(all_objs))
        self.wait(5)
        self.play(FadeIn(all_objs))



        self.wait(2)

