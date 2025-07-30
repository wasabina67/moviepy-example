# moviepy-example
MoviePy example

## Initialize

### Setup

```bash
uv init --app --python 3.12
```

### Create venv

```bash
uv venv
```

### Add MoviePy dependency

```bash
uv add moviepy
```

### Add ruff, black dev dependency

```bash
uv add --dev ruff black
```

```bash
uv run ruff check .
```

```bash
uv run black .
```

### Install dependencies

```bash
uv sync
```

### Activate venv (if not using `uv run`)

```bash
source .venv/bin/activate
```

```bash
python main.py
```

```bash
deactivate
```

## Run

```bash
uv run python main.py
```
