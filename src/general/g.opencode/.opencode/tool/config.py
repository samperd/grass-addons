"""

Configuration file for GRASS environment variables and tool settings.

Copyright (c) 2026 David Sampson

"""

# Configration for the GRASS general environment
GISBASE = "/usr/lib/grass84"
GRASS_HOME = "home"
GRASS_USER = "sampson"
GRASS_GISDBASE = "/home/sampson/grassdata"
GRASS_LOCATION = "Sample_Python_Addon"
GRASS_MAPSET = "PERMANENT"

# Configuration for the grass-region.py opencode tool
GRASS_REGIONS_OUTPUT_FORMAT = "raw_text"
GRASS_REGIONS_FLAG = "p"

# Configuration for the grass-man-page opencode tool
GRASS_MAN_PAGE_MAX_AGE_DAYS = 20