# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:58:19 2015

@author: Sai Guruprasad & G V Balakrishna
"""
import cmath as cm
import numpy.linalg as lm
import numpy as np
import sympy as sp

if __name__=="__main__":
	import sys
	help(int(sys.argv[1]))

def help(n)
	print("Refer to documentation on how to use the following program for analysis")
	print("1. Loop Closure Equation - from function_file import loop_closure \n loop_closure(ang_vel2,ang_vel3,ang_vel4,ang_acc2,ang_acc3,ang_acc4)")

def loop_closure(w2,w3,w4,a2,a3,a4):
    r2 = w4*(complex(a3,w3**2)) - w3*(complex(a4,w4**2));
    r3 = w2*(complex(a4,w4**2)) - w4*(complex(a2,w2**2));
    r4 = w3*(complex(a2,w2**2)) - w2*(complex(a3,w3**2));
    r1 = -r2-r3-r4;
    return r1,r2,r3,r4;  
    
def three_position(d2,d3,gamma2,gamma3,psi2,psi3,phi2,phi3):
    Al=[[cm.exp(psi2*cm.np.pi*1j/180)-1,cm.exp(gamma2*cm.np.pi*1j/180)-1],[cm.exp(psi3*cm.np.pi*1j/180)-1,cm.exp(gamma3*cm.np.pi*1j/180)-1]];
    Bl=[[d2],[d3]];
    Cl=lm.solve(Al,Bl);
    l1=Cl[0]; l2=Cl[1];
    Ar=[[cm.exp(phi2*cm.np.pi*1j/180)-1,cm.exp(gamma2*cm.np.pi*1j/180)-1],[cm.exp(phi3*cm.np.pi*1j/180)-1,cm.exp(gamma3*cm.np.pi*1j/180)-1]];
    Br=[[d2],[d3]];
    Cr=lm.solve(Ar,Br);
    l3=Cr[0]; l4=Cr[1];
    l5=l2-l4;
    l6=l1+l5-l3;
    return l1,l2,l3,l4,l5,l6;
    
def freudenstein(f1,x0,x_n,n,psi1,psi2,phi1,phi2):
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
    return r1,r2,r3,r4,psi,phi;


