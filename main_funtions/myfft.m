function [Fv,FECG] = myfft(tin,fin)
%MYFFT Summary of this function goes here
%   Detailed explanation goes here
ECG = fin;
t=tin;
L = length(t);
Ts = mean(diff(t));                                 % Sampling Time
Fs = 1/Ts;                                          % Sampling Frequency
Fn = Fs/2;                                          % Nyquist Frequency
FECG = fft(ECG);                                  % Fourier Transform (Normalised)
Fv = linspace(0, 1, fix(L/2)+1)*Fn;                 % Frequency Vector
Iv = 1:length(Fv);                                  % Index Vector
FECG= abs(FECG(Iv))/L;                              % deger normal fft'nin absulat value'sunu aliyor
end

