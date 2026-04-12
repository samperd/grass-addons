---
author: GRASS Development Team
date_created: '2003'
date_downloaded: '2026-01-14T23:59:25.394008'
latest_change: "Tuesday Dec 17 20:17:20 2024 in commit: d962e90c026708a4815ea2b9f46c0e84c17de22d\n\
  \n\n\nMain index |\nGeneral index |\nTopics index |\nKeywords index |\nGraphical\
  \ index |\nFull index\n\n\n\xA9 2003-2025\nGRASS Development Team,\nGRASS GIS 8.4.3dev\
  \ Reference Manual"
source_url: https://grass.osgeo.org/grass84/manuals/g.gui.html
tags:
- general
- GUI
- user interface
title: g.gui - GRASS GIS manual
---

[](man-pages/index.md)

* * *

## NAME

_**g.gui**_ \- Launches a GRASS graphical user interface (GUI) session.  
Optionally updates default user interface settings. 

## KEYWORDS

[general](man-pages/general.md), [GUI](man-pages/topic_GUI.md), [user interface](keywords.html#user interface)

## SYNOPSIS

**g.gui**  


**g.gui --help**  


**g.gui** [-**fdn**] [**ui** =_string_] [**workspace** =_name.gxw_] [--**help**] [--**verbose**] [--**quiet**] [--**ui**] 

### Flags:

**-f**
    Start GUI in the foreground
    By default the GUI starts in the background and control is immediately returned to the caller. When GUI runs in foregreound, it blocks the command line
**-d**
    Update default user interface settings
**-n**
    Do not launch GUI after updating the default user interface settings
**\--help**
    Print usage summary
**\--verbose**
    Verbose module output
**\--quiet**
    Quiet module output
**\--ui**
    Force launching GUI dialog

### Parameters:

**ui** =_string_
    User interface
    Options: _wxpython, text, gtext_
    Default: _wxpython_
    **wxpython** : wxPython based GUI (wxGUI)
    **text** : command line interface only
    **gtext** : command line interface with GUI startup screen
**workspace** =_name.gxw_
    Name of workspace file to load on start-up
    This is valid only for wxGUI (wxpython)

#### Table of contents

  * DESCRIPTION
  * NOTES
  * EXAMPLES
    * Set default user interface settings
    * Load workspace from command line
  * SEE ALSO
  * AUTHORS



## DESCRIPTION

The _g.gui_ module allows user to start the Graphical User Interface (GUI) from the command line prompt or to change the default User Interface (UI) settings. 

GRASS GIS comes with both a wxPython-based GUI aka _[wxGUI](man-pages/wxGUI.md)_ (**ui=wxpython**) and command line text-based UI (**ui=text**). 

## NOTES

If the **-d** update flag is given or the `GRASS_GUI` environmental [variable](man-pages/variables.md) is unset, then the GRASS internal variable `GUI` is permanently changed and the selected **ui** will be used as the default UI from then on. 

All GRASS internal variables (see _[g.gisenv](man-pages/g.gisenv.md)_) are stored in the user's home directory in a hidden file called `$HOME/.grass8/rc` on Unix-based operating systems and `%APPDATA%\GRASS8\rc` on MS Windows. Note that these GRASS internal variables are not the shell environment variables and the `rc` file is not a classic UNIX run command file, it just contains persistent GRASS variables. 

## EXAMPLES

### Set default user interface settings

Set default user interface setting to command line, text-based UI: 
    
    
    g.gui -d ui=text
    

Set default user interface setting to the graphical user interface (GUI) and _launch_ the GUI: 
    
    
    g.gui -d ui=wxpython
    

Set default user interface setting to the graphical user interface (GUI) but _do not launch_ the GUI: 
    
    
    g.gui -dn ui=wxpython
    

### Load workspace from command line

Start the GUI from command line with an existing workspace: 
    
    
    g.gui workspace=myproject.gxw
    

## SEE ALSO

_[wxGUI](man-pages/wxGUI.md), [g.gisenv](man-pages/g.gisenv.md), [GRASS variables](man-pages/variables.md) _

[wxGUI wiki page](https://grasswiki.osgeo.org/wiki/WxPython-based_GUI_for_GRASS)

## AUTHORS

Martin Landa, FBK-irst, Trento, Italy  
Hamish Bowman, Otago University, Dunedin, New Zealand (fine tuning) 

## SOURCE CODE

Available at: [g.gui source code](https://github.com/OSGeo/grass/tree/main/general/g.gui) ([history](https://github.com/OSGeo/grass/commits/main/general/g.gui)) 

Latest change: Tuesday Dec 17 20:17:20 2024 in commit: d962e90c026708a4815ea2b9f46c0e84c17de22d 

* * *

[Main index](man-pages/index.md) | [General index](man-pages/general.md) | [Topics index](man-pages/topics.md) | [Keywords index](man-pages/keywords.md) | [Graphical index](man-pages/graphical_index.md) | [Full index](man-pages/full_index.md)

© 2003-2025 [GRASS Development Team](https://grass.osgeo.org), GRASS GIS 8.4.3dev Reference Manual 
