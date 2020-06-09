# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import sys
from itertools import cycle

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "validation":
    rut = GetParams("rut")
    result = GetParams("result")

    try:
        validated = False
        rut = rut.upper();
        rut = rut.replace("-", "")
        rut = rut.replace(".", "")
        aux = rut[:-1]
        dv = rut[-1]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s) % 11
        if str(res) == dv:
            validated = True
        elif dv == "K" and res == 10:
            validated = True

        SetVar(result, validated)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

