from csv import DictReader
from yaml import safe_load
from json import dumps


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        record = dict(zip(headers, values))
        records.append(record)
    return records

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    for line in lines:
        if '#' in line:
            line = line.split('#', 1)[0]
        line = line.strip()
        if not line:
            continue
        if line.startswith('-'):
            val_str = line[1:].strip()
            if current_list_key is not None:
                result[current_list_key].append(val_str)
            continue
        if ':' in line:
            key, val_str = line.split(':', 1)
            key = key.strip()
            val_str = val_str.strip()
            if not val_str:
                current_list_key = key
                result[current_list_key] = []
            else:
                current_list_key = None
                val_lower = val_str.lower()
                if val_lower in ('true', 'yes'):
                    result[key] = True
                elif val_lower in ('false', 'no'):
                    result[key] = False
                else:)
                    try:
                        result[key] = int(val_str)
                    except ValueError:
                        try:
                            result[key] = float(val_str.replace(',', '.'))
                        except ValueError:
                            result[key] = val_str
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    merged_rows = []
    for row in rows:
        new_row = row.copy()
        row_key_value = row.get(key)
        if row_key_value in extra:
            extra_data = extra[row_key_value]
            for ex_key, ex_val in extra_data.items():
                if ex_key not in new_row:
                    new_row[ex_key] = ex_val
        merged_rows.append(new_row)
    return merged_rows

def records_to_json(records: list[dict]) -> str:
    return dumps(records, sort_keys=True, indent=2, ensure_ascii=False)