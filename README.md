<h2>CSC3002 Assignment </h2>

**CRRLUC003  ||  Lucas Carr**

*Implementation of FIFO, LRU, and Optimal page replacement algorithms*


To Run: 

    The program takes 2 arguments, execute it by running: python3 paging.py [arg1] [arg2]

    [arg1] refers to the number of page references you would like

    [arg2] refers to the number of frames you would like

Output Example for case of:          ***python3 pages.py 15 5***

    _________________________________________________________________ 

    Number of References:  15                                               #Provided by 1st Argument
    Number of Frames:  5                                                    #Provided by 2nd Argument (or defualt = 3)
    Page References:  [7, 6, 2, 1, 6, 1, 2, 7, 4, 5, 4, 8, 2, 6, 0]         #Generated Reference String
    _________________________________________________________________ 

    FIFO:  9  page faults.                                                  #Output for FIFO Algorithm
    LRU:  9  page faults.                                                   #Output for LRU Algorithm
    OPT:  8  page faults.                                                   #Output for OPT Algorithm
    _________________________________________________________________ 




If you would like, you may run the program with *only* the 1st argument (that is, where you specify the number of page references you want). In this case,
the number of frames will default to 3. 

