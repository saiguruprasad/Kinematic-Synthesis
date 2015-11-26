% Three position synthesis

%Taking the two delta terms first
d2=input('Enter the first position vector : ');
d3=input('Enter the second position vector : ');

%Coupler angle values
gamma2=input('Enter the value of the coupler angle difference between position 1 & 2 : ');
gamma3=input('Enter the value of the coupler angle difference between position 1 & 3 : ');

%Assuming angles of the input and output angles
phi2=input('Enter the value of the input angle difference between position 1 & 2 : ');
phi3=input('Enter the value of the input angle difference between position 1 & 3 : ');
psi2=input('Enter the value of the output angle difference between position 1 & 2 : ');
psi3=input('Enter the value of the output angle difference between position 1 & 3 : ');

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