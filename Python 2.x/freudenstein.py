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
from sympy import *
from numpy import *
import matplotlib.pyplot as plt

#x=Symbol('x');
n=3; x0=1; x_n=2; psi1=30; psi2=120; phi1=240; phi2=330; 
f1=raw_input('Enter Function : ');
f2=simplify(f1);
xf=zeros(n+2);
yf=zeros(n+2);
xf[0]=x0; yf[0]=f2.subs({'x':x0}).evalf();
xf[n+1]=x_n; yf[n+1]=f2.subs({'x':x_n}).evalf();
for k in range(3):
    xf[k+1]=(x0+x_n)/2.0 - (((x_n-x0)/2)*cos((2*(k+1)-1)*pi/(2*n)));
    yf[k+1]=f2.subs({'x':xf[k+1]}).evalf();
    
a2,b2=symbols('a2,b2');
eqs=(a2*x0 + b2 - psi1, a2*x_n + b2 - psi2); 
loo=solve(eqs,[b2,a2]);
a1=loo[a2]; b1=loo[b2];
eqs=(a2*yf[0] + b2 - phi1, a2*yf[n+1] + b2 - phi2);
loo=solve(eqs,[b2,a2]);
c1=loo[a2]; d1=loo[b2];
psi=zeros(n+2); phi=zeros(n+2);
psi[n-n]=psi1; psi[n+1]=psi2; phi[n-n]=phi1; phi[n+1]=phi2;
for k in range(3):
    psi[k+1]=a1*xf[k+1]+b1;
    phi[k+1]=c1*yf[k+1]+d1;

k11,k22,k33=symbols('k11,k22,k33');
eqn1=k11*cos(psi[1]*pi/180)+k22*cos(phi[1]*pi/180)+k33-cos((psi[1]-phi[1])*pi/180);
eqn2=k11*cos(psi[2]*pi/180)+k22*cos(phi[2]*pi/180)+k33-cos((psi[2]-phi[2])*pi/180);
eqn3=k11*cos(psi[3]*pi/180)+k22*cos(phi[3]*pi/180)+k33-cos((psi[3]-phi[3])*pi/180);
las=solve([eqn1,eqn2,eqn3],[k11,k22,k33]);
k1=las[k11];
k2=las[k22];
k3=las[k33];

r1=1;
r2=r1/k2;
r4=r1/k1;
r3=((2.0*r2*r4*k3)+r1**2.0+r2**2.0+r4**2.0)**0.5;

print r1
print r2
print r3
print r4

#plt.plot([0,1],[0,0],color='r');
#plt.hold('on')
#plt.plot([0,r2*cos(psi[n-n]*pi/180)],[0,r2*sin(psi[n-n]*pi/180)],color='r')
#plt.hold('on')
#plt.plot([1,r4*cos((phi[n-n]-180)*pi/180)],[0,r4*sin((phi[n-n]-180)*pi/180)],color='r')
#plt.plot([r2*cos(psi[n-n]*pi/180),r4*cos((phi[n-n]-180)*pi/180)],[r2*sin(psi[n-n]*pi/180),r4*sin((phi[n-n]-180)*pi/180)],color='r')

#plt.plot([0,r2*cos(psi[1]*pi/180),r4*cos((phi[1]-180)*pi/180),1],[0,r2*sin(psi[1]*pi/180),r4*sin((phi[1]-180)*pi/180),0],color='b')
col=['r','b','g','k','r'];
for k in range(5):
    plt.hold('on')
    plt.plot([0,r2*cos(psi[k]*pi/180),r4*cos((phi[k]-180)*pi/180),1],[0,r2*sin(psi[k]*pi/180),r4*sin((phi[k]-180)*pi/180),0],color=col[k]);
