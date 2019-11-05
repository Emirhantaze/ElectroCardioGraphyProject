function [t,f] = delete_first(t,f)
flag = true;
i=1;
difft = diff(t);
t=t(20:length(t));
f =f(20:length(f));
while flag 
    if(difft(i)>0.006)
    flag=false;
    end
    i=i+1;
end
t=t(i:length(t));
f =f(i:length(f));
end

