#!/Users/karina/Documents/GitHub-Projects/Sistema-de-Seguimiento-de-Egresados-FEI/sse-env/bin/python3.9

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdal_fillnodata as a convenience to use as a script
from osgeo_utils.gdal_fillnodata import *  # noqa
from osgeo_utils.gdal_fillnodata import main

deprecation_warn("gdal_fillnodata")
sys.exit(main(sys.argv))