# root

*Community 0 | 1 files | cohesion 1.00*

## Definition

This community groups 1 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `create_database`, `get_geocoding_data`, `get_location_data`, `insert_location`, `print_banner`, `print_table_data`, `print_table_structure`. Core file: `main.py` (7 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `main.py` | py | utility | 7 | no |

## Key Symbols

- `insert_location` (function, `main.py:10`) `def insert_location(conn, data)`
- `print_table_structure` (function, `main.py:27`) `def print_table_structure(conn)`
- `print_table_data` (function, `main.py:38`) `def print_table_data(conn)`
- `create_database` (function, `main.py:49`) `def create_database(database_file)`
- `get_location_data` (function, `main.py:81`) `def get_location_data(ip, access_key)`
- `get_geocoding_data` (function, `main.py:91`) `def get_geocoding_data(query, region)`
- `print_banner` (function, `main.py:108`) `def print_banner()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [taint medium] `main.py` -> `main.py` via `requests` (0 hops)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `main.py`)? What purpose do they serve?
- Is the dangerous import `requests` in `main.py` still required, or can it be isolated?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `main.py`
