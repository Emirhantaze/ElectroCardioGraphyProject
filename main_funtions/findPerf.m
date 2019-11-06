function [t,f] = findPerf(t,f,flag)
[t,f]=delete_first(t,f); %burada ilk ba?ta hatal? gelen k?sm? düzeltiyoruz
f=f-movmean(f,	75);        %dc value ve low freqanslara filtre at?yoruz

temp=[];
ii=0;
if(flag)
for i = 1:length(f)-1000
    temp=[temp mean(diff(f(i:i+1000)))];
    if abs(temp(i))==min(abs(temp))
        ii=i;
    end
end
% for içinde toplam bulunan türev de?erlerinin ortalamas?n? al?p en dü?ük
% ortlalmal? yeri buluyor tabi istenirse istenmezse hiç çal??m?yor
f=f(ii:ii+1000);
t=t(ii:ii+1000);
end
end

