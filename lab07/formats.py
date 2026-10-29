from csv import DictReader
from json import dumps

def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = text.splitlines()
    reader = DictReader(lines)
    return [{k.strip(): v.strip() for k, v in row.items()} for row in reader]

def _parse_scalar(value: str):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    low = value.lower()
    if low in ('true', 'yes'):
        return True
    if low in ('false', 'no'):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    if value.count(',') == 1:
        left, _, right = value.partition(',')
        if left.lstrip('-+').isdigit() and right.isdigit():
            return float(f"{left}.{right}")
    return value

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
                result[current_list_key].append(_parse_scalar(val_str))
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
                result[key] = _parse_scalar(val_str)
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
