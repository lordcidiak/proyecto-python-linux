 #!/usr/bin/env python3
import os
import shutil
from datetime import datetime
from PIL import Image


class PhotoOrganizer:
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG','png','avi']

    def folder_to_photodate(self, file):
        date = self.photo_info_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d') + '/' + date.strftime('thumbnail')

    def photo_info_date(self, file):

        photo = Image.open(file)
        info = photo._getexif()
        date = datetime.fromtimestamp(os.path.getmtime(file))
        if info:
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        return date
        imagen = Image.open(file)
        miniatura = (100, 100)
        imagen.thumbnail(miniatura)
        imagen.save(file)

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

