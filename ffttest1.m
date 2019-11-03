function [FECG] = ffttest1(fin,tin,x)
ECG = fin;
t=tin;
flag = true;
i=1;
difft = diff(t);
while flag 
    if(difft(i)>0.004)
    flag=false;
    end
    i=i+1;
end
% plot(t5(i:length(t5)),f5(i:length(f5)))
t=t(i:length(t));
ECG =ECG(i:length(ECG));
L = length(t);
Ts = mean(diff(t));                                 % Sampling Time
Fs = 1/Ts;                                          % Sampling Frequency
Fn = Fs/2;                                          % Nyquist Frequency
FECG = fft(ECG);                                    % Fourier Transform (Normalised)
Fv = linspace(0, 1, fix(L/2)+1)*Fn;                 % Frequency Vector
Iv = 1:length(Fv);                                  % Index Vector
figure(1)
subplot(2,2,1);
plot(Fv, abs(FECG(Iv))/L)
xlim([1 80]);
grid
subplot(2,2,2);
plot(t,ifft(FECG));
subplot(2,2,3);
for i = fix(length(FECG)/x):fix((x-1)*length(FECG)/x)
FECG(i)=0;
end
for i = 1:15
    FECG(i)=0;
end
FECG(1)=0;
j=1;

[~ ,a] = findpeaks(abs(FECG));
for i = 1:fix(L/2)+1
if a(j)==i
    j=j+1;
else
    FECG(i)=abs(FECG(i)/3);
end

end

plot(t,ifft(FECG));

figure(1)
subplot(2,2,4);
plot(Fv, abs(FECG(Iv))/L)
end
