# MortageVsRenterAdvisor
Should you buy or rent an apartment? Let's use this dashboard to figure it out

## Setup

This project uses `uv` for dependency management.

1.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
    *Windows:* `.venv\Scripts\activate`

2.  Sync dependencies (this installs streamlit):
    ```bash
    uv sync
    ```
3.  Verify streamlit is installed:
    ```bash
    python -c "import streamlit; print('streamlit version:', streamlit.__version__)"
    ```
4.  (If import failed) add it, then sync:
    ```bash
    uv add streamlit
    uv sync
    ```

## How to Run

Use the venv's streamlit binary explicitly if `streamlit` is not on PATH:

```bash
.venv/bin/streamlit run scr/main_dashboard.py
```
Recommended (ensures correct interpreter):
```bash
python -m streamlit run scr/main_dashboard.py
```
If file not found:
```bash
ls scr/main_dashboard.py || ls src/main_dashboard.py
python -m streamlit run src/main_dashboard.py
```

IMPORTANT: Do NOT run:
```bash
/usr/bin/python3 .venv/bin/streamlit run ...
```
That mixes system python with venv scripts and causes ModuleNotFoundError.

Quick verification before running:
```bash
.venv/bin/python -c "import streamlit; print('streamlit OK')"
```

Troubleshooting:
1. Activate: `source .venv/bin/activate`
2. Check python: `which python` (must point inside .venv)
3. Missing module: `uv add streamlit && uv sync`
4. Force clean reinstall: `uv sync --reinstall`
5. Path check: `ls scr/ || ls src/`
6. Run: `python -m streamlit run scr/main_dashboard.py`
