import dropbox

token = "XYXa5-NxPcQAAAAAAAANIVkB6PEfnHC5giPLKjBknzVh9qqj2XQIsVeLbphFiFRN"

dbx = dropbox.Dropbox(token)

path = "/Frutillas/Contabilidad/2017 - 2"
for entry in dbx.files_list_folder(path).entries:
    file = entry.name
    dbx.files_download_to_file(file, path + "/" + file)
