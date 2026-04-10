## DESCRIPTION

g.tools provides User Addons menu integration for GRASS GIS. This module adds a new "User Addons" top-level menu to the GRASS wxGUI at the same level as "File", "Settings", "Raster", and "Vector".

The primary purpose of g.tools is to provide:
- A parent container for user-specific GRASS addons
- Integration point for menu structure management
- CLI and GUI interfaces for menu operations

The "User Addons" menu contains the "Addon Extensions" section, which provides access to the GRASS addon manager (g.extension).

## PARAMETERS

- **action**: Action to perform (default: status)
  - **install**: Install the User Addons menu in GRASS wxGUI
  - **uninstall**: Remove the User Addons menu
  - **list**: List available menus in the wxGUI
  - **status**: Show current menu status

## FLAGS

- **-g**: Launch GUI dialog instead of command line
- **--ui**: Launch GUI dialog (alternative flag)

## NOTES

### Menu Structure

The User Addons menu is added at the top level of the GRASS wxGUI menu bar, alongside:
- File
- Settings
- Raster
- Vector
- Temporal
- 3D Raster

### Installation Requirements

- Write access to ~/.grass8/toolboxes/ directory
- GRASS wxGUI must be restarted to see menu changes
- Existing menu files are backed up before modification

### Menu XML Files

g.tools manages these XML configuration files:
- **menudata.xml**: wxGUI menu structure (critical - parsed directly by wxGUI)
- **toolboxes.xml**: Toolbox configuration
- **main_menu.xml**: Main menu reference

### For Addon Developers

Other addons can depend on g.tools for menu placement by:
1. Ensuring g.tools is installed
2. Adding menu entries via the menu XML API
3. Documenting dependency on g.tools

## EXAMPLES

### Show Menu Status

Display the current menu status:

```sh
g.tools
```

Output:
```
User Addons menu: Installed
Available menus (10):
  - File
  - Settings
  - Raster
  - Vector
  - User Addons
```

### Install User Addons Menu

Install the User Addons menu:

```sh
g.tools action=install
```

Output:
```
Backing up existing menu files...
  Backed up: menudata.xml
Adding User Addons menu...
User Addons menu installed successfully
Restart GRASS wxGUI to see changes
```

### Uninstall User Addons Menu

Remove the User Addons menu:

```sh
g.tools action=uninstall
```

### List Available Menus

List all menus in the wxGUI:

```sh
g.tools action=list
```

### Launch GUI

Open the graphical management dialog:

```sh
g.tools --ui
```

or:

```sh
g.tools -g
```

The GUI dialog provides:
- Current menu status display
- Install/Uninstall buttons
- Refresh status button
- Help access

## SEE ALSO

- [g.extension](https://grass.osgeo.org/grass-stable/manuals/g.extension.html) - GRASS addon manager
- [g.echo](https://grass.osgeo.org/grass-addons/manuals/g.echo.html) - Example GRASS addon with GUI
- [GRASS wxGUI](https://grass.osgeo.org/grass-stable/manuals/wxGUI.html) - GRASS wxGUI documentation
- [Menu XML Configuration](https://grasswiki.osgeo.org/wiki/GRASS_WxGUI_Menu_System) - Menu system wiki

## AUTHORS

GRASS Development Team

## COPYRIGHT

This program is free software under the GNU General Public License (>=v2).
Read the file COPYING that comes with GRASS for details.