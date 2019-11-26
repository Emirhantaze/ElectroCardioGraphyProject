
delete(instrfind);
s=serial('COM3');
fopen(s);
pause(.01);
out=fscanf(s);
i = 0;
f20=0;
t20=0;
pause(3); %this is a test
tic
while toc < 10
    i= i +1;
    out = fscanf(s);
    f20(i)=str2double(out);
    t20(i)=toc;
end
plot(t20,f20);

