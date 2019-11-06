# ElectroCardioGraphyProject
In this project we are trying to filter noisy ecg signal 
and proccesing it to calculate heart rate and other informations

    Currently main code(approach1) of project is in main_funtions folder 
    
    Approach1 takes 7 different arguments to calculate and show bpm, fft and signals
    
    apprach1(t,f,useperfect,selectedmod,lowfreq,highfreq,x)
    t=time vector;
    f=signal vector;
    useperfect= 
        this is a logical value here this defines do you want to take best 1000 value or whole signal
    selectedmod=
        this takes 3 different values (butter , cheby , elliptic ) for the 
        inputs other than that equals to not filtering signal
    lowfreq=
        this determines the low cutoff frequency
    highfreq=
        this determines the high cutoff frequency
    x=
        takes vales between -100 100 but suggested inputs
            for elliptic value is 19
            for butter value is 50
            for cheby value is 30

Warning!!! This applications can not be usable in medical.

    Group Members:
    1:      Emirhan Taze
    2:      Bilal Kütük
    3:      Mücahit Demirci

    Group Name:
    Agu_eeepower

    University:
    Abdullah Gul University
