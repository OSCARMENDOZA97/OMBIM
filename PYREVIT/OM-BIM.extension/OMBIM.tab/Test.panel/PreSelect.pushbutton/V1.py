# -*- coding: utf-8 -*-

# Import pyrevit libraries
from pyrevit import DB, revit
from pyrevit import forms, script

# Get revit document, UI document
doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument
selection = uidoc.Selection  # type: Selection

# import UI Selection
from Autodesk.Revit.UI.Selection import *


# custom selection filter class
class CustomISelectionFilter(ISelectionFilter):
    def __init__(self, nom_category):  # Creas una nueva instancia de clase
        self.nom_category = nom_category

    def AllowElement(self, elem):
        if elem.Category.Name in self.nom_category:
            return True
        else:
            return False


# List of category names:
names_choses = ["Areas", "Ceilings", "Floors", "Roofs", "Walls"]
# Not name of element

# Selection UI for user to choose from
names_chosee = forms.SelectFromList.show(names_choses,
                                         title="Choose Categories",
                                         width=300,
                                         height=350,
                                         button_name="Select Option",
                                         multiselect=True)
# Check if we have a selection
if not names_chosee:
    script.exit()
else:
    try:
        sel_filter = CustomISelectionFilter(names_choses)
        sel_elements = selection.PickObjects(ObjectType.Element,
                                             sel_filter,
                                             "Selecciona los elementos osquitar")
    except Exception as e:
        sel_elements = []
# Import list class
import System
from System.Collections.Generic import List

# Empy Element Id List
element_ids = List[DB.ElementId]()

# Try to get to the list of element Id's to selection

for s in sel_elements:
    try:
        elementId = s.ElementId
        element_ids.Add(elementId)
    except Exception as e:
        pass

# Select the elements
try:
    selection.SetElementIds(element_ids)
except Exception as e:
    pass
