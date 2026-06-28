numbers=[]
def get_numbers():
   
    n=int(input("enter number of elements:"))
 
    for i in range(n):
       i=int(input("enter element"))
       numbers.append(i)
    print(numbers)

def display():
    print("Original list:",numbers)

def rev_list():
    numbers.reverse()
    print("reversed list",numbers)

def largest_no():
    largest =numbers[0]
    for i in numbers:
        if i > largest:
            largest =i
    print("Largest number: ",largest)

def main():
  
    get_numbers()

  
    display()


    rev_list()

    largest_no()

main()   




   



