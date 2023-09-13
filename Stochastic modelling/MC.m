% Uniform Random Number
% Monte Carlo method as an approximated integration technique
% integrate f(x) on the [0,1] interval
% solution: 1/2, 1/3, and 0
clc;
n=50;
x=rand(n,1);
gav=zeros(n,3);
gavvar=NaN(n,3);
gav(1,1)=x(1,1);
gav(1,2)=x(1,1)^2;
gav(1,3)=cos(pi*x(1,1));
for i=2:n
gav(i,1)=sum(x(1:i))/i;
gav(i,2)=sum(x(1:i).^2)/i;
gav(i,3)=sum(cos(pi*x(1:i)))/i;
gavvar(i,1)=var(x(1:i));

gavvar(i,2)=var(x(1:i).^2);
gavvar(i,3)=var(cos(pi*x(1:i)));
end
%
%
%%%%%%%%% Graphics (mean) %%%%%%%%%%
figure(1);
subplot(3,1,1);
plot(gav(:,1));
line((1:n),ones(n,1)/2,'color','red');
legend('Empirical Average','Theoretical Mean',...
'Location','NorthEastOutside');
title('f(x)=x');
%
subplot(3,1,2);
plot(gav(:,2));
line((1:n),ones(n,1)/3,'color','red');
legend('Empirical Average','Theoretical Mean',...
'Location','NorthEastOutside');
title('f(x)=x^2');
%
subplot(3,1,3);
plot(gav(:,3));
line((1:n),ones(n,1)*0,'color','red');
legend('Empirical Average','Theoretical Mean',...
'Location','NorthEastOutside');
title('f(x)=cos(\pi x)');
To export picture to a .eps file one can use
%%%%%%%%% Export a picture %%%%%%%%%%%%%
dire='C:\Dottorato\Teaching\SummerSchoolBertinoro';
figu='\TutorialAntonietta\TutorialRobAnt\Figure\';
figname=strvcat([strcat(dire,figu,'MC1.eps')]);
print (gcf,'-depsc2', figname);
%
%%%%%%%%% Graphics (variance) %%%%%%%%%%
figure(2);
subplot(3,1,1);
plot(gavvar(:,1));
line((1:n),ones(n,1)/12,'color','red');
legend('Empirical Variance','Theoretical Variance',...
'Location','NorthEastOutside');
title('f(x)=x');
%
subplot(3,1,2);
plot(gavvar(:,2));
line((1:n),ones(n,1)*4/45,'color','red');
legend('Empirical Variance','Theoretical Variance',...
'Location','NorthEastOutside');
title('f(x)=x^2');
%
subplot(3,1,3);
plot(gavvar(:,3));
line((1:n),ones(n,1)*1/2,'color','red');
legend('Empirical Variance','Theoretical Variance',...
    'Location','NorthEastOutside');
title('f(x)=cos(\pi x)');