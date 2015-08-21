Constraints:
- Three columns
- Read column by column
- Rendering row by row

Varying lengths in terms of # subjects

input:
A, B, C, D, E, F, G, H # 8 elements, 8/3 -> 2.66 -> 3
# 14 elements -> 4. -> 5



output:
A, D, G, B, E, H, C, F

Fruits
-------
Apple       Durian      Grape
Banana      Eggplant    Huckleberry
Cherry      Fig

# high level: take a sorted list and return a shuffled list that reads column by column for three columsn
1, 2, 3, 4
interval = 2
startVal = 0
output(1, 3, 5)
starVal = 1
output(1, 3, 5, 2, 4, 6)

1  3
2  4

1   3   4
2

1   4    6
2   5    7
3

def shuffle(arr, numCols):
  interval = Math.ceil(len(arr)/numCols)
  output = []
  for startVal in range(interval):
    i = startVal
    # at different startvals, add the next row to the output
    while i < len(arr):
      output.append(arr[i])
      i+=interval
      
  return output
