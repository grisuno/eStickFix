# orphans

*Community 2 | 2 files | cohesion 0.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 0.00). Central symbols: `TestETL`, `TestETLProcessor`, `setUp`, `test_etl_process`, `test_quality_check`, `test_transformation`. Core file: `etl_unit_test.py` (7 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `etl_unit_test.py` | py | testing | 7 | no |
| `install.sh` | sh | utility | 0 | no |

## Key Symbols

- `TestETL` (class, `etl_unit_test.py:4`) `class TestETL(TestCase)`
- `setUp` (method, `etl_unit_test.py:5`) `def setUp(self)`
- `test_transformation` (method, `etl_unit_test.py:11`) `def test_transformation(self)`
- `test_quality_check` (method, `etl_unit_test.py:18`) `def test_quality_check(self)`
- `TestETLProcessor` (class, `etl_unit_test.py:27`) `class TestETLProcessor(TestCase)`
- `setUp` (method, `etl_unit_test.py:28`) `def setUp(self)`
- `test_etl_process` (method, `etl_unit_test.py:35`) `def test_etl_process(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 2 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (root: etl) and community 2 (orphans).
- [INFERRED] shares_context community 1 <-> 2 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 1 (root: app) and community 2 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `etl_unit_test.py`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `etl_unit_test.py`
- `install.sh`
