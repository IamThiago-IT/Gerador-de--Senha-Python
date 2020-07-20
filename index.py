#gerador de senhas
from random import choice
print('#'*30)
print("{:^}".format("Gerador de senhas"))
print("#"*30)
while True:
  print('{:^30}'.format('A senha gerada é:'))
    for i in range(10):
      dic = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", 
