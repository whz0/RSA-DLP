RSA:

Para la correcta ejecución de este programa, hemos decidido antes de actuar, implementar los siguientes métodos:

- EEA sobre dos números naturales: Recibe 2 números naturales (x::integer, z::integer) y devuelve una 3-upla con e l MCD, x^(-1)mod y, y^(-1) mod x.
- Algoritmo de Exponenciación Rápida (sobre dos números positivos dentro de un rango modular): Recibe como parámetros (base, potencia::integer, modulo::integer) y calcula de manera eficiente el resultado. Retorna 1 o la solución.

- Miller-Rabin para verificar si un número es primo (probabilístico): Para ello recibe el número (x::integer) y con una cota de 10 intentos, trata de verificar si el número es primo, devolviendo True si lo es y False si no lo es o no encontró solución. Con 10 iteraciones la probabilidad de fallo es de 1/(4^10) = 0,00000095367431640625.

- Búsqueda de coprimo: Recibe como parámetro un número natural (x::integer) y retorna el primer valor que encuentre que sea coprimo con el.

- Algoritmo de Rho-Pollard: Recibe como parámetro un número natural (x::integer) y devuelve uno de sus factores.

Dado todo esto buscamos las claves del RSA de la siguiente forma:

1. Obtenemos dos números primos (por Miller-Rabin) que llamaremos p y q.
2. Con p y q obtenemos n de manera que n = p*q.
3. Establecemos z para que sea igual al orden de n. Este se calcula multiplicando los ordenes de p y q, siendo para estos su totiente (p-1 y q-1).
4. Buscamos también un valor d, el cual es coprimo con z. (Mediante el procedimiento de búsqueda de coprimo).
5. Buscamos ahora un valor que sea el inverso multiplicativo de d modulo z (Mediante el EEA) y lo llamamos e.


Con esto podemos formar la clave pública y privada:
clave pública = (n, d)
clave privada = (p, q, e)

Ahora solo nos queda probar que todo funcione bien. De ser asi, un mensaje que queramos mandar debería cifrarse usando:
cifrado = M^e mod n

y descifrarse usando:
Mensaje = C^d mod n

Para ello usamos el algoritmo de exponenciación rápida implementado anteriormente, así como métodos propios de maple para convertir el texto a valores numéricos (StringTools-ToByteArray, StringTools-convert).

Es de notar que el mensaje antes de procesarlo, lo dividimos en 6-gramas (k-gramas de 6).

Finalmente usamos el algoritmo de Rho-Pollard pasándole como parámetro n, y vemos que con facilidad deduce o p, o q, indicando que nuestro procedimiento no es seguro.
