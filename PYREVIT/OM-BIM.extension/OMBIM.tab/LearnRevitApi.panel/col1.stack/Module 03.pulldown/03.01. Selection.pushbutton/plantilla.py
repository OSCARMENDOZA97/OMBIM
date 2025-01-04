# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "03.01 - Selection",
    "en_gb": "03.01 - Selection",
    "es_es": "003.01 - Selection"
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


# Units Meters Revit API
def mf(meters):    return meters * 3.28084


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
app = __revit__.Application  # Application class

level = FilteredElementCollector(doc) \
    .OfClass(Level) \
    .WhereElementIsNotElementType() \
    .FirstElement()


with Transaction(doc, "Create a Floor") as t:
    t.Start()
    new_floor = CreateFloorAtElevation(doc, 1.50)
    t.Commit()
