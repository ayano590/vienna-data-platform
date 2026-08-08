# vienna-data-platform

Prefect setup

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

start docker stack and create work pool:
docker compose up (--build)
docker compose exec -it prefect-server prefect work-pool create docker-work-pool --type docker

Run prefect commands
uv run prefect deploy
uv run prefect deploy -n hello-flow
uv run prefect deployment run 'hello_flow/hello-flow'  # schedule runs for this deployment
Disclaimer: if you have an empty prefect.yaml, trying to save the deployment configuration will result in an error.
either delete your prefect.yaml and try again, or re-initialize prefect

Docker Setup

switching from prefect work pool type "process" to "docker" for isolated flow runs
create Dockerfile.prefect-worker, install the python lib prefect-docker, and build the image:
docker build -f Dockerfile.prefect-worker -t prefect-worker:test .
docker run --rm prefect-worker:test python -c "import prefect_docker; print(prefect_docker)"
docker run --rm prefect-worker:test prefect worker start --pool docker-work-pool

update docker compose prefect worker to use image

test
docker build -t vienna-data-platform:test .
docker run --rm vienna-data-platform:test

docker pull ghcr.io/ayano590/vienna-data-platform:sha-cfa861b
docker run --rm ghcr.io/ayano590/vienna-data-platform:sha-cfa861b
change tag in prefect.yaml as well

prefect cannot find docker-work-pool, even though it is visible and active in prefect ui
uv run prefect config view
issue: docker prefect service points to localhost, while above command points to cloud

set prefect api url in powershell:
$env:PREFECT_API_URL="http://localhost:4200/api"
uv run prefect deployment ls
docker exec prefect-server prefect config view
uv run prefect deployment inspect hello_flow/hello-flow
docker inspect tremendous-bonobo --format '{{range .Config.Env}}{{println .}}{{end}}'

issue: docker starts workflow in its own docker network, while docker compose stack is in the compose network
docker network ls
change network in prefect ui under work pool settings

run crashed after fixing network issue
docker ps -a --filter "ancestor=ghcr.io/ayano590/vienna-data-platform:sha-cfa861b"