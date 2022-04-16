A = input("Enter a or b = ")

count = 0

for i in range (len(A)) :

    count += A[i:i+1] == "b"

if count <= 2 :
    print("good")

else :
    print("bad")

