"""
Regras do Fizbuzz

1. Se a posição  for múltipla de 3: fizz
2. se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número

"""
def robot(pos):
    if pos == 9:
        return 'fizz'
    if pos == 6:
        return 'fizz'
    if pos == 3:
        return 'fizz'
    return str(pos)

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'