
```markdown
# Riferimento alle Funzioni Built-in di Python (con Esempi)

> **Nota**: `frozendict` e `sentinel` **non** sono attualmente funzioni built-in standard nelle versioni mainstream di Python (Python 3.14 e precedenti). `frozendict` è una funzionalità proposta nella PEP 814 (prevista per Python 3.15), e `sentinel` è proposta nella PEP 661. Gli esempi sotto per queste due si basano sulle specifiche delle proposte e potrebbero richiedere librerie di terze parti o versioni future di Python per funzionare.

---

## A

### `abs(x)`
Restituisce il valore assoluto di un numero.

```python
abs(-5)          # 5
abs(3.14)        # 3.14
abs(-2 + 3j)     # 3.605551275463989
abs(0)           # 0
```

### `aiter(async_iterable)`

Restituisce un iteratore asincrono per un iterabile asincrono (Python 3.10+).

```python
async def demo():
    async def agen():
        yield 1
        yield 2
    async for x in aiter(agen()):
        print(x)
# Output: 1, 2
```

### `all(iterable)`

Restituisce `True` se tutti gli elementi sono veri (o se l'iterabile è vuoto).

```python
all([True, True, True])    # True
all([True, False, True])   # False
all([])                    # True
all([1, 2, 3])             # True
```

### `anext(async_iterator, default)`

Restituisce il prossimo elemento da un iteratore asincrono (Python 3.10+).

```python
async def demo():
    ait = aiter([1, 2, 3])
    print(await anext(ait))        # 1
    print(await anext(ait))        # 2
    print(await anext(ait))        # 3
    print(await anext(ait, 'fine')) # 'fine'
```

### `any(iterable)`

Restituisce `True` se almeno un elemento è vero.

```python
any([False, False, True])   # True
any([False, False])         # False
any([])                     # False
any([0, 1, 2])              # True
```

### `ascii(object)`

Restituisce una rappresentazione stampabile con i caratteri non-ASCII codificati.

```python
ascii('café')       # "'caf\\xe9'"
ascii('hello')      # "'hello'"
ascii('日本語')      # "'\\u65e5\\u672c\\u8a9e'"
ascii([1, 'é'])     # "[1, '\\xe9']"
```

---

## B

### `bin(integer)`

Converte un intero in una stringa binaria con prefisso `"0b"`.

```python
bin(3)      # '0b11'
bin(-10)    # '-0b1010'
bin(0)      # '0b0'
bin(255)    # '0b11111111'
```

### `bool(object=False)`

Restituisce un valore booleano usando la verifica di verità standard.

```python
bool(0)       # False
bool(1)       # True
bool([])      # False
bool('abc')   # True
```

### `breakpoint(*args, **kws)`

Entra nel debugger nel punto di chiamata.

```python
# breakpoint()                    # entra in pdb
# breakpoint('messaggio')         # passa args a sys.breakpointhook
# breakpoint(header='Debug')      # con argomenti keyword
# breakpoint()                    # disabilitabile con PYTHONBREAKPOINT=0
```

### `bytearray(source=b'')`

Restituisce un nuovo array di byte mutabile.

```python
bytearray(5)                # bytearray(b'\x00\x00\x00\x00\x00')
bytearray(b'abc')           # bytearray(b'abc')
bytearray('hi', 'utf-8')    # bytearray(b'hi')
bytearray([65, 66, 67])     # bytearray(b'ABC')
```

### `bytes(source=b'')`

Restituisce un nuovo oggetto bytes immutabile.

```python
bytes(5)                # b'\x00\x00\x00\x00\x00'
bytes('hi', 'utf-8')    # b'hi'
bytes([65, 66, 67])     # b'ABC'
bytes(b'abc')           # b'abc'
```

---

## C

### `callable(object)`

Restituisce `True` se l'oggetto è chiamabile.

```python
callable(print)       # True
callable(42)          # False
callable(lambda: 1)   # True
callable(str)         # True
```

### `chr(i)`

Restituisce la stringa che rappresenta un carattere il cui code point Unicode è `i`.

```python
chr(65)     # 'A'
chr(97)     # 'a'
chr(8364)   # '€'
chr(0x1F600) # '😀'
```

### `classmethod(function)`

Restituisce un metodo di classe per la funzione.

```python
class C:
    @classmethod
    def f(cls, x):
        return cls.__name__, x

