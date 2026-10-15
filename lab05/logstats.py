def parse_event(line):
    parts=line.split(None,2)
    if len(parts)<3:
        raise ValueError("Неверный формат строки: слишком мало данных")
    valid_levels = {"DEBUG","ERROR", "INFO", "WARNING"}
    if parts[1] not in valid_levels:
        raise ValueError("сломанная строка без уровня")
    return {"time": parts[0],
            "level": parts[1],
            "message": parts[2]}


def count_levels(lines):
    counts = {"BROKEN": 0}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts

def top_errors(lines, n):
    error_counts = {}
    for line in lines:
        if not line.strip(): continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass
    error_items=sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return error_items[:n]

def format_report(counts, errors):
    report ="Отчёт по журналу\n\n"
    sorted_keys=sorted(counts.keys())
    for key in sorted_keys:
        report += f"{key}: {counts[key]}\n"
    report += "\nЧастые ошибки:\n"
    for msg, count in errors:
        report += f"- {msg} — {count}\n"
    return report