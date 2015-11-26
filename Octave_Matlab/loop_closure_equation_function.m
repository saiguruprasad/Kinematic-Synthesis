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

