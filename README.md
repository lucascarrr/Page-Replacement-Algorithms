<h2>CSC3002 Assignment </h2>

**CRRLUC003  ||  Lucas Carr**

*Implementation of FIFO, LRU, and Optimal page replacement algorithms*


**To Run**: 

    The program takes 2 arguments, execute it by running: python paging.py [arg1] [arg2]

    [arg1] refers to the number of page references you would like

    [arg2] refers to the number of frames you would like

Output Example for case of: _python3 pages.py 32 3_

    ________________________________________ 

    PAGE REPLACEMENT ALGORITHMS
    ________________________________________ 

    Number of References:  32 
    Number of Frames:  3 
    Page References:  [5, 4, 1, 1, 8, 5, 8, 7, 
    0, 7, 3, 8, 0, 2, 2, 6, 1, 3, 3, 0, 8, 7, 
    7, 4, 3, 6, 7, 0, 3, 8, 6, 3]
    ________________________________________ 

    FIFO:  24  page faults.
    LRU:   25  page faults.
    OPT:   16  page faults.
    ________________________________________ 





If you would like, you may run the program with *only* the 1st argument (that is, where you specify the number of page references you want). In this case,
the number of frames will default to 3. 

You _must_ run the program with at least 1 argument. 

*Program was written to be compiled on python3*