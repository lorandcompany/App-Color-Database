# Kustom Icon Color Database

This repository is a database of app icon colors mainly for use in colorizing notification icons using package names. Based from a [spreadsheet](https://docs.google.com/spreadsheets/d/15xYugLWZIDaVFRkaC9wsctFhGOfjqi4fQngwIjdXVUE/view) made by [Erik Bucik](https://klwp.erikbucik.com/)

# Usage

Use `wg()` function to fetch the `colors.json` file and use JsonPath to find the hex color by package name.

### Example

```
$tc(reg,wg("https://raw.githubusercontent.com/lorandcompany/App-Color-Database/main/colors.json", json, ".[" + your_package_name + "]"), "^$", [custom color if not found])$
```

# Contributing

### Create a file inside `apps` directory. Name it closely related to the app.
The file name is meant to allow others to find existing apps easily. Name it something that someone would search. Like naming "Boost for Reddit" as `boost`. There's no need for file extensions.
### Follow the format given below.
```
App Name: Your App Name
Package Name: app.package.name
Hex Color: #FFFFFF
```
Incorrect markup with mark it as invalid by an automated script. Make sure that the hex color has the format of #RRGGBB. No alphas.
### Create a pull request
If the format is followed, then we will commit your changes to the database.

# License
This database follows the DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE contained in `#community-kode-database` inside the [official Kustom Discord server](https://discord.gg/Wk6uaKMpE3)
```
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
