%{
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
%}

function [ xf,yf,psi,phi ] = chebyshev_spacing( f1,x0,x_n,n,psi1,psi2,phi1,phi2 )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

syms x

xe=zeros(1,n); xf=zeros(1,n+2);
y=zeros(1,n); yf=zeros(1,n+2);
f2=symfun(f1,x);
y0=f2(x0);
y_n=f2(x_n);
xf(1)=x0; yf(1)=y0;
for k=1:n
    xf(k+1)=(x0+x_n)/2 - (((x_n-x0)/2)*cos((2*k-1)*pi/(2*n)));
    yf(k+1)=f2(xf(k+1));
end
xf(k+2)=x_n; yf(k+2)=y_n;

%Angles at the precision points
syms a1 b1
eqn1 = a1*x0 + b1 == psi1;
eqn2 = a1*x_n + b1 == psi2;
[a,b]=solve([eqn1, eqn2]);
eqn1 = a1*y0+b1 == phi1;
eqn2 = a1*y_n+b1 == phi2;
[c,d]=solve([eqn1, eqn2]);
psi=zeros(1,n+2); phi=zeros(1,n+2);
psi(1)=psi1; psi(n+2)=psi2; phi(1)=phi1; phi(n+2)=phi2;
for k=1:n
    psi(k+1)=a*xf(k+1)+b;
    phi(k+1)=c*yf(k+1)+d;
end

end

