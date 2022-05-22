import os


def handle_uploaded_file(filename, file):
    try:
        with open(filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    except:
        return False    
    return True
