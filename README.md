### Postioning_Systems_and_Techniques
This Project Consists of 3 techniques to calculate the position in both Indoor and outdoor environments by slight modifications. These techniques majorly dependent on the radio communication between the device and the infrastructure. Also there is technique to use previous results to predict the future paths. These algorithms are 
Types of techniques : 
1) N-lateration 
2) Fingerprinting 
3) HMM 

#### 1)  N-lateration: (N-Lateration.py)
    This technique can be applicable to both 3D and 2D space, respectively inputs wll be changed. This is used to find the center of the calculated location area.

    Usage:
    1)Replace inputs at dataset variable for 4 AP's in 3D space.(line no. 50)
    2)Replace inputs at dataset1 variable for 3 AP's in 2D space. (line no. 52)

    Get Results by running N-Lateration.py file.

#### 2) Fingerprinting: (Fingerprint.py)
    This technique will check the database of fingerprints of the location, each cell pf finerprint will consists of locatoion(x,y) and the RSSI values received from the 4 APs. So when any Mobile Terminal asks for the location, we check the minimum distance location from fingerprint database by comparing the distance using the RSSI values from databse and Mobile terminal. And find the best from the Finerprint Database.

    Usage:
    1) Change the fingerprint Database from (line 136)
    2) Chnage the RSSI received by Mobile terminal (line 139)

    Get the barryCenter as a result.

#### 3) Hidden Markov Model: (main.py , Cell.py)
    This Technique depends on the predicting the next cell movement from past expreience cell movements. We are currently in a cell, we are continously moving further and predicting the next move and predicting the previous move as well, suppose , if we dont know as a user.

    Usage:
    1) It is continouse iteration with the code , need to input next move.(Run main.py)
    
    Get next probable location and previous probable location.




   
