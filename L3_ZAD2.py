def ordinary_polynomial_value_calc(coeff, arg):
  """Function calculate w(x) where w is polynomial
  @pam coeff : (list) list of coefficient of polynomial (first is a_0)
  @pam arg: (float) argument of function
  @return value: (float) value of this polynomial
  @return count_mult: (int) number how many multiplicatio was done
  @return count_add: (int) number how many adds was done
  """
  # w ciele tej funkcji zawrzyj kod wyliczający wartość wielomianu w tradycyjny sposób;
  # argument 'coeff' niech będzie listą współczynników wielomianu w kolejności od stopnia zerowego (wyrazu wolego) wzwyż;
  # argument 'arg' niech będzie punktem, w którym chcemy policzyć wartość wielomianu;
  # w zmiennej 'count_mult' zwróć liczbę mnożeń, jakie zostału wykonane do uzyskania tego wyniku;
  # w zmiennej 'count_add' zwróć liczbę dodawań, jakie zostału wykonane do uzyskania tego wyniku;
  value = coeff[0]
  before = arg
  count_mult = 0
  count_add = 0
  for coef in coeff[1:]:
    value += coef * before
    before *= arg
    count_add += 1
    count_mult += 2
  return value, count_mult, count_add
  
def smart_polynomial_value_calc(coeff, arg):
  """Function calculate w(x) where w is polynomial using horner scheme
  @pam coeff : (list) list of coefficient of polynomial (first is a_0)
  @pam arg: (float) argument of function
  @return value: (float) value of this polynomial
  @return count_mult: (int) number how many multiplicatio was done
  @return count_add: (int) number how many adds was done
  """
  # w ciele tej funkcji zawrzyj kod wyliczający wartość wielomianu w sposób maksymalnie ograniczający liczbę wykonywanych mnożeń;
  # argument 'coeff' niech będzie listą współczynników wielomianu w kolejności od stopnia zerowego (wyrazu wolego) wzwyż;
  # argument 'arg' niech będzie punktem, w którym chcemy policzyć wartość wielomianu;
  # w zmiennej 'count_mult' zwróć liczbę mnożeń, jakie zostału wykonane do uzyskania tego wyniku;
  # w zmiennej 'count_add' zwróć liczbę dodawań, jakie zostału wykonane do uzyskania tego wyniku;

  value = coeff[-1] 
  count_mult = 0
  count_add = 1
  for n in range( len(coeff) - 2, -1, -1):
    value *= arg
    value += coeff[n] 
    count_add += 1
    count_mult += 1
    

  
  return value, count_mult, count_add
  
  
# jeśli potrzebujesz, możesz dopisać również inne funkcje (pomocnicze), 
# jednak główne cele zadania muszą być realizowane w powyższych dwóch funkcjach;

if __name__ == "__main__":
  print(ordinary_polynomial_value_calc([0,1,4,5,6], 0))
  print(ordinary_polynomial_value_calc([0,1,4,5,6], 2))
  print(smart_polynomial_value_calc([0,1,4,5,6], 0))
  print(smart_polynomial_value_calc([0,1,4,5,6], 2))