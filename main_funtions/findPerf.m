function [t,f] = findPerf(t,f,flag)
[t,f]=delete_first(t,f); %burada ilk basta hatali gelen kisim duzeltiliyor
f=f-movmean(f,	75);        %dc value ve low freqanslara filtre atiyoruz

temp=[];
ii=0;
if(flag)
for i = 1:length(f)-100
    temp=[temp mean(diff(f(i:i+100)))];
    if abs(temp(i))==min(abs(temp))
        ii=i;
    end
end
% for icinde toplam bulunan turev degerlerinin ortalamasini alip en direk
% ortlalmali yeri buluyor tabi istenirse istenmezse hic almiyor
f=f(ii:ii+100);
t=t(ii:ii+100);
end
end

