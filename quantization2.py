from manim import *
import math
import numpy as np
from scipy.stats import norm


class Quantization(Scene):
    def construct(self):
        all_objs = VGroup()
        