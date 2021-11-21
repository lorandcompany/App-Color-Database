import os
import re

app_name_re = re.compile("App Name: (.*)")
package_name_re = re.compile("Package Name: (.*)")
hex_color_re = re.compile("Hex Color: (#.*{6})")

app_list = {}

print(os.listdir("/apps/"))
for item in os.listdir("/apps/")
  app_name = app_name_re.group(f.readline())
  package_name = package_name_re.group(f.readline())
  hex_color = hex_color_re.group(f.readline())
  
  print(app_name)
  print(package_name)
  print(hex_color)
