import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive('D:/1. Development/Python_new_2023/Section 18/compressed.zip',
                    'D:/1. Development/Python_new_2023/Section 18/1')
