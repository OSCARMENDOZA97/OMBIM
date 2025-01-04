# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "02.03 - FutureProof",
    "en_gb": "02.02 - FutureProof",
    "es_es": "02.02 - FutureProof"
}  # Nombre de del botón mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 30.06.2024
____________________________________________
Descripción
Examples of C# code translated to Python
____________________________________________
Author Oscar Mendoza 
"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

# .NET Importaciones
import clr
clr.AddReference('System')
from System.Collections.Generic import List

__min_revit_ver__ = 2022


# Units Meters Revit API
def mf(meters):
    return meters * 3.28084


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
app = __revit__.Application  # Application class


if rvt_year >= 2022:
    rule = FilterStringRule(valueProvider, evaluator, ruleString)
else:
    rule = FilterStringRule(valueProvider, evaluator, ruleString, caseSensitive)



