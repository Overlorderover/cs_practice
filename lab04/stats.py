
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

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        try:
            record = parse_record(cleaned_line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    city_totals = {}
    city_counts = {}
    for record in records:
        city = record["city"]
        temp = record["temperature"]
        city_totals[city] = city_totals.get(city, 0.0) + temp
        city_counts[city] = city_counts.get(city, 0) + 1
    averages = {}
    for city in city_totals:
        avg = city_totals[city] / city_counts[city]
        averages[city] = round(avg, 1)
    return averages

