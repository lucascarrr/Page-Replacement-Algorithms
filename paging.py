# Source code for CSC3002 Assignment 3
# Lucas Carr
# CRRLUC003
# 17/04/22

#libararies
import sys
import random as r

#Source Code
#Helper Functions
def generate_reference_string(number_of_pages):
    page_array = [] 
    for page in range(number_of_pages):
        page_array.append(r.randrange(0,9))
    return page_array

#FIFO Replacement Algorithm
def fifo_replacement(reference_string, frame_size):
    page_faults = 0
    fifo_queue = []
    for element in reference_string:
        print (element)
        if element not in fifo_queue:
            if len(fifo_queue) == frame_size:
                fifo_queue.pop()
                fifo_queue.append(element)
                page_faults += 1
            else:
                fifo_queue.append(element)
    return page_faults


#LRU Replacement Algorithm


#Optimal Replacement Algorithm


#Main Functionality
def main():
    size = int(sys.argv[1])                                     #this is the size of the reference string
    number_of_frames = 3                                       
    reference_string = generate_reference_string(size)
    print ("FIFO: ", fifo_replacement(reference_string, number_of_frames), " page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()
