    1:
        as we look to do graphs and our values we found that time at begining is too fast 
        function delete_first deletes un wanted first values;
    2:
        fft test function applies a dc filter and also gives the resulsts of fourrier of function itself
        this gives us information f signal and how to make ilter design
    3:
        after that point we aim to design cheby and butterworth filters u can found their funtions in 
        filters folder;
        test change
    4: 
        next step is going a bit further and make filters uniqe for each signal
        a:
            first we know that there are lower and higher unwanted frequncies in our functions 
            the deal is how to find which are them are necessary ones:
        b:
            At first we try to find best part of signal itself
        c: 
            using islocalmax,min and its coefficients determining the real peaks and drops;
        d:
            then wheter filtering or avaraging the areas which are nnot the "R S T" peaks or drops;
        
        this is the first approches to filter signal;
        
        a:
            the second methodology is a bit strange and their codes are not written right now
            in this method we mainly focus on a perfect ecg signal and correlations with this perfect signal;
        b: 
            to reach that what we think was while we don't have data of perfect signal we will take an image of perfect signal and using c# we take data of signal from image;
        c: 
            after getting data we try to match the perfect signal and normal signal with scaling to
            perfect signal;
        d:
            after that what we have to do is choosing best one using coorellation and using this
            signal as a reference to our filter designs 