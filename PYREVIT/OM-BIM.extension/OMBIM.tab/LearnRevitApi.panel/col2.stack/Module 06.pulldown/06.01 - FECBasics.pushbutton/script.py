# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "06.01 FilteredElementCollector",
    "en_gb": "06.01 FilteredElementCollector",
    "es_es": "06.01 FilteredElementCollector"
}  # Nombre de del botón mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 25.02.2024
____________________________________________
Descripción
Esto es un archivo de plantilla para Pyrevit Scripts
____________________________________________
Acciones:
- Revisar que la versión sea en 2021
__________________________________________
Author: Oscar Mendoza"""  # Descripcion

### EXTRA: Tú puedes borrar esto
__helpurl__ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
__min_revit_ver__ = 2021
__max_revit_ver__ = 2025

### EXTRAS
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╠═╣║  ║║ ║║║║║╣ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╩ ╩╚═╝╩╚═╝╝╚╝╚═╝╚═╝
# ==================================================
from Autodesk.Revit.DB import *
import clr
from Autodesk.Revit.UI import FilterDialog

clr.AddReference('System')
from System.Collections.Generic import List


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# ==================================================

doc = __revit__.ActiveUIDocument.Document  # Tipo: Document
uidoc = __revit__.ActiveUIDocument  # type: object #tipo: UIDocument

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
# ==================================================
# 1️⃣ Walls


walls       = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType().ToElements()
# Incluye curtain panel and Model in Place
walls_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsElementType().ToElementIds()
# BuiltinCategoryEnumeration

random_wall  = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().FirstElement()
random_wall_TypeID= FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().FirstElementId()
# BuiltinCategoryEnumeration

walls_class = FilteredElementCollector(doc).OfClass(Wall).ToElements()
wall_type_class = FilteredElementCollector(doc).OfClass(WallType).ToElementIds()
# CLASE REVISAR BIEN

# print('Of Category: {} Elements'.format(len(walls)))
# print('Of Category: {} Elements'.format(len(walls_class)))

# 2️⃣ Modify to Get Other Elements

floor       = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()
floor_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsElementType().ToElementIds()
# BuiltinCategoryEnumeration

floor_class     = FilteredElementCollector(doc).OfClass(Floor).ToElements() # Incluye structural foundation
floor_type_class = FilteredElementCollector(doc).OfClass(FloorType).ToElementIds()
# CLASE REVISAR BIEN
# print('Of Category: {} Elements'.format(len(floor)))
# print('Of Category: {} Elements'.format(len(floor_class)))

# 3️⃣ Get Rooms( Some classes are located in more specific namespaces!)

rooms         = FilteredElementCollector(doc).OfClass(SpatialElement).ToElements()
# Incluye structural foundation
room_category = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).\
                    WhereElementIsNotElementType().\
                    ToElements()
# print('Of Category: {} Elements'.format(len(rooms)))
# print('Of Category: {} Elements'.format(len(room_category)))

# 4️⃣ Combine Selection
# Use Revit API FILTERS when you get many category at once!
# 1️⃣ List of Categories
cats = [BuiltInCategory.OST_Walls,
        BuiltInCategory.OST_Floors,
        BuiltInCategory.OST_Windows,
        BuiltInCategory.OST_Furniture]
List_Cats = List[BuiltInCategory](cats)  # Categories

#2️⃣Filters
multi_cat_filter = ElementMulticategoryFilter(List_Cats)

#3️⃣Apply Filters to FEC
all_Elements = FilteredElementCollector(doc)\
                    .WherePasses(multi_cat_filter)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

# for x in all_Elements:
#     print(x)

# 5️⃣ Loadable Families (Doors, Windows, Generic Models)
# If select family instances class obtain all Windows, Pilar Structural, Windows (Use Category)
# . OF Category (Include model in place)

doors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()
windows = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
GenericModels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).WhereElementIsNotElementType().ToElements()


# 6️⃣ Materiales
mats = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()

nombre_mats = [x.Name for x in mats]
nombre_mats_ordenados = sorted(nombre_mats)

# Compare revit lockup - database
# for nombre in nombre_mats_ordenados:
#     print(nombre)

# 7️⃣ Views OverView (Inherited Classes)
views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).\
                WhereElementIsNotElementType().\
                ToElements()
# Utilizar esto
views_ = FilteredElementCollector(doc).OfClass(View).ToElements()

# data = []
# for view in views:
#     typ       = str(type(view)).replace('<type', '')
#     view_type = str(view.ViewType)
#     cat       = str(view.Category.BuiltInCategory) if View.Category else 'N/A'
#
#     data.append([typ,view_type,cat])
#
# from pyrevit import script
# output = script.get_output()
# output.print_table (
#     table_data = data,
#     title = 'Views OverView',
#     columns = ['Type', 'ViewType', 'Built-In Category']
# )

# 8️⃣ Filter Views with List Compression (Basic)
all_views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).\
                WhereElementIsNotElementType().\
                ToElements()
schedules = [view for view in all_views if isinstance(view, ViewSchedule)]   # Schedules

schedules2 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Schedules).\
                            WhereElementIsNotElementType().\
                            ToElements()
views_3D        = [view for view in all_views if view.ViewType == ViewType.ThreeD]
views_elevation = [view for view in all_views if view.ViewType == ViewType.Elevation]
views_section = [view for view in all_views if view.ViewType == ViewType.Section]


for x in schedules2:
    print(x.Name)

