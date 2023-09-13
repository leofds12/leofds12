c=879;
K=1.6;
f=@(k,x) (k/c)*((x/c).^(k-1)).*exp(-(x/c).^k);
x=linspace(0,4000,10000);
    plot(x,f(K(i),x),'displayName',num2str(K(i)))

