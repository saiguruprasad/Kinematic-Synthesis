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

from __future__ import division
import numpy as np
import cmath as cm
import numpy.linalg as lm

d2=eval(raw_input('Enter the first position vector : '));
d3=eval(raw_input('Enter the second position vector : '));
d4=eval(raw_input('Enter the third position vector : '));
a2=eval(raw_input('Enter the first angle difference of output linkage : '));
a3=eval(raw_input('Enter the second angle difference of output linkage : '));
a4=eval(raw_input('Enter the third angle difference of output linkage : '));
b2=eval(raw_input('Enter a value for the input angle : '));

delta2=((cm.exp(1j*a3*cm.pi/180)-1)*d4) - ((cm.exp(1j*a4*cm.pi/180)-1)*d3);
delta3=-1*(((cm.exp(1j*a2*cm.pi/180)-1)*d4) - ((cm.exp(1j*a4*cm.pi/180)-1)*d2));
delta4=((cm.exp(1j*a2*cm.pi/180)-1)*d3) - ((cm.exp(1j*a3*cm.pi/180)-1)*d2);
delta1=-delta2-delta3-delta4;
delta=delta1+(delta2*cm.exp(1j*b2*cm.pi/180));

ctheta3=((np.abs(delta4)**2-np.abs(delta3)**2-np.abs(delta)**2)/(2*np.abs(delta3)*np.abs(delta)));
stheta3=np.absolute((1-ctheta3**2)**0.5);
theta3=np.arctan2(stheta3,ctheta3);
b3=np.angle(delta)+theta3-np.angle(delta3);
theta3d=(2*np.pi)-theta3;
b3d=np.angle(delta)+theta3d-np.angle(delta3);

ctheta4=((np.abs(delta3)**2-np.abs(delta4)**2-np.abs(delta)**2)/(2*np.abs(delta4)*np.abs(delta)));
stheta4=np.absolute((1-ctheta4**2)**0.5);
theta4=np.arctan2(stheta4,ctheta4);
b4=np.angle(delta)-theta4-np.angle(delta4);
b4d=np.angle(delta)+theta4-np.angle(delta4)+np.pi;

Al=[[cm.exp(b2*cm.pi*1j/180)-1,cm.exp(a2*cm.pi*1j/180)-1],[cm.exp(b3*cm.pi*1j/180)-1,cm.exp(a3*cm.pi*1j/180)-1]];
Bl=[[d2],[d3]];
Cl=lm.solve(Al,Bl);
W=Cl[0]; Z=Cl[1];
r=[W,Z];
r_l=np.absolute(r);
r_ar=np.angle(r);
r_a=np.rad2deg(r_ar);
print 'Link W Length :',r_l[0],'Angle :',r_a[0]
print 'Link Z Length :',r_l[1],'Angle :',r_a[1]