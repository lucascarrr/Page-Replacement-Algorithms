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

def find_optimal_element(future_pages, current_queue):
    values = [current_queue[0], current_queue[1], current_queue[2]]
    positions = [-1, -1, -1]
    counter = 0
    print (future_pages)
    print (current_queue)

    for element in future_pages:

        if element == values[0] and positions[0] == -1:
            positions[0] = future_pages[counter]

        elif element == values[1] and positions[1] == -1:
            positions[1] = future_pages[counter]

        elif element == values[2] and positions[2] == -1:
            positions[2] = future_pages[counter]

        counter += 1

    return (max(positions))

#FIFO Replacement Algorithm
def FIFO(frame_size, reference_string):
    page_faults = 0
    fifo_queue = []

    for element in reference_string:
        if element not in fifo_queue:
            if len(fifo_queue) == frame_size:
                fifo_queue.pop(0)
                fifo_queue.append(element)
                page_faults += 1
            else:
                fifo_queue.append(element)
                page_faults += 1
                
    return page_faults

#LRU Replacement Algorithm
def LRU(frame_size, reference_string):
    page_faults = 0
    lru_queue = []

    for element in reference_string:
        if element in lru_queue:
            lru_queue.remove(element)
            lru_queue.append(element)
        elif len(lru_queue) == frame_size:
            lru_queue.pop(0)
            lru_queue.append(element)
            page_faults += 1
        else:
            lru_queue.append(element)
            page_faults += 1
    
    return page_faults

#Optimal Replacement Algorithm
def OPT(frame_size, reference_string):
    page_faults = 0
    opt_queue = []
    counter = 0
    

    for element in reference_string:
        if element not in opt_queue:
            if len(opt_queue) == 3:
                element_to_remove = find_optimal_element(reference_string[counter+1:], opt_queue)
                opt_queue.remove(element_to_remove)
                opt_queue.append(element)
                page_faults += 1
            else:
                opt_queue.append(element)
                page_faults += 1
        counter += 1
        
    return page_faults

        
#Main Functionality
def main():
    size = int(sys.argv[1])                                     #this is the size of the reference string
    number_of_frames = 3                                       
    reference_string = generate_reference_string(size)

    print ("FIFO: ", FIFO(number_of_frames, reference_string), " page faults.")
    print ("LRU: ", LRU(number_of_frames, reference_string), " page faults.")
    print ("OPT: ", OPT(number_of_frames, reference_string), " page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()
