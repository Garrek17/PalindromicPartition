#Palindromic Partitioning Exercise: Given a string input,
#print every partition of the string such that each partition
#is a palindrome.
def palindromicRecursion(input, output):

    #end condition
    if len(input)<1:
        print(output)

    for j in range(1,len(input)+1):

        cur = input[0:j]
        #test if palindrome valid
        leftIndex=0
        rightIndex=len(cur)-1
        bool=1
        while rightIndex>leftIndex:
            if cur[leftIndex]!=cur[rightIndex]:
                bool=0
                break
            leftIndex=leftIndex+1
            rightIndex=rightIndex-1

        #if palindrone is valid condition
        if bool==1:
            palindromicRecursion(input[j:], output + " (" + cur + ")")

#Test Code
palindromicRecursion("boolaboolaboola","")




