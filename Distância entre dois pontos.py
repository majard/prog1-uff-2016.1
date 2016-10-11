import math
x1 = eval(input('x1 = '))
y1 = eval(input('y1 = '))
x2 = eval(input('x2 = '))
y2 = eval(input('y2 = '))
# calcula a distância usando teorema de pitágoras, com módulo da diferença entre os valores de x e y(distância na reta)
# como catetos de um triângulo retângulo e a hipotenusa como distância
print('A distancia entre os dois pontos eh ', math.sqrt(((math.fabs(x1 - x2))**2 + (math.fabs(y1 - y2))**2)))