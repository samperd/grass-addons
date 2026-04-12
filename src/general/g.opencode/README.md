# Opencode custom tools for GRASS GIS

[![GRASS GIS module](https://img.shields.io/badge/GRASS%20GIS-module-%23009000)](https://grass.osgeo.org/)

This project develops custom OpenCode tools for GRASS GIS, focusing on:
* Creating custom tools for GRASS GIS functionality
* Integrating with OpenCode for enhanced development
* Providing examples of tool development patterns
* Maintaining documentation and testing for reliability

## How to use this project

### Getting Started

To contribute to this project:

* Clone the repository using Git.
* Explore the .opencode/tool/ directory for existing tools.
* Follow the development guidelines in AGENTS.md.



### Getting the GitHub Actions work

If you have the repository on GitHub, you can also reuse the GitHub
Actions defined in the repository (under `.github`). Initially, most of
them will fail, but once you do the renaming, most of them should start
working.

For the workflow uploading documentation to GitHub Pages to
work, you will need you to
[set up Deploy key and a Secret](https://github.com/marketplace/actions/github-pages-action#1-add-ssh-deploy-key)
for your repository. Once the keys are in place, the online documentation
will be published as GitHub Pages website automatically.
The URL for the website is available in the Settings of your repository.

## Files which usually are not part of a module

These are the files in this repository which usually are not part of
a GRASS GIS module source code, but are useful for a standalone repository.

* README (README.md) is very useful for a standalone repository,
  but is not required for a GRASS GIS module because installation,
  code contributions, etc. are already described in the main repository.
* LICENSE file makes it easier to identify the license (even when the
  license is specified elsewhere). It is not required for the modules
  in the main repository as there is a license file already included.
* Files in .github/ directory for GitHub Actions, Continuous Integration, etc.

## Contributing Tools

Consider contributing new tools to the
[GRASS GIS Addons repository](https://grass.osgeo.org/development/code-submission/)
through pull request on GitHub.
This provides maintenance support from the core team and easier distribution.
Develop tools here first, then submit mature tools to the official addons.

## How to contribute to this repository

Fork the project and submit a pull request or open an issue.
