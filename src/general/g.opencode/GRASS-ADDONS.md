# GRASS-ADDONS.md - Listing of GRASS Commands
This document was created by https://codebeautify.org/html-to-markdown in order to convert the [GRASS GIS 8.4.3dev Addons Manual Pages](https://grass.osgeo.org/grass-stable/manuals/addons/) from HTML to Markdown.


GRASS GIS 8.4 Addons Manual pages   

GRASS GIS 8.4 Addons Manual pages
---------------------------------

[GRASS GIS](https://grass.osgeo.org) is free software, anyone may develop his/her own extensions (addons). The [GRASS GIS Addons repository](https://github.com/OSGeo/grass-addons) on GitHub contains a growing list of links to GRASS GIS extensions, which are currently not part of the core software package.  
Addons can easily be **installed** in your local GRASS GIS installation through the graphical user interface (_Menu - Settings - Addons Extension - Install_) or via the [g.extension](../g.extension.html) command.

_These manual pages are updated daily. Last run: 14 Jan 2026_

How to contribute?

You may propose your Addon to the [GRASS GIS Addons repository](https://github.com/OSGeo/grass-addons). Please read the [Contributing](https://github.com/OSGeo/grass-addons/blob/grass8/CONTRIBUTING.md) document as well as the [GRASS GIS programming best practice](https://trac.osgeo.org/grass/wiki/Submitting).

How to get the addons source code:

git clone https://github.com/OSGeo/grass-addons.git

See also log files of compilation: [Linux log files](https://grass.osgeo.org/addons/grass8/logs) | [Windows log files](https://wingrass.fsv.cvut.cz/grass84/addons/grass-8.4.1/logs/)

* * *

#### Table of contents

*   [Display commands (d.\*)](#d)
*   [Database commands (db.\*)](#db)
*   [General commands (g.\*)](#g)
*   [Imagery commands (i.\*)](#i)
*   [Miscellaneous commands (m.\*)](#m)
*   [PostScript commands (ps.\*)](#ps)
*   [Raster commands (r.\*)](#r)
*   [3D raster commands (r3.\*)](#r3)
*   [Temporal commands (t.\*)](#t)
*   [Vector commands (v.\*)](#v)

### Database

*   [db.csw.admin](db.csw.admin.html): CSW database manager
*   [db.csw.harvest](db.csw.harvest.html): CSW database manager
*   [db.csw.run](db.csw.run.html): CSW wsgi handler
*   [db.join](db.join.html): Joins a database table to another database table.

### Display

*   [d.explanation.plot](d.explanation.plot.html): Draw a plot of multiple rasters to explain a raster operation for example a + b = c
*   [d.frame](d.frame.html): Manages display frames on the user's graphics monitor.
*   [d.mon2](d.mon2.html): Starts a graphics display monitor which can be controlled from the command line.
*   [d.region.grid](d.region.grid.html): Drapes a color raster over an shaded relief or aspect map.
*   [d.vect.thematic2](d.vect.thematic2.html): Displays thematic map created from vector features and numeric attributes.

### General

*   [g.citation](g.citation.html): Provide scientific citation for GRASS modules and add-ons.
*   [g.compare.md5](g.compare.md5.html): Checks if two GRASS GIS maps are identical.
*   [g.copyall](g.copyall.html): Copies all or a filtered subset of files of selected type from another mapset to the current working mapset.
*   [g.download.location](g.download.location.html): Download GRASS Location from the web
*   [g.gui.cswbrowser](g.gui.cswbrowser.html): Graphical CSW metadata browser.
*   [g.gui.metadata](g.gui.metadata.html): Graphical ISO/INSPIRE metadata editor.
*   [g.gui.mwprecip](g.gui.mwprecip.html): The module for processing row data of microwave links to precipitation.
*   [g.isis3mt](g.isis3mt.html): Generates an ISIS3 map template file according to the current GRASS GIS coordinate reference system.
*   [g.proj.all](g.proj.all.html): Reprojects raster and vector maps from given location and mapset to current mapset.
*   [g.proj.identify](g.proj.identify.html): Autoidentifies EPSG code from WKT CRS definition.
*   [g.projpicker](g.projpicker.html): Queries projection information spatially.
*   [g.rename.many](g.rename.many.html): Renames multiple maps in the current mapset.

### Imagery

*   [i.ann.maskrcnn.detect](i.ann.maskrcnn.detect.html): Detect features in images using a Mask R-CNN model
*   [i.ann.maskrcnn](i.ann.maskrcnn.html): Mask R-CNN toolset
*   [i.ann.maskrcnn.train](i.ann.maskrcnn.train.html): Train your Mask R-CNN network
*   [i.cutlines](i.cutlines.html): Creates semantically meaningful tile borders
*   [i.cva](i.cva.html): Performs Change Vector Analysis (CVA) in two dimensions.
*   [i.destripe](i.destripe.html): Destripes regularly, about vertical, striped image using Fourier.
*   [i.eb.deltat](i.eb.deltat.html): Computes the difference of temperature between surface skin temperature and air temperature at 2m as part of sensible heat flux calculations.
*   [i.eb.hsebal95](i.eb.hsebal95.html): Performs sensible heat flux iteration (SEBAL 95).
*   [i.eb.z0m0](i.eb.z0m0.html): Computes momentum roughness length (z0m) and surface roughness for heat transport (z0h) after Bastiaanssen (2004).
*   [i.eb.z0m](i.eb.z0m.html): Computes momentum roughness length (z0m) and surface roughness for heat transport (z0h) after Bastiaanssen (2004).
*   [i.edge](i.edge.html): Canny edge detector.
*   [i.eodag](i.eodag.html): Downloads imagery scenes from various providers through the EODAG API.
*   [i.evapo.potrad](i.evapo.potrad.html): Potential evapotranspiration, radiative method after Bastiaanssen (1995)
*   [i.evapo.senay](i.evapo.senay.html): Actual evapotranspiration, method after Senay (2007)
*   [i.evapo.zk](i.evapo.zk.html): Computes global evapotranspiration calculation after Zhang, Kimball, Nemani and Running formulation, 2010.
*   [i.feotio2](i.feotio2.html): Calculates the FeO or TiO2 contents from the Clementine project Moon data.
*   [i.fusion.hpf](i.fusion.hpf.html): Fusing high resolution panchromatic and low resolution multi-spectral data based on the High-Pass Filter Addition technique (Gangkofner, 2008).
*   [i.gabor](i.gabor.html): Creates Gabor filter bank for a 2-dimensional image
*   [i.gcp](i.gcp.html): Manages Ground Control Points (GCPs) non-interactively.
*   [i.gravity](i.gravity.html): Bouguer gravity anomaly computation (full slab).
*   [i.histo.match](i.histo.match.html): Calculate histogram matching of several images.
*   [i.hyper.composite](i.hyper.composite.html): Create RGB/CIR/SWIR and custom false color composites from a hyperspectral 3D raster map.
*   [i.hyper.explore](i.hyper.explore.html): Visualize spectra from hyperspectral 3D raster maps.
*   [i.hyper.export](i.hyper.export.html): Export 3D hyperspectral 3D raster map (for now, only available compressed multi-band GeoTIFF)
*   [i.hyper](i.hyper.html): i.hyper family modules
*   [i.hyper.import](i.hyper.import.html): Hyperspectral imagery import.
*   [i.hyper.preproc](i.hyper.preproc.html): General hyperspectral data preprocessing
*   [i.image.bathymetry](i.image.bathymetry.html): Estimates Satellite Derived Bathymetry (SDB) from multispectral images.
*   [i.in.probav](i.in.probav.html): Imports PROBA-V NDVI data in netCDF format into a raster map with real NDVI data range.
*   [i.landsat8.swlst](i.landsat8.swlst.html): Practical split-window algorithm estimating Land Surface Temperature from Landsat 8 OLI/TIRS imagery (Du, Chen; Ren, Huazhong; Qin, Qiming; Meng, Jinjie; Zhao, Shaohua. 2015)
*   [i.landsat.download](i.landsat.download.html): Downloads Landsat TM, ETM and OLI data from EarthExplorer using landsatxplore library
*   [i.landsat](i.landsat.html): Toolset for downloading and importing of Landsat products
*   [i.landsat.import](i.landsat.import.html): Imports Landsat satellite data downloaded using i.landsat.download.
*   [i.landsat.qa](i.landsat.qa.html): Reclassifies Landsat QA band according to acceptable pixel quality as defined by the user.
*   [i.lmf](i.lmf.html): Performs Temporal Local Maximum Fitting of vegetation indices, works also for surface reflectance data.
*   [i.lswt](i.lswt.html): Computes Lake Surface Water Temperatures (inland water bodies) from TOA Brightness Temperatures.
*   [i.modis.download](i.modis.download.html): Download single or multiple tiles of MODIS products using pyModis.
*   [i.modis](i.modis.html): Aerosol Optical Depth
*   [i.modis.import](i.modis.import.html): Import single or multiple tiles of MODIS products using pyModis.
*   [i.nightlights.intercalibration](i.nightlights.intercalibration.html): Performs inter-satellite calibration on DMSP-OLS Nighttime Lights Time Series
*   [i.ortho.corr](i.ortho.corr.html): Corrects orthophoto taking part of the adjacent orthophotos using a camera angle map.
*   [i.points.auto](i.points.auto.html): Generate ground control points for image group to be rectified.
*   [i.pysptools.unmix](i.pysptools.unmix.html): Extract endmembers from imagery group and perform spectral unmixing using pysptools
*   [i.rh](i.rh.html): Water in atmosphere: relative humidity, water vapour (saturated, actual)
*   [i.rotate](i.rotate.html): Rotates the image around the centre of the computational window
*   [i.sam2](i.sam2.html): Integrates SAMGeo model with text prompt for segmentation in GRASS GIS.
*   [i.sar.speckle](i.sar.speckle.html): Remove speckle from SAR image
*   [i.segment.gsoc](i.segment.gsoc.html): Outputs a single segmented map (raster) based on input values in an image group.
*   [i.segment.hierarchical](i.segment.hierarchical.html): Hierarchical segmentation
*   [i.segment.stats](i.segment.stats.html): Calculates statistics describing raster areas.
*   [i.segment.uspo](i.segment.uspo.html): Unsupervised segmentation parameter optimization
*   [i.sentinel.coverage](i.sentinel.coverage.html): Checks the area coverage of Sentinel-1 or Sentinel-2 scenes selected by filters.
*   [i.sentinel.download](i.sentinel.download.html): Downloads Sentinel satellite data from Copernicus Open Access Hub, USGS Earth Explorer, or Google Cloud Storage.
*   [i.sentinel](i.sentinel.html): Toolset for download and processing of Copernicus Sentinel products
*   [i.sentinel.import](i.sentinel.import.html): Imports Sentinel satellite data downloaded from Copernicus Open Access Hub using i.sentinel.download.
*   [i.sentinel.mask](i.sentinel.mask.html): Creates clouds and shadows masks for Sentinel-2 images.
*   [i.sentinel.parallel.download](i.sentinel.parallel.download.html): Downloads Sentinel-2 images in parallel using i.sentinel.download.
*   [i.sentinel.preproc](i.sentinel.preproc.html): Imports and performs atmospheric correction of Sentinel-2 images.
*   [i.signature.copy](i.signature.copy.html): Copies signature file from a group/subgroup to another group/subgroup.
*   [i.signature.list](i.signature.list.html): Lists signature file of a group/subgroup.
*   [i.signature.remove](i.signature.remove.html): Removes signature file in a group/subgroup.
*   [i.spec.sam](i.spec.sam.html): Performs Spectral angle mapping on satellite/aerial images
*   [i.spec.unmix](i.spec.unmix.html): Performs Spectral mixture analysis of satellite/aerial images
*   [i.superpixels.slic](i.superpixels.slic.html): Perform image segmentation using the SLIC segmentation method.
*   [i.theilsen](i.theilsen.html): Computes Theil-Sen estimator from spectrum.
*   [i.variance](i.variance.html): Analyses variation of variance with variation of resolution
*   [i.water](i.water.html): Water detection from satellite data derived indices, 1 if found, 0 if not
*   [i.wavelet](i.wavelet.html): Decompostion/Recomposition in temporal dimension using wavelets
*   [i.wi](i.wi.html): Calculates different types of water indices.
*   [i.zero2null](i.zero2null.html): Replaces zero values with null at edges, otherwise replaces zero values with appropriate neighboring values.

### Miscellaneous

*   [m.cdo.download](m.cdo.download.html): Downloads data from NCEI's Climate Data Online (CDO) using their v2 API.
*   [m.crawl.thredds](m.crawl.thredds.html): List dataset urls from a Thredds Data Server (TDS) catalog.
*   [m.csv.clean](m.csv.clean.html): Creates a cleaned-up copy a CSV files
*   [m.csw.update](m.csw.update.html): Update catalogue service for the web connections resources candidates.
*   [m.eigensystem](m.eigensystem.html): Computes eigenvalues and eigenvectors for an NxN matrix
*   [m.gcp.filter](m.gcp.filter.html): Filter Ground Control Points (GCPs).
*   [m.printws](m.printws.html): Opens a workspace file and creates a map sheet according to its visible contents.
*   [m.prism.download](m.prism.download.html): Downloads data from the PRISM Climate Group.
*   [m.tnm.download](m.tnm.download.html): Downloads data for specified polygon codes from The National Map (TNM).

### 3D raster

*   [r3.count.categories](r3.count.categories.html): Count categories in vertical direction
*   [r3.forestfrag](r3.forestfrag.html): Computes the forest fragmentation index (Riitters et al. 2000)
*   [r3.profile](r3.profile.html): Outputs the raster map layer values lying on user-defined line(s).
*   [r3.scatterplot](r3.scatterplot.html): Creates a scatter plot of 3D raster maps
*   [r3.to.group](r3.to.group.html): Convert a 3D raster map to imagery group
*   [r3.what](r3.what.html): Queries 3D raster in specified 2D or 3D coordinates.

### Raster

*   [r.accumulate](r.accumulate.html): Calculates weighted flow accumulation, subwatersheds, stream networks, and longest flow paths using a flow direction map.
*   [r.agent.aco](r.agent.aco.html): Agents wander around on the terrain, marking paths to new locations.
*   [r.agent](r.agent.html): Toolset for agent based modeling
*   [r.agent.rand](r.agent.rand.html): Agents wander around on the terrain, marking paths to new locations.
*   [r.area.createweight](r.area.createweight.html): Create a dasymetric weighting layer with Random Forest
*   [r.area](r.area.html): Calculates area of clumped areas and remove areas smaller or greater than given threshold.
*   [r.basin](r.basin.html): Morphometric characterization of river basins
*   [r.bearing.distance](r.bearing.distance.html): Find the bearing and/or straight-line distance from all non-null cells to the specified point.
*   [r.bioclim](r.bioclim.html): Calculates bioclimatic indices.
*   [r.bitpattern](r.bitpattern.html): Compares bit patterns with a raster map.
*   [r.boxplot](r.boxplot.html): Draws the boxplot of raster values. Optionally, this is done per category of a zonal raster layer
*   [r.buildvrt.gdal](r.buildvrt.gdal.html): Build GDAL Virtual Rasters (VRT) over GRASS GIS raster maps
*   [r.catchment](r.catchment.html): Creates a raster buffer of specified area around vector points using cost distances using r.walk.
*   [r.category.trim](r.category.trim.html): Export categories and corresponding colors as QGIS color file or csv file. Non-existing categories and their color definitions will be removed.
*   [r.cell.area](r.cell.area.html): Calculate cell sizes within the computational region
*   [r.centroids](r.centroids.html): Creates vector map of centroids from raster of "clumps".
*   [r.change.info](r.change.info.html): Landscape change assessment
*   [r.clip](r.clip.html): Extracts portion of the input map which overlaps with the current region
*   [r.colors.contrastbrightness](r.colors.contrastbrightness.html): Change the contrast/brightness of a raster.
*   [r.colors.cubehelix](r.colors.cubehelix.html): Create or apply a cubehelix color table to a GRASS raster map
*   [r.colors.matplotlib](r.colors.matplotlib.html): Convert or apply a Matplotlib color table to a GRASS raster map
*   [r.colors.out\_sld](r.colors.out_sld.html): Exports the color table associated with a raster map layer in SLD format.
*   [r.confusionmatrix](r.confusionmatrix.html): Calculates a confusion matrix and accuracies for a given classification using r.kappa.
*   [r.connectivity.corridors](r.connectivity.corridors.html): Compute corridors between habitat patches of an input-layer based on (cost) distance raster maps
*   [r.connectivity.distance](r.connectivity.distance.html): Compute cost-distances between patches of an input vector map
*   [r.connectivity](r.connectivity.html): Toolset for conducting connectivity analysis of ecological networks
*   [r.connectivity.network](r.connectivity.network.html): Compute connectivity measures for a set of habitat patches based on graph-theory
*   [r.convergence](r.convergence.html): Calculate convergence index.
*   [r.cpt2grass](r.cpt2grass.html): Convert or apply a GMT color table to a GRASS raster map
*   [r.crater](r.crater.html): Creates meteorites from craters (-c) or craters from meteorites (default).
*   [r.curvenumber](r.curvenumber.html): Generates curve number raster from landcover and hydrologic soil group
*   [r.damflood](r.damflood.html): Estimate the area potentially inundated in case of dam break
*   [r.denoise](r.denoise.html): r.denoise - denoise topographic data
*   [r.divergence](r.divergence.html): Computes divergence of a vector field defined by magnitude and direction
*   [r.diversity](r.diversity.html): Calculate diversity indices based on a moving window using r.li packages
*   [r.droka](r.droka.html): Calculates run-out distance of a falling rock mass
*   [r.earthworks](r.earthworks.html): Terrain modeling with cut and fill operations
*   [r.edm.eval](r.edm.eval.html): Computes evaluation statistics for a given prediction layer
*   [r.euro.ecosystem](r.euro.ecosystem.html): Sets colors and categories of European ecosystem raster data set
*   [r.exdet](r.exdet.html): Quantification of novel uni- and multi-variate environments
*   [r.extract](r.extract.html): Extracts specified categories of an integer input map.
*   [r.fidimo](r.fidimo.html): Calculating fish dispersal in a river network from source populations with species specific dispersal parameters
*   [r.fill.category](r.fill.category.html): Replaces the values of pixels of a given category with values of the surrounding pixels.
*   [r.findtheriver](r.findtheriver.html): Find the stream pixel nearest the input coordinate
*   [r.flexure](r.flexure.html): Computes lithospheric flexural isostasy
*   [r.flip](r.flip.html): Flips an image.
*   [r.flowaccumulation](r.flowaccumulation.html): Calculates flow accumulation from a flow direction raster map using the Memory-Efficient Flow Accumulation (MEFA) parallel algorithm by Cho (2023).
*   [r.flowfill](r.flowfill.html): Moves water downhill into pools or the ocean/map edge
*   [r.forcircular](r.forcircular.html): Evaluation of circular bioeconomy level of forest ecosystems
*   [r.forestfrag](r.forestfrag.html): Computes the forest fragmentation index (Riitters et al. 2000)
*   [r.fusion](r.fusion.html): image fusion, generalized pan-sharpening
*   [r.futures.calib](r.futures.calib.html): Module for calibrating patch characteristics used as input to r.futures.pga
*   [r.futures.demand](r.futures.demand.html): Script for creating demand table which determines the quantity of land change expected.
*   [r.futures.devpressure](r.futures.devpressure.html): Module for computing development pressure
*   [r.futures.gridvalidation](r.futures.gridvalidation.html): Module for validating land change simulation on a grid
*   [r.futures](r.futures.html): FUTure Urban-Regional Environment Simulation (FUTURES)
*   [r.futures.parallelpga](r.futures.parallelpga.html): Simulates landuse change using FUTURES (r.futures.pga) on multiple CPUs in parallel.
*   [r.futures.pga](r.futures.pga.html): Simulates landuse change using FUTure Urban-Regional Environment Simulation (FUTURES).
*   [r.futures.potential](r.futures.potential.html): Module for computing development potential as input to r.futures.pga
*   [r.futures.potsurface](r.futures.potsurface.html): Module for computing development potential surface from CSV file created by r.futures.potential and predictors
*   [r.futures.simulation](r.futures.simulation.html): Wrapper for r.futures.pga to ensure forward compatibility.
*   [r.futures.validation](r.futures.validation.html): Module for land change simulation validation and accuracy assessment
*   [r.fuzzy.logic](r.fuzzy.logic.html): Performs logical operations on membership images created with r.fuzzy.set or different method. Use families for fuzzy logic.
*   [r.fuzzy.set](r.fuzzy.set.html): Calculate membership value of any raster map according to a user's rules.
*   [r.fuzzy.system](r.fuzzy.system.html): Fuzzy logic classification system with multiple fuzzy logic families implication and defuzzification and methods.
*   [r.gdd](r.gdd.html): Makes each output cell value a function of the values assigned to the corresponding cells in the input raster map layers.
*   [r.gradient](r.gradient.html): Create a gradient map
*   [r.gravity.terrain](r.gravity.terrain.html): A GRASS tool to calculate gravity terrain corrections
*   [r.green.biomassfor.co2](r.green.biomassfor.co2.html): Calculates impact and multifunctionality values
*   [r.green.biomassfor.financial](r.green.biomassfor.financial.html): Estimates bioenergy that can be collected to supply heating plants or biomass logistic centres and that is associated with a positive net revenue for the entire production process
*   [r.green.biomassfor](r.green.biomassfor.html): Toolset for computing the energy potential of biomass from
*   [r.green.biomassfor.impact](r.green.biomassfor.impact.html): Calculates impact and multifunctionality values
*   [r.green.biomassfor.legal](r.green.biomassfor.legal.html): Estimates potential bioenergy depending on forest increment, forest management and forest treatment
*   [r.green.biomassfor.recommended](r.green.biomassfor.recommended.html): Estimates potential bioenergy according to environmental restriction
*   [r.green.biomassfor.technical](r.green.biomassfor.technical.html): Estimates the quantity of woody biomass obtained from a forest surface where extraction is possible given a particular level of mechanisation
*   [r.green.biomassfor.theoretical](r.green.biomassfor.theoretical.html): Estimates potential bioenergy depending on forest increment, forest management and forest treatment
*   [r.green.gshp](r.green.gshp.html): Toolset for computing the Ground Source Heat Pump potential.
*   [r.green.gshp.technical](r.green.gshp.technical.html): Calculate the Ground Source Heat Pump technical potential using the ASHRAE method.
*   [r.green.gshp.theoretical](r.green.gshp.theoretical.html): Calculate the Ground Source Heat Pump potential
*   [r.green](r.green.html): Toolset for computing the residual energy potential of different renewable energies like biomass or hydropower
*   [r.green.hydro.closest](r.green.hydro.closest.html): Move points to the closest vector map
*   [r.green.hydro.delplants](r.green.hydro.delplants.html): Delete segments where there is an existing plant
*   [r.green.hydro.discharge](r.green.hydro.discharge.html): Calculate average natural discharge and minimum flow following regional law an
*   [r.green.hydro.financial](r.green.hydro.financial.html): Assess the financial costs and values
*   [r.green.hydro](r.green.hydro.html): Toolset for computing the hydropower potential.
*   [r.green.hydro.optimal](r.green.hydro.optimal.html): Detect the position of the potential hydropower plants that can produce the highest possible power
*   [r.green.hydro.planning](r.green.hydro.planning.html): Calculate hydropower energy potential with user's recommendations
*   [r.green.hydro.recommended](r.green.hydro.recommended.html): Calculate hydropower energy potential with user's recommendations
*   [r.green.hydro.structure](r.green.hydro.structure.html): Compute channels and penstocks
*   [r.green.hydro.technical](r.green.hydro.technical.html): Hydropower potential with technical constraints
*   [r.green.hydro.theoretical](r.green.hydro.theoretical.html): Calculate the hydropower energy potential for each basin starting from discharge and elevation data. If existing plants are available it computes the potential installed power in the available part of the rivers.
*   [r.green.install](r.green.install.html): Toolset to check that all the necessary Python libraries like scipy
*   [r.gsflow.hydrodem](r.gsflow.hydrodem.html): Creates hydrologically correct MODFLOW DEM from higher-res DEM
*   [r.gwr](r.gwr.html): Calculates geographically weighted regression from raster maps.
*   [r.hand](r.hand.html): Performs Height Above Nearest Drainage (HAND) analysis and flood inundation mapping with HAND method.
*   [r.hants](r.hants.html): Approximates a periodic time series and creates approximated output.
*   [r.hazard.flood](r.hazard.flood.html): Fast procedure to detect flood prone areas.
*   [r.houghtransform](r.houghtransform.html): Performs Hough transformation and extracts line segments from image. Region shall be set to input map. Can work only on small images since map is loaded into memory.
*   [r.hydrobasin](r.hydrobasin.html): Delineates a large number of watersheds using the Memory-Efficient Watershed Delineation (MESHED) OpenMP parallel algorithm by Cho (2025).
*   [r.hydrodem](r.hydrodem.html): Hydrological conditioning, sink removal
*   [r.hydro.flatten](r.hydro.flatten.html): Derive elevation of water bodies for hydro-flattening
*   [r.hypso](r.hypso.html): Outputs a hypsometric and hypsographic graph.
*   [r.in.ahn](r.in.ahn.html): Imports dtm, dsm, chm or laz from the AHN (Actueel Hoogtebestand Nederland (AHN), versions 2–6.
*   [r.info.iso](r.info.iso.html): Creates metadata based on ISO standard for specified raster map.
*   [r.in.nasadem](r.in.nasadem.html): Creates a DEM from 1 arcsec NASADEM tiles.
*   [r.in.ogc.coverages](r.in.ogc.coverages.html): Downloads and imports data from OGC API Coverages server.
*   [r.in.ogc](r.in.ogc.html): Toolset for import of raster data from several OGC API standards
*   [r.in.pdal](r.in.pdal.html): Creates a raster map from LAS LiDAR points using univariate statistics and r.in.xyz.
*   [r.in.srtm.region](r.in.srtm.region.html): Creates a DEM from 3 arcsec SRTM v2.1 or 1 arcsec SRTM v3 tiles.
*   [r.in.usgs](r.in.usgs.html): Download user-requested products through the USGS TNM API
*   [r.in.vect](r.in.vect.html): Converts an external vector layer to a raster layer using gdal.Rasterize (the vector layer will be reprojected first if its CRS is different from the current mapset), and imports this raster layer.
*   [r.in.wcs](r.in.wcs.html): Downloads and imports coverage from WCS server.
*   [r.jpdf](r.jpdf.html): From two series of input raster maps, calculates the joint probability function and outputs the probabilities of occurrence in the specified bins.
*   [r.lake.series](r.lake.series.html): Fills lake at given point(s) to given levels.
*   [r.landscape.evol](r.landscape.evol.html): Simulates the cumulative effect of erosion and deposition on a landscape over time.
*   [r.landscape.evol.old](r.landscape.evol.old.html): Simulates the cumulative effect of erosion and deposition on a landscape over time.
*   [r.learn.ml2](r.learn.ml2.html): Supervised classification and regression with scikit-learn
*   [r.learn.ml](r.learn.ml.html): Supervised classification and regression of GRASS rasters using the python scikit-learn package
*   [r.learn.predict](r.learn.predict.html): Apply a fitted scikit-learn estimator to rasters in a GRASS GIS imagery group.
*   [r.learn.train](r.learn.train.html): Supervised classification and regression of GRASS rasters using the python scikit-learn package.
*   [r.le.pixel](r.le.pixel.html): Contains a set of measures for attributes, diversity, texture, juxtaposition, and edge.
*   [r.lfp](r.lfp.html): Calculates the longest flow paths from a flow direction raster map and a outlets vector map using the Memory-Efficient Longest Flow Path (MELFP) OpenMP parallel algorithm by Cho (2025).
*   [r.local.relief](r.local.relief.html): Creates a local relief model from elevation map.
*   [r.mapcalc.tiled](r.mapcalc.tiled.html): Runs r.mapcalc in parallel over tiles.
*   [r.massmov](r.massmov.html): Estimates run-out and deposition of landslide phenomena over a complex topography.
*   [r.maxent.lambdas](r.maxent.lambdas.html): Computes raw or logistic prediction maps from MaxEnt lambdas files
*   [r.maxent.predict](r.maxent.predict.html): Use a Maxent model to create a suitability distribution layer
*   [r.maxent.setup](r.maxent.setup.html): Helper module to install Maxent to the addon directory
*   [r.maxent.train](r.maxent.train.html): Create and train a Maxent model
*   [r.mblend](r.mblend.html): Blends two rasters of different spatial resolution.
*   [r.mcda.ahp](r.mcda.ahp.html): Generates a raster map classified with analytic hierarchy process (AHP).
*   [r.mcda.electre](r.mcda.electre.html): Multicirtieria decision analysis based on ELECTRE method
*   [r.mcda.input](r.mcda.input.html): Generates a raster map classified with Dominance Rough Set Approach. Use \*.rls file from JAMM, 4eMka2 etc.
*   [r.mcda.output](r.mcda.output.html): Exports criteria raster maps and decision raster map in a \*.isf file (e.g. 4eMka2, jMAF) for dominance rough set approach analysis.
*   [r.mcda.promethee](r.mcda.promethee.html): Multicirtieria decision analysis based on PROMETHEE method
*   [r.mcda.roughset](r.mcda.roughset.html): Generates a MCDA map from several criteria maps using Dominance Rough Set Approach.
*   [r.mcda.topsis](r.mcda.topsis.html): Generates a MCDA map based on TOPSIS algorthm.
*   [r.meb](r.meb.html): Compute the multivariate environmental bias (MEB)
*   [r.mess](r.mess.html): Computes multivariate environmental similarity surface (MES)
*   [r.mregression.series](r.mregression.series.html): Calculates multiple regression between time series: Y(t) = b1\*X1(t) + ... + bn\*Xn(t).
*   [r.mwprecip](r.mwprecip.html): Module for working with microwave links
*   [r.neighborhoodmatrix](r.neighborhoodmatrix.html): Calculates geometry parameters for raster objects.
*   [r.niche.similarity](r.niche.similarity.html): Computes niche overlap or similarity
*   [r.northerness.easterness](r.northerness.easterness.html): Calculation of northerness, easterness and the interaction between northerness and slope
*   [r.null.all](r.null.all.html): Manages NULL values of raster maps in a mapset or their subset.
*   [r.object.activelearning](r.object.activelearning.html): Active learning for classifying raster objects
*   [r.object.spatialautocor](r.object.spatialautocor.html): Spatial autocorrelation of raster objects
*   [r.object.thickness](r.object.thickness.html): Evaluates minimum, maximum and mean thickness of objects of a given category on a raster map.
*   [r.out.kde](r.out.kde.html): Exports raster with variable transparency into an image file
*   [r.out.legend](r.out.legend.html): Create an image file showing the legend of a raster map
*   [r.out.maxent\_swd](r.out.maxent_swd.html): Exports map data as input to MaxEnt in SWD format
*   [r.out.ntv2](r.out.ntv2.html): Exports NTv2 datum transformation grid
*   [r.out.tiff](r.out.tiff.html): Exports a GRASS raster map to a 8/24bit TIFF image file.
*   [r.patch.smooth](r.patch.smooth.html): Module for patching rasters with smoothing along edges
*   [r.pi.corr.mw](r.pi.corr.mw.html): Moving window correlation analysis.
*   [r.pi.csr.mw](r.pi.csr.mw.html): Complete Spatial Randomness analysis on moving window.
*   [r.pi.energy](r.pi.energy.html): Individual-based dispersal model for connectivity analysis - energy based.
*   [r.pi.energy.pr](r.pi.energy.pr.html): Individual-based dispersal model for connectivity analysis (energy based) using iterative patch removal.
*   [r.pi.enn](r.pi.enn.html): Analysis of n-th Euclidean Nearest Neighbor distance.
*   [r.pi.enn.pr](r.pi.enn.pr.html): Patch relevance for Euclidean Nearest Neighbor patches.
*   [r.pi.export](r.pi.export.html): Export of patch based information.
*   [r.pi.fnn](r.pi.fnn.html): Determines patches of given value and performs a nearest-neighbor analysis.
*   [r.pi.graph.dec](r.pi.graph.dec.html): Graph Theory - successive criteria-based deletion of patches.
*   [r.pi.graph](r.pi.graph.html): Graph Theory for connectivity analysis.
*   [r.pi.graph.pr](r.pi.graph.pr.html): Graph Theory - iterative removal (patch relevance analysis).
*   [r.pi.graph.red](r.pi.graph.red.html): Graph Theory - decreasing distance threshold option.
*   [r.pi.grow](r.pi.grow.html): Size and suitability based region growing.
*   [r.pi](r.pi.html): Toolset for multiscale analysis of landscape patch structure.
*   [r.pi.import](r.pi.import.html): Import and generation of patch raster data
*   [r.pi.lm](r.pi.lm.html): Linear regression analysis for patches.
*   [r.pi.neigh](r.pi.neigh.html): Neighbourhood analysis - value of patches within a defined range.
*   [r.pi.nlm.circ](r.pi.nlm.circ.html): Creates a random landscape with defined attributes.
*   [r.pi.nlm](r.pi.nlm.html): Creates a random generated map with values 0 or 1by given landcover and fragment count.
*   [r.pi.nlm.stats](r.pi.nlm.stats.html): Neutral Landscape Generator - index statistics
*   [r.pi.odc](r.pi.odc.html): Omnidirectional connectivity analysis
*   [r.pi.prob.mw](r.pi.prob.mw.html): Probability analysis of 2 random points being in the same patch.
*   [r.pi.prox](r.pi.prox.html): Calculates correlation of two raster maps by calculating correlation function of two corresponding rectangular areas for each raster point and writing the result into a new raster map.
*   [r.pi.rectangle](r.pi.rectangle.html): Generates a rectangle based on a corner coordinate.
*   [r.pi.searchtime](r.pi.searchtime.html): Individual-based dispersal model for connectivity analysis (time-based)
*   [r.pi.searchtime.mw](r.pi.searchtime.mw.html): Individual-based dispersal model for connectivity analysis (time-based) using moving window
*   [r.pi.searchtime.pr](r.pi.searchtime.pr.html): Individual-based dispersal model for connectivity analysis (time-based) using iterative removal of patches
*   [r.popgrowth](r.popgrowth.html): Set of population models (fisheries science)
*   [r.pops.spread](r.pops.spread.html): A dynamic species distribution model for pest or pathogen spread in forest or agricultural ecosystems (PoPS)
*   [r.prominence](r.prominence.html): Calculates Llobera's prominence index
*   [r.quantile.ref](r.quantile.ref.html): Determines quantile for input value from reference raster map layers.
*   [r.random.walk](r.random.walk.html): Performs a 2D random walk inside the computational region and returns the resulting walk.
*   [r.random.weight](r.random.weight.html): Generates a binary raster layer with a random selection of raster cells depending on the weight of each cell in the input weight layer.
*   [r.recode.attr](r.recode.attr.html): Recode raster based on the values in one or more columns in a csv file.
*   [r.regression.series](r.regression.series.html): Makes each output cell value a function of the values assigned to the corresponding cells in the input raster map layers.
*   [r.resamp.tps](r.resamp.tps.html): Performs thin plate spline interpolation with regularization and covariables.
*   [r.richdem.breachdepressions](r.richdem.breachdepressions.html): Breaches depressions using RichDEM
*   [r.richdem.filldepressions](r.richdem.filldepressions.html): Floods depressions using RichDEM
*   [r.richdem.flowaccumulation](r.richdem.flowaccumulation.html): Calculates flow accumulation via one of a variety of methods.
*   [r.richdem.resolveflats](r.richdem.resolveflats.html): Directs flow from flat areas on depression-filled DEMs
*   [r.richdem.terrainattribute](r.richdem.terrainattribute.html): Calculates local terrain attributes.
*   [r.rock.stability](r.rock.stability.html): A tool for preliminary rock failure susceptibility mapping.
*   [r.roughness.vector](r.roughness.vector.html): Calculates surface roughness in a moving-window, as the orientation of vectors normal to surface planes.
*   [r.runoff](r.runoff.html): Computes runoff depth, volume and peak discharge for each cell using SCS Curve Number method.
*   [r.sample.category](r.sample.category.html): Create sampling points from each category in a raster map
*   [r.scatterplot](r.scatterplot.html): Creates a scatter plot of raster maps
*   [r.seasons](r.seasons.html): Extracts seasons from a time series.
*   [r.series.boxplot](r.series.boxplot.html): Draws the boxplot of raster values of a series of input rasters.
*   [r.series.decompose](r.series.decompose.html): Calculates decomposition of time series X.
*   [r.series.diversity](r.series.diversity.html): Compute diversity indici over input layers
*   [r.series.filter](r.series.filter.html): Performs filtering of raster time series X (in time domain).
*   [r.series.lwr](r.series.lwr.html): Approximates a time series and creates approximated, gap-filled output.
*   [r.shaded.pca](r.shaded.pca.html): Creates relief shades from various directions and combines them into RGB composition.
*   [r.shalstab](r.shalstab.html): A model for shallow landslide susceptibility.
*   [r.sim.terrain](r.sim.terrain.html): Dynamic landscape evolution model
*   [r.sim.water.mp](r.sim.water.mp.html): Overland flow hydrologic simulation using path sampling method (SIMWE).
*   [r.skyline](r.skyline.html): Compute the skyline index and / or find the horizon cells in a raster viewshed.
*   [r.skyview](r.skyview.html): Computes skyview factor visualization technique.
*   [r.slope.direction](r.slope.direction.html): Calculates slope following a direction raster.
*   [r.slopeunits.clean](r.slopeunits.clean.html): Clean results of r.slopeunits.create
*   [r.slopeunits.create](r.slopeunits.create.html): Create a raster layer of slope units
*   [r.slopeunits](r.slopeunits.html): Toolset for calculating metrics for slope units
*   [r.slopeunits.metrics](r.slopeunits.metrics.html): Create metrics for slope units
*   [r.slopeunits.optimize](r.slopeunits.optimize.html): Optimize inputs for slope units
*   [r.smooth.seg](r.smooth.seg.html): Generates a piece-wise smooth approximation of the input raster and a discontinuity map.
*   [r.soillossbare](r.soillossbare.html): Calculates annual soil loss \[t/(ha\*a)\] for bare soil. Use r.soillosscropland.py afterwards for grown soil.
*   [r.soils.texture](r.soils.texture.html): Define soil texture from sand and clay grid.
*   [r.stone](r.stone.html): The STONE rockfall module
*   [r.stream.basins](r.stream.basins.html): Delineates basins according stream network.
*   [r.stream.channel](r.stream.channel.html): Calculates local parameters for individual streams.
*   [r.stream.distance](r.stream.distance.html): Calculates distance to and elevation above streams and outlet.
*   [r.stream.order](r.stream.order.html): Calculates Strahler's and more streams hierarchy.
*   [r.stream.segment](r.stream.segment.html): Divides network into near straight-line segments and calculate its order.
*   [r.stream.slope](r.stream.slope.html): Calculates local parameters for slope subsystem.
*   [r.stream.snap](r.stream.snap.html): Snap point to modelled stream network.
*   [r.stream.stats](r.stream.stats.html): Calculates Horton's statistics for Strahler and Horton ordered networks created with r.stream.order.
*   [r.stream.variables](r.stream.variables.html): Calculation of contiguous stream-specific variables that account for the upstream environment (based on r.stream.watersheds).
*   [r.stream.watersheds](r.stream.watersheds.html): Sub-watershed and sub-stream delineation based on the drainage direction and a gridded stream network.
*   [r.subdayprecip.design](r.subdayprecip.design.html): Computes subday design precipitation totals.
*   [r.suitability.regions](r.suitability.regions.html): From suitability map to suitable regions
*   [r.sun.daily](r.sun.daily.html): Runs r.sun for multiple days in loop (mode 2)
*   [r.sun.hourly](r.sun.hourly.html): Runs r.sun in loop for given time range within one day (mode 1 or 2)
*   [r.surf.idw2](r.surf.idw2.html): Provides surface interpolation from raster point data by Inverse Distance Squared Weighting.
*   [r.surf.nnbathy](r.surf.nnbathy.html): Interpolates a raster map using the nnbathy natural neighbor interpolation program.
*   [r.survey](r.survey.html): Returns maps of visibility indexes from multiple survey points
*   [r.terrain.texture](r.terrain.texture.html): Unsupervised nested-means algorithm for terrain classification
*   [r.texture.tiled](r.texture.tiled.html): Runs r.texture in parallel over tiles
*   [r.threshold](r.threshold.html): Find optimal threshold for stream extraction
*   [r.timeofconcentration](r.timeofconcentration.html): Computes per-cell time of concentration (Tc) using the Kirpich equation from longest upstream flow-path length and path-average slope.
*   [r.to.vect.lines](r.to.vect.lines.html): Convert raster rows to vector lines.
*   [r.to.vect.tiled](r.to.vect.tiled.html): Converts a raster map into vector tiles.
*   [r.tpi](r.tpi.html): Calculates the multiscale topographic position index
*   [r.traveltime](r.traveltime.html): Estimation of travel times/isochrones.
*   [r.tri](r.tri.html): Computes the Terrain Ruggedness Index.
*   [r.univar2](r.univar2.html): Calculates univariate statistics from the non-null cells of a raster map.
*   [r.valley.bottom](r.valley.bottom.html): Calculation of Multi-resolution Valley Bottom Flatness (MrVBF) index
*   [r.vector.ruggedness](r.vector.ruggedness.html): Vector Ruggedness Measure
*   [r.vect.stats](r.vect.stats.html): Bins vector points into a raster map.
*   [r.viewshed.cva](r.viewshed.cva.html): Undertakes a "cumulative viewshed analysis" using a vector points map as input "viewing" locations, using r.viewshed to calculate the individual viewsheds.
*   [r.viewshed.exposure](r.viewshed.exposure.html): Visual exposure to defined exposure source.
*   [r.vif](r.vif.html): To calculate the stepwise variance inflation factor.
*   [r.vol.dem](r.vol.dem.html): Creates a 3D raster model (voxels) from a series of raster DEMs
*   [r.wateroutlet.lessmem](r.wateroutlet.lessmem.html): Creates watershed basins from a drainage direction map.
*   [r.width.funct](r.width.funct.html): Calculates the Width Function of a watershed basin.
*   [r.windfetch](r.windfetch.html): Computes wind fetch which is the length of water over which winds blow without obstruction
*   [r.zonal.classes](r.zonal.classes.html): Calculates zonal classes proportion describing raster areas's composition, e.g., in terms of land-cover classes.

### Temporal

*   [t.info.iso](t.info.iso.html): Lists information about space time datasets and maps.
*   [t.rast.boxplot](t.rast.boxplot.html): Draws the boxplot of the raster maps of a space-time raster dataset
*   [t.rast.import.netcdf](t.rast.import.netcdf.html): Import netCDF files that adhere to the CF convention as STRDS.
*   [t.rast.kappa](t.rast.kappa.html): Calculate kappa parameter in a space time raster dataset
*   [t.rast.line](t.rast.line.html): Draws line plots of the raster maps in a space-time raster dataset
*   [t.rast.null](t.rast.null.html): Manages NULL-values of a given space time raster dataset.
*   [t.rast.out.xyz](t.rast.out.xyz.html): Export space time raster dataset to a CSV file.
*   [t.rast.patch](t.rast.patch.html): Patches multiple space time raster maps into a single raster map using r.patch.
*   [t.rast.what.aggr](t.rast.what.aggr.html): Sample a space time raster dataset at specific vector point map returning aggregate values and write the output to stdout or to attribute table
*   [t.rast.whatcsv](t.rast.whatcsv.html): Sample a space time raster dataset at specific space-time point coordinates from a csv file and write the output to stdout
*   [t.stac.catalog](t.stac.catalog.html): Get STAC API Catalog metadata
*   [t.stac.collection](t.stac.collection.html): Get STAC API collection metadata
*   [t.stac](t.stac.html): Toolset for working with SpatioTemporal Asset Catalogs
*   [t.stac.item](t.stac.item.html): Downloads and imports data from a STAC API server.

### Vector

*   [v.area.stats](v.area.stats.html): Populates attribute values from vector features.
*   [v.area.weigh](v.area.weigh.html): Rasterize vector areas using weights
*   [v.boxplot](v.boxplot.html): Draws a boxplot of values from a specified attribute column in a vector dataset, with an optional grouping based on categories in another column.
*   [v.build.pg](v.build.pg.html): Builds PostGIS topology for vector map linked via v.external.
*   [v.centerline](v.centerline.html): Creates a central line of a map of lines
*   [v.centerpoint](v.centerpoint.html): Calculate center points
*   [v.civil](v.civil.html): Generates a alignment for designing roads, channels, and ports in civil engineering
*   [v.class.ml](v.class.ml.html): Classification of a vector maps based on the values in attribute tables
*   [v.class.mlpy](v.class.mlpy.html): Vector supervised classification tool which uses attributes as classification parametres (order of columns matters, names not), cat column identifies feature, class\_column is excluded from classification parametres.
*   [v.class.mlR](v.class.mlR.html): Provides supervised support vector machine classification
*   [v.clean.ogr](v.clean.ogr.html): Imports vector data into a GRASS vector map, cleans the data topologically, and exports them again using OGR library.
*   [v.colors2](v.colors2.html): Sets color rules for features in a vector map using a numeric attribute column.
*   [v.concave.hull](v.concave.hull.html): Creates a concave hull around points.
*   [v.convert.all](v.convert.all.html): Converts all older versions of GRASS vector maps in current mapset to current format.
*   [v.convert](v.convert.html): Imports older versions of GRASS vector maps.
*   [v.db.pyupdate](v.db.pyupdate.html): Updates a column in a vector attribute table using Python code
*   [v.delaunay3d](v.delaunay3d.html): Creates a 3D triangulation from an input vector map containing points or centroids.
*   [v.ellipse](v.ellipse.html): Computes the best-fitting ellipse for given vector data.
*   [v.explode](v.explode.html): "Explode" polylines, splitting them to separate lines (uses v.split + v.category)
*   [v.external.all](v.external.all.html): Links all OGR layers available in given OGR datasource.
*   [v.faultdirections](v.faultdirections.html): Creates a polar plot of fault directions
*   [v.feature.algebra](v.feature.algebra.html): A vector calculator program
*   [v.fixed.segmentpoints](v.fixed.segmentpoints.html): segment points along a vector line with fixed distances
*   [v.flexure](v.flexure.html): Lithospheric flexure: gridded deflections from scattered point loads
*   [v.greedycolors](v.greedycolors.html): Create greedy colors for vector areas.
*   [v.gsflow.export](v.gsflow.export.html): Export databse tables and pour point for GSFLOW input and control files
*   [v.gsflow.gravres](v.gsflow.gravres.html): Set parameters for GSFLOW Hydrologic Response Units (HRUs)
*   [v.gsflow.grid](v.gsflow.grid.html): Builds grid for the MODFLOW component of GSFLOW
*   [v.gsflow.hruparams](v.gsflow.hruparams.html): Set parameters for GSFLOW Hydrologic Response Units (HRUs)
*   [v.gsflow.mapdata](v.gsflow.mapdata.html): Upload data to PRMS data
*   [v.gsflow.reaches](v.gsflow.reaches.html): Build stream "reaches" that link PRMS segments to MODFLOW cells
*   [v.gsflow.segments](v.gsflow.segments.html): Prepares stream segments for PRMS and GSFLOW
*   [v.habitat.dem](v.habitat.dem.html): Calculates DEM derived characteristics of habitats.
*   [v.histogram](v.histogram.html): Draws the histogram of values in a vector attribute column
*   [v.in.csv](v.in.csv.html): Import a CSV file using pyproj for CRS transformation
*   [v.info.iso](v.info.iso.html): Creates metadata based on ISO standard for specified vector map.
*   [v.in.gbif](v.in.gbif.html): importing of GBIF species distribution data
*   [v.in.geopaparazzi](v.in.geopaparazzi.html): Imports data from Geopaparazzi database.
*   [v.in.gns](v.in.gns.html): Imports US-NGA GEOnet Names Server (GNS) country files into a GRASS vector points map.
*   [v.in.gps](v.in.gps.html): Import waypoints, routes, and tracks from a GPS receiver or GPS download file into a vector map.
*   [v.in.natura2000](v.in.natura2000.html): importing of Natura 2000 spatial data of protected areas
*   [v.in.ogc.features](v.in.ogc.features.html): Downloads and imports data from OGC API Features server.
*   [v.in.ogc](v.in.ogc.html): Toolset for import of vector data from several OGC API standards
*   [v.in.osm](v.in.osm.html): Imports OpenStreetMap data into GRASS GIS.
*   [v.in.ply](v.in.ply.html): Creates a vector map from a PLY file.
*   [v.in.pygbif](v.in.pygbif.html): Search and import GBIF species distribution data
*   [v.in.redlist](v.in.redlist.html): importing of IUCN Red List Spatial Data
*   [v.in.survey](v.in.survey.html): Creates multiple vector layers from just one textfile
*   [v.in.wfs2](v.in.wfs2.html): Downloads and imports data from WFS server.
*   [v.isochrones](v.isochrones.html): Creates isochrones from a road map and starting points
*   [v.krige](v.krige.html): Performs ordinary or block kriging for vector maps.
*   [v.kriging](v.kriging.html): Interpolates 2D or 3D raster based on input values located on 2D or 3D point vector layer (method ordinary kriging extended to 3D).
*   [v.label.sa](v.label.sa.html): Create optimally placed labels for vector map(s)
*   [v.lidar.mcc](v.lidar.mcc.html): Reclassifies points of a LiDAR point cloud as ground / non-ground using a multiscale curvature based classification algorithm.
*   [v.link.precip](v.link.precip.html): Links time-windows to vector link map.
*   [v.mapcalc](v.mapcalc.html): Vector map calculator.
*   [v.maxent.swd](v.maxent.swd.html): Export raster values at given point locations as text file in SWD format for input in Maxent. In addition, the addon can export the environmental raster layers as ascii files.
*   [v.median](v.median.html): Return the barycenter of a cloud of point.
*   [v.mrmr](v.mrmr.html): Perform Minimum Redundancy Maximum Relevance Feature Selection on a GRASS Attribute Table
*   [v.multi2singlepart](v.multi2singlepart.html): Split multi-part polygons into single-part polygons.
*   [v.neighborhoodmatrix](v.neighborhoodmatrix.html): Exports the neighborhood matrix of polygons in a vector map
*   [v.net.curvedarcs](v.net.curvedarcs.html): Draws curved arcs between points (e.g. flows)
*   [v.net.salesman.opt](v.net.salesman.opt.html): Creates a cycle connecting given nodes (Traveling salesman problem).
*   [v.nnstat](v.nnstat.html): Indicates clusters, separations or random distribution of point set in 2D or 3D space.
*   [v.out.gps](v.out.gps.html): Exports a vector map to a GPS receiver or file format supported by GPSBabel.
*   [v.out.ply](v.out.ply.html): Exports a vector map to a PLY file.
*   [v.out.png](v.out.png.html): Export vector map as PNG
*   [v.percolate](v.percolate.html): Continuum percolation analysis
*   [v.ply.rectify](v.ply.rectify.html): Imports PLY points, georeferences and exports them.
*   [v.profile.points](v.profile.points.html): Creates a profile (transect) from points
*   [v.rast.bufferstats](v.rast.bufferstats.html): Calculates statistics of raster map(s) for buffers around vector geometries.
*   [v.rast.move](v.rast.move.html): Move vertices by distance specified in a raster
*   [v.scatterplot](v.scatterplot.html): Plots the values of two columns in the attribute table of an input vector layer in a scatterplot.
*   [v.sort.points](v.sort.points.html): Sorts a vector point map according to a numeric column
*   [v.stats](v.stats.html): Calculates vector statistics
*   [v.strds.stats](v.strds.stats.html): Calculates univariate statistics from given space-time raster datasets based on a vector map
*   [v.stream.inbasin](v.stream.inbasin.html): Subset a stream network into just one of its basins
*   [v.stream.network](v.stream.network.html): Build a linked stream network: each link knows its downstream link
*   [v.stream.order](v.stream.order.html): Compute the stream order of stream networks stored in a vector map at specific outlet vector points
*   [v.stream.profiler](v.stream.profiler.html): Build a linked stream network: each link knows its downstream link
*   [v.surf.icw](v.surf.icw.html): IDW interpolation, but distance is cost to get to any other site.
*   [v.surf.mass](v.surf.mass.html): Performs mass-preserving area interpolation.
*   [v.surf.nnbathy](v.surf.nnbathy.html): Interpolates a raster map using the nnbathy natural neighbor interpolation program.
*   [v.surf.rst.cv](v.surf.rst.cv.html): Performs cross-validation proceedure to optimize the parameterization of v.surf.rst tension and smoothing paramters.
*   [v.surf.tps](v.surf.tps.html): Performs thin plate spline interpolation with regularization and covariables.
*   [v.tin.to.rast](v.tin.to.rast.html): Converts (rasterize) a TIN map into a raster map
*   [v.to.rast.multi](v.to.rast.multi.html): Create raster maps for multiple numeric attribute columns of a vector map
*   [v.transects](v.transects.html): Creates transect lines or quadrilateral areas at regular intervals perpendicular to a polyline.
*   [v.vect.stats.multi](v.vect.stats.multi.html): Computes isochrones from collection point in a sewershed
*   [v.vol.idw](v.vol.idw.html): Interpolates point data to a 3D raster map using Inverse Distance Weighting (IDW) algorithm.
*   [v.what.rast.label](v.what.rast.label.html): Uploads raster values and labels to vector point layer
*   [v.what.rast.multi](v.what.rast.multi.html): Uploads values of multiple rasters at positions of vector points to the table.
*   [v.what.spoly](v.what.spoly.html): Queries vector map with overlapping "spaghetti" polygons (e.g. Landsat footprints) at given location. Polygons must have not intersected boundaries.
*   [v.what.strds.timestamp](v.what.strds.timestamp.html): Uploads space time raster dataset values to the attribute table at positions of vector points in space and time.

* * *

© 2013-2026 [GRASS Development Team](https://grass.osgeo.org), GRASS GIS 8 Addons Reference Manual  
_Wed 14 Jan 2026 06:44:17 AM UTC_