
def main():
    
    """input"""
    print("Select the input file:")
    #input_file = input()
    input_file = "input.txt"
    with open(input_file, 'r') as file:
        arr = []
        sums = []
        line = file.readline()
        n, m = line.split()
        n = int(n)
        m = int(m)
        i = 0
        for line in file:
            if i < 10 :
                arr.append(int(line))
                i += 1
            else:
                sums.append(int(line))
                
    print(f"your array: {arr}")
    
    """hash tables creation"""
    chained_div = chained_div_hash(100)
    print("chained_div_hash")
    for a in arr:
        chained_div.insert(a)
    print(f"Have {chained_div.collisions} collisions")
    for s in sums:
        print(f"{s} = ", end = "")
        i = 0
        for a in arr:
            i += 1
            if chained_div.search(s-a):
                print(f"{a} + {s-a}")
                break
            elif i == len(arr):
                 print("0 0")
    print()
    
    chained_mult  = chained_mult_hash(100)
    print("chained_mult_hash")
    for a in arr:
        chained_mult.insert(a)
    print(f"Have {chained_mult.collisions} collisions")
    for s in sums:
        print(f"{s} = ", end = "")
        i = 0
        for a in arr:
            i += 1
            if chained_mult.search(s-a):
                print(f"{a} + {s-a}")
                break
            elif i == len(arr):
                 print("0 0")

    print()
    
    adress_liniar = adress_liniar_hash(3 * len(arr))
    print("adress_liniar")
    for a in arr:
        adress_liniar.insert(a)
    print(f"Have {adress_liniar.collisions} collisions")
    for s in sums:
        print(f"{s} = ", end = "")
        i = 0
        for a in arr:
            i += 1
            if adress_liniar.search(s-a):
                print(f"{a} + {s-a}")
                break
            elif i == len(arr):
                 print("0 0")

    print()
    
    adress_quadric = adress_quadric_hash(3 * len(arr))
    print("adress_quadric")
    for a in arr:
        adress_quadric.insert(a)
    print(f"Have {adress_quadric.collisions} collisions")
    for s in sums:
        print(f"{s} = ", end = "")
        i = 0
        for a in arr:
            i += 1
            if adress_quadric.search(s-a):
                print(f"{a} + {s-a}")
                break
            elif i == len(arr):
                 print("0 0")

    print()
    adress_double = adress_double_hash(3 * len(arr))
    print("adress_double")
    for a in arr:
        adress_double.insert(a)
    print(f"Have {adress_double.collisions} collisions")
    for s in sums:
        print(f"{s} = ", end = "")
        i = 0
        for a in arr:
            i += 1
            if adress_double.search(s-a):
                print(f"{a} + {s-a}")
                break
            elif i == len(arr):
                 print("0 0")
                   

class chained_hash():
    
    def __init__(self, n):
        self.n = n
        self.arr = [None for i in range(n)]
        self.collisions = 0
        
    def hash_func(self, a):
        return 0
    
    def insert(self, a):
        if self.search(a):
            self.collisions += 1
        else:
            self.arr[self.hash_func(a)] = a
            
       
    def search(self, a):
        if self.arr[self.hash_func(a)] != None:
            return True
        else:
            return False

class chained_div_hash(chained_hash):
    
    def hash_func(self, a):
        return a % self.n
    
class chained_mult_hash(chained_hash):

    def hash_func(self, a):
        A = float(0.6180339887498948)
        return int(self.n * ((a * A) % 1))
    
class adress_hash():

    def __init__(self, n):
        self.n = n
        self.arr = [None for i in range(n)]
        self.collisions = 0
        
    def hash_func(self, a, i):
        return 0 
    
    def insert(self, a):
        i = 0
        while i != self.n:
            j = self.hash_fun(a, i)
            if self.arr[j] == None:
                self.arr[j] = a
                check = True
                break
            else:
                self.collisions += 1
                i += 1
        if not check:
            print("Table is full")

    def search(self, a):
        i = 0
        j = self.hash_fun(a, i)
        while i != self.n and self.arr[j] != None:
            j = self.hash_fun(a, i)
            if self.arr[j] == a :
                return True
            else:
                i += 1
        return False
    
class adress_liniar_hash(adress_hash):

    def help_fun(self, a):
        return a % self.n
    
    def hash_fun(self, a, i):
        return(self.help_fun(a) + i) % self.n

class adress_quadric_hash(adress_hash):

    def help_fun(self, a):
        return a % self.n
    
    def hash_fun(self, a, i):
        c1 = 2
        c2 = 1
        return(self.help_fun(a) + c1 * i + c2 * i * i) % self.n
    
class adress_double_hash(adress_hash):

    def help_fun_1(self, a):
        return a % self.n
    
    def help_fun_2(self, a):
        return a % self.n + 1
    
    def hash_fun(self, a, i):
        c1 = 2
        c2 = 1
        return(self.help_fun_1(a) + self.help_fun_2(a) * i ) % self.n
        
main()
