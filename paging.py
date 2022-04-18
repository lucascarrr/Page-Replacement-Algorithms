# Source code for CSC3002 Assignment 3
# Lucas Carr
# CRRLUC003
# 17/04/22

# libararies
import sys
import random as r


# Function to generate a random reference string
def generate_reference_string(number_of_pages):
    page_array = []

    for page in range(number_of_pages):
        page_array.append(r.randrange(0, 9))

    return page_array

# Function called in the OPT algorithm - used to find the optimal page to replace
def find_optimal_element(future_pages, current_queue):
    values = current_queue
    positions = []

    for value in values:
        try:
            positions.append(future_pages.index(value))
        except:
            return value

    return future_pages[max(positions)]

# FIFO Replacement Algorithm
def FIFO(frame_size, reference_string):
    page_faults = 0
    memory = []

    for element in reference_string:
        
        if element not in memory:
            page_faults += 1

            if len(memory) == frame_size:
                memory.pop(0)
                memory.append(element)

            else:
                memory.append(element)

    return page_faults

# LRU Replacement Algorithm
def LRU(frame_size, reference_string):
    page_faults = 0
    memory = []
    times = []

    for element in reference_string:
        for x in range(len(times)):
            times[x] += 1

        if element in memory:
            times[memory.index(element)] = 0

        elif len(memory) == frame_size:
            page_faults += 1
            element_to_remove = times.index(max(times))
            memory.pop(element_to_remove)
            memory.insert(element_to_remove, element)
            times[element_to_remove] = 0

        else:
            page_faults += 1
            memory.append(element)
            times.append(0)

    return page_faults

# Optimal Replacement Algorithm
def OPT(frame_size, reference_string):
    page_faults = 0
    counter = 0
    memory = []

    for element in reference_string:
        if element not in memory:
            page_faults += 1

            if len(memory) == frame_size:
                element_to_remove = find_optimal_element(
                    reference_string[(counter)+1:], memory)
                memory.remove(element_to_remove)
                memory.append(element)
                
            else:
                memory.append(element)

        counter += 1

    return page_faults


# Main Functionality
def main():
    # setting up program variables
    size = int(sys.argv[1])

    try:
        number_of_frames = int(sys.argv[2])
    except:
        number_of_frames = 3

    reference_string = generate_reference_string(size)

    # output handling
    print("_"*(20+(size*3)), "\n")
    print ("PAGE REPLACEMENT ALGORITHMS")
    print("_"*(20+(size*3)), "\n")
    print("Number of References: ", size, "\nNumber of Frames: ",
          number_of_frames, "\nPage References: ", reference_string)
    print("_"*(20+(size*3)), "\n")
    print("FIFO: ", FIFO(number_of_frames, reference_string), " page faults.")
    print("LRU:  ", LRU(number_of_frames, reference_string), " page faults.")
    print("OPT:  ", OPT(number_of_frames, reference_string), " page faults.")
    print("_"*(20+(size*3)), "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error!")
        print("Usage: python paging.py [number of pages] [number of frames]")
    else:
        main()
