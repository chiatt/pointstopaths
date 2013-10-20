"""
/***************************************************************************
 PointsToPaths
                                 A QGIS plugin
 Converts points to lines with verticies grouped by a text or integer field
 and ordered by an integer or date string field
                             -------------------
        begin                : 2011-08-02
        copyright            : (C) 2011 by Cyrus Hiatt
        email                : cyrusnhiatt@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Points To Paths"
def description():
    return "Converts points to lines with verticies grouped by a text or integer field and ordered by an integer or date string field (based on PointsToOne, but intended for wildlife tracking data)"
def version():
    return "Version 0.3"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load PointsToPaths class from file PointsToPaths
    from pointstopaths import PointsToPaths
    return PointsToPaths(iface)
