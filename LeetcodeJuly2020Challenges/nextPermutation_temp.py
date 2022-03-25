inputs = [1,3,2]
if len(inputs) < 2:
    print(inputs)
else:
    i = len(inputs) - 2
    j = len(inputs) - 2
    print("i = ",i)
    print("j = ",j)
    while i > -1:
        if inputs[i] < inputs[-1]:
            print("found position to change!")
            while inputs[i] < inputs[j]:
                j = j - 1
                print("j = ",j)
            inputs[i], inputs[j+1] = inputs[j+1], inputs[i]
            print("swap ",inputs)
        else:
            inputs.append(inputs.pop(i))
            print("sort ",inputs)
        i = i - 1
        print("i = ",i)
