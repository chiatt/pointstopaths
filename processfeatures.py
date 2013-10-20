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
"""
from PyQt4.QtCore import *
from qgis.core import *
from datetime import datetime
from datetime import timedelta

class ProcessFeatures():

    def __init__(self, layer, fname, order_attr_name=None, order_attr_format=None, group_attr_name=None):
        self.layer = layer
        self.fname = fname
        self.order_attr = order_attr_name
        self.format_attr = order_attr_format
        self.group_attr = group_attr_name

    def generatePointDict(self):
        if not self.layer.isValid():
            print "Layer failed to load!"
        else:
            QgsMapLayerRegistry.instance().addMapLayer(self.layer)
            self.provider = self.layer.dataProvider()
            #self.feat = QgsFeature()
            self.features = self.layer.selectedFeatures()
            if len(self.features) == 0:
                self.features = self.provider.getFeatures()
            self.allAttrs = self.provider.attributeIndexes()
            self.feat_dict = {}
            self.order_attr_index = self.provider.fieldNameIndex(self.order_attr)
            self.group_attr_index = self.provider.fieldNameIndex(self.group_attr)
            for feat in self.features:
                self.geom = feat.geometry()
                self.coords = self.geom.asPoint()
                self.attrs = feat.attributes()
                self.order_attr_value = self.attrs[self.order_attr_index]
                self.group_attr_value = self.attrs[self.group_attr_index]
                for attr in self.attrs:
                    try:
                        self.order_value = datetime.strptime(str(self.order_attr_value), str(self.format_attr))
                    except:
                        try:
                            self.order_value = float(self.order_attr_value)
                        except:
                            raise ValueError, 'Order field is not an integer type or date format is invalid'
                    if attr == self.group_attr_value:
                        try:
                            self.feat_dict[attr].append((self.order_value, self.coords[0], self.coords[1]))
                        except:
                            self.feat_dict[attr] = [(self.order_value, self.coords[0], self.coords[1])]
        return self.feat_dict


    def findGaps(self, list_of_times, gap):
        self.arrays = []
        self.current_array = []
        try:
            list_of_times[0][0] + 0
            self.time_delta = gap
        except:
            if gap != None:
                self.time_delta = timedelta(minutes=gap)
        for i in range(len(list_of_times)):
            if gap != None:
                if i < len(list_of_times)-1:
                    self.current_time = list_of_times[i][0]
                    self.future_time = list_of_times[i + 1][0]
                    if self.future_time - self.current_time > self.time_delta:
                        self.current_array.append(list_of_times[i])
                        self.arrays.append(self.current_array)
                        self.current_array = []
                    else:
                        self.current_array.append(list_of_times[i])
                if self.future_time <= self.current_time + self.time_delta:
                    self.current_array.append(list_of_times[i])
            else:
                self.current_array.append(list_of_times[i])
        self.arrays.append(self.current_array)
        return self.arrays


    def writeShapefile(self, points_dict, crs, gap=None):
        self.fields = QgsFields()
        self.fields.append(QgsField("group", QVariant.String))
        self.fields.append(QgsField("begin", QVariant.String))
        self.fields.append(QgsField("end", QVariant.String))
        self.writer = QgsVectorFileWriter(self.fname, "CP1250", self.fields, QGis.WKBLineString, crs, "ESRI Shapefile")
        if self.writer.hasError() != QgsVectorFileWriter.NoError:
            print "Error when creating shapefile: ", self.writer.hasError()
        #gap = 60
        for (ky, vals) in points_dict.iteritems():
            if len(vals) > 1:
                vals.sort()
                self.gapped_vals = self.findGaps(vals, gap)
                for val in self.gapped_vals:
                    if len(val) > 1:
                        val.sort()
                        self.fet = QgsFeature()
                        self.verticies = []
                        for i in val:
                            self.verticies.append(QgsPoint(i[1], i[2]))
                        self.fet.setGeometry(QgsGeometry.fromPolyline(self.verticies))
                        self.fet.setAttributes([str(ky), str(val[0][0]), str(val[-1][0])])
                        self.writer.addFeature(self.fet)
        del self.writer
