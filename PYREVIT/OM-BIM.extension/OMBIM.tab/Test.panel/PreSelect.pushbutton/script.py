# -*- coding: utf-8 -*-

# Import pyrevit libraries
from pyrevit import DB, revit
from pyrevit import forms, script

# Get revit document, UI document
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument  # type: object
selection = uidoc.Selection  # type: Selection

# import UI Selection
from Autodesk.Revit.UI.Selection import *

# Import BuiltInCategory
from Autodesk.Revit.DB import BuiltInCategory, ElementId, Category


# custom selection filter class
class CustomISelectionFilter(ISelectionFilter):
    def __init__(self, category_ids):  # Creas una nueva instancia de clase
        self.category_ids = category_ids

    def AllowElement(self, elem):
        if elem.Category and elem.Category.Id in self.category_ids:
            return True
        else:
            return False


all_categories = []
names_categories = []

# Obtain Category BuilInCategory (Names and id)
for bic in BuiltInCategory.GetValues(BuiltInCategory):
    try:
        category = DB.Category.GetCategory(doc, bic)
        if category:  # Category Exist
            if not category.Name.startswith("<"):  # Annotations
                all_categories.append(category.Id)
                names_categories.append(category.Name)
    except Exception as e:
        continue

names_chosee = forms.SelectFromList.show(names_categories,
                                         title="Choose Categories",
                                         width=300,
                                         height=350,
                                         button_name="Select Option",
                                         multiselect=True)

# Convert select category names back to BuiltInCategory IDs:
selected_category_ids = [category_id
                         for category_id, category_name in zip(all_categories, names_categories)
                         if category_name in names_chosee]
# Check if we have a selection
if not selected_category_ids:
    script.exit()
else:
    try:
        sel_filter = CustomISelectionFilter(selected_category_ids)
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

# Try to get to the list of element id's to selection

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
