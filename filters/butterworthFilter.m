function[e]=butterworthFilter(f)
%[b,a] = butter(n,Wn,ftype)
% n = Filter Order, integer scalar
% Wn = Cut-off Frequency, scalar | two-element vector
%The cutoff frequency is the frequency at which the magnitude response of the filter is 1 / √2.
% ftype = filter type, 'low' | 'bandpass' | 'high' | 'stop'
%{
Filter type, specified as one of the following:
Filter type, specified as one of the following:

'low' specifies a lowpass filter with cutoff frequency Wn. 'low' is the default for scalar Wn.

'high' specifies a highpass filter with cutoff frequency Wn.

'bandpass' specifies a bandpass filter of order 2n if Wn is a two-element vector. 'bandpass' is the default when Wn has two elements.

'stop' specifies a bandstop filter of order 2n if Wn is a two-element vector.
%}
[b,a]=butter(2, .01, 'high');   % calculating values to make fhigh pass filter

e = filter(b,a,f);

[b,a]=butter(2,0.1,'low');

e=filter(b,a,e);

plot(e)