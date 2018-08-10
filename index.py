def firtstEmptySlotFinder (arr) :
    n=len(arr)
    print(n)

    start=-1
    end=-1
    i=0

    while i<n:
        print('i=',i)
        if arr[i]==0:
            start=i
            end=start
            if len(arr)==1:
                return start,end+1
            elif arr[i+1]!=0:
                return start,end+1
            j=i+1
            if j<=n:
                while arr[j] == 0 and j < n:
                    print('j=', j)
                    end = j
                    j = j + 1
                    if j>=n:
                        break

            return start, end+1

        i=i+1
    return start,end+1

def slotsFittingChecker(a,b,requiredSlots):
    if(a-b)>=requiredSlots or (b-a)>=requiredSlots:
        print('yes , these are enough slots for our task')
        return 1
    print('not enough slots for our task')
    return 0


def main():
    aa=[0,0,0,0,1]

    s,e=firtstEmptySlotFinder(aa)
    print(s,e)
    x=slotsFittingChecker(s,e,44)



main()