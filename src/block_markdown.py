def markdown_to_blocks(markdown: str):
    initial_blocks = markdown.split("\n\n")
    new_blocks = []
    for block in initial_blocks:
        new_block = block.strip()
        if len(new_block) != 0:
            new_blocks.append("\n".join(map(lambda b: b.strip(), new_block.split("\n"))))
    return new_blocks