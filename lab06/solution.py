def count_by_extension(paths):
    result = {}
    for path in paths:
        parts = path.split('/')
        filename = parts[-1] if parts else ""

        if '.' in filename:
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""

        result[ext] = result.get(ext, 0) + 1
    return result
