# Nasib Huseynzade P.I.Works Junior Software Developer Application

def isPrime(n): #Simple function in order to determine whether number is prime or not

    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
        return True
    else:
        return False 



def  maximumSum(matrice): #maximum path function for all triangle matrices
  
    k=0 #optimal column index
    m=len(matrice)
    our_list=[matrice[0][0]]

    for i in range(0,m,1): # operation for eliminating prime numbers of matrice

        for j in range(0,i+1,1):

            if isPrime(matrice[i][j])==True:
                
                matrice[i][j]=0

    for i in range(1,m,1):

        for j in range(0,i+1,1):

            if matrice[i][j]==max(matrice[i][k],matrice[i][k+1]):
                
                our_list.append(matrice[i][j])
                k=j
                break
    
    return  our_list, sum(our_list)


our_matrice=[
[215],
[193, 124],
[117, 237, 442],
[218, 935, 347, 235],
[320, 804, 522, 417, 345],
[229, 601, 723, 835, 133, 124],
[248, 202, 277, 433, 207, 263, 257],
[359, 464, 504, 528, 516, 716, 871, 182],
[461, 441, 426, 656, 863, 560, 380, 171, 923],
[381, 348, 573, 533, 447, 632, 387, 176, 975, 449],
[223, 711, 445, 645, 245, 543, 931, 532, 937, 541, 444],
[330, 131, 333, 928, 377, 733, 17, 778, 839, 168, 197, 197],
[131, 171, 522, 137, 217, 224, 291, 413, 528, 520, 227, 229, 928],
[223, 626, 34, 683, 839, 53, 627, 310, 713, 999, 629, 817, 410, 121],
[924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]]



'''our_matrice = [[1],
                [8,4],
                [2,6,9],
                [8,5,9,3]]'''

print(maximumSum(our_matrice))
