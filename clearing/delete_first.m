function [t,f] = delete_first(t,f)
flag = true;
i=1;
difft = diff(t);
while flag 
    if(difft(i)>0.004)
    flag=false;
    end
    i=i+1;
end
t=t(i:length(t));
f =f(i:length(f));
end

