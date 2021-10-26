"""
Regras do Fizbuzz

1. Se a posição  for múltipla de 3: fizz
2. se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número

"""
def robot(pos):
    say = str(pos)
    if pos % 3 == 0 and pos % 5 == 0:
        say ='fizzbuzz'
    elif pos % 5 == 0:
        say ='buzz'
    elif pos % 3 == 0:
        say ='fizz'
    return say


    return str(pos)

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'
    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'
    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'