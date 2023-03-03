import os

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
    os.makedirs("D:\\b\\Json_Integratio\\IntegrationXv26" + x[23:],exist_ok=True)