# Modelo

## Características do Problema

Max $f(x,y) = 21.5 + x sen(4\pi x) + y sen(20\pi y)$

Variáveis independentes: $x$ e $y$

Precisão decimal das variáveis: 4

Intervalos: $x = [-3.0,12.1]$ e $y = [4.1,5.8]$


## Características do AG simples

- Codificação Binária

- Método de seleção proporcional

- Cruzamento em um ponto

- Mutação aleatória

- Parâmetros:

    - Núm. de gerações (Gerações)

    - Tamanho da população

    - Probabilidade de cruzamento (Pc)

    - Probabilidade de mutação (Pm)

## Estrutura do AG Simples

1. Gerar população inicial

2. Iniciar $t=0$

3. Avaliar população inicial

4. Realizar o ciclo evolutivo:

    - Seleção

    - Cruzamento

    - Mutação

    - Avaliar nova população

    - Incremetar $t, t=t+1$

5. Repetir enquanto ($t$ < Gerações)

## Codificação

As variáveis serão codificadas em cadeias com numero de bits conforme a expressão:

$L_{ind} = [log_2 ((l_{sup} - l_{inf}) * 10^{precisão})]$

onde, para $x$:

$L_{ind} = [log_2 ((12.1 - (-3.0)) * 10^4)] = 17.2041$

e para $y$:

$L_{ind} = [log_2 ((5.8 - 4.1) * 10^4)] = 14.0532$

Arredondando esses valores para cima, temos: 

![alt text](Figuras\fig_cadeias.JPG)

Para converter os valores usaremos as potências em base 2 para cada bit, conforme o exêmplo:

![alt text](Figuras\fig_decode.JPG)

Para converter um decimal, usaremos a seguinte expressão:

$x_i = l_{inf} + decimal(11001...11_2)*(\frac{(l_{sup} - l_{inf})}{2^{Lind}-1})$

onde, para esse indíviduo 1 teríamos $x_1$ e $y_1$:

$x_1 = -3.0 + (144254)*(\frac{(12.1 - (-3.0))}{2^{18}-1}) = 5.3093$

$y_1 = 4.1 + (6599)*(\frac{(5.8 - 4.1)}{2^{15}-1}) = 4.4423$

