d2=input('Enter the first position vector : ');
d3=input('Enter the second position vector : ');
d4=input('Enter the third position vector : ');
a2=input('Enter the first angle difference of coupler link : ');
a3=input('Enter the second angle difference of coupler link : ');
a4=input('Enter the third angle difference of coupler link : ');
b2=input('Enter a value for the input angle : ');
c2=input('Enter a value for the output angle : ');

%LH Dyad synthesis
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

%RH Dyad Synthesis
delta=delta1+(delta2*exp(1i*c2*pi/180));
ctheta3=((abs(delta4)^2-abs(delta3)^2-abs(delta)^2)/(2*abs(delta3)*abs(delta)));
stheta3=abs((1-ctheta3^2)^0.5);
theta3=atan2(stheta3,ctheta3);
c3=angle(delta)+theta3-angle(delta3);

ctheta4=((abs(delta3)^2-abs(delta4)^2-abs(delta)^2)/(2*abs(delta4)*abs(delta)));
stheta4=abs((1-ctheta4^2)^0.5);
theta4=atan2(stheta4,ctheta4);
c4=angle(delta)-theta4-angle(delta4);

Ar=[exp(c2*pi*1i/180)-1,exp(a2*pi*1i/180)-1;exp(c3*pi*1i/180)-1,exp(a3*pi*1i/180)-1];
Br=[d2;d3];
Cr=Ar\Br;
Wr=Cr(1); Zr=Cr(2);

l5=Cl(2)-Cr(2);
l6=Cl(1)-Cr(1)+l5;

linklenghts=[Cl(1);Cl(2);Cr(1);Cr(2);l5;l6];
ll_len=abs(linklenghts);
ll_ang=angle(linklenghts)*180/pi;

%Link Lengths
for i=1:6
    fprintf('Link %f : Length = %f , Angle = %f \n',i,ll_len(i),ll_ang(i));
end