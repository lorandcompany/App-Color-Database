import os
import re

app_list = {}

print(os.listdir("apps"))
for item in os.listdir("apps"):
  with open(os.path.join("apps", item), "r") as file:
    try:
      app_name = re.search("App Name: (.*)", file.readline()).group(1)
      package_name = re.search("Package Name: (.*)", file.readline()).group(1)
      hex_color = re.search("Hex Color: (\#.{6})", file.readline()).group(1)
    except Exception as e:
      raise f"{item} has invalid format"
    
    print(app_name)
    print(package_name)
    print(hex_color)
