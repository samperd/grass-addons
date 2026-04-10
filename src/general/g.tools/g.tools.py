#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
# MODULE:    g.tools
#
# PURPOSE:   User Addons menu integration and management
#            - Adds "User Addons" top-level menu to GRASS wxGUI
#            - Provides CLI and GUI interfaces for menu management
#
# AUTHOR(S): GRASS Development Team
#
# COPYRIGHT: (C) 2026 by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
##############################################################################

"""User Addons menu integration for GRASS GIS.

This module provides:
- Installation of "User Addons" top-level menu in GRASS wxGUI
- CLI commands for menu management (status, install, list)
- GUI dialog for interactive menu management
"""

import sys
import os

# Optional wxPython import for GUI mode
try:
    import wx
    WXPYTHON_AVAILABLE = True
except ImportError:
    WXPYTHON_AVAILABLE = False
    wx = None

import grass.script as gs


# =============================================================================
# CLI Functions
# =============================================================================


def get_grass_user_dir():
    """Get user's GRASS directory."""
    return os.path.expanduser("~/.grass8")


def get_toolboxes_dir():
    """Get toolboxes directory."""
    toolboxes = os.path.join(get_grass_user_dir(), "toolboxes")
    if not os.path.exists(toolboxes):
        os.makedirs(toolboxes, exist_ok=True)
    return toolboxes


def list_menus():
    """List current menu structure."""
    toolboxes_dir = get_toolboxes_dir()
    menudata = os.path.join(toolboxes_dir, "menudata.xml")
    
    menus = ["File", "Settings", "Raster", "Vector", "Temporal", "3D Raster", "Image"]
    
    if os.path.exists(menudata):
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(menudata)
            root = tree.getroot()
            for menu in root.findall(".//menu"):
                name = menu.get("name", "")
                if name and name not in menus:
                    menus.append(name)
        except Exception:
            pass
    
    return menus


def install_menu():
    """Install User Addons menu."""
    toolboxes_dir = get_toolboxes_dir()
    menudata = os.path.join(toolboxes_dir, "menudata.xml")
    
    gs.message(f"Installing User Addons menu in {toolboxes_dir}...")
    
    # Simple implementation - just create placeholder
    # Full menu integration would require proper XML handling
    menu_content = """<?xml version="1.0" encoding="UTF-8"?>
<GuiInterface name="menudata">
  <menu name="User Addons">
    <items>
      <menuitem>
        <guisection>User Addons</guisection>
        <label>Addon Extensions</label>
        <handler>g.extension</handler>
        <description>Install and manage GRASS Addon extensions</description>
      </menuitem>
    </items>
  </menu>
</GuiInterface>
"""
    
    try:
        with open(menudata, "w") as f:
            f.write(menu_content)
        gs.message("User Addons menu installed successfully.")
        gs.message("Restart GRASS wxGUI to see changes.")
        return True
    except IOError as e:
        gs.warning(f"Could not install menu: {e}")
        return False


def get_menu_status():
    """Get current menu status."""
    menus = list_menus()
    return {
        "user_addons_installed": "User Addons" in menus,
        "available_menus": menus,
    }


# =============================================================================
# GUI
# =============================================================================

if WXPYTHON_AVAILABLE:

    class GToolsDialog(wx.Dialog):
        """GRASS GIS style dialog for g.tools."""

        def __init__(
            self,
            parent=None,
            title="g.tools - User Addons Menu",
        ):
            super(GToolsDialog, self).__init__(
                parent,
                title=title,
                style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
            )
            self.init_ui()
            self.Centre()
            self.SetMinSize((400, 250))

        def init_ui(self):
            main_sizer = wx.BoxSizer(wx.VERTICAL)
            
            # Title
            title = wx.StaticText(self, label="User Addons Menu")
            font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
            title.SetFont(font)
            main_sizer.Add(title, 0, wx.ALIGN_CENTER | wx.ALL, 15)
            
            # Status
            status = get_menu_status()
            status_text = "Installed" if status["user_addons_installed"] else "Not installed"
            status_label = wx.StaticText(self, label=f"Status: {status_text}")
            main_sizer.Add(status_label, 0, wx.LEFT | wx.RIGHT, 15)
            
            # Info
            info = wx.StaticText(self, label=f"Available menus: {len(status['available_menus'])}")
            main_sizer.Add(info, 0, wx.LEFT | wx.RIGHT, 15)
            
            # Button bar
            button_sizer = wx.BoxSizer(wx.HORIZONTAL)
            
            run_btn = wx.Button(self, label="&Run")
            run_btn.SetDefault()
            close_btn = wx.Button(self, label="&Close")
            help_btn = wx.Button(self, label="&Help")
            
            self.Bind(wx.EVT_BUTTON, lambda e: self.EndModal(wx.ID_OK), run_btn)
            self.Bind(wx.EVT_BUTTON, lambda e: self.EndModal(wx.ID_CANCEL), close_btn)
            self.Bind(wx.EVT_BUTTON, self.on_help, help_btn)
            
            button_sizer.AddStretchSpacer()
            button_sizer.Add(run_btn, 0, wx.RIGHT, 5)
            button_sizer.Add(close_btn, 0, wx.RIGHT, 5)
            button_sizer.Add(help_btn, 0)
            
            main_sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 15)
            self.SetSizer(main_sizer)
            self.Fit()

        def on_help(self, event):
            wx.MessageBox(
                "g.tools - User Addons Menu\n\nInstalls the User Addons menu in GRASS wxGUI.",
                "Help",
                wx.OK | wx.ICON_INFORMATION,
            )


def show_gui():
    """Show GUI dialog."""
    if not WXPYTHON_AVAILABLE:
        gs.fatal("wxPython not available")
    
    app = wx.App(False)
    dialog = GToolsDialog()
    dialog.ShowModal()
    dialog.Destroy()


# =============================================================================
# Main
# =============================================================================


def main():
    """Main function."""
    has_gui = "--gui" in sys.argv
    if has_gui:
        sys.argv = [a for a in sys.argv if a != "--gui"]
    
    options, flags = gs.parser()
    action = options.get("action", "status")
    gui_mode = flags.get("g", False) or has_gui
    
    if gui_mode:
        show_gui()
    else:
        if action == "status":
            status = get_menu_status()
            state = "Installed" if status["user_addons_installed"] else "Not installed"
            gs.message(f"User Addons menu: {state}")
            gs.message(f"Available menus: {len(status['available_menus'])}")
        elif action == "install":
            success = install_menu()
            sys.exit(0 if success else 1)
        elif action == "list":
            for menu in list_menus():
                gs.message(menu)
        else:
            gs.warning(f"Unknown action: {action}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())