import os
import re


def fix_double_docstrings(root_dir):
    # If root_dir is a file, process it directly
    if os.path.isfile(root_dir):
        files = [root_dir]
        root_dir = os.path.dirname(root_dir) or "."
    else:
        files = []
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".py"):
                    files.append(os.path.join(dirpath, filename))

    for filepath in files:
        with open(filepath, "r") as f:
            content = f.read()

        # original_content = content

        # 1. Extract Shebang if present
        shebang = ""
        shebang_match = re.match(r"^(#!.*\n)", content)
        if shebang_match:
            shebang = shebang_match.group(1)
            content = content[
                len(shebang) :
            ]  # Remove shebang from content for processing

        # 2. Find Hexagonal Header (first docstring)
        # It might start with whitespace if shebang was removed, so strip leading whitespace
        content = content.lstrip()

        header_match = re.match(r'(?s)^""".*?hexagon:.*?"""', content)
        if not header_match:
            continue  # No hexagonal header, skip

        full_header = header_match.group(0)
        remaining_content = content[len(full_header) :]

        # 3. Find Second Docstring
        # It might be separated by whitespace or comments (like the shebang if it was in the middle)
        # But we already stripped the shebang if it was at the top.
        # If the shebang was between docstrings, it's now in `remaining_content`.

        # Let's look for the next docstring in remaining_content
        # We need to be careful not to match a string assignment
        # A module docstring must be a standalone string literal.

        # Simple heuristic: Look for """ or ''' starting the next non-whitespace chunk

        next_chunk_match = re.match(
            r'(?s)^\s*(?:#!.*\n)?\s*("""(.*?)""")', remaining_content
        )
        if next_chunk_match:
            print(f"Fixing double docstring in {filepath}")
            _ = next_chunk_match.group(1)
            second_docstring_content = next_chunk_match.group(2).strip()

            # Remove the second docstring from remaining content
            # We need to be careful about what we replace.
            # The match includes leading whitespace/shebang in the group 0? No, group 1 is just the docstring.
            # But we matched with `^\s*(?:#!.*\n)?\s*`

            # Let's just replace the second docstring in the remaining content with nothing (or just the shebang if it was there)
            # Actually, if there was a shebang *between* docstrings, we should preserve it?
            # But we want the shebang at the very top.

            # If we found a shebang at the top (step 1), we use that.
            # If there is a shebang between docstrings, we should probably move it to the top too.

            inner_shebang_match = re.match(r"(?s)^\s*(#!.*\n)", remaining_content)
            if inner_shebang_match and not shebang:
                shebang = inner_shebang_match.group(1)

            # Remove the second docstring and the whitespace/shebang before it
            remaining_content_cleaned = re.sub(
                r'(?s)^\s*(?:#!.*\n)?\s*""".*?"""', "", remaining_content, count=1
            )

            # Merge content
            new_header = full_header[:-3] + f'\n\n{second_docstring_content}\n"""'

            # Reconstruct file
            new_content = shebang + new_header + remaining_content_cleaned

            with open(filepath, "w") as f:
                f.write(new_content)


if __name__ == "__main__":
    fix_double_docstrings("body")
    fix_double_docstrings("venom")
    fix_double_docstrings("carapace")
    fix_double_docstrings("genesis.py")
    fix_double_docstrings("fix_double_docstrings.py")
