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

def deepest_path(paths):
    if not paths:
        return ""

    max_slashes = -1
    best_path = ""

    for path in paths:
        slashes = path.count('/')
        if slashes > max_slashes:
            max_slashes = slashes
            best_path = path
        elif slashes == max_slashes:
            if path < best_path:
                best_path = path

    return best_path