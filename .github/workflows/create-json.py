import os
import re

app_name_re = re.compile("App Name: (.*)")
package_name_re = re.compile("Package Name: (.*)")
hex_color_re = re.compile("Hex Color: (#.*{6})")

app_list = {}

print(os.listdir("/apps/"))
for item in os.listdir("/apps/"):
  with f.open(item, "r") as file:
    app_name = app_name_re.group(file.readline())
    package_name = package_name_re.group(file.readline())
    hex_color = hex_color_re.group(file.readline())

    print(app_name)
    print(package_name)
    print(hex_color)
