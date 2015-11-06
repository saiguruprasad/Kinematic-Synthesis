"""
Copyright (C) 2015 Sai Guruprasad Jakkala, G V Balakrishna

This program is free software: you can redistribute it 
and/or modify it under the terms of the GNU General 
Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any 
later version. This program is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the 
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License 
along with this program. If not, see http://www.gnu.org/licenses/.
"""

from ksynpy import thpos
import cmath as cm
import numpy as np

d2=eval(raw_input('Enter the first position vector : '));
d3=eval(raw_input('Enter the second position vector : '));
gamma2=eval(raw_input('Enter the differnce of couple angle between position 1 & 2 : '));
gamma3=eval(raw_input('Enter the differnce of couple angle between position 1 & 3 : '));
psi2=eval(raw_input('Enter the differnce of crank angle between position 1 & 2 : '));
psi3=eval(raw_input('Enter the differnce of crank angle between position 1 & 3 : '));
phi2=eval(raw_input('Enter the differnce of rocker angle between position 1 & 2 : '));
phi3=eval(raw_input('Enter the differnce of rocker angle between position 1 & 3 : '));
[r1,r2,r3,r4,r5,r6]=thpos(d2,d3,gamma2,gamma3,psi2,psi3,phi2,phi3);
r=[r1,r2,r3,r4,r5,r6];
r_l=np.absolute(r);
r_ar=np.angle(r);
r_a=np.rad2deg(r_ar);
print 'Link 1 Length :',r_l[0],'Angle :',r_a[0]
print 'Link 2 Length :',r_l[1],'Angle :',r_a[1]
print 'Link 3 Length :',r_l[2],'Angle :',r_a[2]
print 'Link 4 Length :',r_l[3],'Angle :',r_a[3]
print 'Link 5 Length :',r_l[4],'Angle :',r_a[4]
print 'Link 6 Length :',r_l[5],'Angle :',r_a[5]
