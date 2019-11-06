function [] = approach1(t,f,useperfect,selectedmod,lowfreq,highfreq)
        
        [t,f]=findPerf(t,f,useperfect);
        [Fv ,Fecg]=myfft(t,f);
        Fecg(1)=0;
        figure(1);
        if(useperfect)
            title('Signal with best 1000 value interval')
        else
            title('This application use signal itself')
        end
        subplot(3,2,1);
        plot(t,f);
        title('Signal.')
        subplot(3,2,2)
        plot(Fv,Fecg);
        title('FFT of signal.')
        Lecg=length(Fv);
        lowfreq=lowfreq/Lecg;
        highfreq=highfreq/Lecg;
        switch selectedmod
            case {'butter','Butter'}
                f=butterworthFilter(f,lowfreq,highfreq);
            case {'cheby','Cheby'}
                f=chebyECG(f,lowfreq,highfreq);
            case {'elliptic','Elliptic'}
                f=elliptic1November(f,lowfreq,highfreq);
        end    
        f=f-min(f);       
        f=(f./max(f))*100;
        sol = qrs(f,peekfind(f));
        subplot(3,2,3)
        title('Filtered Signal with peaks.')
        plot(t,f);
        hold on;
        plot(t(sol(1:length(sol))),f(sol(1:length(sol))),"*r")
        subplot(3,2,4)
        title('Fft of filtered Signal.')
        [Fv ,Fecg]=myfft(t,f);
        Fecg(1)=0;
        plot(Fv,Fecg);
%         plot(signalparter(f,sol))
end

