function [] = test1(f,t)
firstsig=f;
[b,a] = butter(1, .01, 'high');
e = filter(b,a,f);
[b,a] = butter(1, .3, 'low');
e = filter(b,a,e);
f=e;
temp=[];
temp1=[];
for i = 1:length(f)-800
    temp=[temp mean(diff(f(i:i+800)))];
    temp1=[temp1 (diff(f(i:i+800)))];
end
i=min(abs(temp));
f=temp1(i);
f=f-min(f);
% f=f/max(f);
% for i = 1:length(f)
% if(f(i)>200)
% f(i)=200;
% end
% end
% f=f.^3;

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
lmmin=mean(lmin)/4;
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
lmmax=mean(lmax)/4;
lmax=temp;
for i = 1:length(lmax)
if(lmax(i)<lmmax)
    lmax(i)=0;
end
end

ltotal=lmin(2:length(f))+lmax(2:length(f));
epeaks=[];
for i = 1:length(ltotal)
if(ltotal(i)==0)
else
    epeaks=[epeaks i];
end
end
figure(1)
subplot(3,1,1)
plot(1:length(f),f,epeaks,f(epeaks),"*r")
subplot(3,1,2)
plot(epeaks,f(epeaks))
subplot(3,1,3)
plot(abs(fft(f(epeaks))))
%%
eepeaks = [1];
for i = 2:length(epeaks)
 if(epeaks(i)-epeaks(i-1))>5
 eepeaks = [eepeaks i];
 end
end

for i = 2:length(eepeaks)
    if eepeaks(i)-eepeaks(i-1)>1
    f(epeaks(eepeaks(i-1))+1:epeaks(eepeaks(i))-1)= movmean(f(epeaks(eepeaks(i-1))+1:epeaks(eepeaks(i))-1),40);
    end
end
subplot(3,1,1)
plot(1:length(f),f,epeaks,f(epeaks),"*r")
figure(2);
subplot(1,2,1)
f=f-min(f);
f=f.^7;
plot(t,f)
grid on;
subplot(1,2,2)
plot(t,firstsig)
grid on;
end