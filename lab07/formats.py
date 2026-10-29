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

