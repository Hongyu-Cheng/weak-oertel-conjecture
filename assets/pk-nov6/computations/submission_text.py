"""Read mathematical input from a pending submission without approving its proof."""
import json
from pathlib import Path
import re


def read_submission(candidate_id):
    """Return a candidate's proof text using a path independent of the caller's cwd."""
    if not isinstance(candidate_id, str) or re.fullmatch(r"[0-9a-f]{16}", candidate_id) is None:
        raise ValueError("candidate_id must contain exactly 16 lowercase hexadecimal digits")
    repository = Path(__file__).resolve().parents[3]
    candidate = repository / "candidates" / (candidate_id + ".json")
    data = json.loads(candidate.read_text(encoding="utf-8"))
    if data.get("candidate_id") != candidate_id or not isinstance(data.get("proof"), str):
        raise ValueError("candidate identity or proof text is invalid: " + candidate_id)
    return data["proof"]
