#!/usr/bin/env python3
import os
import shutil
from datetime import datetime
from PIL import Image
import sys
import glob, os

class PhotoOrganizer:
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG','mp4','avi']
            
    size = (128, 128)
    def imgthumb(self, imgname):
        try:
            size = 128, 128
            thumbs = self.folder_path_from_photo_date(imgname)
            os.makedirs(thumbs)
            file, ext = os.path.splitext(imgname)
            im = Image.open(imgname)
            im.thumbnail(size)
            im.save(file , "JPEG")
            shutil.move(file, thumbs)
            
        except IOError:
            print("cannot create thumbnail for", imgname)
        
    def folder_path_from_photo_date(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def photo_shooting_date(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        date = datetime.fromtimestamp(os.path.getmtime(file))
        if info:
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        return date

    def move_photo(self, file):
        new_folder = self.folder_path_from_photo_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)
        self.imgthumb(file)

    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photos:
            self.move_photo(filename)


PO = PhotoOrganizer()
PO.organize()
