% Three position synthesis function generation

syms x

f1=input('Enter the function for the relation between input and output link : ');
x0=input('Enter the lower limit of x : ');
x_n=input('Enter the upper limit of x : ');
n=3;
psi1=input('Enter the lower value of the input angle : ');
psi2=input('Enter the upper value of the input angle : ');
phi1=input('Enter the lower value of the output angle : ');
phi2=input('Enter the upper value of the output angle : ');

[xf,yf,psi,phi]=chebyshev_spacing(f1,x0,x_n,n,psi1,psi2,phi1,phi2);

gamma2=input('Enter the value of the coupler angle difference between position 1 & 2 : ');
gamma3=input('Enter the value of the coupler angle difference between position 1 & 3 : ');

Al=[exp((psi(2)-psi(1))*pi*1i/180)-1,exp(gamma2*pi*1i/180)-1;exp((psi(3)-phi(1))*pi*1i/180)-1,exp(gamma3*pi*1i/180)-1];
Bl=[exp((phi(2)-phi(1))*pi*1i/180)-1;exp((phi(3)-phi(1))*pi*1i/180)-1];
Cl=Al\Bl;

Z3=1;
Z1=Cl(1);
Z5=Cl(2);
Z4=-(Z1+Z3+Z5);

linklenghts=[Z1,Z5,Z3,Z4];
ll_len=abs(linklenghts);

%Link Lenghts
for i=1:4
    fprintf('Link %f : Length = %f  \n',i,ll_len(i));
end