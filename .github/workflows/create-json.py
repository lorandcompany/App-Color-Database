import os
import re
import json

app_list = {}

packages = []

invalid_files = []

for item in os.listdir("apps"):
  with open(os.path.join("apps", item), "r") as file:
    try:
      app_name = re.search("App Name: (.*)", file.readline()).group(1)
      package_name = re.search("Package Name: (.*)", file.readline()).group(1)
      hex_color = re.search("Hex Color: (\#.{6})", file.readline()).group(1)

      if package_name in packages:
        print(f"[WARNING] File {item} with package name {package_name} already exists. Ignoring...")
      packages.append(package_name)
      app_list[package_name] = hex_color
    except Exception as e:
      invalid_files.append(item)

if invalid_files:
  raise Exception(f"The following apps have an invalid format.\n"+"\n".join(invalid_files))
else:
  print(json.dumps([app_list]))
  with open("colors.json", "w") as file:
    file.write(json.dumps(app_list))
