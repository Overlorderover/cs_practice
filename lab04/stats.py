
def parse_record(line: str) -> dict:
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных ';'")
    city = fields[0].strip()
    temp_str = fields[1].strip()
    date = fields[2].strip()
    if not city or not date:
        raise ValueError("Название города и дата не могут быть пустыми")
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temp_str}'")
    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }
