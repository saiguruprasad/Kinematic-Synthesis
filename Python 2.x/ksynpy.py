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
import cmath as cm
import numpy.linalg as lm
import numpy as np
import sympy as sp      
from __future__ import division
import matplotlib.pyplot as plt
     
def lpcs(w2,w3,w4,a2,a3,a4):
    r2 = w4*(complex(a3,w3**2)) - w3*(complex(a4,w4**2));
    r3 = w2*(complex(a4,w4**2)) - w4*(complex(a2,w2**2));
    r4 = w3*(complex(a2,w2**2)) - w2*(complex(a3,w3**2));
    r1 = -r2-r3-r4;
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
    return r1,r2,r3,r4;  
    
def thpos(d2,d3,gamma2,gamma3,psi2,psi3,phi2,phi3):
    Al=[[cm.exp(psi2*cm.pi*1j/180)-1,cm.exp(gamma2*cm.pi*1j/180)-1],[cm.exp(psi3*cm.pi*1j/180)-1,cm.exp(gamma3*cm.pi*1j/180)-1]];
    Bl=[[d2],[d3]];
    Cl=lm.solve(Al,Bl);
    l1=Cl[0]; l2=Cl[1];
    Ar=[[cm.exp(phi2*cm.pi*1j/180)-1,cm.exp(gamma2*cm.pi*1j/180)-1],[cm.exp(phi3*cm.pi*1j/180)-1,cm.exp(gamma3*cm.pi*1j/180)-1]];
    Br=[[d2],[d3]];
    Cr=lm.solve(Ar,Br);
    l3=Cr[0]; l4=Cr[1];
    l5=l2-l4;
    l6=l1+l5-l3;
    return l1,l2,l3,l4,l5,l6;
    
def frst(f1,x0,x_n,n,psi1,psi2,phi1,phi2):
    f2=sp.simplify(f1);
    xf=np.zeros(n+2);
    yf=np.zeros(n+2);
    xf[0]=x0; yf[0]=f2.subs({'x':x0}).evalf();
    xf[n+1]=x_n; yf[n+1]=f2.subs({'x':x_n}).evalf();
    for k in range(3):
        xf[k+1]=(x0+x_n)/2.0 - (((x_n-x0)/2.0)*np.cos((2*(k+1)-1)*np.pi/(2*n)));
        yf[k+1]=f2.subs({'x':xf[k+1]}).evalf();
    
    a2,b2=sp.symbols('a2,b2');
    eqs=(a2*x0 + b2 - psi1, a2*x_n + b2 - psi2); 
    loo=sp.solve(eqs,[b2,a2]);
    a1=loo[a2]; b1=loo[b2];
    eqs=(a2*yf[0] + b2 - phi1, a2*yf[n+1] + b2 - phi2);
    loo=sp.solve(eqs,[b2,a2]);
    c1=loo[a2]; d1=loo[b2];
    psi=np.zeros(n+2); phi=np.zeros(n+2);
    psi[n-n]=psi1; psi[n+1]=psi2; phi[n-n]=phi1; phi[n+1]=phi2;
    for k in range(3):
        psi[k+1]=a1*xf[k+1]+b1;
        phi[k+1]=c1*yf[k+1]+d1;
    
    k11,k22,k33=sp.symbols('k11,k22,k33');
    eqn1=k11*np.cos(psi[1]*np.pi/180)+k22*np.cos(phi[1]*np.pi/180)+k33-np.cos((psi[1]-phi[1])*np.pi/180);
    eqn2=k11*np.cos(psi[2]*np.pi/180)+k22*np.cos(phi[2]*np.pi/180)+k33-np.cos((psi[2]-phi[2])*np.pi/180);
    eqn3=k11*np.cos(psi[3]*np.pi/180)+k22*np.cos(phi[3]*np.pi/180)+k33-np.cos((psi[3]-phi[3])*np.pi/180);
    las=sp.solve([eqn1,eqn2,eqn3],[k33,k22,k11]);
    k1=las[k11];
    k2=las[k22];
    k3=las[k33];

    r1=1;
    r2=r1/k2;
    r4=r1/k1;
    r3=((2*r2*r4*k3)+r1**2+r2**2+r4**2)**0.5;
    col=['r','b','g','k','r'];
	for k in range(5):
    		plt.hold('on')
    		plt.plot([0,r2*cos(psi[k]*pi/180),r4*cos((phi[k]-180)*pi/180),1],[0,r2*sin(psi[k]*pi/180),r4*sin((phi[k]-180)*pi/180),0],color=col[k]);
    return r1,r2,r3,r4,psi,phi;
	
