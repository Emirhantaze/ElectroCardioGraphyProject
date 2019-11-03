
delete(instrfind);
s = serial('COM3');
fopen(s);
pause(.01);
out=fscanf(s);

i=0;
f12=0;
t12=0;
pause(1);
tic
while toc<10
i=i+1;
out = fscanf(s);
f12(i)=str2double(out);
t12(i)=toc;
end
plot(t12,f12);
