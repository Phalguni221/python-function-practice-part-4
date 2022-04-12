#Maximum number
def max_num(a, b, c):
    return max([a, b, c])
        
print(max_num(1,2,3))

#Multiple List 
def mult_list(a, b, c):
   answer = a * b * c
   return answer

print(mult_list(1,2,3))

print(mult_list(2,3,4))

#Reverse String 
def rev_string(txt):
 return txt[::-1]

print(rev_string("Hello World"))

#Range function
def num_within(a,b,c):
    return a in range(b-1, c+3)

print(num_within(3,2,4))

#Pascal's Triangle
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)

pascal(5)

pascal(10)


