# This script belongs to Nasib Huseynzade, 10.05.2022

def isPrime(n): #Simple function in order to determine whether number is prime or not

    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
        return True
    else:
        return False 


def  maximumSum(matrice): #maximum path function for all triangle matrices
  
    m=len(matrice)

    for i in range(0,m,1): # operation for eliminating prime numbers of matrice

        for j in range(0,i+1,1):

            if isPrime(matrice[i][j])==True:
                
                matrice[i][j]=0

    for i in range(0,m,1): # if there are neighbor zeros, corresponding element of upper raw must be zero

        for j in range(1,i,1):
            
            if (matrice[i][j-1]==0 and matrice[i][j]==0):

                matrice[i-1][j-1]=0

    for i in range(m-2, -1, -1): #main loop - from bottom to top 

        for j in range(0,i+1,1):

            matrice[i][j]+=max(matrice[i+1][j],matrice[i+1][j+1])
          
    return matrice[0][0] #end of function
