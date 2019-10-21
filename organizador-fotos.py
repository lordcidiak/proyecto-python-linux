  #!/usr/bin/env python3
import os
import shutil
from datetime import datetime
from PIL import Image


class PhotoOrganizer:
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG','png','avi']

    def folder_to_photodate(self, file):
        fecha = self.photo_info_date(file)
        return fecha.strftime('%Y') + '/' + fecha.strftime('%Y-%m-%d') 

    def photo_info_date(self, file):

        photo = Image.open(file)
        info = photo._getexif()
        fecha = datetime.fromtimestamp(os.path.getmtime(file))
        if info:
            if 36867 in info:
                fecha = info[36867]
                fecha = datetime.strptime(fecha, '%Y:%m:%d %H:%M:%S')
        return fecha
        

    def move_photo(self, file):
        new_folder = self.folder_to_photodate(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photos:
            self.move_photo(filename)




PO = PhotoOrganizer()
PO.organize()
