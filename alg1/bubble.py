array = [4, 3, 5, 2, 9, 1]

def bubble(array):
    sorted = array.copy()
    
    for _ in range(len(array)):
    
        for j, el in enumerate(sorted):

            if (j < len(sorted) - 1) and (sorted[j] > sorted[j+1]):
                sorted[j] = sorted[j+1]
                sorted[j+1] = el
                
    return sorted
if __name__ == '__main__':
    print(bubble(array))
