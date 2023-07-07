
s=tf('s');
z=tf('z',0.0002);

tau= (1000*pi)/2;

%G=(1/(1+s*tau));

G=1/((s+1)^2);

bode(G)

Gz=c2d(G,0.0002,'zoh')
syms z

iztrans(6.366e-08/( z - 1))