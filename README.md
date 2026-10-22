# ðŸ“‹ Dockerized To-Do List Application

> A simple, polished To-Do List web app (Flask + HTML/CSS/JavaScript) packaged
> and run with **Docker**. The application demonstrates container concepts from
> **Units 1â€“4**, including persistent storage, networking, security, optimization,
> automation, Kubernetes deployment, and health monitoring.

---

## Table of Contents
1. [Project Title](#1-project-title)
2. [Project Objective](#2-project-objective)
3. [Problem Statement](#3-problem-statement)
4. [Proposed Solution](#4-proposed-solution)
5. [Technologies Used](#5-technologies-used)
6. [Why Docker Is Used](#6-why-docker-is-used)
7. [Unit 1 Concepts Demonstrated](#7-unit-1-concepts-demonstrated)
8. [Unit 2 Concepts Demonstrated](#8-unit-2-concepts-demonstrated)
9. [System Architecture](#9-system-architecture)
10. [Project Folder Structure](#10-project-folder-structure)
11. [Application Setup](#11-application-setup)
12. [Running Without Docker](#12-running-without-docker)
13. [Creating the Docker Image](#13-creating-the-docker-image)
14. [Running the Docker Container](#14-running-the-docker-container)
15. [Docker Lifecycle Demonstration](#15-docker-lifecycle-demonstration)
16. [Docker Logs](#16-docker-logs)
17. [Docker Exec](#17-docker-exec)
18. [Docker Image Layers](#18-docker-image-layers)
19. [Docker History](#19-docker-history)
20. [Docker Namespaces Explanation](#20-docker-namespaces-explanation)
21. [Docker Architecture Explanation](#21-docker-architecture-explanation)
22. [Docker Compose](#22-docker-compose)
23. [Docker Hub](#23-docker-hub)
24. [Docker Registry Workflow](#24-docker-registry-workflow)
25. [Testing Procedure](#25-testing-procedure)
26. [Expected Output](#26-expected-output)
27. [Unit III and IV Concepts](#27-unit-iii-and-iv-concepts)
- [Appendix A: Docker Commands Reference](#appendix-a-docker-commands-reference)
- [Appendix B: `docker run` vs `docker start` vs `docker exec`](#appendix-b-docker-run-vs-docker-start-vs-docker-exec)

---

## 1. Project Title

**Dockerized To-Do List Application**

---

## 2. Project Objective

To build a small, working web application and **containerize it with Docker**, so
that I can practically demonstrate the core container concepts taught in
**Units 1â€“4** of the
*Container Based Application Development* course.

The application itself (a To-Do list) stays simple so the focus remains on
container concepts: Docker image layers and lifecycle, persistent storage,
container networking, runtime security, optimized builds, automation, and
deployment health.

---

## 3. Problem Statement

Traditional applications suffer from the classic *"but it works on my machine"*
problem. An app that runs on the developer's laptop may fail on another machine
because of different operating systems, missing Python versions, or missing
library versions.

We need a way to **package the application together with everything it needs to
run** (the Python runtime, Flask, and our code) into a single unit that runs the
**same way everywhere** â€” the professor's laptop, a lab machine, or a server.

---

## 4. Proposed Solution

Use **containerization with Docker**:

- Write the To-Do app in **Flask** (Python) with a plain **HTML/CSS/JavaScript** UI.
- Write a **Dockerfile** that describes exactly how to package the app.
- Build a **Docker image** from that Dockerfile.
- Run the image as a **Docker container** that behaves identically on any machine
  with Docker installed.
- Use **Docker Compose** to start the whole thing with a single command.
- Publish the image to **Docker Hub** so anyone can pull and run it.

Task data is stored in SQLite under `/data/tasks.db`. Docker Compose mounts a
named volume at `/data`, so tasks survive container replacement.

---

## 5. Technologies Used

| Layer            | Technology                    | Why |
|------------------|-------------------------------|-----|
| Frontend         | HTML, CSS, Vanilla JavaScript | Simple UI, no framework needed |
| Backend          | Python 3.12, Flask 3.1.3      | Lightweight web framework, easy to explain |
| Containerization | Docker, Dockerfile, Docker Compose | The subject of Units 1 & 2 |
| Base image       | `python:3.12-slim`            | Small, official Python image |


---

## 6. Why Docker Is Used

**What is Docker?**
Docker is a platform that packages an application and all of its dependencies into
a portable unit called a **container**.

**Where is it used in my project?**
The whole To-Do app (Python + Flask + our code) is packaged into one Docker image
and run as one container.

**Why is it used?**
- **Portability** â€” runs the same on any machine with Docker.
- **Consistency** â€” removes the *"works on my machine"* problem.
- **Isolation** â€” the app runs in its own sandbox, separate from the host.
- **Easy setup** â€” no need to manually install Python or Flask on the host; one
  `docker run` starts everything.
- **Lightweight** â€” containers share the host OS kernel, so they are far lighter
  than full virtual machines.

---

## 7. Unit 1 Concepts Demonstrated

> Unit 1 is mostly **theory**. Below, each concept is mapped to where it appears in
> this project (in practice or in documentation).

| Unit 1 Concept | What it is | Where / how it shows up here |
|----------------|-----------|------------------------------|
| **Introduction to Containers** | A container is a lightweight, isolated, runnable package of software. | Our whole app runs as one container. |
| **Containerization** | Packaging an app + dependencies into an image. | The `Dockerfile` packages Flask + our code. |
| **Containerization benefits** | Portability, consistency, isolation, speed, efficiency. | Explained in [Â§6](#6-why-docker-is-used); shown by `docker run` working anywhere. |
| **History / evolution** | From physical servers â†’ VMs â†’ containers â†’ Docker (2013). | Viva talking point (see below). |
| **Containers vs Virtualization** | Containers share the host kernel; VMs each run a full guest OS. | See the comparison table below. |
| **Container components & architecture** | Image, container, runtime, engine. | `docker images`, `docker ps`, `docker inspect`. |
| **Container runtime** | Low-level software that actually runs containers (e.g. `runc`). | Explained in [Â§21](#21-docker-architecture-explanation). |
| **Docker** | The most popular container platform. | Used throughout. |
| **Kubernetes & other tech (theory only)** | Orchestrators that manage many containers. | Documentation only â€” **not** implemented (Unit 4/5). |
| **Use cases & benefits** | Microservices, CI/CD, cloud, dev environments. | Documentation only. |
| **Microservices (theory only)** | App split into small independent services. | Explained as *future* direction; we use **one** container now. |
| **Containers as a Service â€” CaaS (theory only)** | Cloud service to run containers (ECS, ACI, GKE). | Documentation only. |
| **Serverless computing (theory only)** | Run code without managing servers (AWS Lambda). | Documentation only. |

### Containers vs Virtualization (Unit 1 comparison)

| Aspect | Virtual Machine | Container (our project) |
|--------|-----------------|--------------------------|
| Guest OS | Full OS per VM | **No** guest OS; shares host kernel |
| Size | Gigabytes | Megabytes (**varies by platform and build; measure it locally**) |
| Startup | Minutes | Varies by host |
| Isolation | Hardware-level (hypervisor) | OS-level (namespaces + cgroups) |
| Overhead | High | Low |

### History / evolution (viva talking point)
Physical servers (one app per costly server) â†’ **Virtual Machines** (many VMs per
server, but each carries a heavy full OS) â†’ **Containers** (share the host kernel,
lightweight) â†’ **Docker (2013)** made containers easy and popular â†’ orchestration
(Kubernetes) for running containers at scale.

---

## 8. Unit 2 Concepts Demonstrated

> Unit 2 is **practical**. Every concept below is actually used in this project.

| Unit 2 Concept | Where it is demonstrated |
|----------------|--------------------------|
| **Docker introduction** | The project uses Docker end-to-end. |
| **Docker architecture** | [Â§21](#21-docker-architecture-explanation): CLI â†’ daemon â†’ containerd â†’ runc â†’ kernel. |
| **Docker client & daemon** | Every `docker ...` command = client talking to the daemon. |
| **Docker image** | We build `todo-app:1.0` (`docker images`). |
| **Docker container** | We run `todo-container` (`docker ps`). |
| **Docker layered approach** | The `Dockerfile` is ordered to create clean, cacheable layers. |
| **Docker image layers** | Visible with `docker history todo-app:1.0` ([Â§18](#18-docker-image-layers)/[Â§19](#19-docker-history)). |
| **Docker namespaces** | Explained in [Â§20](#20-docker-namespaces-explanation); shown via container's own hostname & PID. |
| **Docker container lifecycle** | Demonstrated in [Â§15](#15-docker-lifecycle-demonstration): createâ†’runâ†’stopâ†’startâ†’pauseâ†’unpauseâ†’remove. |
| **Docker components** | Client, daemon, images, containers, registry â€” all used. |
| **Docker setup / installation** | [Â§11](#11-application-setup) (`docker --version`, `docker info`). |
| **Working with Docker** | The whole build â†’ run â†’ inspect workflow. |
| **Dockerfile** | See [`Dockerfile`](Dockerfile) and [Â§13](#13-creating-the-docker-image). |
| **Docker commands** | [Appendix A](#appendix-a-docker-commands-reference). |
| **Docker Hub** | [Â§23](#23-docker-hub). |
| **Docker Registry** | [Â§24](#24-docker-registry-workflow). |
| **Push image to Docker Hub** | [Â§24](#24-docker-registry-workflow) (commands provided, done by student). |
| **Docker Compose** | See [`docker-compose.yml`](docker-compose.yml) and [Â§22](#22-docker-compose). |

---

## 9. System Architecture

For this version the app runs as **one single container**.

```
        User
         â”‚  (types in browser)
         â–¼
   Web Browser  â”€â”€ HTTP :5000 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
         â”‚                                  â”‚
         â–¼                                  â”‚  published port
   Flask Application (app.py)               â”‚  5000 (host) -> 5000 (container)
         â”‚  (Python code, in-memory list)   â”‚
         â–¼                                  â”‚
   Docker Container  â—„â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
   Docker Engine (daemon)
         â”‚
         â–¼
   Container Runtime (containerd â†’ runc)
         â”‚
         â–¼
   Host OS / Linux Kernel  (namespaces + cgroups provide isolation)
```

- **One image â†’ one container â†’ one Flask app.**
- No separate frontend/backend/database containers (that is Unit 3+).

---

## 10. Project Folder Structure

```
dockerized-todo/
â”‚
â”œâ”€â”€ app.py                # Flask backend: routes + in-memory task list
â”œâ”€â”€ requirements.txt      # Python dependency (Flask), version-pinned
â”œâ”€â”€ Dockerfile            # Recipe to build the Docker image (layered)
â”œâ”€â”€ docker-compose.yml    # Runs the single app service with one command
â”œâ”€â”€ .dockerignore         # Files to keep OUT of the image
â”œâ”€â”€ README.md             # This documentation
â”‚
â”œâ”€â”€ templates/
â”‚   â””â”€â”€ index.html        # The HTML page (served by Flask)
â”‚
â””â”€â”€ static/
    â”œâ”€â”€ style.css         # Styling (clean, responsive)
    â””â”€â”€ script.js         # Vanilla JS: fetch API calls, render, filter
```

### What each file does

| File | Purpose |
|------|---------|
| `app.py` | Creates the Flask app, stores tasks in a Python list, defines routes: `/`, `/api/tasks`, `/add`, `/complete/<id>`, `/delete/<id>`. |
| `requirements.txt` | Lists `Flask==3.1.3`. Docker installs this during the build. |
| `Dockerfile` | Instructions Docker follows to build the image (`FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`). |
| `docker-compose.yml` | Defines the single `todo-app` service so we can run it with `docker compose up`. |
| `.dockerignore` | Prevents junk (caches, venv, `.git`) from being copied into the image. |
| `templates/index.html` | The web page structure; Flask renders it at `/`. |
| `static/style.css` | Colours, layout, responsive design. |
| `static/script.js` | Talks to the Flask API using `fetch()`, draws tasks, handles Add/Complete/Delete/Filter and errors. |

---

## 11. Application Setup

### Prerequisites
- **Docker Desktop** (includes Docker Engine + Docker Compose) â€” for the Docker parts.
- **Python 3.10+** â€” only if you want to run the app *without* Docker.

### Verify Docker is installed and running
```bash
docker --version
```
```bash
docker info
```
- `docker --version` â†’ prints the Docker version (e.g. `Docker version 29.7.2`).
- `docker info` â†’ shows details about the running Docker engine. If this errors
  with *"cannot connect to the Docker daemon"*, **start Docker Desktop first**.

---

## 12. Running Without Docker

Useful to confirm the app works before containerizing it.

```bash
cd dockerized-todo
python -m pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5000** in your browser.

> ðŸ’¡ **Windows note:** if the bare `pip` command gives
> *"pip is not recognized..."*, call it through Python with
> **`python -m pip install -r requirements.txt`** (as shown above). This works
> anywhere Python is on your PATH. On some systems the launcher `py -m pip` also works.

> This proves the raw Flask app works. Docker will do exactly the same thing, just
> inside a container.

---

## 13. Creating the Docker Image

The image is built from the [`Dockerfile`](Dockerfile). Build it with:

```bash
docker build -t todo-app:1.0 .
```

- `docker build` â†’ builds an image from the Dockerfile.
- `-t todo-app:1.0` â†’ **t**ags (names) the image `todo-app` with version `1.0`.
- `.` â†’ the **build context** = the current folder (Docker sends these files to the daemon).

Check that it was created:
```bash
docker images
```

### The Dockerfile explained (line by line)

```dockerfile
FROM python:3.12-slim          # 1. Base layer: a small official Python image
WORKDIR /app                   # 2. Set /app as the working directory in the image
COPY requirements.txt .        # 3. Copy ONLY the dependency list first (for caching)
RUN pip install --no-cache-dir -r requirements.txt   # 4. Install Flask
COPY . .                       # 5. Copy the rest of the app code
EXPOSE 5000                    # 6. Document that the app listens on port 5000
CMD ["python", "app.py"]       # 7. The command run when the container starts
```

> **Why copy `requirements.txt` before the code?** So Docker can **cache** the
> `pip install` layer. If we change only `app.py`, Docker reuses the cached
> dependency layer and the rebuild is almost instant (proven in [Â§26](#26-expected-output)).

---

## 14. Running the Docker Container

```bash
docker run -d -p 5000:5000 --name todo-container todo-app:1.0
```

- `docker run` â†’ create **and** start a container from the image.
- `-d` â†’ **d**etached (runs in the background).
- `-p 5000:5000` â†’ **publish** port: `HOST:CONTAINER`. Opens `localhost:5000`.
- `--name todo-container` â†’ give the container a friendly name.
- `todo-app:1.0` â†’ the image to run.

Open **http://localhost:5000** â€” the To-Do app is now served from inside Docker.

Check it is running:
```bash
docker ps
```

---

## 15. Docker Lifecycle Demonstration

A container moves through these states:

```
     docker run                docker stop            docker start
 (image) â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º RUNNING â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º STOPPED â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º RUNNING
                       â”‚                                               â”‚
              docker pause â”‚                                    docker rm â”‚  (must stop first)
                       â–¼                                               â–¼
                    PAUSED â”€â”€ docker unpause â”€â”€â–º RUNNING            REMOVED
```

**Commands to demonstrate it:**
```bash
docker ps                       # RUNNING
docker stop todo-container      # -> STOPPED
docker ps -a                    # shows it as "Exited"
docker start todo-container     # -> RUNNING again
docker pause todo-container     # -> PAUSED (processes frozen)
docker unpause todo-container   # -> RUNNING
docker rm -f todo-container     # -> REMOVED
```

> ðŸ”‘ **Important teaching point:** because our data is stored **in memory**, when
> you `stop` and `start` the container, the Python process restarts and all tasks
> reset to the 3 seed tasks. Any task you added is gone. This is expected â€”
> persistence is a **Unit 3** topic.

---

## 16. Docker Logs

```bash
docker logs todo-container
```

- **What:** shows everything the app printed to stdout/stderr (Flask's startup
  message and every HTTP request).
- **Why:** the main way to debug a container without going inside it.

Live/follow mode:
```bash
docker logs -f todo-container
```
(`-f` = follow; press `Ctrl+C` to stop watching.)

---

## 17. Docker Exec

```bash
docker exec -it todo-container bash
```

- **What:** runs a command **inside a running container**. `-it` gives an
  interactive terminal, so you get a shell prompt *inside* the container.
- **Why:** to look around inside the container â€” check files, environment, Python version.

Useful one-off examples (no interactive shell needed):
```bash
docker exec todo-container python --version   # Python inside the container
docker exec todo-container ls -la /app         # our files inside the image
docker exec todo-container hostname            # the container's own hostname
```

> On **Git Bash (Windows)** a leading `/app` can get rewritten to a Windows path.
> If that happens, prefix the command with `MSYS_NO_PATHCONV=1`, e.g.
> `MSYS_NO_PATHCONV=1 docker exec todo-container ls -la /app`.

---

## 18. Docker Image Layers

Docker builds an image as a **stack of read-only layers**. Each Dockerfile
instruction that changes the filesystem adds one layer:

```
CMD ["python","app.py"]     â†’ startup config      (0 B)
EXPOSE 5000                 â†’ metadata            (0 B)
COPY . .                    â†’ APPLICATION layer   (our code)
RUN pip install ...         â†’ DEPENDENCY install layer (Flask + libs)
COPY requirements.txt .     â†’ dependency list layer
WORKDIR /app                â†’ working-dir layer
FROM python:3.12-slim       â†’ BASE layer          (Python + Debian)
```

**Layer caching:** Docker reuses ("caches") a layer if its instruction and inputs
have not changed. Because we copy `requirements.txt` **before** the app code,
editing `app.py` does not invalidate the `pip install` layer, so rebuilds are fast.

---

## 19. Docker History

See the actual layers of the built image:

```bash
docker history todo-app:1.0
```

Real output from this project:

```
IMAGE          CREATED         CREATED BY                                      SIZE
9f4936386813   1 minute ago    CMD ["python" "app.py"]                         0B
<missing>      1 minute ago    EXPOSE [5000/tcp]                               0B
<missing>      1 minute ago    COPY . . # buildkit                             57.3kB
<missing>      1 minute ago    RUN /bin/sh -c pip install --no-cache-dir -râ€¦   15.3MB
<missing>      1 minute ago    COPY requirements.txt . # buildkit              12.3kB
<missing>      1 minute ago    WORKDIR /app                                    8.19kB
<missing>      14 hours ago    CMD ["python3"]                                 0B
...            (the remaining layers come from the python:3.12-slim base image)
```

- The **top 6 layers** are the ones **our Dockerfile** created.
- The layers marked `<missing>` below them come from the **base image**
  (`python:3.12-slim`). `<missing>` just means those layers have no separate local
  image ID â€” it is **not** an error.
- The biggest layer of ours is `RUN pip install` (**15.3 MB** â€” Flask + its libraries).

---

## 20. Docker Namespaces Explanation

> We do **not** create namespaces manually. Docker uses **Linux namespaces**
> automatically to give each container its own isolated view of the system.

| Namespace | What it isolates | Effect on our To-Do container |
|-----------|------------------|-------------------------------|
| **PID** | Process IDs | The container has its own process tree. Our Flask process has a small PID inside (we saw PID `49`) and cannot see host processes. |
| **NET** | Network (interfaces, IPs, ports) | The container gets its own IP (we saw `172.17.0.3`) and its own port 5000, mapped to the host's 5000. |
| **MNT** | Filesystem mount points | The container sees its own filesystem (`/app`, `/usr`, ...) â€” not the host's folders. |
| **UTS** | Hostname | The container has its own hostname (we saw `9c3bbb7bcedb`), independent of the host. |
| **IPC** | Inter-process communication (shared memory) | The container's IPC is separate from the host and other containers. |
| **USER** | User & group IDs | Container UIDs can be mapped separately from host UIDs. |

**In one line:** namespaces are what make a container *feel* like its own little
machine, even though it shares the host's kernel. (Resource limits like CPU/RAM are
handled by a related feature called **cgroups**.)

---

## 21. Docker Architecture Explanation

```
   You type:  docker run ...        (the request)
        â”‚
        â–¼
   Docker CLI (client)   â”€â”€ sends the command over the Docker API â”€â”€â–º
        â”‚
        â–¼
   Docker Daemon (dockerd)          â”€â”€ the "brain"; builds images, manages containers
        â”‚
        â–¼
   containerd                       â”€â”€ high-level container runtime (manages lifecycle)
        â”‚
        â–¼
   runc                             â”€â”€ low-level runtime; actually creates the container
        â”‚                              using Linux namespaces + cgroups
        â–¼
   Container  â”€â”€â–º  our Flask Application
        â”‚
        â–¼
   Linux Kernel                     â”€â”€ shared by the host and all containers
```

| Component | Role |
|-----------|------|
| **Docker Client (CLI)** | The `docker` command you type. Sends requests to the daemon. |
| **Docker Daemon (`dockerd`)** | Listens for requests; builds images, starts/stops containers, manages networks. The client and daemon can even be on different machines. |
| **containerd** | A high-level runtime that manages the complete container lifecycle (pull, start, stop). |
| **runc** | The low-level runtime that actually spawns the container process using kernel features. |
| **Linux Kernel** | Provides **namespaces** (isolation) and **cgroups** (resource limits). Shared by all containers â€” this is why containers are lightweight. |

**Client â†” Daemon in this project:** every command such as `docker build` or
`docker ps` is the **client** sending a request; the **daemon** does the actual
work and sends the result back.

---

## 22. Docker Compose

The `todo-app` service builds the multi-stage Dockerfile, publishes host port
5000, keeps SQLite data in the `todo-data` volume, and runs as
`todo-container`. Its health check calls the real `/health` endpoint.

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down
```

## 23. Docker Hub and automated publishing

The GitHub Actions workflow publishes `zeeshanwasim/todo-app:latest` and
`zeeshanwasim/todo-app:sha-<commit>` after tests and the image build pass on a
push to `main`. Pull requests only build and test; they do not receive Docker
Hub credentials and cannot publish. No version tag is created because this
repository does not currently define a release version.

To allow publishing, create a Docker Hub access token with only the permission
needed to push this repository. In GitHub, open **Settings → Secrets and
variables → Actions → New repository secret** and add:

- `DOCKER_USERNAME`: your Docker Hub username (`zeeshanwasim` for the configured image).
- `DOCKER_TOKEN`: the access token (never commit or share it).

## 24. Local build and run

Prerequisites: Git, Docker Desktop with Compose, a GitHub account, and a Docker
Hub account if you want to publish manually.

```bash
docker build -t todo-app:1.0 .
docker run --rm -p 5000:5000 todo-app:1.0
```

Or use Compose, which also persists data between container replacements:

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down
```

Open <http://localhost:5000>. Check the actual health endpoint at
<http://localhost:5000/health>. Compose uses the registry name
`zeeshanwasim/todo-app:latest` and builds locally. To measure your built image
size, run `docker images zeeshanwasim/todo-app:latest`; no size reduction is
claimed without comparing an available original image to the new build.

## 25. Tests

Tests use Flask's test client and a fresh temporary SQLite database for each
test. They cover the home page and frontend assets, seeded tasks, create,
complete, delete, invalid inputs, missing task IDs, and the health endpoint.

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
```

The same suite can run in the dedicated Docker test stage (pytest is not copied
into the production runtime image):

```bash
docker build --target test -t todo-app:test .
docker run --rm todo-app:test
```

`requirements-dev.txt` contains pytest; it is not installed in the runtime
image. The application dependencies remain in `requirements.txt`.

## 26. GitHub SSH and CI/CD setup

Generate an SSH key on your computer (accept the suggested file location and
protect the private key with a passphrase):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Copy the **public** key (`.pub` file) to GitHub under **Settings → SSH and GPG
keys → New SSH key**. Keep the private key on your computer; never share it.
Verify the account connection with:

```bash
ssh -T git@github.com
```

If this directory is not already a Git repository, initialize and commit it:

```bash
git init
git add .
git commit -m "Upgrade Docker build and CI/CD"
```

Check for an existing remote before adding one so you do not replace it:

```bash
git remote -v
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git
```

If `origin` already exists, verify it points to the intended repository; update
it only if that is your deliberate choice. Push the main branch:

```bash
git branch -M main
git push -u origin main
```

In the GitHub repository's **Actions** tab, open the **CI and Docker delivery**
workflow. A failed test or image build prevents publishing. A successful trusted
push to `main` publishes `latest` and the traceable `sha-<commit>` tag. Verify
publication by opening the workflow run and Docker Hub repository, then try:

```bash
docker pull zeeshanwasim/todo-app:latest
docker run --rm -p 5000:5000 zeeshanwasim/todo-app:latest
```

The workflow runs tests and builds on pushes to `main` and pull requests that
target `main`. Only a push to `main` can publish. Docker Hub publishing is not a
remote server deployment.

## 27. Optional remote deployment

No deployment host or credentials are configured in this repository, so a
remote deployment is not active. To activate the conditional deployment job,
configure these repository variables and secrets:

- Variable `DEPLOY_HOST`: SSH hostname or IP of a server with Docker Engine.
- Variable `DEPLOY_USER`: SSH account that can run Docker.
- Optional variable `DEPLOY_PORT`: SSH port (defaults to 22).
- Variable `DEPLOY_FINGERPRINT`: SSH host-key fingerprint for the target server.
- Secret `DEPLOY_SSH_KEY`: private key for that account; never commit or share it.
- The `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets above, for pulling the image.

The server must accept the corresponding SSH public key, have Docker installed,
and permit that account to run Docker. Deployment is restricted to successful
pushes to `main` after publication. The job starts a candidate container and
checks `/health` before replacing the current one, and attempts to restore the
previous container if the replacement is unhealthy. A workflow run is the
source of truth for whether deployment succeeded; publishing alone does not
mean it was deployed.

## 28. Troubleshooting

- **Docker build fails:** confirm Docker Desktop is running and retry with
  `docker build --no-cache -t todo-app:1.0 .` to rule out stale layers.
- **Tests fail:** run `python -m pip install -r requirements.txt -r requirements-dev.txt`
  and `python -m pytest -q`; inspect the first failing assertion.
- **Port 5000 is busy:** stop the other service or change the host side of the
  mapping, for example `-p 5001:5000`, then open port 5001.
- **Container is unhealthy:** inspect `docker compose logs` and
  `docker inspect todo-container`; confirm `/health` responds inside the app.
- **Docker Hub login or push fails:** check the `DOCKER_USERNAME` and
  `DOCKER_TOKEN` repository secrets and token push permission. Never put the
  token in a command committed to the repository.
- **Image pull fails:** verify the repository and tag spelling, successful
  publish job, and repository visibility or Docker Hub login.
- **Workflow secrets are missing:** publishing requires both Docker Hub secrets;
  GitHub does not provide repository secrets to fork pull request workflows.
- **Remote deployment fails:** check `DEPLOY_HOST`, `DEPLOY_USER`, optional
  `DEPLOY_PORT`, `DEPLOY_FINGERPRINT`, `DEPLOY_SSH_KEY`, server SSH access, and Docker permissions.

The image size and deployment status must be measured from actual local Docker
and GitHub Actions runs; neither is assumed successful by this documentation.

---
## Appendix A: Docker Commands Reference

For each command: **what it does Â· why we use it Â· example.**

| Command | What it does | Why (in this project) | Example |
|---------|--------------|-----------------------|---------|
| `docker --version` | Prints Docker version | Confirm Docker is installed | `docker --version` |
| `docker info` | Shows engine details | Confirm the daemon is running | `docker info` |
| `docker build` | Builds an image from a Dockerfile | Create our `todo-app` image | `docker build -t todo-app:1.0 .` |
| `docker images` | Lists local images | Confirm the image was built | `docker images` |
| `docker run` | Creates + starts a container | Launch the To-Do app | `docker run -d -p 5000:5000 --name todo-container todo-app:1.0` |
| `docker ps` | Lists **running** containers | See if the app is up | `docker ps` |
| `docker ps -a` | Lists **all** containers (incl. stopped) | See stopped containers in the lifecycle | `docker ps -a` |
| `docker logs` | Shows a container's output | Debug / view requests | `docker logs todo-container` |
| `docker exec` | Runs a command inside a running container | Look inside the container | `docker exec -it todo-container bash` |
| `docker stop` | Stops a running container | Lifecycle demo | `docker stop todo-container` |
| `docker start` | Starts a stopped container | Lifecycle demo | `docker start todo-container` |
| `docker pause` | Freezes a container's processes | Lifecycle demo | `docker pause todo-container` |
| `docker unpause` | Resumes a paused container | Lifecycle demo | `docker unpause todo-container` |
| `docker inspect` | Shows detailed JSON info | See status, IP, ports, command | `docker inspect todo-container` |
| `docker history` | Shows an image's layers | Explain layered approach | `docker history todo-app:1.0` |
| `docker rename` | Renames a container | Show container management | `docker rename todo-container my-todo` |
| `docker port` | Shows port mappings | Confirm 5000 is published | `docker port todo-container` |
| `docker rm` | Removes a (stopped) container | Clean up | `docker rm todo-container` |
| `docker rmi` | Removes an image | Clean up | `docker rmi todo-app:1.0` |
| `docker system prune` | Removes unused data (âš ï¸ destructive) | Free disk space | `docker system prune` |

> âš ï¸ `docker system prune` deletes stopped containers, unused networks and dangling
> images. Run it only when you understand what will be removed.

---

## Appendix B: `docker run` vs `docker start` vs `docker exec`

A very common **viva question**. Simple distinction:

| Command | Works on | What it does |
|---------|----------|--------------|
| `docker run` | an **image** | **Creates a new container** from the image **and** starts it. (New container every time.) |
| `docker start` | an **existing, stopped container** | **Restarts the same container** that already exists. Keeps its identity/name. |
| `docker exec` | a **running container** | Runs an **extra command inside** a container that is **already running** (e.g. open a shell). |

**One-line memory aid:**
> `run` = make a new one Â· `start` = wake an existing one Â· `exec` = go inside a running one.

---

*Built for the Container Based Application Development course â€” Unit 1 & Unit 2 mini-project.*
