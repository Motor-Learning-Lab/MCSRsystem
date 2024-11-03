# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:17:09 2024

@author: Zhuoxin
"""
import kineticstoolkit.lab as ktk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the C3D fiel into a Dictionary
Subject2_R1_path = r"../MCrawdata/Subject2/Ex_V2_R1_S20001.c3d"
Subject2_R2_path = r"../MCrawdata/Subject2/Ex_V2_R2_S20002.c3d"


# Read the C3D fiel into a Dictionary
Subject2_R1 = ktk.read_c3d(Subject2_R1_path)['Points']
Subject2_R2 = ktk.read_c3d(Subject2_R2_path)['Points']


Subject2_R1 = Subject2_R1.ui_edit_events()