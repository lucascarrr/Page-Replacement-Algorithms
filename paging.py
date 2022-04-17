# Source code for CSC3002 Assignment 3
# Lucas Carr
# CRRLUC003
# 17/04/22

# libararies
import sys
import random as r

# Source Code

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

    for element in reference_string:
        if element in memory:
            memory.remove(element)
            memory.append(element)
        elif len(memory) == frame_size:
            memory.pop(0)
            memory.append(element)
            page_faults += 1
        else:
            memory.append(element)
            page_faults += 1

    return page_faults

# Optimal Replacement Algorithm
def OPT(frame_size, reference_string):
    page_faults = 0
    memory = []
    counter = 0

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
    size = int(sys.argv[1])
    number_of_frames = 3
    reference_string = generate_reference_string(size)

    print("FIFO: ", FIFO(number_of_frames, reference_string), " page faults.")
    print("LRU: ", LRU(number_of_frames, reference_string), " page faults.")
    print("OPT: ", OPT(number_of_frames, reference_string), " page faults.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
