function [  ] = freudenstein_equation_function( f1,x0,x_n,n,psi1,psi2,phi1,phi2 )
%UNTITLED7 Summary of this function goes here
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

%Equation solving using Freudenstein Equation
syms k11 k22 k33
eqn1 = k11*cosd(psi(2)) + k22*cosd(phi(2)) + k33 == cosd(psi(2)-phi(2));
eqn2 = k11*cosd(psi(3)) + k22*cosd(phi(3)) + k33 == cosd(psi(3)-phi(3));
eqn3 = k11*cosd(psi(4)) + k22*cosd(phi(4)) + k33 == cosd(psi(4)-phi(4));
[k1,k2,k3]=solve([eqn1,eqn2,eqn3]);

%Link lenghts
r1=1;
r4=1/double(k1);
r2=1/double(k2);
r3=(2*r2*r4*double(k3))+r4^2+r2^2+r1^2;
fprintf('Link one : %f \n',r1);
fprintf('Link two : %f \n',r2);
fprintf('Link three : %f \n',r3);
fprintf('Link four : %f \n',r4);
end

