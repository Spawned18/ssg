import shutil
import os
from copy_static import copy_directory, generate_pages_recursive

def clean_public_directory(public_path):
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.makedirs(public_path)

if __name__ == '__main__':
    public_dir = 'public'
    static_dir = 'static'
    content_dir = 'content'
    template_file = 'template.html'

    clean_public_directory(public_dir)
    copy_directory(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_file, public_dir)
    
    print("Public directory updated successfully!")

