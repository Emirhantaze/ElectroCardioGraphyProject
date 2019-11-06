function [] = approach1(t,f,useperfect,selectedmod,lowfreq,highfreq)
 %%       
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
        
        plot(t,f);
        hold on;
        plot(t(sol(1:length(sol))),f(sol(1:length(sol))),"*r")
        title(subplot(3,2,3),'Filtered Signal with peaks.')
        subplot(3,2,4)
        
        [Fv ,Fecg]=myfft(t,f);
        Fecg(1)=0;
        plot(Fv,Fecg);
        title(subplot(3,2,4),'Fft of filtered Signal.')
%%        
        subplot(3,1,3)
        
        
        pt=islocalmax(f(sol(1:length(sol))));
        p=[];
       
        for i = 1:length(pt)
            
            if pt(i)==true
                p(i)=i;
            end
        end
        i=1;
        while i<=length(p)
            if(p(i)==0)
                p(i)=[];
            else
                i=i+1;
            end
        end
        
        bpm=[];
        for i = 2:length(p)
            bpm(i)=60/(t(sol(p(i)))-t(sol(p(i-1))));
        end
       bpm(1)=mean(bpm(2:length(bpm)));
       
       plot(t(sol(p)),bpm)
       ylim([60 120])
       a=mean(bpm);
       legendmean=sprintf('Mean BPM: %.6f',a);
       legend(legendmean)
       grid on;
%%       
end

