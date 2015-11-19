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
d2=input('Enter the first position vector : ');
d3=input('Enter the second position vector : ');
d4=input('Enter the third position vector : ');
a2=input('Enter the first angle difference of output linkage : ');
a3=input('Enter the second angle difference of output linkage : ');
a4=input('Enter the third angle difference of output linkage : ');
b2=input('Enter a value for the input angle : ');

delta2=((exp(1i*a3*pi/180)-1)*d4) - ((exp(1j*a4*pi/180)-1)*d3);
delta3=-1*(((exp(1i*a2*pi/180)-1)*d4) - ((exp(1i*a4*pi/180)-1)*d2));
delta4=((exp(1i*a2*pi/180)-1)*d3) - ((exp(1i*a3*pi/180)-1)*d2);
delta1=-delta2-delta3-delta4;
delta=delta1+(delta2*exp(1i*b2*pi/180));

ctheta3=((abs(delta4)^2-abs(delta3)^2-abs(delta)^2)/(2*abs(delta3)*abs(delta)));
stheta3=abs((1-ctheta3^2)^0.5);
theta3=atan2(stheta3,ctheta3);
b3=angle(delta)+theta3-angle(delta3);
theta3d=(2*pi)-theta3;
b3d=angle(delta)+theta3d-angle(delta3);

ctheta4=((abs(delta3)^2-abs(delta4)^2-abs(delta)^2)/(2*abs(delta4)*abs(delta)));
stheta4=abs((1-ctheta4^2)^0.5);
theta4=atan2(stheta4,ctheta4);
b4=angle(delta)-theta4-angle(delta4);
b4d=angle(delta)+theta4-angle(delta4)+pi;

Al=[exp(b2*pi*1i/180)-1,exp(a2*pi*1i/180)-1;exp(b3*pi*1i/180)-1,exp(a3*pi*1i/180)-1];
Bl=[d2;d3];
Cl=Al\Bl;
W=Cl(1); Z=Cl(2);

fprintf('Link W : Length=%f, Angle=%f \n',abs(W),angle(W));
fprintf('Link Z : Length=%f, Angle=%f \n',abs(Z),angle(Z));
