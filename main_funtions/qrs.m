function [sol] =  qrs(f,epeaks)
   sol=[];
  a= mean(f)+30;
   for i = 2:length(epeaks)-1
      
        if (abs(f(epeaks(i))-f(epeaks(i-1)))>a)||(abs(f(epeaks(i))-f(epeaks(i+1)))>a)
            sol=[sol , epeaks(i)];
        else
            
        end
   end
end