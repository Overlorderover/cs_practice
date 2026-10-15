def parse_event(line):
    dict=line.split(None,2)
    if len(dict)<3:
        raise ValueError("Неверный формат строки: слишком мало данных")
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if dict[1] not in valid_levels:
        raise ValueError("сломанная строка без уровня")
    return {"time": dict[0],
            "level": dict[1],
            "message": dict[2]}


def count_levels(lines):
    counts = {"BROKEN": 0,
              "DEBUG": 0,
              "INFO": 0,
              "WARNING": 0,
              "ERROR": 0}
    for line in lines:
        if not line.strip():  # Если строка пустая или состоит только из пробелов
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] += 1
        except ValueError:
            counts["BROKEN"] += 1
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
    report += "\nЧастые ошибки::\n"
    for msg, count in errors:
        report += f"- {msg} - {count}\n"
    return report.strip()