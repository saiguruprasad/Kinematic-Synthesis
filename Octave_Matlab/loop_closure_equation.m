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