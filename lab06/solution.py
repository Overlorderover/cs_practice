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

def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    if n_bytes < 1024:
        return f"{n_bytes} Б"

    size = float(n_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.1f} {units[unit_index]}"