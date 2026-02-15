import os
import subprocess
from datetime import datetime

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

    def _notes_in_dir(dir_rel_from_docs):
        """Return list of (full_path, rel_path_from_docs) for .md files in a docs/ subdir, excluding index.md."""
        base_dir = os.path.join(env.project_dir, 'docs', dir_rel_from_docs)
        if not os.path.exists(base_dir):
            return []

        out = []
        for name in os.listdir(base_dir):
            if not name.endswith('.md'):
                continue
            if name == 'index.md':
                continue
            full_path = os.path.join(base_dir, name)
            if os.path.isfile(full_path):
                rel_path = os.path.relpath(full_path, os.path.join(env.project_dir, 'docs'))
                out.append((full_path, rel_path))
        return out

    def _format_single_or_none(item):
        if item is None:
            return "None"
        display_date = item['date'].split(' ')[0]
        return f"- `{display_date}` [{item['title']}](./{os.path.basename(item['path'])})"

    def _latest_note_in_current_dir(kind):
        """kind: 'created' or 'updated'"""
        page_file_path = env.page.file.src_path
        current_dir_rel = os.path.dirname(page_file_path)
        entries = _notes_in_dir(current_dir_rel)
        if not entries:
            return None

        data = []
        for full, rel in entries:
            date = get_git_date(full, kind)
            if not date:
                ts = os.path.getctime(full) if kind == 'created' else os.path.getmtime(full)
                date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            data.append({
                'title': get_page_title(full),
                'path': rel,
                'date': date,
            })

        data.sort(key=lambda x: x['date'], reverse=True)
        return data[0]

    @env.macro
    def latest_created_note_in_dir():
        """Latest created note within the current page's directory (excluding index.md)."""
        return _format_single_or_none(_latest_note_in_current_dir('created'))

    @env.macro
    def latest_updated_note_in_dir():
        """Latest updated note within the current page's directory (excluding index.md)."""
        return _format_single_or_none(_latest_note_in_current_dir('updated'))

    def get_git_date(file_path, date_type='created'):
        cmd = []
        if date_type == 'created':
            # Get the date of the first commit that introduced the file
            cmd = ['git', 'log', '--diff-filter=A', '--follow', '--format=%ai', '--', file_path]
        else: # updated
            # Get the date of the last commit
            cmd = ['git', 'log', '-1', '--format=%ai', '--', file_path]
            
        try:
            # Run git command
            result = subprocess.check_output(cmd, cwd=env.project_dir).decode('utf-8').strip()
            if result:
                # If multiple lines (e.g. diff-filter=A might show moves), take the last one (oldest) for creation
                # For updated, it's just one line usually.
                lines = result.split('\n')
                return lines[-1] if date_type == 'created' else lines[0]
            return None
        except Exception:
            return None

    def get_page_title(full_path):
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Try to find YAML frontmatter title
                # Or find first h1
                lines = content.split('\n')
                for line in lines:
                    if line.strip().startswith('# '):
                        return line.strip()[2:]
            return os.path.basename(full_path).replace('.md', '')
        except:
            return os.path.basename(full_path).replace('.md', '')

    def get_all_content_files():
        docs_dir = os.path.join(env.project_dir, 'docs')
        files_list = []
        for root, dirs, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, docs_dir)
                    
                    # Skip the main homepage
                    if rel_path == 'index.md':
                        continue
                        
                    files_list.append((full_path, rel_path))
        return files_list

    @env.macro
    def recent_created_notes(limit=5):
        files = get_all_content_files()
        data = []
        for full, rel in files:
            date = get_git_date(full, 'created')
            if not date:
                # Fallback to file system creation time
                date = datetime.fromtimestamp(os.path.getctime(full)).strftime('%Y-%m-%d %H:%M:%S')
            
            data.append({
                'title': get_page_title(full),
                'path': rel,
                'date': date
            })
        
        # Sort by date descending
        data.sort(key=lambda x: x['date'], reverse=True)
        
        output = ""
        for item in data[:limit]:
            display_date = item['date'].split(' ')[0] # YYYY-MM-DD
            output += f"- `{display_date}` [{item['title']}](./{item['path']})\n"
        return output

    @env.macro
    def recent_updated_notes(limit=5):
        files = get_all_content_files()
        data = []
        for full, rel in files:
            date = get_git_date(full, 'updated')
            if not date:
                # Fallback to file system modification time
                date = datetime.fromtimestamp(os.path.getmtime(full)).strftime('%Y-%m-%d %H:%M:%S')
            
            data.append({
                'title': get_page_title(full),
                'path': rel,
                'date': date
            })
        
        # Sort by date descending
        data.sort(key=lambda x: x['date'], reverse=True)
        
        output = ""
        for item in data[:limit]:
            display_date = item['date'].split(' ')[0]
            output += f"- `{display_date}` [{item['title']}](./{item['path']})\n"
        return output
