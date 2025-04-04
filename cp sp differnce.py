CP = int(input("Enter Cp"))
SP = int(input("ENter SP"))
if CP>SP:
     Loss = CP-SP
     print("Loss",Loss)
else:
    profit = SP-CP    
    print("profit",profit)
