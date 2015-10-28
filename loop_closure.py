# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:16:05 2015

@author: Sai Guruprasad
"""

from function_file import loop_closure
import cmath as cm
import matplotlib.pyplot as plt
import numpy as np

w2=eval(raw_input('Angular Velocity of link 2 : '));
w3=eval(raw_input('Angular Velocity of link 3 : '));
w4=eval(raw_input('Angular Velocity of link 4 : '));
a2=eval(raw_input('Angular Acceleration of link 2 : '));
a3=eval(raw_input('Angular Acceleration of link 3 : '));
a4=eval(raw_input('Angular Acceleration of link 4 : '));
[r1,r2,r3,r4]=loop_closure(w2,w3,w4,a2,a3,a4);
r1_l=abs(r1); r1_a=cm.phase(r1)*180/cm.pi;
r2_l=abs(r2); r2_a=cm.phase(r2)*180/cm.pi;
r3_l=abs(r3); r3_a=cm.phase(r3)*180/cm.pi;
r4_l=abs(r4); r4_a=cm.phase(r4)*180/cm.pi;
print 'Link 1 Length :',r1_l,'Angle :',r1_a
print 'Link 2 Length :',r2_l,'Angle :',r2_a
print 'Link 3 Length :',r3_l,'Angle :',r3_a
print 'Link 4 Length :',r4_l,'Angle :',r4_a

a=180-r1_a;
plt.hold('on')
plt.plot([0,r2_l*np.cos((a+r2_a)*np.pi/180),r3_l*np.cos((a+r3_a)*np.pi/180),r1_l*np.cos((a+r4_a)*np.pi/180)],[0,r2_l*np.sin((a+r2_a)*np.pi/180),r3_l*np.sin((a+r3_a)*np.pi/180),0],color='k');
#ax.annotate('A',(r2_l*np.cos((a+r2_a)*np.pi/180),r2_l*np.sin((a+r2_a)*np.pi/180)))