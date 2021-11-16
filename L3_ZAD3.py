
def counting_chars_without_ifs(filename):
  """Fuction count numers of chars in given filename
  @pam filename: (str) path to file with text
  @return char_count: (dict) dictionary with numbers of chars in text"""
  with open(filename, 'r') as file_ref:
    text = file_ref.read()
    words = text.lower()
    char_count = {}
    letters = set(words) - set(' \n \t')
  for letter in letters:
    char_count[letter] = words.count(letter)

    
  # uzupełnij ciało tej funkcji kodem realizującym cel zadania;
  # w zmiennej 'char_count' zwróć słownik zawierający wszystkie znaki tekstu 
  # jako klucze i ich liczebnoć jako wartości np. {'a': 6, 'b': 2 ...};
  # jeli potrzebujesz, możesz dopisać również inne funkcje (pomocnicze), 
  # jednak główny cel zadania musi być realizowany w tej funkcji;
  return char_count

if __name__ == "__main__":
  print(counting_chars_without_ifs('C:\\Users\\mkarc\\studia\\AISD\\lista3\\L3_ZAD3_sample_text.txt'))