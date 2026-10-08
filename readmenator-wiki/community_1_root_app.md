# root: app

*Community 1 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `TestApp`, `test_create_config`, `test_etl_status`, `test_index`, `test_start_etl`. Core file: `app_unit_test.py` (5 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 0 | no |
| `app_unit_test.py` | py | testing | 5 | no |

## Key Symbols

- `TestApp` (class, `app_unit_test.py:7`) `class TestApp(TestCase)`
- `test_index` (method, `app_unit_test.py:9`) `def test_index(self, mock_render_template)`
- `test_create_config` (method, `app_unit_test.py:23`) `def test_create_config(self, mock_db, mock_User, mock_UserController, mock_url_f`
- `test_start_etl` (method, `app_unit_test.py:40`) `def test_start_etl(self, mock_data_navigator, mock_ETLProcessor, mock_DataQualit`
- `test_etl_status` (method, `app_unit_test.py:52`) `def test_etl_status(self, mock_current_user, mock_ProcessController, mock_render`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (root: etl) and community 1 (root: app).
- [INFERRED] shares_context community 1 <-> 2 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 1 (root: app) and community 2 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root: app changed?
- Should root: app be split, given cohesion 1.00?

## Sources

- `app.py`
- `app_unit_test.py`
