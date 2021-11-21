import os
import re

app_list = {}

invalid_files = []

print(os.listdir("apps"))
for item in os.listdir("apps"):
  with open(os.path.join("apps", item), "r") as file:
    try:
      app_name = re.search("App Name: (.*)", file.readline()).group(1)
      package_name = re.search("Package Name: (.*)", file.readline()).group(1)
      hex_color = re.search("Hex Color: (\#.{6})", file.readline()).group(1)
    except Exception as e:
      invalid_files.append(item)

if invalid_files:
  raise Exception(f"The following apps have an invalid format.\n"+"\n".join(invalid_files))
