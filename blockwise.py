from manim import *
import math
import numpy as np
from scipy.stats import norm




class Blockwise(Scene):
    def construct(self):

        class NormalEx(VGroup):
            def __init__(self, mean=0, std=.05):
                super().__init__()
                
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


                self.add(axes, func1)

                self.f = f
                self.axes = axes
                self.plot = func1


                area1 = axes.get_riemann_rectangles(
                    graph=func1, x_range=[lower_x, 0], dx=std/2, color=[BLUE, GREEN], input_sample_type="center"
                )

                area2 = axes.get_riemann_rectangles(
                    graph=func1, x_range=[0, upper_x], dx=std/2, color=[GREEN, BLUE], input_sample_type="center"
                )

                self.add(area1,area2)


        class OutlierEx(VGroup):
            def __init__(self, mean=0, std=.05):
                super().__init__()
                
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


                self.add(axes, func1)

                self.f = f
                self.axes = axes
                self.plot = func1


                area1 = axes.get_riemann_rectangles(
                    graph=func1, x_range=[lower_x, upper_x], dx=(upper_x-lower_x)/16, color=[BLUE, GREEN], input_sample_type="center"
                )
                
                self.add(area1)


        # Create instances of NormalEx and OutlierEx
        normal_graph = NormalEx()
        outlier_graph = OutlierEx()

        # Position the outlier graph at the top right

        graphs = VGroup()

        self.add(outlier_graph)
        self.wait(2)
        self.play(outlier_graph.animate.scale(.3))
        self.wait(2)
        self.play(outlier_graph.animate.shift(RIGHT * 4 + UP * 2.25))

        normal_graph.scale(0.3)
        self.play(FadeIn(normal_graph))
        graphs.add(outlier_graph, normal_graph)

        rt = .9*.9
        for x, y in [(0, 2.25),(-4, 2.25),(-4, 0),(-4, -2.25),(0, -2.25),(4, -2.25),(4,0)]:
            new = normal_graph.copy()
            self.play(new.animate.shift(RIGHT * x + UP * y), run_time=1*rt)
            rt *= .9
            graphs.add(new)

        # Create copies of the NormalEx graph and position them

        self.wait(2)
        self.play(FadeOut(graphs))
        self.wait(5)
        self.play(FadeIn(graphs))
        self.wait(2)