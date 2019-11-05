function [] = approach1(t,f,useperfect,selectedmod,lowfreq,highfreq)
        
        [t,f]=findPerf(t,f,useperfect);
        switch selectedmod
            case
        end    
        f=f-min(f);       
        f=(f./max(f))*100;
        sol = qrs(f,peekfind(f));
        plot(sol(1:length(sol)),f(sol(1:length(sol))),"*r")
       figure(3)
       plot(signalparter(f,sol))
end

