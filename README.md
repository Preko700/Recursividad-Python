# Biblioteca de Funciones Recursivas en Python

## 📋 Descripción

Esta biblioteca contiene una colección completa de funciones implementadas utilizando diferentes técnicas de recursividad en Python. El repositorio incluye ejemplos de recursividad de pila, recursividad de cola y otros patrones recursivos para resolver diversos problemas algorítmicos.

## ✨ Características principales

- ✅ Implementaciones de recursividad de pila y de cola
- ✅ Funciones para manipulación de dígitos y números
- ✅ Operaciones matemáticas recursivas
- ✅ Manipulación de listas usando técnicas recursivas
- ✅ Algoritmos de búsqueda y transformación recursivos

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/usuario/recursividad-python.git

# Acceder al directorio
cd recursividad-python
```

## 💻 Uso

Puedes importar las funciones individuales en tus proyectos de Python:

```python
from recursividad import suma_impar, palindromo, ultimo_par

# Ejemplos de uso
resultado = suma_impar(135)  # Suma los dígitos impares: 1+3+5=9
es_palindromo = palindromo(1221)  # Verifica si 1221 es palíndromo: True
ultimo = ultimo_par([1, 4, 7, 8, 3])  # Encuentra el último número par: 8
```

## 📚 Contenidos del Repositorio

El repositorio está organizado en diferentes secciones según el tipo de recursividad y la naturaleza de los problemas:

### 1. Recursividad de Pila

Funciones implementadas con recursividad tradicional (de pila):

#### Funciones Básicas
- `suma_impar(n)`: Suma los dígitos impares de un número
- `cuente_par(n)`: Cuenta los dígitos pares en un número
- `iguales(n)`: Verifica si el primer y último dígito son iguales
- `suma10(n)`: Verifica si la suma de los dígitos es mayor o igual a 10
- `cuente_dig(n, d)`: Cuenta cuántas veces aparece un dígito en un número

#### Funciones Intermedias
- `revise_num(n)`: Clasifica los dígitos de un número según sean <= 4 o > 4
- `hay_par(n)`: Verifica si hay algún dígito par en el número
- `forme1(n)`: Forma un nuevo número solo con los dígitos 1 del número original

### 2. Recursividad de Cola

Funciones implementadas con recursividad de cola (más eficiente en uso de memoria):

- `restard(d, n)`: Resta un dígito específico a todos los dígitos de un número
- `cambia(n)`: Cambia dígitos divisores de 4 por ceros
- `todos_div(n, d)`: Verifica si todos los dígitos de un número son divisores de un dígito
- `divida(d, n)`: Separa un número en dos según si los dígitos son >= o < que un dígito dado
- `suma_coc(n)`: Calcula la sumatoria de cocientes según una fórmula
- `moda(n)`: Encuentra el dígito que más se repite en un número

### 3. Manipulación de Listas Recursivas

- `delete_allNum(lista, ele)`: Elimina todas las ocurrencias de un elemento en una lista
- `ultimo_par(lista)`: Encuentra el último número par en una lista
- `cambie_repetidos(lista)`: Reemplaza elementos repetidos por -1
- `permutaciones(lista)`: Genera todas las posibles permutaciones de una lista
- `interseccion(lista1, lista2)`: Encuentra los elementos comunes entre dos listas
- `invertir(lista)`: Invierte el orden de los elementos de una lista (usando sublistas)
- `invertir1(lista)`: Invierte el orden de los elementos de una lista (sin usar sublistas)

### 4. Operaciones Numéricas Especiales

- `palindromo(n)`: Verifica si un número es palíndromo
- `dig_mitad(n)`: Obtiene el dígito central de un número o 0 si tiene longitud par
- `suma_digitos(n)`: Calcula la suma de dígitos pares e impares
- `octal_decimal(n)`: Convierte un número octal a decimal

## 📝 Ejemplos de Uso

### Ejemplo 1: Verificar si un número es palíndromo

```python
>>> palindromo(38583)
True
>>> palindromo(2442)
True
>>> palindromo(4)
True
>>> palindromo(1010010)
False
>>> palindromo("a")
"Error, debe recibir un número."
```

### Ejemplo 2: Manipulación de dígitos

```python
>>> restard(7, 9978)
2201
>>> restard(7, 1084)
10
>>> cambia(1488)
1000
>>> cambia(4275)
275
```

### Ejemplo 3: Trabajando con listas

```python
>>> delete_allNum([0, 5, 1, 2, 5, 3, 4], 5)
[0, 1, 2, 3, 4]
>>> ultimo_par([23, 72, 149, 34])
34
>>> ultimo_par([1, 3, 5, 7])
None
>>> cambie_repetidos([1, 2, 5, 3, 1, 5, 1])
[1, 2, 5, 3, -1, -1, -1]
```

## 🔍 Detalles de Implementación

### Recursividad de Cola vs Recursividad de Pila

- **Recursividad de Pila**: Las operaciones pendientes se acumulan en la pila de llamadas hasta llegar al caso base, para luego resolverse en orden inverso.

- **Recursividad de Cola**: Las llamadas recursivas se realizan como la última operación de la función, permitiendo optimizaciones por parte del compilador/intérprete.

Ejemplo de función con recursividad de cola:

```python
def restard(d, n1):
    if isinstance(d, int) and isinstance(n1, int):
        return RP(abs(d), abs(n1), 0, 0)
    else:
        return "Error"
        
def RP(d, n1, e, res):
    if n1 == 0:
        return res
    elif n1%10==d:
        return RP(d, n1//10, e+1,res+(n1%10-d*10**e))
    elif n1%10-d<=0:
        return RP(d,n1//10,e+1,res+0*10**e)
    else:
        return RP(d, n1//10, e+1,res+n1%10*10**e)
```

## 🧪 Pruebas

El código incluye ejemplos de entrada y salida como comentarios para cada función. 
Para probar las funciones puedes ejecutarlas directamente:

```python
# Ejemplo de uso
print(palindromo(12321))  # True
print(cambia(1488))       # 1000
print(ultimo_par([7, 4, 9, 2, 5]))  # 2
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 👨‍💻 Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una sugerencia:

1. Haz un fork del proyecto
2. Crea una nueva rama (`git checkout -b feature/improvement`)
3. Haz commit de tus cambios (`git commit -m 'Add some improvement'`)
4. Haz push a la rama (`git push origin feature/improvement`)
5. Abre un Pull Request
