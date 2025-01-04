# -*- coding: utf-8 -*-
__title__ = "03.05 Rename Views"
__doc__ = """Date    = 07.09.2024
_____________________________________________________________________
Description:
Code for lesson 03.05 - Rename views
Tutorial on using selection and modifying properties
_____________________________________________________________________
Author: Oscar Mendoza"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ==================================================
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.UI.Selection import (ObjectType,
                                         PickBoxStyle,
                                         Selection)
from Snippets.Selection import get_selected_elements
from pyrevit import forms

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ==================================================
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

selection = uidoc.Selection  # type: Selection

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝  MAIN
# ==================================================
# 1️⃣. GET VIEWS  (FILTER OF VIEW CLASS)
selected_elements = get_selected_elements()
selected_views = [el for el in selected_elements if issubclass(type(el), View)]
# 1️⃣. Pyrevit-Forms
if not selected_views:
    selected_views = forms.select_views()
    if not selected_views:
        forms.alert('There were no Views Selected.\n'
                    ' Please Try Again. OWMB', exitscript=True)
# 2️⃣. GET USER INPUT (Effective input)  ## REVIT PYTHON WRIPPER ##
# prefix = ""
# find = "B"
# replace = "A"
# suffix = ""
from rpw.ui.forms import (FlexForm, Label, TextBox, Separator, Button)
components = [Label('Prefix:'), TextBox('prefix'),
              Label('Find:'), TextBox('find'),
              Label('Replace:'), TextBox('replace'),
              Label('Suffix:'), TextBox('suffix'),
              Separator(), Button('Select')]
form = FlexForm('Title', components)
form.show()

# It's returns dictionary

user_inputs = form.values

prefix = user_inputs['prefix']
find = user_inputs['find']
replace = user_inputs['replace']
suffix = user_inputs['suffix']


for view in selected_views:
    # 3️⃣. NEW NAME (Unique view name)
    current_name = view.Name
    if find in current_name:
        new_name = prefix + view.Name.replace(find, replace) + suffix
        # 4. RENAME VIEWS
        with Transaction(doc, __title__) as t:  # Name of Addin
            t.Start()
            for i in range(20):
                try:
                    view.Name = new_name  # Unnique name
                    print("{} -> {}".format(current_name, new_name))
                    break
                except:
                    new_name += "*"
            t.Commit()
