def findKLargest(stream, k):
    largest = [] # list of k elements sorted ascending
    while (stream.notEmpty()):
        num = stream.emit()
        if (len(largest) < k):
            largest.append(num)
        else:
            if (num > largest[0]):
                del largest[0]
                largest.append(num)
                largest.sort()

findKLargest(stream, 5)