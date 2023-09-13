
function X = weibull(alpha,beta,n)
% X = weibull(alpha,beta,n)
% genera una muestra de tama\˜{n}o n de una distribucion Weibull
% de parametros (alpha,beta). La funcion de densidad es:
% f(t;a,b) = (b/a)*(t/a)ˆ(b-1)*exp(-(t/a)ˆb)
% Generacion de los numeros aleatorios
X = rand(n,1);
% Generacion de una Extreme Value Standard
X = log(-log(X));
% Generacion de una Extreme Value de parametros (u,b)
b = 1/beta;
u = log(alpha);
X = b*X + u;
% Generacion de la Weibull
X = exp(X);
