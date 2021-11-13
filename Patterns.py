#Number triangle
rows = 9

b = -1

for i in range(rows, 0, -1):

    b += 1

    for j in range(1, i + 1):

        print(b, end= " ")

    print("\r")
    
#Star
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)


#Pyramid
# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)


#Heart
# define size n = even only
n = 8

# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n+1

# loops for upper part
for i in range(n//2-1):
	for j in range(m):
		
		# condition for printing stars to GFG upper line
		if i == n//2-2 and (j == 0 or j == m-1):
			print("*", end=" ")
			
		# condition for printing stars to left upper
		elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
							or (j-i == m//2-n//2+3 and j > m//4)):
			print("*", end=" ")
			
		# condition for printing stars to right upper
		elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
						or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
			print("*", end=" ")
			
		# condition for printing spaces
		else:
			print(" ", end=" ")
	print()

# loops for lower part
for i in range(n//2-1, n):
	for j in range(m):
		
		# condition for printing stars
		if (i-j == n//2-1) or (i+j == n-1+m//2):
			print('*', end=" ")
			
		# condition for printing spaces
		else:
			print(' ', end=" ")
			
	print()
