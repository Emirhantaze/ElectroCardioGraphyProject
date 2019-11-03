function [t,f] = findPerf(t,f)
[t,f]=delete_first(t,f);
f=f-movmean(f,	75);

temp=[];
ii=0;
for i = 1:length(f)-1000
    temp=[temp mean(diff(f(i:i+1000)))];
    if abs(temp(i))==min(abs(temp))
        ii=i;
    end
end
f=f(ii:ii+1000);
t=t(ii:ii+1000);
end

