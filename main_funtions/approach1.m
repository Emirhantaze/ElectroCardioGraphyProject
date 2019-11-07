function [] = approach1(t,f,useperfect,selectedmod,lowfreq,highfreq,x)
 %%     how code works is explained in each function
 %      but if you have problems you can contact me via github
 %      or emtiyltezkry@gmail.com
 %      or emirhan.taze@agu.edu.tr
 %      feel free to ask anything about code
 %%     getting perf values of signal and plotting itself and fft
 %      used funtions are findperf,myfft
        [t,f]=findPerf(t,f,useperfect);
        [Fv ,Fecg]=myfft(t,f);
        Fecg(1)=0;
        
        figure(1)
        subplot(3,2,1);
        plot(t,f);
        title('Signal.')
        subplot(3,2,2)
        plot(Fv,Fecg);
        title('FFT of signal.')
        Lecg=length(Fv);
%%      filtering signal if user speficies the filter
%       used funtions are butterworthfilter,chebyECG,elliptic1November
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
%%      scaling the signal
        f=f-min(f);       
        f=(f./max(f))*100;
%%      peak finding plotting filtered signnal with peaks and fft of it
        sol = qrs(f,peekfind(f),x);
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
%%      calculating bpm and ploting it with respect to each peak interval
%       here no funtions are used. Code will be explained line by linew after that point 
        subplot(3,1,3)
        pt=islocalmax(f(sol(1:length(sol))));
            %here code re-evulated peaks from determined peaks
        p=[];       
        for i = 1:length(pt)            
            if pt(i)==true
                p(i)=i;
            end
        end
            %above for loop gets only the peaked values for more
            %informations help islocalmax
        i=1;
        while i<=length(p)
            if(p(i)==0)
                p(i)=[];
            else
                i=i+1;
            end
        end 
            %this while loop deletes the 0 values inside of the p vector
        bpm=[];
        for i = 2:length(p)
            bpm(i)=60/(t(sol(p(i)))-t(sol(p(i-1))));
        end
            %in that for loop bpm is calculated for each 2 series peaks
       bpm(1)=mean(bpm(2:length(bpm)));
            %here because above first valeu is not assigned it sets the
            %mean opf the total bpm
%%     plotting bpm and calculating mean value
       plot(t(sol(p)),bpm)
       ylim([60 120])
       a=mean(bpm);
       legendmean=sprintf('Mean BPM: %.6f',a);
       legend(legendmean)
       grid on;
%%       
end

