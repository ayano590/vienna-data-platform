# vienna-data-platform

Prefect setup

first, create the work pool:
docker compose exec -it prefect-server prefect work-pool create default --type process

Changing to uv package manager

disclaimer: do not use anaconda python environments, as these cause issues in conjunction with uv
either temporarily deactivate the conda env for every session:
conda deactivate
or deactivate conda auto activation entirely:
conda init --reverse powershell cmd.exe

check python version
uv pip list --python python

then
uv init
uv add prefect pytest ruff
uv sync
uv run pytest

Initialize prefect
uv run prefect init  # creates the prefect.yaml
select docker, and provide image name and tag from ghcr.io
if your image has no tag, copy digest and convert:
...@sha256:123 -> ...:sha-123
move the image+tag info to deployments:work_pool:job_variables:image
set build, push and pull to null, since prefect does not build the docker images, but github actions
add name, description, entrypoint
for the worker, add the work pool name you used during pool creation

Run prefect commands
uv run prefect deploy
uv run prefect deploy -n hello-flow
uv run prefect deployment run 'hello_flow/hello-flow'  # schedule runs for this deployment
Disclaimer: if you have an empty prefect.yaml, trying to save the deployment configuration will result in an error.
either delete your prefect.yaml and try again, or re-initialize prefect