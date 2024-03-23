from manim import *
import math
import numpy as np




class SinGraph(Scene):
    def construct(self):
        # create the axes and the curve
        axes = Axes(
            x_range=[-PI/4, 9*PI/4, PI/4], 
            y_range=[-1.25, 1.25, .5],
            tips=False,
        )
        #.to_edge(DL, buff=0.25)
        
        # Add x-axis labels at multiples of PI/4
        x_labels = VGroup()
        for x in np.arange(-1, 9, 1):
            if x % 2 and abs(x) != 1:
                label = MathTex("\\frac{%d\pi}{4}" % x)
            elif x == 0 or x < 0:
                label = MathTex("")
            elif x % 2:
                label = MathTex("\\frac{\pi}{4}")
            elif x == 2:
                label = MathTex("\\frac{\pi}{2}")
            elif x == 4:
                label = MathTex("\pi}")
            elif x == 8:
                label = MathTex("2\pi}")
            else:
                label = MathTex("\\frac{%d\pi}{2}" % (x//2))

            if x < (5*PI)/4:
                label.next_to(axes.c2p((x*PI)/4, 0), DOWN)
            else:
                label.next_to(axes.c2p((x*PI)/4, 0), UP)
            x_labels.add(label)
        

        y_labels = VGroup()
        for x in np.arange(-1,1.1,.5):
            if x == 0: 
                label = MathTex("")
            else:
                label = MathTex(x)
            label.next_to(axes.c2p(0, x), LEFT)
            y_labels.add(label)


        #axes.add(x_labels, y_labels)

        func1 = axes.plot(lambda x: np.sin(x), x_range=[0, 2 * PI], color=BLUE)
        func1_lab = (
            MathTex("y={sin}({x})").scale(0.8).next_to(func1, UR, buff=0).set_color(BLUE)
        )

        # self.add(axes, func1) #, func1_lab)
        self.play(Create(axes), run_time=1, rate_func=rate_functions.linear)

        self.wait(0.5)

        self.play(Create(func1), run_time=1.25, rate_func=rate_functions.ease_in_out_back)
        self.play(FadeIn(func1_lab), run_time=.2, rate_func=rate_functions.linear)

        self.wait(2)

        self.play(FadeIn(x_labels), run_time=.7, rate_func=rate_functions.linear)
        self.play(FadeIn(y_labels), run_time=.7, rate_func=rate_functions.linear)

        self.wait()


        # Create Gray Sampling Lines

        gray_lines = VGroup()
        red_dots = VGroup()
        for k in np.arange(0, 2.1*PI, PI/4):

            if k%PI == 0:
                dot = Dot().set_color(RED).move_to(axes.c2p(k, func1.underlying_function(k)))
                self.wait(.3)
                self.add(dot)
                red_dots.add(dot)
                self.wait(.6)

            else:
                line1 = DashedLine(
                    start=axes.c2p(k, 0),
                    end=axes.c2p(k, func1.underlying_function(k)),
                    stroke_color=LIGHT_GRAY,
                    stroke_width=5,
                )
                line2 = Line(
                    start=axes.c2p(k, 0),
                    end=axes.c2p(k, func1.underlying_function(k)),
                    stroke_color=GRAY,
                    stroke_width=10,
                )

                dot = Dot().set_color(RED).move_to(axes.c2p(k, func1.underlying_function(k)))

                self.play(Create(line1), run_time=.6, rate_func=rate_functions.linear)
                self.play(Create(line2), run_time=.3, rate_func=rate_functions.ease_in_back)
                self.remove(line1)
                self.add(dot)
                gray_lines.add(line2)
                red_dots.add(dot)

        self.wait(3)

        self.play(FadeOut(x_labels,y_labels), run_time=.3)
        
        self.wait(3)

        self.play(FadeOut(gray_lines), run_time=.3)
        self.wait(.5)
        self.play(FadeOut(func1, func1_lab), run_time=.3)

        self.wait(3)

        # Create Yellow Quantize Lines

        quantized_lines = VGroup()
        quantized_labels = VGroup()
        qmap = ["11", "10", "01", "00"]
        idx=0
        for x in np.arange(3*PI/4, 7*PI/4, PI/4):
            y = func1.underlying_function(x)
            line = DashedLine(
                        start=axes.c2p(0, y),
                        end=axes.c2p(9*PI/4, y),
                        stroke_color=YELLOW_D,
                        stroke_width=5,
                    )
            quantized_lines.add(line)

        
            label = Tex(qmap[idx])
            label.next_to(axes.c2p(0, y), LEFT)
            idx +=1
            quantized_labels.add(label)
        self.play(Create(quantized_lines), run_time=1.5, rate_func=rate_functions.ease_in_out_back)
        self.wait(.8)
        self.play(FadeIn(quantized_labels), run_time=.7, rate_func=rate_functions.linear)

        self.wait(2)

        # Create Digital Graph

        digital_graph = VGroup()
        for idx, x in enumerate(np.arange(0, 2.1*PI, PI/4)):
            if x > 0 and x != PI/2:
                y1 = min(func1.underlying_function(x-(PI/4)), math.sqrt(2)/2)
                y2 = min(func1.underlying_function(x), math.sqrt(2)/2)
                vert_line = Line(
                    start=axes.c2p(x, y1),
                    end=axes.c2p(x, y2),
                    stroke_color=RED,
                    stroke_width=10,
                )
                self.play(Create(vert_line),run_time=.5)
                digital_graph.add(vert_line)

            y = min(func1.underlying_function(x), math.sqrt(2)/2)
            hor_line = Line(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x+(PI/4), y),
                    stroke_color=RED,
                    stroke_width=10,
                )
            self.play(Create(hor_line), run_time=.5)
            self.play(FadeOut(red_dots[idx]))
            digital_graph.add(hor_line)
    
        self.wait(2)

        digital_graph.add(quantized_labels, quantized_lines)
        self.play(FadeOut(digital_graph))

        self.wait(2)

        digital_graph3 = VGroup()
        for x in np.arange(0, 2.1*PI, PI/8):
            if x > 0 or not (x >= 3*PI/8 and x <= 5*PI/8):
                y1 = min(func1.underlying_function(x-(PI/8)), math.sqrt(2+math.sqrt(2))/2)
                y2 = min(func1.underlying_function(x), math.sqrt(2+math.sqrt(2))/2)
                vert_line = Line(
                    start=axes.c2p(x, y1),
                    end=axes.c2p(x, y2),
                    stroke_color=RED,
                    stroke_width=10,
                )
                digital_graph3.add(vert_line)

            y = min(func1.underlying_function(x), math.sqrt(2+math.sqrt(2))/2)
            hor_line = Line(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x+(PI/8), y),
                    stroke_color=RED,
                    stroke_width=10,
                )
            digital_graph3.add(hor_line)

        
        
        qmap = ["111","110","101","100","011","010","001","000"]
        idx=0
        for x in np.arange(5*PI/8, .02+6*PI/4, PI/8):
            y = func1.underlying_function(x)
            line = DashedLine(
                        start=axes.c2p(0, y),
                        end=axes.c2p(9*PI/4, y),
                        stroke_color=YELLOW_D,
                        stroke_width=5,
                    )
            digital_graph3.add(line)

            
            label = Tex(qmap[idx])
            label.next_to(axes.c2p(0, y), LEFT)
            idx +=1
            digital_graph3.add(label)
        self.play(FadeIn(digital_graph3), run_time=1.5, rate_func=rate_functions.ease_in_out_back)

        self.wait(2)
        self.play(FadeOut(digital_graph3))        
        self.wait(2)
        self.play(FadeIn(digital_graph))        
        self.wait(2)
        self.play(FadeOut(digital_graph))

        self.wait(2)