from csv import DictReader
from yaml import safe_load

def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = text.splitlines()
    reader = DictReader(lines)
    return [dict(row) for row in reader]

def parse_settings(lines: list[str]) -> dict:
    if not lines:
        return {}
    yaml_text = "\n".join(lines)
    result = safe_load(yaml_text)
    return result if result is not None else {}


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
