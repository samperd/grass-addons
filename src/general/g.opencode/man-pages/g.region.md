---
author: GRASS Development Team
date_created: '2003'
date_downloaded: '2026-01-14T23:53:52.843486'
latest_change: "Saturday May 17 11:05:53 2025 in commit: bef61c72260f7362148f7e946a63e2bb22efed23\n\
  \n\n\nMain index |\nGeneral index |\nTopics index |\nKeywords index |\nGraphical\
  \ index |\nFull index\n\n\n\xA9 2003-2025\nGRASS Development Team,\nGRASS GIS 8.4.3dev\
  \ Reference Manual"
source_url: https://grass.osgeo.org/grass84/manuals/g.region.html
tags:
- general
- settings
- computational region
- extent
- resolution
- level1
title: g.region - GRASS GIS manual
---

[](man-pages/index.md)

* * *

## NAME

_**g.region**_ \- Manages the boundary definitions for the geographic region. 

## KEYWORDS

[general](man-pages/general.md), [settings](man-pages/topic_settings.md), [computational region](keywords.html#computational region), [extent](keywords.html#extent), [resolution](keywords.html#resolution), [level1](keywords.html#level1)

## SYNOPSIS

**g.region**  


**g.region --help**  


**g.region** [-**dsplectwmn3bgfauo**] [**region** =_name_] [**raster** =_name_[,_name_ ,...]] [**raster_3d** =_name_] [**vector** =_name_[,_name_ ,...]] [**n** =_value_] [**s** =_value_] [**e** =_value_] [**w** =_value_] [**t** =_value_] [**b** =_value_] [**rows** =_value_] [**cols** =_value_] [**res** =_value_] [**res3** =_value_] [**nsres** =_value_] [**ewres** =_value_] [**tbres** =_value_] [**zoom** =_name_] [**align** =_name_] [**grow** =_value_] [**save** =_name_] [--**overwrite**] [--**help**] [--**verbose**] [--**quiet**] [--**ui**] 

### Flags:

**-d**
    Set from default region
**-s**
    Save as default region
    Only possible from the PERMANENT mapset
**-p**
    Print the current region
**-l**
    Print the current region in lat/long using the current ellipsoid/datum
**-e**
    Print the current region extent
**-c**
    Print the current region map center coordinates
**-t**
    Print the current region in GMT style
**-w**
    Print the current region in WMS style
**-m**
    Print region resolution in meters (geodesic)
**-n**
    Print the convergence angle (degrees CCW)
    The difference between the projection's grid north and true north, measured at the center coordinates of the current region.
**-3**
    Print also 3D settings
**-b**
    Print the maximum bounding box in lat/long on WGS84
**-g**
    Print in shell script style
**-f**
    Print in shell script style, but in one line (flat)
**-a**
    Align region to resolution (default = align to bounds, works only for 2D resolution)
**-u**
    Do not update the current region
**-o**
    Force update of the current region
**\--overwrite**
    Allow output files to overwrite existing files
**\--help**
    Print usage summary
**\--verbose**
    Verbose module output
**\--quiet**
    Quiet module output
**\--ui**
    Force launching GUI dialog

### Parameters:

**region** =_name_
    Set current region from named region
**raster** =_name[,_name_ ,...]_
    Set region to match raster map(s)
**raster_3d** =_name_
    Set region to match 3D raster map(s) (both 2D and 3D values)
**vector** =_name[,_name_ ,...]_
    Set region to match vector map(s)
**n** =_value_
    Value for the northern edge
**s** =_value_
    Value for the southern edge
**e** =_value_
    Value for the eastern edge
**w** =_value_
    Value for the western edge
**t** =_value_
    Value for the top edge
**b** =_value_
    Value for the bottom edge
**rows** =_value_
    Number of rows in the new region
**cols** =_value_
    Number of columns in the new region
**res** =_value_
    2D grid resolution (north-south and east-west)
**res3** =_value_
    3D grid resolution (north-south, east-west and top-bottom)
**nsres** =_value_
    North-south 2D grid resolution
**ewres** =_value_
    East-west 2D grid resolution
**tbres** =_value_
    Top-bottom 3D grid resolution
**zoom** =_name_
    Shrink region until it meets non-NULL data from this raster map
**align** =_name_
    Adjust region cells to cleanly align with this raster map
**grow** =_value_
    Number of cells to add to each side of the current region extent
    A negative number shrinks the current region extent
**save** =_name_
    Save current region settings in named region file

#### Table of contents

  * DESCRIPTION
  * DEFINITIONS
  * NOTES
    * Additional parameter information:
  * EXAMPLES
    * Printing extent and raster resolution in 2D and 3D
    * Changing extent and raster resolution using values
    * Changing extent and raster resolution using maps
    * Changing extent and raster resolution in 3D
    * Using g.region in a shell in combination with OGR
    * Using g.region in a shell in combination with GDAL
  * SEE ALSO
  * AUTHOR



## DESCRIPTION

The _g.region_ module allows the user to manage the settings of the current geographic region. These regional boundaries can be set by the user directly and/or set from a region definition file (stored under the `windows` directory in the user's current mapset). The user can create, modify, and store as many geographic region definitions as desired for any given mapset. However, only one of these geographic region definitions will be current at any given moment, for a specified mapset; i.e., GRASS programs that respect the geographic region settings will use the current geographic region settings. 

## DEFINITIONS

**Region:**     In GRASS, a _region_ refers to a geographic area with some defined boundaries, based on a specific map coordinate system and map projection. Each region also has associated with it the specific east-west and north-south resolutions of its smallest units (rectangular units called "cells"). 

The region's boundaries are given as the northernmost, southernmost, easternmost, and westernmost points that define its extent (cell edges). The north and south boundaries are commonly called _northings_ , while the east and west boundaries are called _eastings_. 

The region's cell resolution defines the size of the smallest piece of data recognized (imported, analyzed, displayed, stored, etc.) by GRASS modules affected by the current region settings. The north-south and east-west cell resolutions need not be the same, thus allowing non-square data cells to exist. 

Typically all raster and display modules are affected by the current region settings, but not vector modules. Some special modules diverge from this rule, for example raster import modules and _v.in.region_. **Default Region:**     Each GRASS project (previously called location) has a fixed geographic region, called the default geographic region (stored in the region file `DEFAULT_WIND` under the special mapset `PERMANENT`), that defines the extent of the data base. While this provides a starting point for defining new geographic regions, user-defined geographic regions need not fall within this geographic region. The current region can be reset to the default region with the **-d** flag. The default region is initially set when the project is first created and can be reset using the **-s** flag. **Current Region:**     Each mapset has a current geographic region. This region defines the geographic area in which all GRASS displays and raster analyses will be done. Raster data will be resampled, if necessary, to meet the cell resolutions of the current geographic region setting. **Saved Regions:**     Each GRASS MAPSET may contain any number of pre-defined, and named, geographic regions. These region definitions are stored in the user's current mapset location under the `windows` directory (also referred to as the user's saved region definitions). Any of these pre-defined geographic regions may be selected, by name, to become the current geographic region. Users may also access saved region definitions stored under other mapsets in the current project, if these mapsets are included in the user's mapset search path or the '@' operator is used (`region_name@mapset`). 

## NOTES

After all updates have been applied, the current region's southern and western boundaries are (silently) adjusted so that the north/south distance is a multiple of the north/south resolution and that the east/west distance is a multiple of the east/west resolution. 

With the **-a** flag all four boundaries are adjusted to be even multiples of the resolution, aligning the region to the resolution supplied by the user. The default is to align the region resolution to match the region boundaries. 

The **-m** flag will report the region resolution in meters. The resolution is calculated by averaging the resolution at the region boundaries. This resolution is calculated by dividing the geodesic distance in meters at the boundary by the number of rows or columns. For example the east / west resolution (ewres) is determined from an average of the geodesic distances at the North and South boundaries divided by the number of columns. 

The **-p** (or **-g**) option is recognized last. This means that all changes are applied to the region settings before printing occurs. 

The **-g** flag prints the current region settings in shell script style. This format can be given back to _g.region_ on its command line. This may also be used to save region settings as shell environment variables with the UNIX eval command, "`eval `g.region -g``". 

With **-u** flag current region is not updated even if one or more options for changing region is used (**res=** , **raster=** , etc). This can be used for example to print modified region values for further use without actually modifying the current region. Similarly, **-o** flag forces to update current region file even when e.g., only printing was specified. Flag **-o** was added in GRASS GIS version 8 to simulate _g.region_ behavior in prior versions when current region file was always updated unless **-u** was specified. 

### Additional parameter information:

**zoom=**_name_     Shrink current region settings to the smallest region encompassing all non-NULL data in the named raster map layer that fall inside the user's current region. In this way you can tightly zoom in on isolated clumps within a bigger map. 

If the user also includes the **raster=**_name_ option on the command line, **zoom=**_name_ will set the current region settings to the smallest region encompassing all non-NULL data in the named **zoom** map that fall inside the region stated in the cell header for the named **raster** map. **align=**_name_     Set the current resolution equal to that of the named raster map, and align the current region to a row and column edge in the named map. Alignment only moves the existing region edges outward to the edges of the next nearest cell in the named raster map - not to the named map's edges. To perform the latter function, use the **raster=**_name_ option. 

## EXAMPLES

### Printing extent and raster resolution in 2D and 3D

` g.region -p `      This will print the current region in the format: 
    
    
    projection: 1 (UTM)
    zone:       13
    datum:      nad27
    ellipsoid:  clark66
    north:      4928000
    south:      4914000
    west:       590000
    east:       609000
    nsres:      20
    ewres:      20
    rows:       700
    cols:       950
    

` g.region -p3 `      This will print the current region and the 3D region (used for voxels) in the format: 
    
    
    projection: 1 (UTM)
    zone:       13
    datum:      nad27
    ellipsoid:  clark66
    north:      4928000
    south:      4914000
    west:       590000
    east:       609000
    top:        1.00000000
    bottom:     0.00000000
    nsres:      20
    nsres3:     20
    ewres:      20
    ewres3:     20
    tbres:      1
    rows:       700
    rows3:      700
    cols:       950
    cols3:      950
    depths:     1
    

` g.region -g `      The **-g** option prints the region in the following script style (key=value) format: 
    
    
    n=4928000
    s=4914000
    w=590000
    e=609000
    nsres=20
    ewres=20
    rows=700
    cols=950
    

` g.region -bg `      The **-bg** option prints the region in the following script style (key=value) format plus the boundary box in latitude-longitude/WGS84: 
    
    
    n=4928000
    s=4914000
    w=590000
    e=609000
    nsres=20
    ewres=20
    rows=700
    cols=950
    LL_W=-103.87080682
    LL_E=-103.62942884
    LL_N=44.50164277
    LL_S=44.37302019
    

` g.region -l `      The **-l** option prints the region in the following format: 
    
    
    long: -103.86789484 lat: 44.50165890 (north/west corner)
    long: -103.62895703 lat: 44.49904013 (north/east corner)
    long: -103.63190061 lat: 44.37303558 (south/east corner)
    long: -103.87032572 lat: 44.37564292 (south/west corner)
    rows:       700
    cols:       950
    Center longitude: 103:44:59.170374W [-103.74977]
    Center latitude:  44:26:14.439781N [44.43734]
    

` g.region -pm `      This will print the current region in the format (latitude-longitude project): 
    
    
    projection: 3 (Latitude-Longitude)
    zone:       0
    ellipsoid:  wgs84
    north:      90N
    south:      40N
    west:       20W
    east:       20E
    nsres:      928.73944902
    ewres:      352.74269109
    rows:       6000
    cols:       4800
    

Note that the resolution is here reported in meters, not decimal degrees. 

### Changing extent and raster resolution using values

` g.region n=7360100 e=699000 `      will reset the northing and easting for the current region, but leave the south edge, west edge, and the region cell resolutions unchanged. 

` g.region n=51:36:05N e=10:10:05E s=51:29:55N w=9:59:55E res=0:00:01 `      will reset the northing, easting, southing, westing and resolution for the current region, here in DMS latitude-longitude style (decimal degrees and degrees with decimal minutes can also be used). 

` g.region -dp s=698000 `      will set the current region from the default region for the GRASS project, reset the south edge to 698000, and then print the result. 

` g.region n=n+1000 w=w-500 `      The n=_value_ may also be specified as a function of its current value: n=n+_value_ increases the current northing, while n=n-_value_ decreases it. This is also true for s=_value_ , e=_value_ , and w=_value_. In this example the current region's northern boundary is extended by 1000 units and the current region's western boundary is decreased by 500 units. 

` g.region n=s+1000 e=w+1000 `      This form allows the user to set the region boundary values relative to one another. Here, the northern boundary coordinate is set equal to 1000 units larger than the southern boundary's coordinate value, and the eastern boundary's coordinate value is set equal to 1000 units larger than the western boundary's coordinate value. The corresponding forms s=n-_value_ and 

w=e-_value_ may be used to set the values of the region's southern and western boundaries, relative to the northern and eastern boundary values. 

### Changing extent and raster resolution using maps

` g.region raster=soils `      This form will make the current region settings exactly the same as those given in the cell header file for the raster map layer _soils_. 

` g.region raster=soils zoom=soils `      This form will first look up the cell header file for the raster map layer _soils_ , use this as the current region setting, and then shrink the region down to the smallest region which still encompasses all non-NULL data in the map layer _soils_. Note that if the parameter _raster=soils_ were not specified, the zoom would shrink to encompass all non-NULL data values in the soils map that were located within the _current region_ settings. 

` g.region -up raster=soils `      The **-u** option suppresses the re-setting of the current region definition. This can be useful when it is desired to only extract region information. In this case, the cell header file for the soils map layer is printed without changing the current region settings. 

` g.region -up zoom=soils save=soils `      This will zoom into the smallest region which encompasses all non-NULL soils data values, and save the new region settings in a file to be called _soils_ and stored under the `windows` directory in the user's current mapset. The current region settings are not changed. 

### Changing extent and raster resolution in 3D

` g.region b=0 t=3000 tbres=200 res3=100 g.region -p3 `      This will define the 3D region for voxel computations. In this example a volume with bottom (0m) to top (3000m) at horizontal resolution (100m) and vertical resolution (200m) is defined. 

### Using g.region in a shell in combination with OGR

Extracting a spatial subset of the external vector map `soils.shp` into new external vector map `soils_cut.shp` using the OGR _ogr2ogr_ tool:  

    
    
    eval `g.region -g`
    ogr2ogr -spat $w $s $e $n soils_cut.shp soils.shp
    

This requires that the project and the SHAPE file CRS' match. 

### Using g.region in a shell in combination with GDAL

Extracting a spatial subset of the external raster map `p016r035_7t20020524_z17_nn30.tif` into new external raster map `p016r035_7t20020524_nc_spm_wake_nn30.tif` using the GDAL _gdalwarp_ tool:  

    
    
    eval `g.region -g`
    gdalwarp -t_srs "`g.proj -wf`" -te $w $s $e $n \
             p016r035_7t20020524_z17_nn30.tif \
             p016r035_7t20020524_nc_spm_wake_nn30.tif
    

Here the input raster map does not have to match the project's coordinate reference system since it is reprojected on the fly. 

## SEE ALSO

_[g.access](man-pages/g.access.md), [g.mapsets](man-pages/g.mapsets.md), [g.proj](man-pages/g.proj.md)   
Environment variables: [GRASS_REGION and WIND_OVERRIDE](variables.html#internal) _

## AUTHOR

Michael Shapiro, U.S.Army Construction Engineering Research Laboratory 

## SOURCE CODE

Available at: [g.region source code](https://github.com/OSGeo/grass/tree/main/general/g.region) ([history](https://github.com/OSGeo/grass/commits/main/general/g.region)) 

Latest change: Saturday May 17 11:05:53 2025 in commit: bef61c72260f7362148f7e946a63e2bb22efed23 

* * *

[Main index](man-pages/index.md) | [General index](man-pages/general.md) | [Topics index](man-pages/topics.md) | [Keywords index](man-pages/keywords.md) | [Graphical index](man-pages/graphical_index.md) | [Full index](man-pages/full_index.md)

© 2003-2025 [GRASS Development Team](https://grass.osgeo.org), GRASS GIS 8.4.3dev Reference Manual 
