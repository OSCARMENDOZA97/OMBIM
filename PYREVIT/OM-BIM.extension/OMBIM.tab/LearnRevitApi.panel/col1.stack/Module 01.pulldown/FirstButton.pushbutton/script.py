# -*- coding: utf-8 -*-
__title__ = "03.04 - Sum Rooms"
__doc__ = """Date    = 02.01.2023
_____________________________________________________________________
Description:
Tool to Sum selected Rooms.
If no rooms selected, you will be asked to select them.
_____________________________________________________________________
Author: Erik Frits"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.UI.Selection import (ObjectType,
                                         PickBoxStyle,
                                         Selection)

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

selection = uidoc.Selection  # type: Selection


# ⌨ INICIA EL CODIGO ACA

# 🔓 Use Transaction to Modify Document
# (Avoid placing inside of loops)
t = Transaction(doc, 'Change Name')

t.Start()  # 🔓 Start Transaction
# Changes Here...
t.Commit()  # 🔒 Commit Transaction

print('-' * 50)
print('Script esta finalizado')
print('Plantilla fue elaborada por Oscar Mendoza.')

from Autodesk.Revit.DB import *

