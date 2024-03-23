from manim import *
import math
import numpy as np
from scipy.stats import norm




class NormalGraph(Scene):
    def construct(self):

        mean = 0
        std = .05
        lower_x = mean - std * 4
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


        lowppf = norm.cdf(upper_x, mean, std)
        upppf = norm.cdf(lower_x, mean, std)

        dist = norm.ppf(np.linspace(lowppf,upppf,17), mean, std)

        line_group = VGroup()
        rects = VGroup()

        color1 = [ManimColor(c) for c in [BLUE, GREEN]]
        colors1 = color_gradient(color1, 8)

        for x in range(len(dist)-1):
            x1 = dist[x]
            x2 = dist[x+1]
            y = func1.underlying_function((x2+x1)/2)

            if x <= 7:
                # y = func1.underlying_function((x2))
                color = colors1[x]
            else:
                # y = func1.underlying_function((x1))
                color = colors1[(8-x)-1]
            line = Line(
                        start=axes.c2p(x1, 0),
                        end=axes.c2p(x2, 0),
                        stroke_color=color,
                        stroke_width=5,
                    )
            

            p1 = VectorizedPoint().move_to(axes.c2p(x1, 0))
            p2 = VectorizedPoint().move_to(axes.c2p(x2, 0))
            p3 = VectorizedPoint().move_to(axes.c2p(x2, y))
            p4 = VectorizedPoint().move_to(axes.c2p(x1, y))
            points = VGroup(p1,p2,p3,p4)
            bar = Rectangle().replace(points, stretch=True)
            bar.set_style(
                fill_color= color,
                stroke_color= BLACK,
                stroke_width= 1,
                fill_opacity=1
            )
            line_group.add(line)
            rects.add(bar)
        
        # area1 = axes.get_riemann_rectangles(
        #     graph=func1, x_range=[lower_x, 0], dx=std/2, color=[BLUE, GREEN], input_sample_type="center"
        # )

        self.play(FadeTransformPieces(line_group, rects))

        all_objs = VGroup(line_group, rects, axes, func1)

        self.wait(2)
        self.play(FadeOut(all_objs))
        self.wait(5)
        self.play(FadeIn(all_objs))



        self.wait(2)

        self.wait(4)
