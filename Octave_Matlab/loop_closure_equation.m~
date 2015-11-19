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


%Loop Closure Equation

%Input variables
w2=input('Enter angular velocity of link 2 (rad/s) : ');
w3=input('Enter angular velocity of link 3 (rad/s) : ');
w4=input('Enter angular velocity of link 4 (rad/s) : ');
a2=input('Enter angular acceeration of link 2 (rad/s^2) : ');
a3=input('Enter angular acceeration of link 3 (rad/s^2) : ');
a4=input('Enter angular acceeration of link 4 (rad/s^2) : ');

%Solving using the Loop closure equation and its derivatives
r2 = w4*(a3 + w3^2*1i) - w3*(a4 + w4^2*1i);
r3 = w2*(a4 + w4^2*1i) - w4*(a2 + w2^2*1i);
r4 = w3*(a2 + w2^2*1i) - w2*(a3 + w3^2*1i);
r1 = -r2 -r3 -r4;
r = [r1;r2;r3;r4];

%Link Lengths and Angles
r_len=abs(r);
r_ang=angle(r)*180/pi;
fprintf('Link one : Length = %f , Angle = %f \n',r_len(1),r_ang(1));
fprintf('Link two : Length = %f , Angle = %f \n',r_len(2),r_ang(2));
fprintf('Link three : Length = %f , Angle = %f \n',r_len(3),r_ang(3));
fprintf('Link four : Length = %f , Angle = %f \n',r_len(4),r_ang(4));
