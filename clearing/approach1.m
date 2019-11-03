function [] = approach1(t,f)
        cla
        [t,f]=findPerf(t,f);
        f=f-min(f);
        f=(f./max(f))*100;
        sol = signalparter(f,peekfind(f));
        plot(sol(1:length(sol)),f(sol(1:length(sol))),"*r")
        figure (2);
        plot(sol(1:length(sol)),f(sol(1:length(sol))))
end

