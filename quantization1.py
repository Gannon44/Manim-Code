from manim import *
import math
import numpy as np
from scipy.stats import norm


class Quantization(Scene):
    def construct(self):

        quant = VGroup()
        title = Tex("define Quantization( tensor ):").scale(.7).to_corner(UL).shift(DOWN*.5)
        self.play(FadeIn(title), run_time=.5)

        step1 = Tex("1. Normalize tensor to range [-1, 1]").scale(.7).to_corner(UL).shift(DOWN*1+RIGHT*.5)
        self.play(FadeIn(step1), run_time=.5)
        self.wait(2)

        step1a = Tex("a. Let N = the absmax of tensor").scale(.7).to_corner(UL).shift(DOWN*1.5+RIGHT*1)
        step1b = Tex("b. Divide all values in tensor by N").scale(.7).to_corner(UL).shift(DOWN*2+RIGHT*1)

        self.play(FadeIn(step1a), run_time=.5)
        self.wait(1)
        self.play(FadeIn(step1b), run_time=.5)
        self.wait(2)

        step2 = Tex("2. Find closest map value").scale(.7).to_corner(UL).shift(DOWN*2.5+RIGHT*.5)
        self.play(FadeIn(step2), run_time=.5)
        self.wait(2)

        step3 = Tex("3. Map to the quantized key").scale(.7).to_corner(UL).shift(DOWN*3+RIGHT*.5)
        self.play(FadeIn(step3), run_time=.5)
        self.wait(2)
        
        step4 = Tex("4. Return tensor").scale(.7).to_corner(UL).shift(DOWN*3.5+RIGHT*.5)
        self.play(FadeIn(step4), run_time=.5)
        self.wait(2)

        quant.add(title, step1, step1a, step1b, step2, step3, step4)
        # self.play(quant.animate.scale(.75))
        # self.play(quant.animate.to_edge(LEFT))



        dequant = VGroup()
        dtitle = Tex("define Dequantization( tensor ):").scale(.7).move_to(title.get_edge_center(RIGHT), LEFT).shift(RIGHT*2.5)
        self.play(FadeIn(dtitle), run_time=.5)
        self.wait(1)

        dstep1 = Tex("1. Map to the value").scale(.7).move_to(title.get_edge_center(RIGHT), LEFT).shift(DOWN*.5+RIGHT*3)
        self.play(FadeIn(dstep1), run_time=.5)
        self.wait(2)

        dstep2 = Tex("2. Denormalize tensor").scale(.7).move_to(title.get_edge_center(RIGHT), LEFT).shift(DOWN*1+RIGHT*3)
        self.play(FadeIn(dstep2), run_time=.5)
        self.wait(2)

        dstep2a = Tex("a. Multiply all values in tensor by N").scale(.7).move_to(title.get_edge_center(RIGHT), LEFT).shift(DOWN*1.5+RIGHT*3.5)
        self.play(FadeIn(dstep2a), run_time=.5)
        self.wait(2)        
        
        dstep3 = Tex("3. Return tensor").scale(.7).move_to(title.get_edge_center(RIGHT), LEFT).shift(DOWN*2+RIGHT*3)
        self.play(FadeIn(dstep3), run_time=.5)
        self.wait(2)

        dequant.add(dtitle, dstep1, dstep2, dstep2a, dstep3)

        self.wait(2)
        self.play(FadeOut(quant, dequant))
        self.wait(5)
        self.play(FadeIn(quant, dequant))



        self.wait(2)

