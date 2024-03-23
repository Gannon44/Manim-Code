from manim import *
import math
import numpy as np
from scipy.stats import norm


class Quantization(Scene):
    def construct(self):
        all_objs = VGroup()
        
        img_name = ""
        
        corona= ImageMobject(f"assets/{img_name}.png")
        corona.scale(1.2)
        corona.to_edge(RIGHT, buff=1)

        self.add(corona)