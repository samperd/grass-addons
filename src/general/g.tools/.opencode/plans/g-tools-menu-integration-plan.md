# g.tools Menu Integration Plan

## Objective

Create a "User Addons" top-level menu in GRASS wxGUI at the same level as "File", "Settings", "Raster", "Vector", "Temporal", "3D Raster".

The "Addon Extensions" section will be moved from the "Settings" menu to the "User Addons" menu.

## Status: IMPLEMENTED ✓

This plan has been implemented. Current structure:

- `g.tools.py` - Main module (status + GUI only)
- `install.sh` - Installs addon + runs menu-install.sh
- `uninstall.sh` - Removes addon + runs menu-uninstall.sh
- `menu-install.sh` - Creates menu XML files
- `menu-uninstall.sh` - Removes menu XML files

## Current GRASS Menu Structure

The current GRASS wxGUI menu has these top-level menus:
- File
- Settings
- Raster
- Vector
- Temporal
- 3D Raster
- Image
- Map
- Database

## Target Menu Structure

### New "User Addons" Menu

The new "User Addons" menu will contain:

1. **Addon Extensions** (moved from Settings)
   - Install extensions from addons [g.extension]
   - Manage Installed Extensions [g.extension]

2. (Future sections can be added by dependent addons)
   - Additional menu entries can be added by addons that depend on g.tools

## Implementation Steps

### Step 1: Backup Existing Menu Files

Before any modification, backup:
- `~/.grass8/toolboxes/menudata.xml`
- `~/.grass8/toolboxes/toolboxes.xml`
- `~/.grass8/toolboxes/main_menu.xml`

### Step 2: Create Install Script

Create `g.tools` install script that:
1. Creates menu XML files if they don't exist
2. Adds "User Addons" top-level menu
3. Moves "Addon Extensions" from Settings to User Addons
4. Validates XML structure before saving

### Step 3: Create Uninstall Script

Create `g.tools` uninstall script that:
1. Removes "User Addons" menu
2. Restores "Addon Extensions" to "Settings" menu
3. Validates XML structure after removal

## Important Notes

### menudata.xml is CRITICAL

- **menudata.xml**: AUTO-GENERATED and CRITICAL - wxGUI parses this file directly
- **toolboxes.xml**: Configuration definition, but menudata.xml is what wxGUI actually uses
- When toolboxes.xml changes, menudata.xml needs to be regenerated

### Safety

- Always create backups before modification
- Validate XML before saving
- Provide restore/rollback capability

## Menu XML Structure

### menudata.xml Entry for User Addons

```xml
<menu>
    <name>&amp;User Addons</name>
    <items>
        <menuitem>
            <guisection>User Addons</guisection>
            <label>Addon Extensions</label>
            <handler>g.extension</handler>
            <description>Install and manage GRASS Addon extensions</description>
        </menuitem>
    </items>
</menu>
```

## Related Files

- [g.extension](https://grass.osgeo.org/grass-stable/manuals/g.extension.html) - GRASS addon manager
- [GRASS wxGUI Menu System](https://grass.osgeo.org/grass-stable/manuals/wxGUI.html) - Menu configuration

## Exit Criteria

- [x] "User Addons" menu appears in GRASS wxGUI
- [x] "Addon Extensions" accessible from User Addons
- [x] Install script works without errors
- [x] Uninstall script restores previous state
- [x] Other addons can depend on g.tools for menu location