# -*- coding: utf-8 -*-
__title__ = {
    "en_us": "02.02 - Translate C# to Python",
    "en_gb": "02.02 - Translate C# to Python",
    "es_es": "02.02 - Translate C# a Python"
}  # Nombre de del botón mostrado en Revit UI
__doc__ = """Version = 1.0
Fecha   = 30.06.2024
____________________________________________
Descripción
Examples of C# code translated to Python
Create Floors
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
def mf(meters):return meters * 3.28084


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


# ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦╦  ╦╔╗╔╔═╗
# ║  ╠╦╝║╣ ╠═╣ ║ ║╣   ║  ║╣ ║║  ║║║║║ ╦
# ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝  ╚═╝╚═╝╩╩═╝╩╝╚╝╚═╝

# new_ceiling = Ceiling.Create(doc,list_of_curves , ceil_type_id, levelId)


def CreateCeilingAtElevation(document, level, elevation):
    # Type (Document, Level,Float) -> Ceiling
    """Function to create a ceiling"""

    first = XYZ(0, 0, 0)
    second = XYZ(mf(20), 0, 0)
    third = XYZ(mf(20), mf(15), 0)
    fourth = XYZ(0, mf(15), 0)
    profile = CurveLoop()
    profile.Append(Line.CreateBound(first, second))
    profile.Append(Line.CreateBound(second, third))
    profile.Append(Line.CreateBound(third, fourth))
    profile.Append(Line.CreateBound(fourth, first))

    list_curve_loops = List[CurveLoop]()
    list_curve_loops.Add(profile)

    ceil_type_id = doc.GetDefaultElementTypeId(ElementTypeGroup.CeilingType)
    ceiling = Ceiling.Create(document,
                             list_curve_loops,
                             ceil_type_id,
                             level.Id)
    param = ceiling.get_Parameter(BuiltInParameter.CEILING_HEIGHTABOVELEVEL_PARAM)
    param.Set(elevation)

    return ceiling


# with Transaction(doc, "Create a Ceiling") as t:
#     t.Start()
#     new_wall = CreateCeilingAtElevation(doc, level, mf(10))
#     t.Commit()

# ╔═╗╔═╗╔╦╗  ╔═╗╦  ╦╔═╗╦═╗╦═╗╦╔╦╗╔═╗
# ╚═╗║╣  ║   ║ ║╚╗╔╝║╣ ╠╦╝╠╦╝║ ║║║╣
# ╚═╝╚═╝ ╩   ╚═╝ ╚╝ ╚═╝╩╚═╩╚═╩═╩╝╚═╝

def ElementOverride():
    # Select Element
    id = uidoc.Selection.PickObject(ObjectType.Element, "Select an element").ElementId

    # Graphic Settings
    ogs = OverrideGraphicSettings()
    ogs.SetProjectionLineColor(Color(8, 51, 162))

    # Change color
    with Transaction(doc, "Set Element Override") as t:
        t.Start()
        doc.ActiveView.SetElementOverrides(id, ogs)
        t.Commit()


# ElementOverride()


# ╔═╗╦  ╔═╗╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗
# ╠╣ ║  ║ ║║ ║╠╦╝  ║  ╠╦╝║╣ ╠═╣ ║ ║╣
# ╚  ╩═╝╚═╝╚═╝╩╚═  ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝
# Floor structural in one level without level

# new_floor = Floor.Create(doc, profile, floortypeID, LevelId)


def CreateFloor(doc, level):
    # Type (Document, Level) -> Floor
    """Function to create a floor"""
    # Get a floor type

    floorTypeId = Floor.GetDefaultFloorType(doc, False)

    # Build a floor profile for the floor creation

    first = XYZ(0, 0, 0)
    second = XYZ(mf(20), 0, 0)
    third = XYZ(mf(20), mf(15), 0)
    fourth = XYZ(0, mf(15), 0)
    profile = CurveLoop()
    profile.Append(Line.CreateBound(first, second))
    profile.Append(Line.CreateBound(second, third))
    profile.Append(Line.CreateBound(third, fourth))
    profile.Append(Line.CreateBound(fourth, first))

    list_curve_loops = List[CurveLoop]()
    list_curve_loops.Add(profile)

    return Floor.Create(doc,
                        list_curve_loops,
                        floorTypeId,
                        level.Id)


# with Transaction(doc, "Create a Floor") as t:
#     t.Start()
#     new_floor = CreateFloor(doc, level)
#     t.Commit()

# ╔═╗╦  ╔═╗╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗
# ╠╣ ║  ║ ║║ ║╠╦╝  ║  ╠╦╝║╣ ╠═╣ ║ ║╣
# ╚  ╩═╝╚═╝╚═╝╩╚═  ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝
# Floor structural in one level with elevation

# new_floor = Floor.Create(doc, profile, floorTypeId, level)

def CreateFloorAtElevation(doc, elevation):
    # Type (Document, elevation) -> Floor
    """Function to create a floor"""

    # Get a floor type for floor creation

    floorTypeId = Floor.GetDefaultFloorType(doc, False)

    # Build a floor profile
    first = XYZ(0, 0, 0)
    second = XYZ(mf(20), 0, 0)
    third = XYZ(mf(20), mf(15), 0)
    fourth = XYZ(0, mf(15), 0)
    profile = CurveLoop()
    profile.Append(Line.CreateBound(first, second))
    profile.Append(Line.CreateBound(second, third))
    profile.Append(Line.CreateBound(third, fourth))
    profile.Append(Line.CreateBound(fourth, first))

    list_curve_loops = List[CurveLoop]()
    list_curve_loops.Add(profile)

    floor = Floor.Create(doc,
                         list_curve_loops,
                         floorTypeId,
                         level.Id)

    param = floor.get_Parameter(BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM)
    param.Set(mf(elevation))

    return floor


with Transaction(doc, "Create a Floor") as t:
    t.Start()
    new_floor = CreateFloorAtElevation(doc, 1.50)
    t.Commit()
