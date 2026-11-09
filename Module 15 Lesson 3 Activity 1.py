s=[1, 3, 5, 7, 9, 11, 13, 15, 17]
input("List: " + str(s) + " n=9 Press Enter to continue...")
g=int(input("Max checks to find any number in the list: "))
t=int(input("Pick a number from the list: "))

input("Checking the number through Binary Search... Press Enter to continue...")
l, h=0, len(s) - 1
st=0
while l <= h:
    m=(l+h)//2
    st+=1
    print("Round: ", s," - checked", s[m])
    if s[m] == t:
        break
    elif s[m] < t:
        l=m+1
    else:
        h=m-1
print("Found ", t, "in position", m+1, "after", st, "steps.")
