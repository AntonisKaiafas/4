string = input("Δώσε μία πρόταση:")
def trans(string):
    
    x = 0
    for c in string:
        x = x + ord(c)

    print("Το 'string' μεταφρασμένο σε αριθμό σύμφωνα με τον κώδικα ASCII ειναι:",x)
    if x%2==1:
        print("Ο αριθμός είναι πρώτος")
    else:
        print("Ο αριθμός δεν είναι πρώτος")
    
    
trans(string)
