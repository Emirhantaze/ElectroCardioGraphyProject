
delete(instrfind);
s = serial('COM5');
fopen(s);
pause(.01);
out=fscanf(s)

i=0;
f4=0;
t4=0;
pause(3);
tic
while toc<10
i=i+1;
out = fscanf(s);
f4(i)=str2double(out);
t4(i)=toc;
end
plot(t4,f4);
