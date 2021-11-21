import os
import re

app_name_re = re.compile("App Name: (.*)")
package_name_re = re.compile("Package Name: (.*)")
hex_color_re = re.compile("Hex Color: (\#[.*]{6})")

app_list = {}

print(os.listdir("apps"))
for item in os.listdir("apps"):
  with open(os.path.join("apps", item), "r") as file:
    app_name = app_name_re.search(file.readline()).group(0)
    package_name = package_name_re.search(file.readline()).group(0)
    hex_color = hex_color_re.search(file.readline()).group(0)

    print(app_name)
    print(package_name)
    print(hex_color)
