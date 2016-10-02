n = int(input("Type a number:"))
if (n%2) == 0:
    nextnumb = n/2
else:
    nextnumb = 3 * n + 1
print ("The next number in the sequence is " + str(nextnumb))
