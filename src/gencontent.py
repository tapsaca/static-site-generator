import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("Missing h1 header")

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "w") as new_file:
        new_file.write(page)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        if os.path.isfile(from_path):
            if Path(from_path).suffix == ".md":
                generate_page(from_path, template_path, f"{dest_dir_path}/index.html")
        else:
            dest_path = os.path.join(dest_dir_path, file)
            os.mkdir(dest_path)
            generate_pages_recursively(from_path, template_path, dest_path)

def read_file(path: str):
    with open(path) as file:
        return file.read()