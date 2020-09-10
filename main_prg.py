#CryptoArithmetic puzzle solver
#For two words
#operations = addition and subtraction

word1 = input('Enter first word: ')
word2 = input('Enter second word: ')
word3 = input('Enter the result word: ')
global operation
operation = input('Choose operation(default = 1):\n1] Sum(word1 + word2 = word3)\n2]Difference(word1 - word2 = word3)')
if operation == '2':
    temp = word3
    word3 = word1
    word1 = temp
dict_var = { var :  None for var in set(word1+word2+word3)}
val_available = [i for i in range(10)]

def display(w1_n1,w2_n2,w3_n3):
    global operation
    if operation == '2':
        print('\nOperation: Difference')
        print(f'{w3_n3} - {w2_n2} = {w1_n1}')
    else:
        print('\nOperation: Sum')
        print(f'{w1_n1} + {w2_n2} = {w3_n3}')

def check(word1,word2,word3,dict_var):
    # print('check running')
    m=1
    w1_n1 = 0
    for i in range(len(word1)-1,-1,-1):
        w1_n1 +=m* dict_var[word1[i]]
        m*=10

    m=1
    w2_n2 = 0
    for i in range(len(word2)-1,-1,-1):
        w2_n2 +=m* dict_var[word2[i]]
        m*=10

    m=1
    w3_n3 = 0
    for i in range(len(word3)-1,-1,-1):
        w3_n3 +=m* dict_var[word3[i]]
        m*=10

    if w3_n3 == (w1_n1 + w2_n2):
        display(w1_n1,w2_n2,w3_n3)
        return True
    return False


def recursive_assignment(word1,word2,word3,dict_var,n):
    # print('recursion running')
    # print(dict_var)
    #base case
    if n == len(dict_var)-1:
        # print('base case running')
        for i in range(10):
            if i in val_available:
                #generally digit at highest place value is not 0
                if i ==0 and (list(dict_var)[n] == word1[0] or list(dict_var)[n] == word2[0] or list(dict_var)[n] == word3[0]):
                    continue
                dict_var[list(dict_var)[n]] = i
                if check(word1,word2,word3,dict_var):
                    return True
        return False
    for i in range(10):
        if i in val_available:
            #generally digit at highest place value is not 0
            if i ==0 and (list(dict_var)[n] == word1[0] or list(dict_var)[n] == word2[0] or list(dict_var)[n] == word3[0]):
                    continue
            dict_var[list(dict_var)[n]] = i
            val_available.remove(i)
            if recursive_assignment(word1,word2,word3,dict_var,n+1):
                return True
            val_available.append(i)
    return False




def cryptoarithmetic_solver(word1,word2,word3,dict_var):
    if len(dict_var) > 10:
        print('Invalid Encrypted Strings')
        return False
    return recursive_assignment(word1,word2,word3,dict_var,0)  #0 denotes first index


if cryptoarithmetic_solver(word1,word2,word3,dict_var):
    print(dict_var)
else:
    print('No solution')


