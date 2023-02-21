from queue import LifoQueue
print("Stack Example\n")
loopCtrl = 1
while loopCtrl == 1:
    loopCtrl = 2
    choice = int(input("Choose your function:\n\t1. Add Item\n\t2. Take Out Item\n\t3. Check If Full\n\t4. Check If Full\n\t5. Check Top Item\n>"))
    if choice == 1:
        stack = LifoQueue(maxsize=5)
        itemToAdd = input("Enter the Item you would like to add:\n> ")
        stack.put(itemToAdd)
        print(f"Current Stack: {stack}")