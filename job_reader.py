def read_job_description(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print("Error reading job file:", e)
        return ""