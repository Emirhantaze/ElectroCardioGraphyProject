function [t,f] = findPerf(t,f)
[t,f]=delete_first(t,f);
f=f-movmean(f,75);
% plot(t,f);
end

