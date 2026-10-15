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
