from zt3re import annotations as ann
from zt3re.families import UnionFind, _lis_anchors


def good_func():
    return {"name": "uart_tx_byte", "summary": "Transmit one byte over USART",
            "description": "Waits for TDBE and writes the byte to the data register.",
            "category": "uart", "confidence": "high",
            "params": [{"name": "b", "type": "u8", "description": "byte to send"}],
            "returns": {"type": "void", "description": ""}}


def test_valid_function_passes():
    assert ann.validate_function("x", good_func()) == []


def test_function_requires_description_and_identifier():
    n = good_func()
    n["name"] = "1bad"
    n["description"] = ""
    errs = ann.validate_function("x", n)
    assert any("invalid name" in e for e in errs)
    assert any("description" in e for e in errs)


def test_struct_validation_flags_overlap_and_unknown_type():
    t = {"structs": {"S": {"description": "a struct", "size": 8, "fields": [
        {"name": "a", "offset": 0, "type": "u32", "description": "first"},
        {"name": "b", "offset": 2, "type": "u32", "description": "overlaps a"},
        {"name": "c", "offset": 4, "type": "Nope", "description": "bad type"}]}}, "enums": {}}
    errs = ann.validate_types(t)
    assert any("overlapping" in e for e in errs)
    assert any("unknown type" in e for e in errs)


def test_lis_anchors_drops_crossing_pairs():
    pm = {1: 10, 2: 20, 3: 15, 4: 30}      # (3->15) crosses (2->20)
    assert _lis_anchors(pm) == [(1, 10), (2, 20), (4, 30)] or _lis_anchors(pm) == [(1, 10), (3, 15), (4, 30)]


def test_union_find():
    uf = UnionFind()
    a, b, c = ("A", 1), ("B", 1), ("C", 1)
    uf.union(a, b)
    assert uf.find(a) == uf.find(b) != uf.find(c)
