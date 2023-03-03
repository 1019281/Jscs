import os

path = ('D:\\b\\Json_Integratio\\IntegrationXv26')
for root, dirs, files in os.walk(path, topdown=False):
    if not files and not dirs:
        os.rmdir(root)