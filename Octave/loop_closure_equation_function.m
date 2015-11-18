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


function [  ] = loop_closure_equation_function( w2,w3,w4,a2,a3,a4 )
%UNTITLED8 Summary of this function goes here
%   Detailed explanation goes here

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
end

