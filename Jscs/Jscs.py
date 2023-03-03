import os
import random
def get_all_folders(path):
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders.append(item_path)
            folders += get_all_folders(item_path)
    return folders
folders = get_all_folders('D:\\b\\Json_Integration\\2')

for x in folders:
   ra = random.randint(11111, 99999)
   d= "Json_Integration" + str(ra)
   if('层岩' in x.split("\\")[-1]):
       os.system(f"tp_converter.exe -i " + '"' + x + '"' + ' -n "' + d + '"' + " -m 6" " -o " + '"' + "D:\\b\\Json_Integratio\\IntegrationXv26" + x[23:] + str(ra) + '"')
   elif('提瓦特'in x.split("\\")[-1]):
       os.system(f"tp_converter.exe -i " + '"' + x + '"' + ' -n "' + d + '"' + " -m 3" " -o " + '"' + "D:\\b\\Json_Integratio\\IntegrationXv26" + x[23:] + str(ra) + '"')
   elif('渊下' in x.split("\\")[-1]):
       os.system(f"tp_converter.exe -i " + '"' + x + '"' + ' -n "' + d + '"' + " -m 5" " -o " + '"' + "D:\\b\\Json_Integratio\\IntegrationXv26" + x[23:] + str(ra) + '"')
   else:
       os.system(f"tp_converter.exe -i " + '"' + x + '"' + ' -n "' + d + '"' + " -m 3" " -o " + '"' + "D:\\b\\Json_Integratio\\IntegrationXv26" + x[23:] + str(ra) + '"')