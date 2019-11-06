function [epeaks] = peekfind(f)
        %% bu k?s?mda coefficiantlar?yla beraber peak varm? yok mu onu hesapl?yoruz 
        [~,lmin] = islocalmin(f);
        [~,lmax] = islocalmax(f);
        temp = lmin;
        %%burada peak olmuyan yerlerde lmin 0 oldu?u için onlar? yok
        %ediyoruz
        
        i = 1;
        while i<=length(lmin)
        if(lmin(i)==0)
            lmin(i)=[];
        else
            i=i+1;
        end

        end
        lmmin=mean(lmin)/3;    
        %burada ortalamas?n? al?p alt?nda kalanlar? yaalnc? peak yap?yoruz 
        lmin=temp;
        for i = 1:length(lmin)
        if(lmin(i)<lmmin)
            lmin(i)=0;
        end
        end
        %yine ayn? procces
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
        %sonra peakleri ve droplar? birle?tiriyoruz
        ltotal=lmin(1:length(f))+lmax(1:length(f));
        epeaks=[];
        for i = 1:length(ltotal)
        if(ltotal(i)==0)
        else
            %burada hangi noktalardo olduklar?n? buluyor bu peaklerin
            epeaks=[epeaks i];
        end
        end
        
      
end