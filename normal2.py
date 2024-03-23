from manim import *
import math
import numpy as np
from scipy.stats import norm




class NormalGraph(Scene):
    def construct(self):
        all_objs = VGroup()
        mean = 0
        std = .05
        lower_x = mean - std * 8
        upper_x = mean + std * 4

        f = lambda x: norm.pdf(x, mean, std)
        
        # create the axes and the curve
        axes = Axes(
            x_range=[lower_x, upper_x, std/2], 
            y_range=[0, f(mean) + .1, (f(mean) + .1) / 4],
            tips=False,
        )


        func1 = axes.plot(f, x_range=[lower_x,upper_x], color=RED)

        func1.set_z_index(1)

        # self.add(axes, func1) #, func1_lab)
        self.play(FadeIn(axes), run_time=1, rate_func=rate_functions.linear)

        self.wait(0.5)

        self.play(Create(func1), run_time=1.25, rate_func=rate_functions.ease_in_out_back)

        self.wait(2)
        all_objs.add(axes, func1)

        line1 = VGroup()
        for x in np.arange(lower_x, upper_x, (upper_x-lower_x)/16):
            line = Line(
                        start=axes.c2p(x, 0),
                        end=axes.c2p(x+std/2, 0),
                        stroke_color=BLUE,
                        stroke_width=5,
                    )
            line1.add(line)

        area1 = axes.get_riemann_rectangles(
            graph=func1, x_range=[lower_x, upper_x], dx=(upper_x-lower_x)/16, color=[BLUE, GREEN, BLUE], input_sample_type="center"
        )

        line1.set_opacity(0)
        self.play(FadeTransformPieces(line1, area1))

        all_objs.add(area1)

        self.wait(2)
        self.play(FadeOut(all_objs))
        self.wait(5)
        self.play(FadeIn(all_objs))



        self.wait(2)

        self.wait(4)
