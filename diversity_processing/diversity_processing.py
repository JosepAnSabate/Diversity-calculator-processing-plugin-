# -*- coding: utf-8 -*-

"""
/***************************************************************************
 DiversityProcessing
                                 A QGIS plugin
 Calculates several common indices of diversity
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-10-08
        copyright            : (C) 2021 by Josep ANdreu Sabaté
        email                : josep.andreu@e-campus.uab.cat
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

__author__ = 'Josep ANdreu Sabaté'
__date__ = '2021-10-08'
__copyright__ = '(C) 2021 by Josep ANdreu Sabaté'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .diversity_processing_provider import DiversityProcessingProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class DiversityProcessingPlugin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = DiversityProcessingProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
