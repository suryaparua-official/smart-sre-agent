import os

def read_app_logs(file_path="app.log"):
    """
    Reads the last 10 lines of a specified log file.
    Input should be the filename (e.g., 'app.log').
    """
    try:
        # Handling potential agent string formatting issues
        clean_path = file_path.strip().strip("'").strip('"')
        if not os.path.exists(clean_path):
            return f"Error: The file '{clean_path}' was not found."
            
        with open(clean_path, "r") as f:
            content = f.readlines()
            return "".join(content[-10:])
    except Exception as e:
        return f"Error reading logs: {str(e)}"

def create_config_fix(config_content):
    """
    Creates or updates a config.yaml file with the suggested fix.
    Input should be the string content to be written into the file.
    """
    try:
        clean_content = config_content.strip().strip("'").strip('"')
        with open("config.yaml", "w") as f:
            f.write(clean_content)
        return "SUCCESS: config.yaml has been created with the provided configuration."
    except Exception as e:
        return f"Error creating config file: {str(e)}"
