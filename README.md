# **Blockchain**

#### Uma `blockchain` simples de usar e segura `(em desenvolvimento)`

------

## **_Instalação_**

```bash
$git clone git@github.com:paulindavzl/blockchain.git
$pip install -r requirements.txt
```
___
## **_Aplicação_**

## Gerar e validar uma **blockchain** simples

```python
from blockchain import Block, Blockchain

# exemplo de dados usados na criação da blockchain
data = {
    'id': 0,
    'name': 'Test'
}
# crie uma instância da classe Block()
my_block = Block()

# use .update(...) para adicionar os dados na blockchain
my_block.update(data) # os dados precisam ser em formato de dicionário

# use .generate() para calcular o hash
my_block.generate()

# use .show() para retornar os dados da blockchain
print(my_block.show())
```

**_saída:_**

```bash
{'id': 0, 'name': 'Test', ..., 'hash':'00...', 'nonce': ..., ...}
```

A ordem de geração *__sempre__* será essa!

A **blockchain** tem algumas _keys_ reservadas:

* init_order

* hash

* nonce

* sequence

* requirement

* expire

E no futuro poderá usar:

* previous_hash

* id_previous_hash

Evite usar essas chaves no dicionário usado em *update* para evitar erros e bugs!

### Para validar uma `blockchain`, use:

```python
# instância da classe Blockchain()
validator = Blockchain()

# use o método is_valid(...) para validar uma blockchain
print(validator.is_valid(my_block))
```

**_saída:_**

```bash
{'result': True} / {'result': False, 'cause': ...}
```

As causas da `blockchain` retornar invalidez podem ser:

* expired - quando já expirou a data pré-definida

* expire_invalid - quando a data de expiração está inválida, possivelmente modificada

* different_hashes - quando as hashes não coincidem, possivelmente modificada
___
## **_Atributos_**

### É possível adicionar alguns atributos para aumentar a segurança da `blockchain`:

## **init_order**

### Altera a ordem em que os dados são organizados para calcular o hash. Existem três possíveis valores para `init_order`:

* top

É o valor padrão do atributo, os dados serão organizados do jeito que foram declarados
```python
from blockchain import Block

# dados usados na criação da blockchain
data = {
    'id': 0,
    'name': 'Test'
}

# ao instanciar a classe Block(), declare o atributo também
my_block = Block(init_order='top')
```

* bottom

Os dados serão reorganizados do último ao primeiro
```python
from blockchain import Block

# dados usados na criação da blockchain
data = {
    'id': 0,
    'name': 'Test'
}

# ao instanciar a classe Block(), declare o atributo também
my_block = Block(init_order='bottom')
```

Os valores de `data` serão invertidos: `{'name': 'Test', 'id': 0}`

* random

Os dados serão reorganizados de forma aleatória
```python
from blockchain import Block

# dados usados na criação da blockchain
data = {
    'id': 0,
    'name': 'Test'
}

# ao instanciar a classe Block(), declare o atributo também
my_block = Block(init_order='random')
```

Os valores serão reorganizados de forma aleatória e ao usar o método `.show()`, o dicionário terá uma nova chave: `sequence`

## **private_key**

### Adiciona uma chave privada que não é retornada ao usar o método `.show()`

### Por padrão, `private_key` é definida como `None`
```python
from blockchain import Block, Blockchain

# exemplo de chave privada (use uma variável de ambiente)
PRIVATE_KEY = 'paulindavzl123'

# ao instanciar a classe Block(), declare private_key
my_block = Block(private_key=PRIVATE_KEY)
```
É importante que ao analisar a `blockchain`, a `chave privada` seja informada novamente
```python
# instância da classe Blockchain()
validator = Blockchain()

# declarar private_key no método is_valid()
validator.is_valid(my_block, private_key=PRIVATE_KEY)
```
A segurança da `private_key` depende de como o usuário à guarda em seu `script`!

## **expire**

### Define um tempo limite para a validez da blockchain

`expire` pode ser declarado com quatro formas diferentes, podem ser em:

* Segundos
```python
from blockchain import Block

# declarar expire em segundos ao instanciar Block()
my_block = Block(expire='30s')
```

* Minutos
```python
from blockchain import Block

# declarar expire em minutos ao instanciar Block()
my_block = Block(expire='5m')
```

* Horas
```python
from blockchain import Block

# declara expire em horas ao instanciar Block()
my_block = Block(expire='1h')
```

O atributo `expire` aceita somente números com uma possível letra no final, indicando a medida de tempo (`s`, `m` ou `h`).

Caso a medida de tempo não for informada, o valor dado será tratado em `segundos`!

Caso outra letra seja passada ou a letra esteja em `maiúscula`, um erro será gerado! Use somente letras minúsculas!

## **requirement**

### Indica com quantos caractéres a hash deve começar. Não é recomendado que modifique.
## **⚠️exigências muito longas podem prejudicar o desempenho!⚠️**

`requirement` recebe uma `lista` com dois valores:
```python
from blockchain import Block

# instância da classe Block() passando requirement
my_block = Block(requirement=[2, '00'])
```

Por padrão, `requirement=[2, '00']`, e para modificá-lo, passe uma lista com quantos caractéres iniciais devem ser analisados e como eles devem estar!

Não é recomendado que modifique.
## **⚠️exigências muito longas podem prejudicar o desempenho!⚠️**