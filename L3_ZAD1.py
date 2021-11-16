

def probability(n, k, p):
  """Fuction count propability of less or k sucess in n attempts
  @pam n: (int) number of attempts
  @pam k: (int) number of max success in n attempts
  @pam p: (float) propability of single sucess
  @return prob: (float) propability of less or k sucess in n attempts
  @return count_mult: (int) number how many multiplicatio was done
  """
  # w ciele funkcji umieść swój kod realizujący cel zadania;
  # argument 'n' niech będzie liczbą prób;
  # argument 'k' niech będzie maksymalną liczbą sukcesów;
  # argument 'p' niech będzie prawdpodobieństwem sukcesu w pojedynczej próbie;
  # w zmiennej 'prob' zwróć oczekiwane prawdopodobieństwo;
  # w zmiennej 'count_mult' zwróć liczbę mnożeń, jaką wykonał Twój program;
  # jeśli potrzebujesz, możesz dopisać również inne funkcje (pomocnicze), 
  # jednak główny cel zadania musi być realizowany w tej funkcji;

  def to_n_pow(base, pow, count_mult):
    result = 1
    while pow:
      if pow % 2 == 0:
        pow //= 2
        base *= base
        count_mult += 3
      else:
        pow //= 2
        result *= base
        base *= base
        count_mult += 3
    return result , count_mult

  prob = 0
  count_mult = 0
  if k == n:
    return 1, 0
  elif k > n // 2: # in this case we use opposite event
    m = n-k 
    factor_p = (1-p)/p
    count_mult += 1
    single_probabilitis = [1 for i in range(0,m)]
    single_probabilitis[0] , count_mult = to_n_pow(p, n, count_mult)
    for i in range(0,m-1):
      single_probabilitis[i+1] = single_probabilitis[i] * factor_p * (n-i)/(i+1)
      count_mult += 3
    prob = 1 - sum(single_probabilitis)
  else:
    m = k
    factor_p = p/(1-p)
    count_mult += 1
    single_probabilitis = [1 for i in range(0,m+1)]
    single_probabilitis[0], count_mult = to_n_pow((1-p), n, count_mult) 
    for i in range(0,m):
      single_probabilitis[i+1] = single_probabilitis[i] * factor_p * (n-i)/(i+1)
      count_mult += 3
    prob = sum(single_probabilitis)

  
  return (prob, count_mult)

if __name__ == "__main__":
  print(probability(1000,1000,0.5))
  print(probability(1000,0,0.001))
  print(probability(100,50,0.6))
  print(probability(10,9,0.9))



