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
import sympy as sp
import numpy as np

def chebyshev_spacing(f1,x0,x_n,n,psi1,psi2,phi1,phi2):
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
        
    return xf,yf,psi,phi;