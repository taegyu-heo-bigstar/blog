import os

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    @env.macro
    def list_files(directory):
        """
        Lists all markdown files in a directory as links.
        Assumes the directory is relative to the docs directory.
        """
        docs_dir = os.path.join(env.project_dir, 'docs')
        target_dir = os.path.join(docs_dir, directory)
        
        if not os.path.exists(target_dir):
            return "Directory not found."

        files = []
        for f in os.listdir(target_dir):
            if f.endswith('.md') and f != 'index.md':
                files.append(f)
        
        # Sort files (usually by date if filename starts with YYYY-MM-DD)
        files.sort(reverse=True) # Newest first

        markdown_list = ""
        for f in files:
            # Create a simple link with the filename as the text
            # You might want to extract the title from the file content later if needed
            # For now, filename is used.
            link_text = f.replace('.md', '')
            markdown_list += f"- [{link_text}](./{f})\n"
            
        return markdown_list
    
    @env.macro
    def list_siblings():
        """
        Lists all markdown files in the same directory as the current page.
        """
        # Get the current page's file path derived from docs_dir
        # page.file.src_path returns path relative to docs/ e.g., 'notes/os/index.md'
        page_file_path = env.page.file.src_path
        
        # Get directory relative to docs/ e.g., 'notes/os'
        current_dir_rel = os.path.dirname(page_file_path)
        
        # Absolute path to the directory
        target_dir = os.path.join(env.project_dir, 'docs', current_dir_rel)

        if not os.path.exists(target_dir):
            return "Directory not found."

        files = []
        for f in os.listdir(target_dir):
            # Exclude current file (index.md) and other non-md files
            if f.endswith('.md') and f != os.path.basename(page_file_path):
                files.append(f)
        
        files.sort(reverse=True)

        markdown_list = ""
        for f in files:
            link_text = f.replace('.md', '')
            markdown_list += f"- [{link_text}](./{f})\n"
            
        if not markdown_list:
            return "_No posts found._"
            
        return markdown_list
