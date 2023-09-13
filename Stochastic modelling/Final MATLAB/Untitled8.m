close all
% Hacer a = 3, b = 3
n=500;
a=600;
b=1.5;
x = rand('WEIBULL',a,b);
% Ahora el histograma.
[N,h]=hist(rvs,10);
% Cambiar el ancho de las barras.
N=N/(h(2)-h(1))/n;
% Ahora obtenemos la densidad de probabilidad teórica.
x = 0:.05:1;
y = betapdf(x,a,b);
plot(x,y)
axis equal
bar(h,N,1,'w')
hold on
plot(x,y,'k')
hold off