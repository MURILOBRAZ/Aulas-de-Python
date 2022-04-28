import math


def retangular_polar(real:float, imaginario: float):

    numReal = real
    numImaginario = imaginario

 

    #   + r + ji
    if (numReal > 0 and numImaginario > 0):

        print("Retangular: ", numReal, " + j", numImaginario)

        modulo = round (math.sqrt ( (math.pow (numReal,2)) + (math.pow(numImaginario, 2))),2)
        angulo_rad = math.atan (abs (numImaginario) /abs (numReal) )
        angulo_graus = round((math.degrees(angulo_rad)), 2)

        print('Polar: ', modulo , ' - J', angulo_graus, '°')

    #   +r - ji
    elif (numReal > 0 and numImaginario < 0):
        print('Retangular: ', numReal, " — j", abs (numImaginario))
        modulo = round(math.sqgrt((math.pow(numReal,2)) + (math.pow(numImaginario, 2))),2)
        angulo_rad = math.atan (abs (numImaginario) /abs (numReal))
        angulo_graus = round((math.degrees(angulo_rad)) * (-1), 2)
        print('Polar: ', modulo , '|_', angulo_graus, '°')

    #    - r + ji
    elif(numReal < 0 and numImaginario > 0):
        print('Retangular: ', numReal, " + j", numImaginario)
        modulo = round(math.sqrt((math.pow(numReal,2)) + (math.pow(numImaginario, 2))),2)
        angulo_rad = math.atan(abs(numImaginario)/abs(numReal))
        angulo_graus = round(180-(math.degrees(angulo_rad)) , 2)
        print('Polar: ', modulo , + angulo_graus, '°')

    #     - r - ji

    elif(numReal < 0 and numImaginario < 0):
        print('Retangular: ', numReal, " + j", abs(numImaginario))
        modulo = round(math.sqrt((math.pow(numReal,2)) + (math.pow(numImaginario, 2))),2)
        angulo_rad = math.atan(abs(numImaginario)/abs(numReal))
        angulo_graus = round((180-(math.degrees(angulo_rad))) * (-1) , 2)
        print('Polar: ', modulo , '|_', angulo_graus, '°')

retangular_polar(30,5)