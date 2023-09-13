% Example 2.2
% Establecer los parámetros.
lam = 2;
n = 1000;
% Genera las variables aleatorias.
uni = rand(1,n);
X = -log(uni)/lam;% .
x=0:.1:5;
% Esta es una función del Statistics Toolbox.
y=exppdf(x,1/2);
% Obtenemos la información del histograma.
[N,h]=hist(X,10);
% Cambiar el ancho de la barras para hacer que corresponda con la densidad
%de probabilidad teórica -ver taller anterior, ecuación 1.
N=N/(h(2)-h(1))/n;
% Graficamos.
bar(h,N,1,'w')
hold on
plot(x,y)
hold off
xlabel('X')
ylabel('f(x) - Exponencial')