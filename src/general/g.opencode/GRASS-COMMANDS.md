# GRASS-COMMANDS.md - Listing of GRASS Commands
This document was created by https://codebeautify.org/html-to-markdown in order to convert the [GRASS GIS 8.4.3dev Reference Manual: Full index](https://grass.osgeo.org/grass84/manuals/full_index.html) from HTML to Markdown.


 GRASS GIS 8.4.3dev Reference Manual: Full index - GRASS GIS Manual     

[![GRASS logo](grass_logo.png)](index.html)

* * *

GRASS GIS 8.4.3dev Reference Manual
-----------------------------------

**Geographic Resources Analysis Support System**, commonly referred to as [GRASS GIS](https://grass.osgeo.org), is a [Geographic Information System](https://en.wikipedia.org/wiki/Geographic_information_system) (GIS) used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization. GRASS is currently used in academic and commercial settings around the world, as well as by many governmental agencies and environmental consulting companies.

This reference manual details the use of modules distributed with Geographic Resources Analysis Support System (GRASS), an open source ([GNU GPLed](https://www.gnu.org/licenses/gpl.html)), image processing and geographic information system (GIS).

Go [back to help overview](index.html)

#### Table of contents

*   [Display commands (d.\*)](full_index.html#d)
*   [Database commands (db.\*)](full_index.html#db)
*   [General commands (g.\*)](full_index.html#g)
*   [Imagery commands (i.\*)](full_index.html#i)
*   [Miscellaneous commands (m.\*)](full_index.html#m)
*   [PostScript commands (ps.\*)](full_index.html#ps)
*   [Raster commands (r.\*)](full_index.html#r)
*   [3D raster commands (r3.\*)](full_index.html#r3)
*   [Temporal commands (t.\*)](full_index.html#t)
*   [Vector commands (v.\*)](full_index.html#v)
*   [wxGUI Graphical User Interface](full_index.html#wxGUI)
*   [Further pages](full_index.html#further)

### Display commands (d.\*)

[d.background](d.background.html)

Fills the graphics display frame with user defined color.

[d.barscale](d.barscale.html)

Displays a barscale on the graphics monitor.

[d.colorlist](d.colorlist.html)

Outputs a list of all available display colors.

[d.colortable](d.colortable.html)

Displays the color table associated with a raster map layer.

[d.correlate](d.correlate.html)

Prints a graph of the correlation between raster maps (in pairs).

[d.erase](d.erase.html)

Erases the contents of the active graphics display frame with user defined color.

[d.font](d.font.html)

Selects the font in which text will be displayed on the user's graphics monitor.

[d.fontlist](d.fontlist.html)

Lists the available fonts.

[d.frame](d.frame.html)

Manages display frames on the user's graphics monitor.

[d.geodesic](d.geodesic.html)

Displays a geodesic line, tracing the shortest distance between two geographic points along a great circle, in a longitude/latitude data set.

[d.graph](d.graph.html)

Program for generating and displaying simple graphics on the display monitor.

[d.grid](d.grid.html)

Overlays a user-specified grid in the active display frame on the graphics monitor.

[d.his](d.his.html)

Displays the result obtained by combining hue, intensity, and saturation (HIS) values from user-specified input raster map layers.

[d.histogram](d.histogram.html)

Displays a histogram in the form of a pie or bar chart for a user-specified raster map.

[d.info](d.info.html)

Displays information about the active display monitor.  

[d.labels](d.labels.html)

Displays text labels (created with v.label) to the active frame on the graphics monitor.

[d.legend](d.legend.html)

Displays a legend for a 2D or 3D raster map in the active frame of the graphics monitor.

[d.legend.vect](d.legend.vect.html)

Displays a vector legend in the active graphics frame.

[d.linegraph](d.linegraph.html)

Generates and displays simple line graphs in the active graphics monitor display frame.

[d.mon](d.mon.html)

Controls graphics display monitors from the command line.

[d.northarrow](d.northarrow.html)

Displays a north arrow on the graphics monitor.

[d.out.file](d.out.file.html)

Saves the contents of the active display monitor to a graphics file.

[d.path](d.path.html)

Finds shortest path for selected starting and ending node.

[d.polar](d.polar.html)

Draws polar diagram of angle map such as aspect or flow directions

[d.profile](d.profile.html)

Plots profile of a transect.

[d.rast.arrow](d.rast.arrow.html)

Draws arrows representing cell aspect direction for a raster map containing aspect data.

[d.rast.edit](d.rast.edit.html)

Edits cell values in a raster map.

[d.rast](d.rast.html)

Displays user-specified raster map in the active graphics frame.

[d.rast.leg](d.rast.leg.html)

Displays a raster map and its legend on a graphics window

[d.rast.num](d.rast.num.html)

Overlays cell category values on a raster map displayed in the active graphics frame.

[d.redraw](d.redraw.html)

Redraws the content of currently selected monitor.

[d.rgb](d.rgb.html)

Displays three user-specified raster maps as red, green, and blue overlays in the active graphics frame.

[d.rhumbline](d.rhumbline.html)

Displays the rhumbline joining two longitude/latitude coordinates.

[d.shade](d.shade.html)

Drapes a color raster over an shaded relief or aspect map.

[d.text](d.text.html)

Draws text in the active display frame on the graphics monitor using the current font.

[d.title](d.title.html)

Create a TITLE for a raster map in a form suitable for display with d.text.

[d.to.rast](d.to.rast.html)

Saves the contents of the active display monitor to a raster map.

[d.vect.chart](d.vect.chart.html)

Displays charts of vector data in the active frame on the graphics monitor.

[d.vect](d.vect.html)

Displays user-specified vector map in the active graphics frame.

[d.vect.thematic](d.vect.thematic.html)

Displays a thematic vector map in the active graphics frame.

[d.what.rast](d.what.rast.html)

Allows the user to interactively query raster map layers at user-selected locations.

[d.what.vect](d.what.vect.html)

Allows the user to interactively query vector map layers at user-selected locations.

[d.where](d.where.html)

Identifies the geographic coordinates associated with point locations given in display coordinates.

### Database commands (db.\*)

[db.columns](db.columns.html)

List all columns for a given table.

[db.connect](db.connect.html)

Prints/sets general DB connection for current mapset.

[db.copy](db.copy.html)

Copy a table.  

[db.createdb](db.createdb.html)

Creates an empty database.

[db.databases](db.databases.html)

Lists all databases for a given driver and location.

[db.describe](db.describe.html)

Describes a table in detail.

[db.drivers](db.drivers.html)

Lists all database drivers.

[db.dropcolumn](db.dropcolumn.html)

Drops a column from selected attribute table.

[db.dropdb](db.dropdb.html)

Removes an existing database.

[db.droptable](db.droptable.html)

Drops an attribute table.

[db.execute](db.execute.html)

Executes any SQL statement.  

[db.in.ogr](db.in.ogr.html)

Imports attribute tables in various formats.

[db.login](db.login.html)

Sets user/password for DB driver/database.

[db.out.ogr](db.out.ogr.html)

Exports attribute tables into various formats.

[db.select](db.select.html)

Selects data from attribute table.  

[db.tables](db.tables.html)

Lists all tables for a given database.

[db.test](db.test.html)

Test database driver, database must exist and set by db.connect.

[db.univar](db.univar.html)

Calculates univariate statistics on selected table column.

### General commands (g.\*)

[g.access](g.access.html)

Controls access to the current mapset for other users on the system.  

[g.cairocomp](g.cairocomp.html)

Overlays multiple X Pixmaps.

[g.copy](g.copy.html)

Creates copies of maps and other elements  

[g.dirseps](g.dirseps.html)

Internal GRASS utility for converting directory separator characters.  

[g.download.location](g.download.location.html)

Download GRASS project (location) from the web  

[g.download.project](g.download.project.html)

Download GRASS project from the web  

[g.extension.all](g.extension.all.html)

Rebuilds or removes all locally installed GRASS Addons extensions.  

[g.extension](g.extension.html)

Maintains GRASS Addons extensions in local GRASS installation.  

[g.filename](g.filename.html)

Prints GRASS data base file names.

[g.findetc](g.findetc.html)

Searches for GRASS support files.

[g.findfile](g.findfile.html)

Searches for GRASS data base files and sets variables for the shell.

[g.gisenv](g.gisenv.html)

Outputs and modifies the user's current GRASS variable settings.  

[g.gui.animation](g.gui.animation.html)

Tool for animating a series of raster and vector maps or a space time raster or vector dataset.

[g.gui.datacatalog](g.gui.datacatalog.html)

Tool for browsing, modifying and managing GRASS maps.

[g.gui.dbmgr](g.gui.dbmgr.html)

Launches graphical attribute table manager.

[g.gui.gcp](g.gui.gcp.html)

Georectifies a map and allows managing Ground Control Points.

[g.gui.gmodeler](g.gui.gmodeler.html)

Graphical Modeler.  

[g.gui](g.gui.html)

Launches a GRASS graphical user interface (GUI) session.  

[g.gui.iclass](g.gui.iclass.html)

Tool for supervised classification of imagery data.  

[g.gui.image2target](g.gui.image2target.html)

Georectifies a map and allows managing Ground Control Points for 3D correction.

[g.gui.mapswipe](g.gui.mapswipe.html)

Interactively compares two maps by swiping a visibility bar.

[g.gui.photo2image](g.gui.photo2image.html)

Corrects scanning distortions of a paper photo.

[g.gui.psmap](g.gui.psmap.html)

Tool for creating hardcopy map outputs.

[g.gui.rdigit](g.gui.rdigit.html)

Interactive editing and digitizing of raster maps.

[g.gui.rlisetup](g.gui.rlisetup.html)

Configuration tool for r.li modules.

[g.gui.timeline](g.gui.timeline.html)

Allows comparing temporal datasets by displaying their temporal extents in a plot.

[g.gui.tplot](g.gui.tplot.html)

Plots the values of temporal datasets.

[g.gui.vdigit](g.gui.vdigit.html)

Interactive editing and digitization of vector maps.

[g.list](g.list.html)

Lists available GRASS data base files of the user-specified data type optionally using the search pattern.

[g.manual](g.manual.html)

Displays the manual pages of GRASS modules.

[g.mapset](g.mapset.html)

Changes/reports current mapset.  

[g.mapsets](g.mapsets.html)

Modifies/prints the user's current mapset search path.  

[g.message](g.message.html)

Prints a message, warning, progress info, or fatal error in the GRASS way.  

[g.mkfontcap](g.mkfontcap.html)

Generates the font configuration file by scanning various directories for fonts.

[g.parser](g.parser.html)

Provides automated parser, GUI, and help support for GRASS scipts.

[g.pnmcomp](g.pnmcomp.html)

Overlays multiple PPM image files.

[g.ppmtopng](g.ppmtopng.html)

Converts between PPM/PGM and PNG image formats.

[g.proj](g.proj.html)

Prints or modifies GRASS projection information files (in various co-ordinate system descriptions).  

[g.region](g.region.html)

Manages the boundary definitions for the geographic region.

[g.remove](g.remove.html)

Removes data base element files from the user's current mapset using the search pattern.

[g.rename](g.rename.html)

Renames data base element files in the user's current mapset.

[g.search.modules](g.search.modules.html)

Search in GRASS modules using keywords

[g.tempfile](g.tempfile.html)

Creates a temporary file and prints it's file name.

[g.version](g.version.html)

Displays GRASS GIS version info.  

### Imagery commands (i.\*)

[i.albedo](i.albedo.html)

Computes broad band albedo from surface reflectance.

[i.aster.toar](i.aster.toar.html)

Calculates Top of Atmosphere Radiance/Reflectance/Brightness Temperature from ASTER DN.

[i.atcorr](i.atcorr.html)

Performs atmospheric correction using the 6S algorithm.  

[i.band.library](i.band.library.html)

Prints available semantic label information used for multispectral data.

[i.biomass](i.biomass.html)

Computes biomass growth, precursor of crop yield calculation.

[i.cca](i.cca.html)

Canonical components analysis (CCA) program for image processing.

[i.cluster](i.cluster.html)

Generates spectral signatures for land cover types in an image using a clustering algorithm.  

[i.colors.enhance](i.colors.enhance.html)

Performs auto-balancing of colors for RGB images.

[i.eb.eta](i.eb.eta.html)

Actual evapotranspiration for diurnal period (Bastiaanssen, 1995).

[i.eb.evapfr](i.eb.evapfr.html)

Computes evaporative fraction and root zone soil moisture.

[i.eb.hsebal01](i.eb.hsebal01.html)

Computes sensible heat flux iteration SEBAL 01.

[i.eb.netrad](i.eb.netrad.html)

Net radiation approximation (Bastiaanssen, 1995).

[i.eb.soilheatflux](i.eb.soilheatflux.html)

Soil heat flux approximation (Bastiaanssen, 1995).

[i.emissivity](i.emissivity.html)

Computes emissivity from NDVI, generic method for sparse land.

[i.evapo.mh](i.evapo.mh.html)

Computes evapotranspiration calculation modified or original Hargreaves formulation, 2001.

[i.evapo.pm](i.evapo.pm.html)

Computes potential evapotranspiration calculation with hourly Penman-Monteith.

[i.evapo.pt](i.evapo.pt.html)

Computes evapotranspiration calculation Priestley and Taylor formulation, 1972.

[i.evapo.time](i.evapo.time.html)

Computes temporal integration of satellite ET actual (ETa) following the daily ET reference (ETo) from meteorological station(s).

[i.fft](i.fft.html)

Fast Fourier Transform (FFT) for image processing.

[i.gensig](i.gensig.html)

Generates statistics for i.maxlik from raster map.

[i.gensigset](i.gensigset.html)

Generates statistics for i.smap from raster map.

[i.group](i.group.html)

Creates, edits, and lists groups of imagery data.

[i.his.rgb](i.his.rgb.html)

Transforms raster maps from HIS (Hue-Intensity-Saturation) color space to RGB (Red-Green-Blue) color space.

[i.ifft](i.ifft.html)

Inverse Fast Fourier Transform (IFFT) for image processing.

[i.image.mosaic](i.image.mosaic.html)

Mosaics several images and extends colormap.

[i.in.spotvgt](i.in.spotvgt.html)

Imports SPOT VGT NDVI data into a raster map.

[i.landsat.acca](i.landsat.acca.html)

Performs Landsat TM/ETM+ Automatic Cloud Cover Assessment (ACCA).

[i.landsat.toar](i.landsat.toar.html)

Calculates top-of-atmosphere radiance or reflectance and temperature for Landsat MSS/TM/ETM+/OLI

[i.maxlik](i.maxlik.html)

Classifies the cell spectral reflectances in imagery data.  

[i.modis.qc](i.modis.qc.html)

Extracts quality control parameters from MODIS QC layers.

[i.oif](i.oif.html)

Calculates Optimum-Index-Factor table for spectral bands

[i.ortho.camera](i.ortho.camera.html)

Select and modify the imagery group camera reference file.

[i.ortho.elev](i.ortho.elev.html)

Select or modify the target elevation model.

[i.ortho.init](i.ortho.init.html)

Interactively creates or modifies entries in a camera initial exposure station file for imagery group referenced by a sub-block.

[i.ortho.photo](i.ortho.photo.html)

Menu driver for the photo imagery programs.

[i.ortho.rectify](i.ortho.rectify.html)

Orthorectifies an image by using the image to photo coordinate transformation matrix.

[i.ortho.target](i.ortho.target.html)

Select or modify the imagery group target.

[i.ortho.transform](i.ortho.transform.html)

Computes a coordinate transformation based on the control points.

[i.pansharpen](i.pansharpen.html)

Image fusion algorithms to sharpen multispectral with high-res panchromatic channels

[i.pca](i.pca.html)

Principal components analysis (PCA) for image processing.

[i.rectify](i.rectify.html)

Rectifies an image by computing a coordinate transformation for each pixel in the image based on the control points.

[i.rgb.his](i.rgb.his.html)

Transforms raster maps from RGB (Red-Green-Blue) color space to HIS (Hue-Intensity-Saturation) color space.

[i.segment](i.segment.html)

Identifies segments (objects) from imagery data.

[i.signatures](i.signatures.html)

Manage imagery classification signature files

[i.smap](i.smap.html)

Performs contextual image classification using sequential maximum a posteriori (SMAP) estimation.

[i.spectral](i.spectral.html)

Displays spectral response at user specified locations in group or images.

[i.svm.predict](i.svm.predict.html)

Predict with a SVM  

[i.svm.train](i.svm.train.html)

Train a SVM  

[i.target](i.target.html)

Targets an imagery group to a GRASS location and mapset.

[i.tasscap](i.tasscap.html)

Performs Tasseled Cap (Kauth Thomas) transformation.

[i.topo.corr](i.topo.corr.html)

Computes topographic correction of reflectance.

[i.vi](i.vi.html)

Calculates different types of vegetation indices.  

[i.zc](i.zc.html)

Zero-crossing "edge detection" raster function for image processing.

### Miscellaneous commands (m.\*)

[m.cogo](m.cogo.html)

A simple utility for converting bearing and distance measurements to coordinates and vice versa.  

[m.measure](m.measure.html)

Measures the lengths and areas of features.

[m.nviz.image](m.nviz.image.html)

Creates a 3D rendering of GIS data.  

[m.nviz.script](m.nviz.script.html)

Creates fly-through script to run in NVIZ.

[m.proj](m.proj.html)

Converts coordinates from one projection to another (cs2cs frontend).

[m.transform](m.transform.html)

Computes a coordinate transformation based on the control points.

### PostScript commands (ps.\*)

[ps.map](ps.map.html)

Produces hardcopy PostScript map output.

### Raster commands (r.\*)

[r.basins.fill](r.basins.fill.html)

Generates watershed subbasins raster map.

[r.blend](r.blend.html)

Blends color components of two raster maps by a given ratio.

[r.buffer](r.buffer.html)

Creates a raster map showing buffer zones surrounding cells that contain non-NULL category values.

[r.buffer.lowmem](r.buffer.lowmem.html)

Creates a raster map showing buffer zones surrounding cells that contain non-NULL category values.  

[r.buildvrt](r.buildvrt.html)

Build a VRT (Virtual Raster) from the list of input raster maps.

[r.carve](r.carve.html)

Generates stream channels.  

[r.category](r.category.html)

Manages category values and labels associated with user-specified raster map layers.

[r.circle](r.circle.html)

Creates a raster map containing concentric rings around a given point.

[r.clump](r.clump.html)

Recategorizes data in a raster map by grouping cells that form physically discrete areas into unique categories.

[r.coin](r.coin.html)

Tabulates the mutual occurrence (coincidence) of categories for two raster map layers.

[r.colors](r.colors.html)

Creates/modifies the color table associated with a raster map.

[r.colors.out](r.colors.out.html)

Exports the color table associated with a raster map.

[r.colors.stddev](r.colors.stddev.html)

Sets color rules based on stddev from a raster map's mean value.

[r.composite](r.composite.html)

Combines red, green and blue raster maps into a single composite raster map.

[r.compress](r.compress.html)

Compresses and decompresses raster maps.

[r.contour](r.contour.html)

Produces a vector map of specified contours from a raster map.

[r.cost](r.cost.html)

Creates a raster map showing the cumulative cost of moving between different geographic locations on an input raster map whose cell category values represent cost.

[r.covar](r.covar.html)

Outputs a covariance/correlation matrix for user-specified raster map layer(s).

[r.cross](r.cross.html)

Creates a cross product of the category values from multiple raster map layers.

[r.describe](r.describe.html)

Prints terse list of category values found in a raster map layer.

[r.distance](r.distance.html)

Locates the closest points between objects in two raster maps.

[r.drain](r.drain.html)

Traces a flow through an elevation model or cost surface on a raster map.

[r.external](r.external.html)

Links GDAL supported raster data as a pseudo GRASS raster map.

[r.external.out](r.external.out.html)

Redirects raster output to file utilizing GDAL library rather than storing in GRASS raster format.

[r.fill.dir](r.fill.dir.html)

Filters and generates a depressionless elevation map and a flow direction map from a given elevation raster map.

[r.fill.stats](r.fill.stats.html)

Rapidly fills 'no data' cells (NULLs) of a raster map with interpolated values (IDW).

[r.fillnulls](r.fillnulls.html)

Fills no-data areas in raster maps using spline interpolation.

[r.flow](r.flow.html)

Constructs flowlines.  

[r.geomorphon](r.geomorphon.html)

Calculates geomorphons (terrain forms) and associated geometry using machine vision approach.

[r.grow.distance](r.grow.distance.html)

Generates a raster map containing distances to nearest raster features and/or the value of the nearest non-null cell.

[r.grow](r.grow.html)

Generates a raster map layer with contiguous areas grown by one cell.

[r.gwflow](r.gwflow.html)

Numerical calculation program for transient, confined and unconfined groundwater flow in two dimensions.

[r.his](r.his.html)

Generates red, green and blue (RGB) raster map layers combining hue, intensity and saturation (HIS) values from user-specified input raster map layers.

[r.horizon](r.horizon.html)

Computes horizon angle height from a digital elevation model.  

[r.import](r.import.html)

Imports raster data into a GRASS raster map using GDAL library and reprojects on the fly.

[r.in.ascii](r.in.ascii.html)

Converts a GRASS ASCII raster file to binary raster map.

[r.in.aster](r.in.aster.html)

Georeference, rectify, and import Terra-ASTER imagery and relative DEMs using gdalwarp.

[r.in.bin](r.in.bin.html)

Import a binary raster file into a GRASS raster map layer.

[r.in.gdal](r.in.gdal.html)

Imports raster data into a GRASS raster map using GDAL library.

[r.in.gridatb](r.in.gridatb.html)

Imports GRIDATB.FOR map file (TOPMODEL) into a GRASS raster map.

[r.in.mat](r.in.mat.html)

Imports a binary MAT-File(v4) to a GRASS raster.

[r.in.pdal](r.in.pdal.html)

Creates a raster map from LAS LiDAR points using univariate statistics.

[r.in.png](r.in.png.html)

Imports non-georeferenced PNG format image.

[r.in.poly](r.in.poly.html)

Creates raster maps from ASCII polygon/line/point data files.

[r.in.srtm](r.in.srtm.html)

Imports SRTM HGT files into raster map.

[r.in.wms](r.in.wms.html)

Downloads and imports data from OGC WMS and OGC WMTS web mapping servers.

[r.in.xyz](r.in.xyz.html)

Creates a raster map from an assemblage of many coordinates using univariate statistics.

[r.info](r.info.html)

Outputs basic information about a raster map.

[r.kappa](r.kappa.html)

Calculates error matrix and kappa parameter for accuracy assessment of classification result.

[r.lake](r.lake.html)

Fills lake at given point to given level.

[r.latlong](r.latlong.html)

Creates a latitude/longitude raster map.

[r.li.cwed](r.li.cwed.html)

Calculates contrast weighted edge density index on a raster map

[r.li.daemon](r.li.daemon.html)

Support module for r.li landscape index calculations.

[r.li.dominance](r.li.dominance.html)

Calculates dominance's diversity index on a raster map

[r.li.edgedensity](r.li.edgedensity.html)

Calculates edge density index on a raster map, using a 4 neighbour algorithm

[r.li](r.li.html)

Landscape structure analysis package overview

[r.li.mpa](r.li.mpa.html)

Calculates mean pixel attribute index on a raster map

[r.li.mps](r.li.mps.html)

Calculates mean patch size index on a raster map, using a 4 neighbour algorithm

[r.li.padcv](r.li.padcv.html)

Calculates coefficient of variation of patch area on a raster map

[r.li.padrange](r.li.padrange.html)

Calculates range of patch area size on a raster map

[r.li.padsd](r.li.padsd.html)

Calculates standard deviation of patch area a raster map

[r.li.patchdensity](r.li.patchdensity.html)

Calculates patch density index on a raster map, using a 4 neighbour algorithm

[r.li.patchnum](r.li.patchnum.html)

Calculates patch number index on a raster map, using a 4 neighbour algorithm.

[r.li.pielou](r.li.pielou.html)

Calculates Pielou's diversity index on a raster map

[r.li.renyi](r.li.renyi.html)

Calculates Renyi's diversity index on a raster map

[r.li.richness](r.li.richness.html)

Calculates richness index on a raster map

[r.li.shannon](r.li.shannon.html)

Calculates Shannon's diversity index on a raster map

[r.li.shape](r.li.shape.html)

Calculates shape index on a raster map

[r.li.simpson](r.li.simpson.html)

Calculates Simpson's diversity index on a raster map

[r.mapcalc](r.mapcalc.html)

Raster map calculator.

[r.mapcalc.simple](r.mapcalc.simple.html)

Calculates a new raster map from a simple r.mapcalc expression.

[r.mask](r.mask.html)

Creates a MASK for limiting raster operation.

[r.mfilter](r.mfilter.html)

Performs raster map matrix filter.

[r.mode](r.mode.html)

Finds the mode of values in a cover map within areas assigned the same category value in a user-specified base map.

[r.neighbors](r.neighbors.html)

Makes each cell category value a function of the category values assigned to the cells around it, and stores new cell values in an output raster map layer.

[r.null](r.null.html)

Manages NULL-values of given raster map.

[r.object.geometry](r.object.geometry.html)

Calculates geometry parameters for raster objects.

[r.out.ascii](r.out.ascii.html)

Converts a raster map layer into a GRASS ASCII text file.

[r.out.bin](r.out.bin.html)

Exports a GRASS raster to a binary array.

[r.out.gdal](r.out.gdal.html)

Exports GRASS raster maps into GDAL supported formats.

[r.out.gridatb](r.out.gridatb.html)

Exports GRASS raster map to GRIDATB.FOR map file (TOPMODEL).

[r.out.mat](r.out.mat.html)

Exports a GRASS raster to a binary MAT-File.

[r.out.mpeg](r.out.mpeg.html)

Converts raster map series to MPEG movie.

[r.out.png](r.out.png.html)

Export a GRASS raster map as a non-georeferenced PNG image.

[r.out.pov](r.out.pov.html)

Converts a raster map layer into a height-field file for POV-Ray.

[r.out.ppm](r.out.ppm.html)

Converts a GRASS raster map to a PPM image file.

[r.out.ppm3](r.out.ppm3.html)

Converts 3 GRASS raster layers (R,G,B) to a PPM image file.

[r.out.vrml](r.out.vrml.html)

Exports a raster map to the Virtual Reality Modeling Language (VRML).

[r.out.vtk](r.out.vtk.html)

Converts raster maps into the VTK-ASCII format.

[r.out.xyz](r.out.xyz.html)

Exports a raster map to a text file as x,y,z values based on cell centers.

[r.pack](r.pack.html)

Exports a raster map as GRASS GIS specific archive file

[r.param.scale](r.param.scale.html)

Extracts terrain parameters from a DEM.  

[r.patch](r.patch.html)

Creates a composite raster map layer by using known category values from one (or more) map layer(s) to fill in areas of "no data" in another map layer.

[r.path](r.path.html)

Traces paths from starting points following input directions.

[r.plane](r.plane.html)

Creates raster plane map given dip (inclination), aspect (azimuth) and one point.

[r.profile](r.profile.html)

Outputs the raster map layer values lying on user-defined line(s).

[r.proj](r.proj.html)

Re-projects a raster map from given project to the current project.

[r.quant](r.quant.html)

Produces the quantization file for a floating-point map.

[r.quantile](r.quantile.html)

Compute quantiles using two passes.

[r.random.cells](r.random.cells.html)

Generates random cell values with spatial dependence.

[r.random](r.random.html)

Creates randomly placed raster cells or vector points  

[r.random.surface](r.random.surface.html)

Generates random surface(s) with spatial dependence.

[r.reclass.area](r.reclass.area.html)

Reclasses a raster map greater or less than user specified area size (in hectares).

[r.reclass](r.reclass.html)

Reclassify raster map based on category values.  

[r.recode](r.recode.html)

Recodes categorical raster maps.

[r.region](r.region.html)

Sets the boundary definitions for a raster map.

[r.regression.line](r.regression.line.html)

Calculates linear regression from two raster maps: y = a + b\*x.

[r.regression.multi](r.regression.multi.html)

Calculates multiple linear regression from raster maps.

[r.relief](r.relief.html)

Creates shaded relief map from an elevation map (DEM).  

[r.report](r.report.html)

Reports statistics for raster maps.

[r.resamp.bspline](r.resamp.bspline.html)

Performs bilinear or bicubic spline interpolation with Tykhonov regularization.

[r.resamp.filter](r.resamp.filter.html)

Resamples raster map layers using an analytic kernel.

[r.resamp.interp](r.resamp.interp.html)

Resamples raster map to a finer grid using interpolation.

[r.resamp.rst](r.resamp.rst.html)

Reinterpolates and optionally computes topographic analysis from input raster map to a new raster map (possibly with different resolution) using regularized spline with tension and smoothing.

[r.resamp.stats](r.resamp.stats.html)

Resamples raster map layers to a coarser grid using aggregation.

[r.resample](r.resample.html)

GRASS raster map layer data resampling capability.

[r.rescale.eq](r.rescale.eq.html)

Rescales histogram equalized the range of category values in a raster map layer.

[r.rescale](r.rescale.html)

Rescales the range of category values in a raster map layer.

[r.rgb](r.rgb.html)

Splits a raster map into red, green and blue maps.

[r.ros](r.ros.html)

Generates rate of spread raster maps.  

[r.semantic.label](r.semantic.label.html)

Manages semantic label information assigned to a single raster map or to a list of raster maps.

[r.series.accumulate](r.series.accumulate.html)

Makes each output cell value a accumulationfunction of the values assigned to the corresponding cells in the input raster map layers.

[r.series](r.series.html)

Makes each output cell value a function of the values assigned to the corresponding cells in the input raster map layers.

[r.series.interp](r.series.interp.html)

Interpolates raster maps located (temporal or spatial) in between input raster maps at specific sampling positions.

[r.shade](r.shade.html)

Drapes a color raster over an shaded relief or aspect map.

[r.sim.sediment](r.sim.sediment.html)

Sediment transport and erosion/deposition simulation using path sampling method (SIMWE).

[r.sim.water](r.sim.water.html)

Overland flow hydrologic simulation using path sampling method (SIMWE).

[r.slope.aspect](r.slope.aspect.html)

Generates raster maps of slope, aspect, curvatures and partial derivatives from an elevation raster map.  

[r.solute.transport](r.solute.transport.html)

Numerical calculation program for transient, confined and unconfined solute transport in two dimensions

[r.spread](r.spread.html)

Simulates elliptically anisotropic spread.  

[r.spreadpath](r.spreadpath.html)

Recursively traces the least cost path backwards to cells from which the cumulative cost was determined.

[r.statistics](r.statistics.html)

Calculates category or object oriented statistics.

[r.stats](r.stats.html)

Generates area statistics for raster map.

[r.stats.quantile](r.stats.quantile.html)

Compute category quantiles using two passes.

[r.stats.zonal](r.stats.zonal.html)

Calculates category or object oriented statistics (accumulator-based statistics).

[r.stream.extract](r.stream.extract.html)

Performs stream network extraction.

[r.sun](r.sun.html)

Solar irradiance and irradiation model.  

[r.sunhours](r.sunhours.html)

Calculates solar elevation, solar azimuth, and sun hours.  

[r.sunmask](r.sunmask.html)

Calculates cast shadow areas from sun position and elevation raster map.  

[r.support](r.support.html)

Allows creation and/or modification of raster map layer support files.

[r.support.stats](r.support.stats.html)

Update raster map statistics

[r.surf.area](r.surf.area.html)

Prints estimation of surface area for raster map.

[r.surf.contour](r.surf.contour.html)

Generates surface raster map from rasterized contours.

[r.surf.fractal](r.surf.fractal.html)

Creates a fractal surface of a given fractal dimension.

[r.surf.gauss](r.surf.gauss.html)

Generates a raster map using gaussian random number generator.  

[r.surf.idw](r.surf.idw.html)

Provides surface interpolation from raster point data by Inverse Distance Squared Weighting.

[r.surf.random](r.surf.random.html)

Produces a raster surface map of uniform random deviates with defined range.

[r.terraflow](r.terraflow.html)

Performs flow computation for massive grids.

[r.texture](r.texture.html)

Generate images with textural features from a raster map.

[r.thin](r.thin.html)

Thins non-null cells that denote linear features in a raster map layer.

[r.tile](r.tile.html)

Splits a raster map into tiles.

[r.tileset](r.tileset.html)

Produces tilings of the source projection for use in the destination region and projection.

[r.timestamp](r.timestamp.html)

Modifies a timestamp for a raster map.  

[r.to.rast3](r.to.rast3.html)

Converts 2D raster map slices to one 3D raster volume map.

[r.to.rast3elev](r.to.rast3elev.html)

Creates a 3D volume map based on 2D elevation and value raster maps.

[r.to.vect](r.to.vect.html)

Converts a raster map into a vector map.

[r.topidx](r.topidx.html)

Creates a topographic index (wetness index) raster map from an elevation raster map.

[r.topmodel](r.topmodel.html)

Simulates TOPMODEL which is a physically based hydrologic model.

[r.transect](r.transect.html)

Outputs raster map layer values lying along user defined transect line(s).

[r.univar](r.univar.html)

Calculates univariate statistics from the non-null cells of a raster map.  

[r.unpack](r.unpack.html)

Imports a GRASS GIS specific raster archive file (packed with r.pack) as a raster map

[r.uslek](r.uslek.html)

Computes USLE Soil Erodibility Factor (K).

[r.usler](r.usler.html)

Computes USLE R factor, Rainfall erosivity index.

[r.viewshed](r.viewshed.html)

Computes the viewshed of a point on an elevation raster map.  

[r.volume](r.volume.html)

Calculates the volume of data "clumps".  

[r.walk](r.walk.html)

Creates a raster map showing the anisotropic cumulative cost of moving between different geographic locations on an input raster map whose cell category values represent cost.

[r.water.outlet](r.water.outlet.html)

Creates watershed basins from a drainage direction map.

[r.watershed](r.watershed.html)

Calculates hydrological parameters and RUSLE factors.

[r.what.color](r.what.color.html)

Queries colors for a raster map layer.

[r.what](r.what.html)

Queries raster maps on their category values and category labels.

### 3d raster commands (r3.\*)

[r3.colors](r3.colors.html)

Creates/modifies the color table associated with a 3D raster map.

[r3.colors.out](r3.colors.out.html)

Exports the color table associated with a 3D raster map.

[r3.cross.rast](r3.cross.rast.html)

Creates cross section 2D raster map from 3D raster map based on 2D elevation map

[r3.flow](r3.flow.html)

Computes 3D flow lines and 3D flow accumulation.

[r3.gradient](r3.gradient.html)

Computes gradient of a 3D raster map and outputs gradient components as three 3D raster maps.

[r3.gwflow](r3.gwflow.html)

Numerical calculation program for transient, confined groundwater flow in three dimensions.

[r3.in.ascii](r3.in.ascii.html)

Converts a 3D ASCII raster text file into a (binary) 3D raster map.

[r3.in.bin](r3.in.bin.html)

Imports a binary raster file into a GRASS 3D raster map.

[r3.in.v5d](r3.in.v5d.html)

Import 3-dimensional Vis5D files.

[r3.in.xyz](r3.in.xyz.html)

Create a 3D raster map from an assemblage of many coordinates using univariate statistics

[r3.info](r3.info.html)

Outputs basic information about a user-specified 3D raster map layer.

[r3.mapcalc](r3.mapcalc.html)

Raster map calculator.

[r3.mask](r3.mask.html)

Establishes the current working 3D raster mask.

[r3.mkdspf](r3.mkdspf.html)

Creates a display file from an existing 3D raster map according to specified threshold levels.

[r3.neighbors](r3.neighbors.html)

Makes each voxel value a function of the values assigned to the voxels around it, and stores new voxel values in an output 3D raster map

[r3.null](r3.null.html)

Explicitly create the 3D NULL-value bitmap file.

[r3.out.ascii](r3.out.ascii.html)

Converts a 3D raster map layer into a ASCII text file.

[r3.out.bin](r3.out.bin.html)

Exports a GRASS 3D raster map to a binary array.

[r3.out.netcdf](r3.out.netcdf.html)

Export a 3D raster map as netCDF file.

[r3.out.v5d](r3.out.v5d.html)

Exports GRASS 3D raster map to 3-dimensional Vis5D file.

[r3.out.vtk](r3.out.vtk.html)

Converts 3D raster maps into the VTK-ASCII format.

[r3.retile](r3.retile.html)

Retiles an existing 3D raster map with user defined x, y and z tile size.

[r3.stats](r3.stats.html)

Generates volume statistics for 3D raster maps.

[r3.support](r3.support.html)

Allows creation and/or modification of 3D raster map layer support files.

[r3.timestamp](r3.timestamp.html)

Modifies a timestamp for a 3D raster map.  

[r3.to.rast](r3.to.rast.html)

Converts 3D raster maps to 2D raster maps

[r3.univar](r3.univar.html)

Calculates univariate statistics from the non-null cells of a 3D raster map.  

### Temporal commands (t.\*)

[t.connect](t.connect.html)

Prints/sets general temporal GIS database connection for current mapset.

[t.copy](t.copy.html)

Creates a copy of a space time raster dataset.

[t.create](t.create.html)

Creates a space time dataset.

[t.info](t.info.html)

Lists information about space time datasets and maps.

[t.list](t.list.html)

Lists space time datasets and maps registered in the temporal database.

[t.merge](t.merge.html)

Merges several space time datasets into a single space time dataset.

[t.rast.accdetect](t.rast.accdetect.html)

Detects accumulation patterns in temporally accumulated space time raster datasets created by t.rast.accumulate.

[t.rast.accumulate](t.rast.accumulate.html)

Computes cyclic accumulations of a space time raster dataset.

[t.rast.aggregate.ds](t.rast.aggregate.ds.html)

Aggregates data of an existing space time raster dataset using the time intervals of a second space time dataset.

[t.rast.aggregate](t.rast.aggregate.html)

Aggregates temporally the maps of a space time raster dataset by a user defined granularity.

[t.rast.algebra](t.rast.algebra.html)

Apply temporal and spatial operations on space time raster datasets using temporal raster algebra.

[t.rast.colors](t.rast.colors.html)

Creates/modifies the color table associated with each raster map of the space time raster dataset.

[t.rast.contour](t.rast.contour.html)

Produces a space time vector dataset of specified contours from a space time raster dataset.

[t.rast.export](t.rast.export.html)

Exports space time raster dataset.

[t.rast.extract](t.rast.extract.html)

Extracts a subset of a space time raster datasets.

[t.rast.gapfill](t.rast.gapfill.html)

Replaces gaps in a space time raster dataset with interpolated raster maps.

[t.rast.import](t.rast.import.html)

Imports space time raster dataset.

[t.rast.list](t.rast.list.html)

Lists registered maps of a space time raster dataset.

[t.rast.mapcalc](t.rast.mapcalc.html)

Performs spatio-temporal mapcalc expressions on temporally sampled maps of space time raster datasets.

[t.rast.neighbors](t.rast.neighbors.html)

Performs a neighborhood analysis for each map in a space time raster dataset.

[t.rast.out.vtk](t.rast.out.vtk.html)

Exports space time raster dataset as VTK time series.

[t.rast.series](t.rast.series.html)

Performs different aggregation algorithms from r.series on all or a subset of raster maps in a space time raster dataset.

[t.rast.to.rast3](t.rast.to.rast3.html)

Converts a space time raster dataset into a 3D raster map.

[t.rast.to.vect](t.rast.to.vect.html)

Converts a space time raster dataset into a space time vector dataset

[t.rast.univar](t.rast.univar.html)

Calculates univariate statistics from the non-null cells for each registered raster map of a space time raster dataset.

[t.rast.what](t.rast.what.html)

Sample a space time raster dataset at specific vector point coordinates and write the output to stdout using different layouts

[t.rast3d.algebra](t.rast3d.algebra.html)

Apply temporal and spatial operations on space time 3D raster datasets using temporal 3D raster algebra.

[t.rast3d.extract](t.rast3d.extract.html)

Extracts a subset of a space time 3D raster dataset.

[t.rast3d.list](t.rast3d.list.html)

Lists registered maps of a space time raster3d dataset.

[t.rast3d.mapcalc](t.rast3d.mapcalc.html)

Performs r3.mapcalc expressions on maps of sampled space time 3D raster datasets.

[t.rast3d.univar](t.rast3d.univar.html)

Calculates univariate statistics from the non-null cells for each registered 3D raster map of a space time 3D raster dataset.

[t.register](t.register.html)

Assigns timestamps and registers raster, vector and raster3d maps in a space time dataset.

[t.remove](t.remove.html)

Removes space time datasets from temporal database.

[t.rename](t.rename.html)

Renames a space time dataset

[t.sample](t.sample.html)

Samples the input space time dataset(s) with a sample space time dataset and print the result to stdout.

[t.select](t.select.html)

Select maps from space time datasets by topological relationships to other space time datasets using temporal algebra.

[t.shift](t.shift.html)

Shifts temporally the maps of a space time dataset.

[t.snap](t.snap.html)

Snaps temporally the maps of a space time dataset.

[t.support](t.support.html)

Modifies the metadata of a space time dataset.

[t.topology](t.topology.html)

Lists temporal topology of a space time dataset.

[t.unregister](t.unregister.html)

Unregisters raster, vector and raster3d maps from the temporal database or a specific space time dataset.

[t.upgrade](t.upgrade.html)

Upgrades the version of the temporal database.

[t.vect.algebra](t.vect.algebra.html)

Apply temporal and spatial operations on space time vector datasets using temporal vector algebra.

[t.vect.db.select](t.vect.db.select.html)

Prints attributes of vector maps registered in a space time vector dataset.

[t.vect.export](t.vect.export.html)

Exports a space time vector dataset as GRASS GIS specific archive file.

[t.vect.extract](t.vect.extract.html)

Extracts a subset of a space time vector dataset.

[t.vect.import](t.vect.import.html)

Imports a space time vector dataset from a GRASS GIS specific archive file.

[t.vect.list](t.vect.list.html)

Lists registered maps of a space time vector dataset.

[t.vect.observe.strds](t.vect.observe.strds.html)

Observes specific locations in a space time raster dataset over a period of time using vector points.

[t.vect.univar](t.vect.univar.html)

Calculates univariate statistics of attributes for each registered vector map of a space time vector dataset

[t.vect.what.strds](t.vect.what.strds.html)

Stores raster map values at spatial and temporal positions of vector points as vector attributes.

### Test commands (test.\*)

[test.r3flow](test.r3flow.html)

Testing flow lines.

[test.raster3d.lib](test.raster3d.lib.html)

Performs unit and integration tests for the raster3d library

### Vector commands (v.\*)

[v.buffer](v.buffer.html)

Creates a buffer around vector features of given type.

[v.build.all](v.build.all.html)

Rebuilds topology on all vector maps in the current mapset.

[v.build](v.build.html)

Creates topology for vector map.  

[v.build.polylines](v.build.polylines.html)

Builds polylines from lines or boundaries.

[v.category](v.category.html)

Attaches, deletes or reports vector categories to/from/of map geometry.

[v.centroids](v.centroids.html)

Adds missing centroids to closed boundaries.

[v.class](v.class.html)

Classifies attribute data, e.g. for thematic mapping

[v.clean](v.clean.html)

Toolset for cleaning topology of vector map.

[v.clip](v.clip.html)

Extracts features of input map which overlay features of clip map.

[v.cluster](v.cluster.html)

Performs cluster identification.

[v.colors](v.colors.html)

Creates/modifies the color table associated with a vector map.

[v.colors.out](v.colors.out.html)

Exports the color table associated with a vector map.

[v.db.addcolumn](v.db.addcolumn.html)

Adds one or more columns to the attribute table connected to a given vector map.

[v.db.addtable](v.db.addtable.html)

Creates and connects a new attribute table to a given layer of an existing vector map.

[v.db.connect](v.db.connect.html)

Prints/sets DB connection for a vector map to attribute table.

[v.db.dropcolumn](v.db.dropcolumn.html)

Drops a column from the attribute table connected to a given vector map.

[v.db.droprow](v.db.droprow.html)

Removes a vector feature from a vector map through attribute selection.

[v.db.droptable](v.db.droptable.html)

Removes existing attribute table of a vector map.

[v.db.join](v.db.join.html)

Joins a database table to a vector map table.

[v.db.reconnect.all](v.db.reconnect.all.html)

Reconnects attribute tables for all vector maps from the current mapset to a new database.

[v.db.renamecolumn](v.db.renamecolumn.html)

Renames a column in the attribute table connected to a given vector map.

[v.db.select](v.db.select.html)

Prints vector map attributes.

[v.db.univar](v.db.univar.html)

Calculates univariate statistics on selected table column for a GRASS vector map.

[v.db.update](v.db.update.html)

Updates a column in the attribute table connected to a vector map.

[v.decimate](v.decimate.html)

Decimates a point cloud  

[v.delaunay](v.delaunay.html)

Creates a Delaunay triangulation from an input vector map containing points or centroids.

[v.dissolve](v.dissolve.html)

Dissolves adjacent or overlaping features sharing a common category number or attribute.

[v.distance](v.distance.html)

Finds the nearest element in vector map 'to' for elements in vector map 'from'.

[v.drape](v.drape.html)

Converts 2D vector features to 3D by sampling of elevation raster map.

[v.edit](v.edit.html)

Edits a vector map, allows adding, deleting and modifying selected vector features.

[v.external](v.external.html)

Creates a new pseudo-vector map as a link to an OGR-supported layer or a PostGIS feature table.

[v.external.out](v.external.out.html)

Defines vector output format.

[v.extract](v.extract.html)

Selects vector features from an existing vector map and creates a new vector map containing only the selected features.

[v.extrude](v.extrude.html)

Extrudes flat vector features to 3D vector features with defined height.  

[v.fill.holes](v.fill.holes.html)

Fill holes in areas by keeping only outer boundaries

[v.generalize](v.generalize.html)

Performs vector based generalization.

[v.hull](v.hull.html)

Produces a 2D/3D convex hull for a given vector map.

[v.import](v.import.html)

Imports vector data into a GRASS vector map using OGR library and reprojects on the fly.

[v.in.ascii](v.in.ascii.html)

Creates a vector map from an ASCII points file or ASCII vector file.

[v.in.db](v.in.db.html)

Creates new vector (points) map from database table containing coordinates.

[v.in.dxf](v.in.dxf.html)

Converts file in DXF format to GRASS vector map.

[v.in.e00](v.in.e00.html)

Imports E00 file into a vector map.

[v.in.geonames](v.in.geonames.html)

Imports geonames.org country files into a vector points map.

[v.in.lines](v.in.lines.html)

Imports ASCII x,y\[,z\] coordinates as a series of lines.

[v.in.mapgen](v.in.mapgen.html)

Imports Mapgen or Matlab-ASCII vector maps into GRASS.

[v.in.ogr](v.in.ogr.html)

Imports vector data into a GRASS vector map using OGR library.

[v.in.pdal](v.in.pdal.html)

Converts LAS LiDAR point clouds to a GRASS vector map with PDAL.

[v.in.region](v.in.region.html)

Creates a vector polygon from the current region extent.

[v.in.wfs](v.in.wfs.html)

Imports GetFeature from a WFS server.

[v.info](v.info.html)

Outputs basic information about a vector map.

[v.kcv](v.kcv.html)

Randomly partition points into test/train sets.

[v.kernel](v.kernel.html)

Generates a raster density map from vector points map.  

[v.label](v.label.html)

Creates paint labels for a vector map from attached attributes.

[v.label.sa](v.label.sa.html)

Create optimally placed labels for vector map(s)

[v.lidar.correction](v.lidar.correction.html)

Corrects the v.lidar.growing output. It is the last of the three algorithms for LIDAR filtering.

[v.lidar.edgedetection](v.lidar.edgedetection.html)

Detects the object's edges from a LIDAR data set.

[v.lidar.growing](v.lidar.growing.html)

Building contour determination and Region Growing algorithm for determining the building inside

[v.lrs.create](v.lrs.create.html)

Creates a linear reference system.

[v.lrs.label](v.lrs.label.html)

Creates stationing from input lines, and linear reference system.

[v.lrs.segment](v.lrs.segment.html)

Creates points/segments from input lines, linear reference system and positions read from stdin or a file.

[v.lrs.where](v.lrs.where.html)

Finds line id and real km+offset for given points in vector map using linear reference system.

[v.mkgrid](v.mkgrid.html)

Creates a vector map of a user-defined grid.

[v.neighbors](v.neighbors.html)

Neighborhood analysis tool for vector point maps.  

[v.net.alloc](v.net.alloc.html)

Allocates subnets for nearest centers.  

[v.net.allpairs](v.net.allpairs.html)

Computes the shortest path between all pairs of nodes in the network.

[v.net.bridge](v.net.bridge.html)

Computes bridges and articulation points in the network.

[v.net.centrality](v.net.centrality.html)

Computes degree, centrality, betweeness, closeness and eigenvector centrality measures in the network.

[v.net.components](v.net.components.html)

Computes strongly and weakly connected components in the network.

[v.net.connectivity](v.net.connectivity.html)

Computes vertex connectivity between two sets of nodes in the network.

[v.net.distance](v.net.distance.html)

Computes shortest distance via the network between the given sets of features.  

[v.net.flow](v.net.flow.html)

Computes the maximum flow between two sets of nodes in the network.

[v.net](v.net.html)

Performs network maintenance.

[v.net.iso](v.net.iso.html)

Splits subnets for nearest centers by cost isolines.  

[v.net.path](v.net.path.html)

Finds shortest path on vector network.

[v.net.salesman](v.net.salesman.html)

Creates a cycle connecting given nodes (Traveling salesman problem).  

[v.net.spanningtree](v.net.spanningtree.html)

Computes minimum spanning tree for the network.

[v.net.steiner](v.net.steiner.html)

Creates Steiner tree for the network and given terminals.  

[v.net.timetable](v.net.timetable.html)

Finds shortest path using timetables.

[v.net.visibility](v.net.visibility.html)

Performs visibility graph construction.

[v.normal](v.normal.html)

Tests for normality for vector points.

[v.out.ascii](v.out.ascii.html)

Exports a vector map to a GRASS ASCII vector representation.  

[v.out.dxf](v.out.dxf.html)

Exports vector map to DXF file format.

[v.out.ogr](v.out.ogr.html)

Exports a vector map layer to any of the supported OGR vector formats.  

[v.out.postgis](v.out.postgis.html)

Exports a vector map layer to PostGIS feature table.

[v.out.pov](v.out.pov.html)

Converts GRASS x,y,z points to POV-Ray x,z,y format.

[v.out.svg](v.out.svg.html)

Exports a vector map to SVG file.

[v.out.vtk](v.out.vtk.html)

Converts a vector map to VTK ASCII output.

[v.outlier](v.outlier.html)

Removes outliers from vector point data.

[v.overlay](v.overlay.html)

Overlays two vector maps offering clip, intersection, difference, symmetrical difference, union operators.

[v.pack](v.pack.html)

Exports a vector map as GRASS GIS specific archive file

[v.parallel](v.parallel.html)

Creates parallel line to input vector lines.

[v.patch](v.patch.html)

Creates a new vector map by combining other vector maps.

[v.perturb](v.perturb.html)

Random location perturbations of vector points.

[v.profile](v.profile.html)

Vector map profiling tool

[v.proj](v.proj.html)

Re-projects a vector map from one project to the current project.

[v.qcount](v.qcount.html)

Indices for quadrat counts of vector point lists.

[v.random](v.random.html)

Generates random 2D/3D vector points.

[v.rast.stats](v.rast.stats.html)

Calculates univariate statistics from a raster map based on a vector map and uploads statistics to new attribute columns.

[v.reclass](v.reclass.html)

Changes vector category values for an existing vector map according to results of SQL queries or a value in attribute table column.

[v.rectify](v.rectify.html)

Rectifies a vector by computing a coordinate transformation for each object in the vector based on the control points.

[v.report](v.report.html)

Reports geometry statistics for vector maps.

[v.sample](v.sample.html)

Samples a raster map at vector point locations.

[v.segment](v.segment.html)

Creates points/segments from input vector lines and positions.

[v.select](v.select.html)

Selects features from vector map (A) by features from other vector map (B).

[v.split](v.split.html)

Splits vector lines to shorter segments.

[v.support](v.support.html)

Updates vector map metadata.

[v.surf.bspline](v.surf.bspline.html)

Performs bicubic or bilinear spline interpolation with Tykhonov regularization.

[v.surf.idw](v.surf.idw.html)

Provides surface interpolation from vector point data by Inverse Distance Squared Weighting.

[v.surf.rst](v.surf.rst.html)

Performs surface interpolation from vector points map by splines.  

[v.timestamp](v.timestamp.html)

Modifies a timestamp for a vector map.  

[v.to.3d](v.to.3d.html)

Performs transformation of 2D vector features to 3D.

[v.to.db](v.to.db.html)

Populates attribute values from vector features.

[v.to.lines](v.to.lines.html)

Converts vector polygons or points to lines.

[v.to.points](v.to.points.html)

Creates points along input lines in new vector map with 2 layers.

[v.to.rast](v.to.rast.html)

Converts (rasterize) a vector map into a raster map.

[v.to.rast3](v.to.rast3.html)

Converts a vector map (only points) into a 3D raster map.

[v.transform](v.transform.html)

Performs an affine transformation (shift, scale and rotate) on vector map.

[v.type](v.type.html)

Changes type of vector features.

[v.univar](v.univar.html)

Calculates univariate statistics of vector map features.  

[v.unpack](v.unpack.html)

Imports a GRASS GIS specific vector archive file (packed with v.pack) as a vector map

[v.vect.stats](v.vect.stats.html)

Count points in areas, calculate statistics from point attributes.

[v.vol.rst](v.vol.rst.html)

Interpolates point data to a 3D raster map using regularized spline with tension (RST) algorithm.

[v.voronoi](v.voronoi.html)

Creates a Voronoi diagram constrained to the extents of the current region from an input vector map containing points or centroids.

[v.what](v.what.html)

Queries a vector map at given locations.

[v.what.rast](v.what.rast.html)

Uploads raster values at positions of vector points to the table.

[v.what.rast3](v.what.rast3.html)

Uploads 3D raster values at positions of vector points to the table.

[v.what.strds](v.what.strds.html)

Uploads space time raster dataset values at positions of vector points to the table.

[v.what.vect](v.what.vect.html)

Uploads vector values at positions of vector points to the table.

* * *

[Main index](index.html) | [Topics index](topics.html) | [Keywords index](keywords.html) | [Graphical index](graphical_index.html) | [Full index](full_index.html)

© 2003-2025 [GRASS Development Team](https://grass.osgeo.org), GRASS GIS 8.4.3dev Reference Manual

