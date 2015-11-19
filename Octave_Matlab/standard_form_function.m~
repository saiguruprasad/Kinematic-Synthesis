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


function [  ] = standard_form_function( d2,d3,gamma2,gamma3,phi2,phi3,psi2,psi3 )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
%Equation solving
%LH Dyad
Al=[exp(phi2*pi*1i/180)-1,exp(gamma2*pi*1i/180)-1;exp(phi3*pi*1i/180)-1,exp(gamma3*pi*1i/180)-1];
Bl=[d2;d3];
Cl=Al\Bl;

%RH Dyad

Ar=[exp(psi2*pi*1i/180)-1,exp(gamma2*pi*1i/180)-1;exp(psi3*pi*1i/180)-1,exp(gamma3*pi*1i/180)-1];
Br=[d2;d3];
Cr=Ar\Br;

l5=Cl(2)-Cr(2);
l6=Cl(1)-Cr(1)+l5;

linklenghts=[Cl(1);Cl(2);Cr(1);Cr(2);l5;l6];
ll_len=abs(linklenghts);
ll_ang=angle(linklenghts)*180/pi;

%Link Lengths
for i=1:6
    fprintf('Link %f : Length = %f , Angle = %f \n',i,ll_len(i),ll_ang(i));
end

end

