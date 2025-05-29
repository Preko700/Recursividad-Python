###########################################
#          Recursividad de Pila          #
###########################################
# EJERCICIOS INICIALES SOBRE RECURSIVIDAD #
###########################################
#E Numeros Enteros
#R Numeros Enteros
#S Numeros Enteros
def suma_impar(n1):
    if isinstance(n1,int):
        return suma_imparP(abs(n1))
    else:
        return "Error"
def suma_imparP(num):
  if num == 0:
    return 0
  elif num % 10 % 2 != 0:
    return num % 10 + suma_impar(num // 10)
  else:
    return suma_impar(num // 10)
###########################################
#E Numeros Enteros
#R Numeros Enteros
#S Numeros Enteros
def cuente_par(num):
    if isinstance(num,int):
        return cuente_parP(abs(num))
    else:
        return "Error"
def cuente_parP(n1):
    if n1==0:
        return 0
    elif n1%10%2==0:
        return 1+cuente_parP(n1//10)
    else:
        return cuente_parP(n1//10)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Valores Booleanos
def iguales(n1):
    if isinstance(n1,int):
        return igualesP(abs(n1))
    else:
        return "Error"
def igualesP(n1):
    n2=n1%10
    if VI(n1)==n2:
        return True
    else:
        return False
def VI(n1):
    if n1==0:
        return 0
    elif n1<10:
        return n1
    else:
        return VI(n1//10)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Valores Booleanos
def suma10(num):
    if isinstance(num, int):
        return suma10P(abs(num))>=10
    else:
        return "Error"
def suma10P(num):
    if num==0:
        return 0
    else:
        return num%10+suma10P(num//10)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Valores Booleanos
def cuente_dig(n,d):
    if isinstance(n,int) and isinstance(d,int):
        return CDP(abs(n),abs(d))
    else:
        return "Error"
def CDP(n,d):
    if n==0:
        return 0
    elif n%10==d:
        return 1+CDP(n//10,d)
    else:
        return CDP(n//10,d)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S una tupla
def revise_num(n):
    if isinstance(n,int):
        return RNP(abs(n),[0,0])
    else:
        return "Error"
def RNP(n,l1):
    if n == 0:
        return tuple(l1)
    elif n % 10 <= 4:
        l1[0] += 1
        return RNP(n // 10, l1)
    else:
        l1[1] += 1
        return RNP(n // 10, l1)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Valores Booleanos
def hay_par(n):
    if isinstance(n,int):
        return HPP(abs(n))
    else:
        return "Error"
def HPP(n1):
    if n1 == 0:
        return False
    elif n1 % 10 % 2 == 0:
        return True
    else:
        return HPP(n1 // 10)
##########################################
#      EJERCICIOS SOBRE RECURSIVIDAD.    #
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Numeros Enteros
def forme1(n):
    if isinstance(n,int):
        return FP(abs(n),0)
    else:
        return "Error"
def FP(n,e):
    if n==0:
        return 0
    elif n%10==1:
        return n%10*10**e+FP(n//10,e+1)
    else:
        return FP(n//10,e)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Numeros Enteros
def num_append(n1, n2):
    if isinstance(n1,int) and isinstance(n2,int):
        return NAP(n1,n2)
    else:
        return "Error"
def NAP(n1, n2):
    if n2 == 0:
        return n1
    else:
        num_dig_n2 = contar_digitos(n2)
        return n1 * (10 ** num_dig_n2) + n2
def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Numeros Enteros
def multi(n1, n2):
    if isinstance(n1,int) or isinstance(n1,float) and isinstance(n2,int) or isinstance(n2,float):
        return MP(abs(n1),abs(n2))
    else:
        return "Error"
def MP(n1,n2):
    if n2==0:
        return 1
    else:
        return n1+n2+MP(n1,n2-1)
##########################################
#E Numeros Reales
#R  Numero Real
#S Numeros Reales
def sume_parimpar(n1):
    if isinstance(n1,int):
        return sum(filter(lambda x: x % 2 == 0, [int(d) for d in str(n1)])), sum(filter(lambda x: x % 2 != 0, [int(d) for d in str(n1)]))
    else:
        return "Error"
##########################################
#E Numero Real
#R Numero Real
#S Clasificacion entre perfecto, deficiente, abundante en string
def clasifique(num):
    if not isinstance(abs(num), int) or num <= 0:
        return "Error: Debe ingresar un número entero positivo."
    suma_divisores = sum(divisores(num))
    if suma_divisores == num:
        return "Perfecto"
    elif suma_divisores < num:
        return "Deficiente"
    else:
        return "Abundante"
def divisores(num):
    return [i for i in range(1, num) if num % i == 0]
##########################################
#E Numeros Enteros
#R Numeros Enteros
#S Valores Booleanos
def dig_ab(n1,n2):
    if isinstance(n1,int) and isinstance(n2,int):
        return DAP(abs(n1),abs(n2))
    else:
        return "Error"
def DAP(n1,n2):
    if n1==0:
        return True
    elif n2==0:
        return False
    elif n1%10==n2%10:
        return DAP(n1//10, n2)
    else:
        return DAP(n1, n2//10)
###############################################################
"EJERCICIOS SOBRE PROGRAMACIÓN RECURSIVA PARA 1er PARCIAL."
###############################################################
###############################################################
"EJERCICIOS RECURSIVIDAD DE COLA"
###############################################################
#E un digito y un numero
#R enteros
#S entero
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
##########################################
#E Numero Entero
#R Numero Entero
#S Numero Enterp
def cambia(n1):
    if isinstance(n1,int):
        return CP(abs(n1),0,0)
    else:
        return  "Error"
def  CP(n1,e,res):
    ultimodig=n1%10
    if n1==0:
        return res
    elif ultimodig%4==0:
        return CP(n1//10,e+1,res+0*10**e)
    else:
        return CP(n1//10,e+1,res+ultimodig*10**e)
##########################################
#E  dos numeros enteros
#R  Numero Entero
#S  Numero Entero
def todos_div(n1,d):
    if isinstance(n1, int) and isinstance(d, int):
        return div(abs(n1), abs(d))
    else:
        return "Error"

def div(n1, d):
    if n1 == 0:
        return True
    elif TDP(n1, d):
        return div(n1 // 10, d)
    else:
        return False

def TDP(n1, d):
    if n1 == 0:
        return True
    elif n1 % 10 == 0 or n1 % d == 0:
        return TDP(n1 // 10, d)
    else:
        return False
##########################################
#E un numero entero y un digito
#S dos numeros
#R Numeros de tipo enteros
def divida(d, n1):
    if isinstance(d, int) and isinstance(n1, int):
        return DP(abs(d), abs(n1), 0, 0)
    else:
        return "Error"
def DP(d, n1, res1, res2):
    if n1 == 0:
        return res1, res2
    else:
        ultimo_digito = n1 % 10
        if ultimo_digito >= d:
            res1 += ultimo_digito * 10**res1
        else:
            res2 += ultimo_digito * 10**res2
        return DP(d, n1 // 10, res1, res2)
##########################################
#E Numero Entero
#R Numero Entero
#S Numero Entero
def suma_coc(n1):
    if isinstance(n1,int):
        return SCP(abs(n1),1,0)
    else:
        return "Error"
def SCP(n1,i,res):
    if i > n1:
        return res
    else:
        nuevo_resultado = i + i / (i * (i + 1))
        return SCP(n1, i + 1, nuevo_resultado)
##########################################
#E Numero Entero
#R Numero Entero
#S Numero Entero
def moda(n1):
    if isinstance(n1,int):
        return MP1(abs(n1),0)
    else:
        return  "Error"
def MP1(n1,res):
    if n1==0:
        return res
    else:
        return MP1(n1//10,res+numeros(n1)/largo(n1))
def largo(n1):
    if n1==0:
        return 0
    else:
        return 1+largo(n1//10)
def numeros(n1):
    if n1 == 0:
        return 0
    else:
        return n1%10 + numeros(n1//10)
###############################################################
"Recursividad utilizando Cola"
###############################################################
#E una lista y un numero entero
#R a una lista y un digito
#S una lista
def delete_allNum(l1,d):
    if isinstance(l1,list) and isinstance(d,int):
        return DANP(l1,d,[])
    else:
        return  "Error"
def DANP(l1,d,l2):
    if l1 == []:
        return l2
    elif l1[0] == d:
        return DANP(l1[1:],d,l2)
    else:
        return  DANP(l1[1:], d,l2+[l1[0]])
###############################################################
#E una lista
#R a una lista
#S una lista
def ultimo_par(l1):
    if isinstance(l1,list):
        return UPP(l1,0)
    else:
        return  "Error"
def UPP(l1,res):
    if l1 == []:
        return res
    elif l1[0] % 2 == 0:
        return UPP(l1[1:], l1[0])
    else:
        return UPP(l1[1:], res)
###############################################################
#E un numero entero
#R numero entero
#S Valor Booleano
def palindromo(n1):
    if isinstance(n1,int):
        return PP(abs(n1),0,0)==n1
    else:
        return "Error, debe recibir un número."
def PP(n1,n2,e):
    if n1==0:
        return n2
    else:
        return PP(n1//10,n2+n1%10*10**e,e+1)
###############################################################
#E un numero entero
#R un numero entero
#S un numero entero de un digito
def dig_mitad(num):
    if isinstance(num, int) and num > 0:
        num_dig = contar_digitos(num)
        if num_dig % 2 == 0:
            return 0
        else:
            return obtener_digito_en_posicion(num, num_dig // 2)
    else:
        return "Error"
def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)
def obtener_digito_en_posicion(num, pos):
    if pos == 0:
        return num % 10
    else:
        return obtener_digito_en_posicion(num // 10, pos - 1)
###############################################################
#E un numero entero
#R un digito
#S una lista
def suma_digitos(n1):
    if isinstance(n1,int):
        return SDP(abs(n1),[])
    else:
        return "Error"
def SDP(n1,res):
    if n1 == 0:
        return res
    else:
        digito_actual = n1 % 10
        if digito_actual % 2 == 0:
            res[0] += digito_actual
        else:
            res[1] += digito_actual
        return SDP(n1 // 10, res)
###############################################################
#E una lista
#R una lista
#S una lista
def cambie_repetidos(l1):
    if isinstance(l1, list):
        # Usamos un conjunto para rastrear los elementos ya vistos
        vistos = set()
        for i, e in enumerate(l1):
            if isinstance(e, list):
                # Si el elemento es una lista, llamamos recursivamente a la función
                l1[i] = cambie_repetidos(e)
            elif e in vistos:
                l1[i] = -1
            else:
                vistos.add(e)
        return l1
    else:
        return "Error"
###############################################################
#E una lista
#R una lista
#S una lista
def permutaciones(lista):
    if not lista:
        return [[]]
    else:
        resultado = []
        for i in range(len(lista)):
            elemento_actual = lista[i]
            restante = lista[:i] + lista[i+1:]
            for perm in permutaciones(restante):
                resultado.append([elemento_actual] + perm)
        return resultado
###############################################################
#E listas
#R listas
#S una lista
def interseccion(lista1, lista2):
    return [num for num in lista1 if num in lista2]
###############################################################
#E una lista
#R una lista
#S una lista
#D Usando Sublistas
def invertir(lista):
    if len(lista) <= 1:
        return lista
    else:
        return invertir(lista[1:]) + [lista[0]]
###############################################################
#E una lista
#R una lista
#S una lista
#D Sin usar Sublistas
def invertir1(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + invertir1(lista[:-1])