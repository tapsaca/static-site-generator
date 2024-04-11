def block_to_block_type(block: str):
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif block.startswith("* "):
        for line in block.split("\n"):
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    elif block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif block.startswith("1. "):
        lines = block.split("\n")
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return "paragraph"
        return "ordered_list"
    return "paragraph"

def markdown_to_blocks(markdown: str):
    initial_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in initial_blocks:
        new_block = block.strip()
        if len(new_block) != 0:
            new_blocks.append("\n".join(map(lambda b: b.strip(), new_block.split("\n"))))
    return new_blocks