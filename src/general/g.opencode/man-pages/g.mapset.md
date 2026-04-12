---
author: GRASS Development Team
date_created: '2003'
date_downloaded: '2026-01-15T00:11:00.815683'
latest_change: "Tuesday Dec 17 20:17:20 2024 in commit: d962e90c026708a4815ea2b9f46c0e84c17de22d\n\
  \n\n\nMain index |\nGeneral index |\nTopics index |\nKeywords index |\nGraphical\
  \ index |\nFull index\n\n\n\xA9 2003-2025\nGRASS Development Team,\nGRASS GIS 8.4.3dev\
  \ Reference Manual"
source_url: https://grass.osgeo.org/grass84/manuals/g.mapset.html
tags:
- general
- settings
title: g.mapset - GRASS GIS manual
---

[](man-pages/index.md)

* * *

## NAME

_**g.mapset**_ \- Changes/reports current mapset.  
Optionally create new mapset or list available mapsets in given project (location). 

## KEYWORDS

[general](man-pages/general.md), [settings](man-pages/topic_settings.md)

## SYNOPSIS

**g.mapset**  


**g.mapset --help**  


**g.mapset** [-**clp**] **mapset** =_name_ [**project** =_name_] [**dbase** =_path_] [--**overwrite**] [--**help**] [--**verbose**] [--**quiet**] [--**ui**] 

### Flags:

**-c**
    Create mapset if it doesn't exist
**-l**
    List available mapsets and exit
**-p**
    Print current mapset and exit
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

**mapset** =_name_ **[required]**
    Name of mapset (default: current search path)
    Name of mapset where to switch
**project** =_name_
    Project (location) name
    Project name (not path to project)
**dbase** =_path_
    GRASS GIS database directory
    Default: path to the current GRASS GIS database

#### Table of contents

  * DESCRIPTION
  * NOTES
  * EXAMPLES
    * Print the name of the current mapset
    * List available mapsets
    * Change the current mapset
    * Create a new mapset
  * SEE ALSO
  * AUTHOR



## DESCRIPTION

_g.mapset_ changes the current working mapset, project (formerly known as location), or GISDBASE (directory with one or more projects). 

With _g.mapset_ , the shell history (i.e. `.bash_history` file of the initial project will be used to record the command history. 

## NOTES

By default, the shell continues to use the history for the old mapset. To change this behaviour the history can be switched to record in the new mapset's history file as follows: 
    
    
    # bash example
    history -w
    history -r /"$GISDBASE/$LOCATION/$MAPSET"/.bash_history
    HISTFILE=/"$GISDBASE/$LOCATION/$MAPSET"/.bash_history
    

## EXAMPLES

### Print the name of the current mapset

To print the name of the current mapset, use the **-p** command as shown below: 
    
    
    g.mapset -p
    

### List available mapsets

To list available mapsets, use the **-l** command as shown below: 
    
    
    g.mapset -l
    

This should list all the mapsets, such as: "landsat new PERMANENT user1." 

### Change the current mapset

To change the current mapset to "user1" use the following command: 
    
    
    g.mapset mapset=user1 project=nc_spm_08_grass7
    

You should receive the following message: "Mapset switched. Your shell continues to use the history for the old mapset." 

### Create a new mapset

To create a new mapset, use the **-c** tag as shown below: 
    
    
    g.mapset -c mapset=new project=nc_spm_08_grass7
    

## SEE ALSO

_[g.gisenv](man-pages/g.gisenv.md), [g.mapsets](man-pages/g.mapsets.md) _

## AUTHOR

Radim Blazek 

## SOURCE CODE

Available at: [g.mapset source code](https://github.com/OSGeo/grass/tree/main/general/g.mapset) ([history](https://github.com/OSGeo/grass/commits/main/general/g.mapset)) 

Latest change: Tuesday Dec 17 20:17:20 2024 in commit: d962e90c026708a4815ea2b9f46c0e84c17de22d 

* * *

[Main index](man-pages/index.md) | [General index](man-pages/general.md) | [Topics index](man-pages/topics.md) | [Keywords index](man-pages/keywords.md) | [Graphical index](man-pages/graphical_index.md) | [Full index](man-pages/full_index.md)

© 2003-2025 [GRASS Development Team](https://grass.osgeo.org), GRASS GIS 8.4.3dev Reference Manual 
