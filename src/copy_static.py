import os
import shutil
from extract_title import extract_title
from markdown_blocks import markdown_to_html_node

def copy_directory(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isdir(src_path):
            copy_directory(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    
    title = extract_title(markdown_content)
    
    full_html_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as f:
        f.write(full_html_content)

    print("Page generated successfully!")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                
                generate_page(from_path, template_path, dest_path)
                
                print(f"Generated page from {from_path} to {dest_path}")

