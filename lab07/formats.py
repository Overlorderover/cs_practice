from csv import DictReader


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = text.splitlines()
    reader = DictReader(lines)
    return [dict(row) for row in reader]