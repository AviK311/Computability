try:
   from sympy import prime
except:
   primes = []

   def initialize_saved_primes():
      with open("saved_primes.txt", 'w') as saved_primes:
         saved_primes.write("[2,3]")
         primes = [2,3]

   def prime(n):
      index = n-1
      current_len = len(primes)
      if index < current_len:
         return primes[index]
      else:
         check = primes[-1]+2
         if check%2 == 0:
            raise Exception("There is a problem with the saved_primes file")
         found = 0
         while found < n - current_len:
            if is_prime(check):
               primes.append(check)
               found += 1
            check += 2
         f = open("saved_primes.txt", 'w')
         f.write(str(primes))
         f.close()
         return primes[index]
      
         


   def is_prime(num):
      if num in primes:
         return True
      i = 2
      while i**2 <= num:
         if num%i == 0:
            return False
         i+=1
      return True
      
          

   with open("saved_primes.txt", 'r') as saved_primes:
      try:
         primes = eval(saved_primes.readline())
      except:
         initialize_saved_primes()


    
