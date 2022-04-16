A = input("Enter a or b = ")

stat = "q0"

for i in range (len(A)) :

    if stat == "q0" and A[i] == "a" :
        stat = "q1"

    elif stat == "q0" and A[i] == "b" :
        stat = "q4"

    elif stat == "q1" and A[i] == "a" :
        stat = "q4"

    elif stat == "q1" and A[i] == "b" :
        stat = "q2"

    elif stat == "q2" and A[i] == "b" :
        stat = "q4"

    elif stat == "q2" and A[i] == "a" :
        stat = "q3"

if stat == "q3" :
    print ("good")

else :
    print ("bad")
