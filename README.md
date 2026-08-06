# vienna-data-platform

Prefect setup

first, create the work pool:
docker compose exec -it prefect-server prefect work-pool create default --type process

Changing to uv package manager

after switching to your conda python env, set the following:
in bash:
export UV_PYTHON=$CONDA_PREFIX
in powershell:
$env:UV_PYTHON = $env:CONDA_PREFIX

check python version
uv pip list --python python

then
uv init
uv add prefect pytest ruff
uv sync
uv run pytest
uv run prefect ...