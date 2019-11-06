function [sol] =  qrs(f,epeaks,x)
   sol=[];
  a= mean(f)+x;
   for i = 2:length(epeaks)-1
      
        if (abs(f(epeaks(i))-f(epeaks(i-1)))>a)||(abs(f(epeaks(i))-f(epeaks(i+1)))>a)
            sol=[sol , epeaks(i)];
        else
            
        end
   end
end