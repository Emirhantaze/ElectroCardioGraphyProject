function [epeaks] = peekfind(f)
        
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
        lmmin=mean(lmin)/3;
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
        lmmax=mean(lmax)/3;
        lmax=temp;
        for i = 1:length(lmax)
        if(lmax(i)<lmmax)
            lmax(i)=0;
        end
        end

        ltotal=lmin(1:length(f))+lmax(1:length(f));
        epeaks=[];
        for i = 1:length(ltotal)
        if(ltotal(i)==0)
        else
            epeaks=[epeaks i];
        end
        end
        
      
end