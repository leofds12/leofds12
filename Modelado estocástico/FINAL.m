  t = 5000;
 x_total = 0;
 UNIFORME=rand(1,t);
for i=1:t 
    COEFICIENTE=1.57; %medido en kg/mm 
    P=0.15; % en dientes/mm
    F=35; %ancho de la cara en mm
    Y=0.46; %adimensional
        
    w1=UNIFORME(i);
    W=((-log(w1))^(1/1.57926))*602.017;
    W_total(i)=W %este W es el diametro, no la fuerza. La fuerza será W multiplicado por un coeficiente
    sigma=100*W*COEFICIENTE*P/(F*Y);
    sigma2_total(i)=sigma; %se mide en kg/mm^2
    
end

