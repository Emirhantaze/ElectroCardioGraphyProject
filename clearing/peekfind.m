function [] = peekfind(f)
    f=f-min(f);
        [~,lmin] = islocalmin(f);
        [~,lmax] = islocalmax(f);
        temp = lmin;
        i = 1;
        while i<=length(lmin)
        if(lmin(i)==0)
            lmin(i)=[];
        else
            i=i+1;
        end

        end
        lmmin=mean(lmin)/4;
        lmin=temp;
        for i = 1:length(lmin)
        if(lmin(i)<lmmin)
            lmin(i)=0;
        end
        end
        temp=lmax;
        i = 1;
        while i<=length(lmax)
        if(lmax(i)==0)
            lmax(i)=[];
        else
            i=i+1;
        end

        end
        lmmax=mean(lmax)/4;
        lmax=temp;
        for i = 1:length(lmax)
        if(lmax(i)<lmmax)
            lmax(i)=0;
        end
        end

        ltotal=lmin(2:length(f))+lmax(2:length(f));
        epeaks=[];
        for i = 1:length(ltotal)
        if(ltotal(i)==0)
        else
            epeaks=[epeaks i];
        end
        end
        figure(1)
        subplot(3,1,1)
        plot(1:length(f),f,epeaks)
        subplot(3,1,2)
        plot(epeaks,f(epeaks))
        subplot(3,1,3)
        plot(abs(fft(f(epeaks))))
end