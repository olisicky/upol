array = [10, 4, 3, 5, 2, 9, 1]

def insertion(array):

    sorted = array.copy()

    for i in range(1, len(array)):

        element = sorted[i]
        j = i - 1
        while element <= sorted[j] and j >= 0:
            checked = sorted[j]
            sorted[j] = element
            sorted[i] = checked
            j -= 1
            i -=1
    return sorted

if __name__ == '__main__':
    print(insertion(array))
