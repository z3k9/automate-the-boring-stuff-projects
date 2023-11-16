import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfile_name = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipfile_name):
            break
        number = number + 1

    backup_zip = zipfile.ZipFile(zipfile_name, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        backup_zip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_' 
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername,filename))
        backup_zip.close()
        





