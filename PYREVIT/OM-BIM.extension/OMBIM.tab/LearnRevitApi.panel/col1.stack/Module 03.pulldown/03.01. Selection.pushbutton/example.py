"""
Wall Create(
	Document document,
	Curve curve,
	ElementId levelId,
	bool structural
)

public Wall CreateWallUsingCurve1(Autodesk.Revit.DB.Document document, Level level)
{
    // define start and end for bound line
    XYZ startPoint = new XYZ(0, 0, 0);
    XYZ endPoint = new XYZ(10, 10, 10);
    
    // create line
    Line line = Line.CreateBound(startPoint, endPoint);

    // Create a wall using the location line
    return Wall.Create(document, geomLine, level.Id, true);
}
"""
"""
Ceilling Create(
	Document document,
	IList<CurveLoop> curveLoops,
	ElementId ceilingTypeId,
	ElementId levelId
Ceiling CreateCeilingAtElevation(Document document, Level level, double elevation)
{
   XYZ first = new XYZ(0, 0, 0);
   XYZ second = new XYZ(20, 0, 0);
   XYZ third = new XYZ(20, 15, 0);
   XYZ fourth = new XYZ(0, 15, 0);
   CurveLoop profile = new CurveLoop();
   profile.Append(Line.CreateBound(first, second));
   profile.Append(Line.CreateBound(second, third));
   profile.Append(Line.CreateBound(third, fourth));
   profile.Append(Line.CreateBound(fourth, first));

   var ceiling = Ceiling.Create(document, new List<CurveLoop> { profile }, ElementId.InvalidElementId, level.Id);
   Parameter param = ceiling.get_Parameter(BuiltInParameter.CEILING_HEIGHTABOVELEVEL_PARAM);
   param.Set(elevation);

   return ceiling;
}
)"""

"""
public static Floor Create(
	Document document,
	IList<CurveLoop> profile,
	ElementId floorTypeId,
	ElementId levelId
)
/// The example below shows how to use Floor.Create method to create a new structural floor (slab) on one level 
/// using a geometry profile and a floor type. 
/// In this sample, the geometry profile is a CurveLoop of lines, you can also use arcs, ellipses and splines.
Floor CreateFloor(Document document, Level level)
{
   // Get a floor type for floor creation
   ElementId floorTypeId = Floor.GetDefaultFloorType(document, false);

   // Build a floor profile for the floor creation
   XYZ first = new XYZ(0, 0, 0);
   XYZ second = new XYZ(20, 0, 0);
   XYZ third = new XYZ(20, 15, 0);
   XYZ fourth = new XYZ(0, 15, 0);
   CurveLoop profile = new CurveLoop();
   profile.Append(Line.CreateBound(first, second));
   profile.Append(Line.CreateBound(second, third));
   profile.Append(Line.CreateBound(third, fourth));
   profile.Append(Line.CreateBound(fourth, first));

   return Floor.Create(document, new List<CurveLoop> { profile }, floorTypeId, level.Id);
}
"""
"""
public static Floor Create(
	Document document,
	IList<CurveLoop> profile,
	ElementId floorTypeId,
	ElementId levelId
)
/// The example below shows how to use Floor.Create method to create a new Floor with specified elevation, on one level 
/// using a geometry profile and a floor type. 
/// It shows how to adapt your code that used NewFloor and NewSlab methods, which are obsolete since 2022.
/// In this sample, the geometry profile is a CurveLoop of lines, you can also use arcs, ellipses and splines.
Floor CreateFloorAtElevation(Document document, double elevation)
{
   // Get a floor type for floor creation
   // You must provide a valid floor type (unlike in now obsolete NewFloor and NewSlab methods).
   ElementId floorTypeId = Floor.GetDefaultFloorType(document, false);

   // Get a level
   // You must provide a valid level (unlike in now obsolete NewFloor and NewSlab methods).
   double offset;
   ElementId levelId = Level.GetNearestLevelId(document, elevation, out offset);

   // Build a floor profile for the floor creation
   XYZ first = new XYZ(0, 0, 0);
   XYZ second = new XYZ(20, 0, 0);
   XYZ third = new XYZ(20, 15, 0);
   XYZ fourth = new XYZ(0, 15, 0);
   CurveLoop profile = new CurveLoop();
   profile.Append(Line.CreateBound(first, second));
   profile.Append(Line.CreateBound(second, third));
   profile.Append(Line.CreateBound(third, fourth));
   profile.Append(Line.CreateBound(fourth, first));

   // The elevation of the curve loops is not taken into account (unlike in now obsolete NewFloor and NewSlab methods).
   // If the default elevation is not what you want, you need to set it explicitly.
   var floor = Floor.Create(document, new List<CurveLoop> { profile }, floorTypeId, levelId);
   Parameter param = floor.get_Parameter(BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM);
   param.Set(offset);

   return floor;
}"""