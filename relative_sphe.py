# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:32:14 2020

@author: Neeraj R
"""

from numpy import deg2rad as d2r
from numpy import rad2deg as r2d
import conv_sphe_cart as conv


def rel_coord(s0, s1):
    s00 = list(s0)
    s10 = list(s1)
    s00[1] =  d2r(s00[1])
    s00[2] =  d2r(s00[2])
    s10[1] =  d2r(s10[1])
    s10[2] =  d2r(s10[2])
    
   
    c0 = conv.sphe_to_cart(s00[0], s00[1], s00[2])
    c1 = conv.sphe_to_cart(s10[0], s10[1], s10[2])
   
    
    c_rel = []
    for i in range(3):
        c_rel.append(c1[i] - c0[i])
    
   
    
    s_rel = conv.cart_to_sphe(c_rel[0], c_rel[1], c_rel[2])
    s_rel1 = s_rel[0], r2d(s_rel[1]), r2d(s_rel[2])
    
    
    
    return s_rel1
    
