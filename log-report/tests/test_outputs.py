import json
from pathlib import Path


def test_report_exists():
    """Criterion 1: The agent produced /app/report.json."""
    assert Path("/app/report.json").exists(), "no /app/report.json found"


def test_report_is_valid_json():
    """Criterion 1 (continued): /app/report.json contains valid JSON."""
    text = Path("/app/report.json").read_text()
    json.loads(text)  # raises if invalid


def test_total_requests():
    """Criterion 2: total_requests equals 6 (the number of log lines)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert "total_requests" in data, "missing key: total_requests"
    assert data["total_requests"] == 6, (
        f"expected total_requests=6, got {data['total_requests']}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals 3 (192.168.0.1, 192.168.0.2, 10.0.0.5)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert "unique_ips" in data, "missing key: unique_ips"
    assert data["unique_ips"] == 3, (
        f"expected unique_ips=3, got {data['unique_ips']}"
    )


def test_top_path():
    """Criterion 4: top_path is '/index.html' (appears 3 times, more than any other path)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert "top_path" in data, "missing key: top_path"
    assert data["top_path"] == "/index.html", (
        f"expected top_path='/index.html', got {data['top_path']!r}"
    )
