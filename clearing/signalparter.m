function [f] = signalparter(f,sol)
    p=islocalmax(sol);
    flag = false;
    for i = 1:length(p)
        if(p(i)==0)
            if(flag==true)
                f(sol(i-1)+15:sol(i)-15)=movmean(f(sol(i-1)+15:sol(i)-15),40);
                flag=false;
            else
                flag=true;
            end
            
        else
            flag = false;
        end
    end
    
end