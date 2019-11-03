function [] = approach1(t,f)
        cla
        
        [t,f]=findPerf(t,f);
        f=f-min(f);
        
%         [f]=chebyECG(f);
%         f=f-min(f);
        f=(f./max(f))*100;
        sol = qrs(f,peekfind(f));
        plot(sol(1:length(sol)),f(sol(1:length(sol))),"*r")
       figure(3)
       plot(signalparter(f,sol))
end

