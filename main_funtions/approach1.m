function [] = approach1(t,f,useperfect,selectedmod,lowfreq,highfreq)
        
        [t,f]=findPerf(t,f,useperfect);
        [Fv ,Fecg]=myfft(t,f);
        figure(3);
        plot(Fv,Fecg);
        title('FFT of signal.')
        Lecg=length(Fv)*2;
        lowfreq=lowfreq/Lecg;
        highfreq=highfreq/Lecg;
        switch selectedmod
            case {'butter','Butter'}
                butterworthFilter(f,lowfreq,highfreq);
            case {'cheby','Cheby'}
                chebyECG(f,lowfreq,highfreq);
            case {'elliptic','Elliptic'}
                elliptic1November(f,lowfreq,highfreq);
        end    
        f=f-min(f);       
        f=(f./max(f))*100;
        sol = qrs(f,peekfind(f));
        plot(sol(1:length(sol)),f(sol(1:length(sol))),"*r")
       figure(3)
       plot(signalparter(f,sol))
end

