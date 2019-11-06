function[e]=chebyECG(f,lowfreq,highfreq)

%{
[b,a] = cheby1(n,Rp,Wp,ftype)
n — Filter order
integer scalar
Filter order, specified as an integer scalar.

Data Types: double

Rp — Peak-to-peak passband ripple
positive scalar
Peak-to-peak passband ripple, specified as a positive scalar expressed in decibels.

If your specification, ℓ, is in linear units, you can convert it to decibels using Rp = 40 log10((1+ℓ)/(1–ℓ)).

Data Types: double

Wp — Passband edge frequency
scalar | two-element vector
Passband edge frequency, specified as a scalar or a two-element vector. The passband edge frequency is the frequency at which the magnitude response of the filter is –Rp decibels. Smaller values of passband ripple, Rp, result in wider transition bands.

If Wp is a scalar, then cheby1 designs a lowpass or highpass filter with edge frequency Wp.

If Wp is the two-element vector [w1 w2], where w1 < w2, then cheby1 designs a bandpass or bandstop filter with lower edge frequency w1 and higher edge frequency w2.

For digital filters, the passband edge frequencies must lie between 0 and 1, where 1 corresponds to the Nyquist rate—half the sample rate or π rad/sample.

For analog filters, the passband edge frequencies must be expressed in radians per second and can take on any positive value.

Data Types: double

ftype — Filter type
'low' | 'bandpass' | 'high' | 'stop'
Filter type, specified as one of the following:

'low' specifies a lowpass filter with passband edge frequency Wp. 'low' is the default for scalar Wp.

'high' specifies a highpass filter with passband edge frequency Wp.

'bandpass' specifies a bandpass filter of order 2n if Wp is a two-element vector. 'bandpass' is the default when Wp has two elements.

'stop' specifies a bandstop filter of order 2n if Wp is a two-element vector.
%}
[b,a] = cheby1(1,3,[lowfreq,highfreq],'bandpass');
e = filter(b,a,f);



% plot(e)