C.f(1)          # ('C', 1)
C().f(2)        # ('C', 2)
```

### `compile(source, filename, mode)`

Compila il codice sorgente in un oggetto codice.

```python
code = compile('x = 1 + 2', '<string>', 'exec')
exec(code)  # x ora vale 3
eval(compile('3 * 4', '<string>', 'eval'))  # 12
compile('print(1)', '<test>', 'single')     # oggetto codice
```

### `complex(real=0, imag=0)`

Crea un numero complesso.

```python
complex(3, 4)     # (3+4j)
complex('2+3j')   # (2+3j)
complex(5)        # (5+0j)
complex()         # 0j
```

---

## D

### `delattr(object, name)`

Elimina un attributo da un oggetto.

```python
class C: pass
c = C()
c.x = 10
delattr(c, 'x')
# c.x ora solleva AttributeError

delattr(C, '__doc__')  # rimuove la docstring della classe
delattr(c, 'y')        # AttributeError se y non esiste
```

### `dict(**kwargs)`

Crea un nuovo dizionario.

```python
dict(a=1, b=2)              # {'a': 1, 'b': 2}
dict([('x', 1), ('y', 2)])  # {'x': 1, 'y': 2}
dict({'k': 'v'})            # {'k': 'v'}
dict(zip('ab', [1, 2]))     # {'a': 1, 'b': 2}
```

### `dir(object)`

Restituisce una lista degli attributi validi per l'oggetto.

```python
dir()           # lista dei nomi nello scope corrente
dir([])         # metodi di list (append, extend, ecc.)
dir('hello')    # metodi di str
dir(int)        # attributi della classe int
```

### `divmod(a, b)`

Restituisce `(a // b, a % b)`.

```python
divmod(10, 3)   # (3, 1)
divmod(10, -3)  # (-4, -2)
divmod(10.5, 3) # (3.0, 1.5)
divmod(-10, 3)  # (-4, 2)
```

---

## E

### `enumerate(iterable, start=0)`

Restituisce un oggetto enumerate che produce coppie `(indice, valore)`.

```python
list(enumerate(['a', 'b', 'c']))        # [(0, 'a'), (1, 'b'), (2, 'c')]
list(enumerate('xy', start=1))          # [(1, 'x'), (2, 'y')]
for i, v in enumerate([10, 20]): pass   # i=0,v=10; i=1,v=20
list(enumerate((), 5))                  # []
```

### `eval(expression, globals=None, locals=None)`

Valuta un'espressione Python.

```python
eval('2 + 3')                   # 5
eval('"a" * 3')                 # 'aaa'
eval('x * 2', {'x': 10})        # 20
eval('len([1,2,3])')            # 3
```

### `exec(object, globals=None, locals=None)`

Esegue codice creato dinamicamente.

```python
exec('x = 10')
exec('for i in range(2): print(i)')  # stampa 0, 1
exec('y = 5 * 2', {})
# il codice nel dizionario globals ora ha y=10
```

---

## F

### `filter(function, iterable)`

Costruisce un iteratore dagli elementi per cui `function` restituisce vero.

```python
list(filter(None, [0, 1, 2, '', 'a']))       # [1, 2, 'a']
list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]
list(filter(str.isdigit, 'a1b2c3'))          # ['1', '2', '3']
tuple(filter(lambda x: x % 2 == 0, range(6))) # (0, 2, 4)
```

### `float(x=0.0)`

Restituisce un numero in virgola mobile.

```python
float(3)            # 3.0
float('3.14')       # 3.14
float('   -1e3  ')  # -1000.0
float()             # 0.0
```

### `format(value, format_spec='')`

Converte un valore in una rappresentazione formattata.

```python
format(3.14159, '.2f')      # '3.14'
format(255, 'x')            # 'ff'
format(255, '#b')           # '0b11111111'
format('hello', '>10')      # '     hello'
```

### `frozendict(iterable=())`

**⚠️ Non è una built-in standard in Python 3.14 e precedenti.** Dizionario immutabile proposto nella PEP 814.

```python
# Sintassi ipotetica / futura (Python 3.15+)
frozendict()                  # frozendict vuoto
frozendict(a=1, b=2)          # da kwargs
frozendict({'x': 1})          # da dict
frozendict([('k', 'v')])      # da tuple chiave-valore
```

### `frozenset(iterable=())`

Restituisce un nuovo oggetto frozenset.

```python
frozenset()                    # frozenset()
frozenset([1, 2, 3])           # frozenset({1, 2, 3})
frozenset('abc')               # frozenset({'a', 'b', 'c'})
frozenset({'a': 1, 'b': 2})    # frozenset({'a', 'b'})
```

---

## G

### `getattr(object, name, default)`

Restituisce il valore di un attributo con nome.

```python
class C: x = 10
getattr(C, 'x')          # 10
getattr(C, 'y', 0)       # 0
getattr('hello', 'upper')()  # 'HELLO'
getattr(C, 'z', None)    # None
```

### `globals()`

Restituisce il dizionario che implementa il namespace globale corrente.

```python
globals()               # dizionario del namespace globale corrente
x = 10
globals()['x']          # 10
'x' in globals()        # True
globals()['new_var'] = 5 # imposta una variabile globale
```

---

## H

### `hasattr(object, name)`

Restituisce `True` se l'oggetto ha l'attributo con nome.

```python
hasattr('hello', 'upper')   # True
hasattr('hello', 'foo')     # False
hasattr([], 'append')       # True
hasattr(1, 'bit_length')    # True
```

### `hash(object)`

Restituisce il valore hash di un oggetto.

```python
hash('hello')       # un intero
hash(42)            # 42
hash((1, 2, 3))     # un intero
hash(frozenset([1])) # un intero
```

### `help(request)`

Invoca il sistema di aiuto integrato.

```python
help()              # aiuto interattivo
help(str)           # aiuto sulla classe str
help('modules')     # lista dei moduli
help(print)         # aiuto sulla funzione print
```

### `hex(x)`

Converte un intero in una stringa esadecimale minuscola con prefisso `"0x"`.

```python
hex(255)    # '0xff'
hex(16)     # '0x10'
hex(-5)     # '-0x5'
hex(0)      # '0x0'
```

---

## I

### `id(object)`

Restituisce l'identità (indirizzo di memoria in CPython) di un oggetto.

```python
id(1)           # un intero
id('hello')     # un intero
id([])          # un intero
id(None)        # un intero
```

### `input(prompt='')`

Legge una riga dall'input, convertendola in stringa.

```python
# name = input('Nome: ')          # mostra il prompt e legge
# num = int(input('Numero: '))    # legge e converte
# input()                         # legge senza prompt
# input('Premi Invio: ')          # attende Invio
```

### `int(x=0, base=10)`

Restituisce un oggetto intero.

```python
int(3.9)          # 3 (tronca)
int('42')         # 42
int('ff', 16)     # 255
int('1010', 2)    # 10
```

### `isinstance(object, classinfo)`

Restituisce `True` se l'oggetto è un'istanza di classinfo.

```python
isinstance(42, int)            # True
isinstance('a', (int, str))    # True
isinstance(3.14, int)          # False
isinstance(True, int)          # True (bool è sottoclasse di int)
```

### `issubclass(class, classinfo)`

Restituisce `True` se class è una sottoclasse di classinfo.

```python
issubclass(bool, int)           # True
issubclass(int, object)         # True
issubclass(str, (int, str))     # True
issubclass(float, int)          # False
```

### `iter(object, sentinel)`

Restituisce un oggetto iteratore.

```python
iter([1, 2, 3])              # list_iterator
iter('abc')                  # str_iterator
iter({'a': 1})               # dict_keyiterator
iter(lambda: 1, 0)           # callable_iterator (si ferma a 0)
```

---

## L

### `len(s)`

Restituisce il numero di elementi in un contenitore.

```python
len('hello')       # 5
len([1, 2, 3])     # 3
len({'a': 1})      # 1
len(range(10))     # 10
```

### `list(iterable=())`

Crea una nuova lista.

```python
list()              # []
list('abc')         # ['a', 'b', 'c']
list(range(3))      # [0, 1, 2]
list({'a': 1})      # ['a']
```

### `locals()`

Restituisce un dizionario del namespace locale corrente.

```python
def f():
    x = 10
    return locals()   # {'x': 10}

locals()              # scope locale corrente
def g(a, b): return locals()  # {'a': ..., 'b': ...}
```

---

## M

### `map(function, iterable, ...)`

Restituisce un iteratore che applica function a ogni elemento.

```python
list(map(str, [1, 2, 3]))          # ['1', '2', '3']
list(map(lambda x: x*2, [1, 2]))   # [2, 4]
list(map(pow, [2, 3], [3, 2]))     # [8, 9]
list(map(int, ['1', '2']))         # [1, 2]
```

### `max(iterable, *, key=None, default=...)`

Restituisce l'elemento più grande.

```python
max([1, 5, 3])               # 5
max('hello')                 # 'o'
max([1, 2], [3, 4])          # [3, 4]
max([], default=0)           # 0
```

### `memoryview(object)`

Restituisce un oggetto memory view.

```python
mv = memoryview(b'abc')
mv[0]          # 97
bytes(mv)      # b'abc'
mv.tolist()    # [97, 98, 99]
len(mv)        # 3
```

### `min(iterable, *, key=None, default=...)`

Restituisce l'elemento più piccolo.

```python
min([1, 5, 3])         # 1
min('hello')           # 'e'
min([1, 2], [0, 3])    # [0, 3]
min([], default=0)     # 0
```

---

## N

### `next(iterator, default)`

Recupera il prossimo elemento da un iteratore.

```python
it = iter([1, 2])
next(it)          # 1
next(it)          # 2
next(it, 'fine')  # 'fine'
next(it)          # StopIteration
```

---

## O

### `object()`

Restituisce un nuovo oggetto senza caratteristiche.

```python
o = object()
type(o)           # <class 'object'>
object() is object()  # False
isinstance(o, object) # True
```

### `oct(x)`

Converte un intero in una stringa ottale con prefisso `"0o"`.

```python
oct(8)      # '0o10'
oct(64)     # '0o100'
oct(-8)     # '-0o10'
oct(0)      # '0o0'
```

### `open(file, mode='r', ...)`

Apre un file e restituisce un oggetto file.

```python
# open('file.txt')                # modalità lettura
# open('file.txt', 'w')           # modalità scrittura
# open('file.txt', 'rb')          # lettura binaria
# open('file.txt', encoding='utf-8') # con codifica
```

### `ord(c)`

Restituisce il code point Unicode di un carattere.

```python
ord('A')     # 65
ord('a')     # 97
ord('€')     # 8364
ord('😀')    # 128512
```

---

## P

### `pow(base, exp, mod=None)`

Restituisce base elevato a exp.

```python
pow(2, 3)         # 8
pow(2, 3, 5)      # 3 (2**3 % 5)
pow(2, -1)        # 0.5
pow(10, 2, 7)     # 2 (100 % 7)
```

### `print(*objects, sep=' ', end='\n')`

Stampa gli oggetti sullo stream di testo.

```python
print('hello')                  # hello
print('a', 'b', sep='-')        # a-b
print('x', end='')              # senza newline
print(1, 2, 3)                  # 1 2 3
```

### `property(fget=None, fset=None, fdel=None)`

Restituisce un attributo property.

```python
class C:
    def __init__(self): self._x = 0
    @property
    def x(self): return self._x
    @x.setter
    def x(self, v): self._x = v

c = C(); c.x = 5; print(c.x)  # 5
```

---

## R

### `range(stop)` / `range(start, stop, step)`

Restituisce una sequenza immutabile di numeri.

```python
list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 6))       # [2, 3, 4, 5]
list(range(0, 10, 3))   # [0, 3, 6, 9]
list(range(5, 0, -1))   # [5, 4, 3, 2, 1]
```

### `repr(object)`

Restituisce una rappresentazione stringa dell'oggetto.

```python
repr('hello')     # "'hello'"
repr(42)          # '42'
repr([1, 2])      # '[1, 2]'
repr({'a': 1})    # "{'a': 1}"
```

### `reversed(seq)`

Restituisce un iteratore inverso.

```python
list(reversed([1, 2, 3]))   # [3, 2, 1]
list(reversed('abc'))       # ['c', 'b', 'a']
list(reversed(range(3)))    # [2, 1, 0]
reversed((1, 2))            # tuple_reverseiterator
```

### `round(number, ndigits=None)`

Arrotonda un numero a ndigits cifre.

```python
round(3.14159, 2)    # 3.14
round(3.7)           # 4
round(2.5)           # 2 (arrotondamento bancario)
round(-2.5)          # -2
```

---

## S

### `set(iterable=())`

Crea un nuovo insieme.

```python
set()                # set()
set([1, 2, 2, 3])    # {1, 2, 3}
set('abc')           # {'a', 'b', 'c'}
set({'a': 1})        # {'a'}
```

### `setattr(object, name, value)`

Imposta un attributo su un oggetto.

```python
class C: pass
c = C()
setattr(c, 'x', 10)    # equivale a c.x = 10
setattr(c, 'y', 'hi')  # imposta attributo stringa
setattr(C, 'z', 99)    # imposta attributo di classe
```

### `sentinel(name, repr=None)`

**⚠️ Non è una built-in standard in Python 3.14 e precedenti.** Oggetto sentinella unico proposto nella PEP 661.

```python
# Sintassi ipotetica / futura (Python 3.15+)
MISSING = sentinel('MISSING')
STOP = sentinel('STOP')
DEFAULT = sentinel('DEFAULT', repr='<DEFAULT>')
assert MISSING is MISSING  # True
```

### `slice(stop)` / `slice(start, stop, step)`

Restituisce un oggetto slice.

```python
s = slice(2)           # slice(None, 2, None)
slice(1, 5)            # slice(1, 5, None)
slice(0, 10, 2)        # slice(0, 10, 2)
[1,2,3,4,5][slice(1,4)] # [2, 3, 4]
```

### `sorted(iterable, *, key=None, reverse=False)`

Restituisce una nuova lista ordinata.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted('hello')                  # ['e', 'h', 'l', 'l', 'o']
sorted([3, 1], reverse=True)    # [3, 1]
sorted(['bb', 'a'], key=len)    # ['a', 'bb']
```

### `staticmethod(function)`

Restituisce un metodo statico per la funzione.

```python
class C:
    @staticmethod
    def f(x):
        return x * 2

C.f(5)      # 10
C().f(3)    # 6
```

### `str(object='')`

Restituisce una versione stringa di un oggetto.

```python
str(42)          # '42'
str(3.14)        # '3.14'
str([1, 2])      # '[1, 2]'
str(None)        # 'None'
```

### `sum(iterable, start=0)`

Somma gli elementi di un iterabile.

```python
sum([1, 2, 3])          # 6
sum([1, 2, 3], 10)      # 16
sum(range(5))           # 10
sum([0.5, 0.5])         # 1.0
```

### `super(type, object_or_type=None)`

Restituisce un oggetto proxy che delega le chiamate di metodo a una classe padre.

```python
class A:
    def f(self): return 'A'

class B(A):
    def f(self):
        return super().f() + 'B'

B().f()    # 'AB'
```

---

## T

### `tuple(iterable=())`

Crea una nuova tupla.

```python
tuple()              # ()
tuple([1, 2, 3])     # (1, 2, 3)
tuple('abc')         # ('a', 'b', 'c')
tuple(range(3))      # (0, 1, 2)
```

### `type(object)` / `type(name, bases, dict)`

Restituisce il tipo di un oggetto o crea una nuova classe.

```python
type(42)            # <class 'int'>
type('hi')          # <class 'str'>
type([])            # <class 'list'>
type('C', (), {})   # crea dinamicamente la classe C
```

---

## V

### `vars(object)`

Restituisce l'attributo `__dict__` di un oggetto.

```python
class C:
    def __init__(self): self.x = 1

vars(C())           # {'x': 1}
vars()              # namespace locale corrente (come locals())
vars(int)           # mappingproxy del namespace di int
```

---

## Z

### `zip(*iterables, strict=False)`

Restituisce un iteratore di tuple che accoppiano elementi da ciascun iterabile.

```python
list(zip([1, 2], ['a', 'b']))       # [(1, 'a'), (2, 'b')]
list(zip('abc', range(3)))          # [('a', 0), ('b', 1), ('c', 2)]
list(zip([1, 2], [3, 4], [5, 6]))   # [(1, 3, 5), (2, 4, 6)]
dict(zip(['a', 'b'], [1, 2]))       # {'a': 1, 'b': 2}
```

---

## _

### `__import__(name, ...)`

Importa un modulo (normalmente chiamato dall'istruzione `import`).

```python
__import__('math')              # <module 'math'>
__import__('os.path')           # importa os, restituisce os
m = __import__('json')          # equivale a import json
__import__('sys').version       # accede a sys.version
```

---

## Riepilogo delle Voci Non Standard

| Funzione       | Stato                           | Riferimento |
| -------------- | ------------------------------- | ----------- |
| `frozendict` | Proposta (PEP 814, Python 3.15) |             |
| `sentinel`   | Proposta (PEP 661, Python 3.15) |             |

Per il codice di produzione, usa `frozenset` per insiemi immutabili e `object()` per valori sentinella finché queste funzionalità non saranno ufficialmente rilasciate.

```

```
