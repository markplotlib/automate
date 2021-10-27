import os

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category

if __name__ == '__main__':
    for item in os.scandir('../data/OrganizeMe'):
        print(item)
