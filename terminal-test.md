#5 transferring context: 332B 0.0s done
#5 DONE 0.0s

#6 [1/5] FROM docker.io/library/python:3.12-slim@sha256:e5c9fa26ffb76e11e0f054f30dc2523a2f9693f0c36c0cf1e39b27e152d899fc
#6 resolve docker.io/library/python:3.12-slim@sha256:e5c9fa26ffb76e11e0f054f30dc2523a2f9693f0c36c0cf1e39b27e152d899fc 0.0s done
#6 DONE 0.1s

#7 [2/5] WORKDIR /app
#7 CACHED

#8 [3/5] COPY requirements.txt .
#8 CACHED

#9 [4/5] RUN pip install --no-cache-dir -r requirements.txt
#9 CACHED

#10 [5/5] COPY . .
#10 CACHED

#11 exporting to image
#11 exporting layers
#11 exporting layers done
#11 exporting manifest sha256:c63afb31e9b01b69d8fe24097a12916259494b4003dd15d655ebcb4d8ca416d9 0.0s done
#11 exporting config sha256:efd32a1e0c21806ed88bbd349609931d575fd446afa0bed4fa165a0ee47851ee done
#11 exporting attestation manifest sha256:89024470dd7795b71c3c67ad21ba85f1647824a03e119b73518a5eafc75efab1 0.0s done
#11 exporting manifest list sha256:ff7e75068a43a3f13f4a5a4be060b3d824d36d43e84422a8bd54052b94f2326b 0.0s done
#11 naming to docker.io/library/todo-app:1.0
#11 naming to docker.io/library/todo-app:1.0 done
#11 unpacking to docker.io/library/todo-app:1.0 0.0s done
#11 DONE 0.2s

#12 resolving provenance for metadata file
#12 DONE 0.0s
[+] up 3/4
 ✔ Image t... Built                                                                                               2.5s
 ✔ Network... Created                                                                                             0.1s
 - Contain... Creating                                                                                            0.1s
 ✘ service... Error response from daemon: Conflict. The container name "/todo-container" is already in use by container "edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214". You have to remove (or rename) that container to be able to reuse that name. 0.0s
Error response from daemon: Conflict. The container name "/todo-container" is already in use by container "edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214". You have to remove (or rename) that container to be able to reuse that name.

What's next:
    Debug this Compose error with Gordon → docker ai "help me fix this compose error"
PS D:\College\CBAD\Mini Project\dockerized-todo> docker build -t todo-app:1.0 
ERROR: docker: 'docker buildx build' requires 1 argument

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Run 'docker buildx build --help' for more information

What's next:
    Debug this build failure with Gordon → docker ai "help me fix this build failure"
PS D:\College\CBAD\Mini Project\dockerized-todo> docker tag todo-app:1.0 YOUR_USERNAME/todo-app:1.0
error parsing reference: "YOUR_USERNAME/todo-app:1.0" is not a valid repository/tag: repository name must be lowercase
PS D:\College\CBAD\Mini Project\dockerized-todo> docker login
Authenticating with existing credentials... [Username: zeeshanwasim12]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
PS D:\College\CBAD\Mini Project\dockerized-todo> docker tag todo-app:1.0 zeeshanwasim12/todo-app:1.0
PS D:\College\CBAD\Mini Project\dockerized-todo> docker push todo-app:1.0 zeeshanwasim12/todo-app:1.0
docker: 'docker push' requires 1 argument

Usage:  docker push [OPTIONS] NAME[:TAG]

Run 'docker push --help' for more information
PS D:\College\CBAD\Mini Project\dockerized-todo> docker push zeeshanwasim12/todo-app:1.0             
The push refers to repository [docker.io/zeeshanwasim12/todo-app]
6310eb16bf42: Pushed 
5b279443e682: Pushed 
44136fa355b3: Pushed 
dbd0b7849e6c: Pushed 
1560cfed01dc: Pushed 
56235e424563: Pushed 
f11ea0d01df4: Pushed 
9bd9651aae98: Pushed 
f2766cbee7d0: Pushed 
5116f3899b71: Pushed 
1.0: digest: sha256:ff7e75068a43a3f13f4a5a4be060b3d824d36d43e84422a8bd54052b94f2326b size: 856
PS D:\College\CBAD\Mini Project\dockerized-todo> docker pull zeeshanwasim12/todo-app:1.0
1.0: Pulling from zeeshanwasim12/todo-app
Digest: sha256:ff7e75068a43a3f13f4a5a4be060b3d824d36d43e84422a8bd54052b94f2326b
Status: Image is up to date for zeeshanwasim12/todo-app:1.0
docker.io/zeeshanwasim12/todo-app:1.0
PS D:\College\CBAD\Mini Project\dockerized-todo> ^C
PS D:\College\CBAD\Mini Project\dockerized-todo> ^C
PS D:\College\CBAD\Mini Project\dockerized-todo> 
 *  History restored 

PS D:\College\CBAD\Mini Project\dockerized-todo> 
 *  History restored 

PS D:\College\CBAD\Mini Project\dockerized-todo> python app.py                                       
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.4:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 144-328-333
127.0.0.1 - - [02/Sep/2026 11:25:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [02/Sep/2026 11:25:22] "GET /static/style.css HTTP/1.1" 200 -
127.0.0.1 - - [02/Sep/2026 11:25:22] "GET /static/script.js HTTP/1.1" 200 -
127.0.0.1 - - [02/Sep/2026 11:25:22] "GET /api/tasks HTTP/1.1" 200 -
127.0.0.1 - - [02/Sep/2026 11:25:22] "GET /favicon.ico HTTP/1.1" 404 -
PS D:\College\CBAD\Mini Project\dockerized-todo> dir


    Directory: D:\College\CBAD\Mini Project\dockerized-todo


Mode                 LastWriteTime         Length Name                                                               
----                 -------------         ------ ----                                                               
d-----        01-09-2026     19:14                static                                                             
d-----        01-09-2026     19:13                templates                                                          
d-----        01-09-2026     19:15                __pycache__                                                        
-a----        01-09-2026     19:39            119 .dockerignore                                                      
-a----        01-09-2026     19:37           2368 app.py                                                             
-a----        01-09-2026     19:38            171 docker-compose.yml                                                 
-a----        01-09-2026     19:39            160 Dockerfile                                                         
-a----        02-09-2026     11:19          32843 README.md                                                          
-a----        01-09-2026     19:39             13 requirements.txt                                                   


PS D:\College\CBAD\Mini Project\dockerized-todo> docker --version
Docker version 29.7.2, build a7dcaa6
PS D:\College\CBAD\Mini Project\dockerized-todo> docker info
Client:
 Version:    29.7.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.119.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.30.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.36.0-desktop.1
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.3.1
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.0.47
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  v0.4.3
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.7
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.31
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.43.3
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.6
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.6.9
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.2.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.24.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-scout.exe

Server:
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
PS D:\College\CBAD\Mini Project\dockerized-todo> docker info
Client:
 Version:    29.7.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.119.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.30.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.36.0-desktop.1
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.3.1
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.0.47
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  v0.4.3
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.7
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.31
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.43.3
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.6
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.6.9
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.2.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.24.0
    Path:     C:\Users\Zeeshan Wasim\.docker\cli-plugins\docker-scout.exe

Server:
 Containers: 2
  Running: 2
  Paused: 0
  Stopped: 0
 Images: 2
 Server Version: 29.7.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Discovered Devices:
  cdi: docker.com/gpu=webgpu
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 nvidia runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: e53c7c1516c3b2bff98eb76f1f4117477e6f4e66
 runc version: v1.3.6-0-g491b69ba
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.6.87.2-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 8
 Total Memory: 5.635GiB
 Name: docker-desktop
 ID: 0c1a5c3b-e796-4567-a874-a13a03e1c38f
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http.docker.internal:3128
 HTTPS Proxy: http.docker.internal:3128
 No Proxy: hubproxy.docker.internal
 Labels:
  com.docker.desktop.address=npipe://\\.\pipe\docker_cli
 Experimental: false
 Insecure Registries:
  hubproxy.docker.internal:5555
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Firewall Backend: iptables

PS D:\College\CBAD\Mini Project\dockerized-todo> docker build -t todo-app .
[+] Building 17.8s (11/11) FINISHED                                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                             0.0s
 => => transferring dockerfile: 199B                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                              3.4s
 => [auth] library/python:pull token for registry-1.docker.io                                                    0.0s
 => [internal] load .dockerignore                                                                                0.0s
 => => transferring context: 159B                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9  0.0s
 => [internal] load build context                                                                                0.0s
 => => transferring context: 12.24kB                                                                             0.0s
 => CACHED [2/5] WORKDIR /app                                                                                    0.0s
 => [3/5] COPY requirements.txt .                                                                                0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                    11.6s
 => [5/5] COPY . .                                                                                               0.1s
 => exporting to image                                                                                           2.4s
 => => exporting layers                                                                                          1.5s
 => => exporting manifest sha256:18b9d385afe4a44faf627e084e4eebc7bea363d8408fa40b99cb7e68e4ef8dfd                0.0s
 => => exporting config sha256:c12036da38534fe3187b6f75bc37751e6bf1db7d8bf819899b15d5ace17c981b                  0.0s
 => => exporting attestation manifest sha256:4c45007cb1063b9ad90b57771826497a24f519a31195500c022f92a5755b635f    0.0s
 => => exporting manifest list sha256:6de7e3cd611c4fd3a21b131b068179c3cb2cd27750a4dc81b7ca7b5c26096ed0           0.0s
 => => naming to docker.io/library/todo-app:latest                                                               0.0s
 => => unpacking to docker.io/library/todo-app:latest                                                            0.7s
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE                         ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:7                       b6421fd6d1c5       1.18GB          299MB    U   
todo-app:1.0                  ff7e75068a43        209MB         51.2MB        
todo-app:latest               6de7e3cd611c        209MB         51.2MB        
zeeshanwasim12/todo-app:1.0   ff7e75068a43        209MB         51.2MB        
PS D:\College\CBAD\Mini Project\dockerized-todo> docker history todo-app
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
6de7e3cd611c   39 seconds ago   CMD ["python" "app.py"]                         0B        buildkit.dockerfile.v0
<missing>      39 seconds ago   EXPOSE [5000/tcp]                               0B        buildkit.dockerfile.v0
<missing>      39 seconds ago   COPY . . # buildkit                             45.1kB    buildkit.dockerfile.v0
<missing>      39 seconds ago   RUN /bin/sh -c pip install --no-cache-dir -r…   15.3MB    buildkit.dockerfile.v0
<missing>      50 seconds ago   COPY requirements.txt . # buildkit              12.3kB    buildkit.dockerfile.v0
<missing>      16 hours ago     WORKDIR /app                                    8.19kB    buildkit.dockerfile.v0
<missing>      30 hours ago     CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      30 hours ago     RUN /bin/sh -c set -eux;  for src in idle3 p…   16.4kB    buildkit.dockerfile.v0
<missing>      30 hours ago     RUN /bin/sh -c set -eux;   savedAptMark="$(a…   41.4MB    buildkit.dockerfile.v0
<missing>      30 hours ago     ENV PYTHON_SHA256=5c8462af5790baf43a321a1559…   0B        buildkit.dockerfile.v0
<missing>      30 hours ago     ENV PYTHON_VERSION=3.12.14                      0B        buildkit.dockerfile.v0
<missing>      30 hours ago     ENV GPG_KEY=7169605F62C751356D054A26A821E680…   0B        buildkit.dockerfile.v0
<missing>      30 hours ago     RUN /bin/sh -c set -eux;  apt-get update;  a…   13.2MB    buildkit.dockerfile.v0
<missing>      30 hours ago     ENV LANG=C.UTF-8                                0B        buildkit.dockerfile.v0
<missing>      30 hours ago     ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      9 days ago       # debian.sh --arch 'amd64' out/ 'trixie' '@1…   87.5MB    debuerreotype 0.17
PS D:\College\CBAD\Mini Project\dockerized-todo> docker run -d --name todo-container -p 5000:5000 todo-app

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
docker: Error response from daemon: Conflict. The container name "/todo-container" is already in use by container "edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                       PORTS                                             NAMES
edb127bc313a   7f3c2055332e   "python app.py"          16 hours ago   Exited (255) 3 minutes ago   0.0.0.0:5000->5000/tcp                            todo-container
54c8b99e245c   mongo:7        "docker-entrypoint.s…"   11 days ago    Up 3 minutes                 0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker start todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker logs todo-container
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 412-290-415
172.17.0.1 - - [01/Sep/2026 14:03:09] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:09] "GET /static/style.css HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:09] "GET /static/script.js HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:09] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:09] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [01/Sep/2026 14:03:12] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:12] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:03:12] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:03:12] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:13] "POST /delete/1 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:13] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:14] "POST /delete/2 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:14] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:14] "POST /delete/3 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:03:14] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:17:45] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:17:45] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:17:45] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:17:45] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:17:59] "POST /add HTTP/1.1" 201 -
172.17.0.1 - - [01/Sep/2026 14:17:59] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:01] "POST /complete/4 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:01] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:04] "POST /complete/4 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:04] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:18] "POST /add HTTP/1.1" 201 -
172.17.0.1 - - [01/Sep/2026 14:18:18] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:36] "POST /complete/4 HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:18:36] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:21:38] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [01/Sep/2026 14:21:38] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:21:38] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [01/Sep/2026 14:21:38] "GET /api/tasks HTTP/1.1" 200 -
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 198-098-080
172.17.0.1 - - [02/Sep/2026 06:00:45] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:45] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:45] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:46] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:46] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [02/Sep/2026 06:00:47] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:47] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:47] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:47] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:48] "GET /api/tasks HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:50] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Sep/2026 06:00:50] "GET /static/style.css HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:50] "GET /static/script.js HTTP/1.1" 304 -
172.17.0.1 - - [02/Sep/2026 06:00:50] "GET /api/tasks HTTP/1.1" 200 -
PS D:\College\CBAD\Mini Project\dockerized-todo> docker exec -it todo-container /bin/sh
# ls
Dockerfile  app.py  docker-compose.yml  requirements.txt  static  templates
# exit

What's next:
    Try Docker Debug for seamless, persistent debugging tools in any container or image → docker debug todo-container
    Learn more at https://docs.docker.com/go/debug-cli/
PS D:\College\CBAD\Mini Project\dockerized-todo> docker inspect todo-container
[
    {
        "Id": "edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214",
        "Created": "2026-09-01T14:03:02.192656277Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 664,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2026-09-02T06:00:39.584103562Z",
            "FinishedAt": "2026-09-02T05:56:28.897167891Z"
        },
        "Image": "sha256:7f3c2055332ea47d0d6f9beea41e040627ecda527be35bcfd1c9beed65ae3853",
        "ResolvConfPath": "/var/lib/docker/containers/edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214/hostname",
        "HostsPath": "/var/lib/docker/containers/edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214/hosts",
        "LogPath": "/var/lib/docker/containers/edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214/edb127bc313a24a89f1da6b3241325e49ec1776c5c5d253250fa951c1910e214-json.log",
        "Name": "/todo-container",
        "RestartCount": 0,
        "Driver": "overlayfs",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "5000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                11,
                118
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/acpi",
                "/proc/asound",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/sys/devices/virtual/powercap",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "Storage": {
            "RootFS": {
                "Snapshot": {
                    "Name": "overlayfs"
                }
            }
        },
        "Mounts": [],
        "Config": {
            "Hostname": "edb127bc313a",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "5000/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.12.14",
                "PYTHON_SHA256=5c8462af5790baf43a321a1559dbe0db06d1be4300fb85fb53c40060668e548a"
            ],
            "Cmd": [
                "python",
                "app.py"
            ],
            "Image": "todo-app:1.0",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "SandboxID": "abd2ab5055a9a58d1ae20f186dd9ceaa18c9a1d0e72cb82947ed1b1045ebe388",
            "SandboxKey": "/var/run/docker/netns/abd2ab5055a9",
            "Ports": {
                "5000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "5000"
                    }
                ]
            },
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "b9fb97a53c65d14f79d37d8f140deef943fbf5399104aeb3a8ba3fc4387f5ce0",
                    "EndpointID": "12189fb020ed76c0eca1f7642c4ebb1c8b6432ba0c1db451cd4468c41dfea50a",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "MacAddress": "92:8b:f1:85:0d:d3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:94cbc89ee71a6529dbc1582b7ed376c60055e5d70e915097cf4c5dc7b77b1660",
            "size": 1811,
            "platform": {
                "architecture": "amd64",
                "os": "linux"
            }
        }
    }
]
PS D:\College\CBAD\Mini Project\dockerized-todo> docker port todo-container
5000/tcp -> 0.0.0.0:5000
5000/tcp -> [::]:5000
PS D:\College\CBAD\Mini Project\dockerized-todo> docker stop todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS         PORTS                                             NAMES
54c8b99e245c   mongo:7   "docker-entrypoint.s…"   11 days ago   Up 6 minutes   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                      PORTS                                             NAMES
edb127bc313a   7f3c2055332e   "python app.py"          16 hours ago   Exited (0) 13 seconds ago                                                     todo-container
54c8b99e245c   mongo:7        "docker-entrypoint.s…"   11 days ago    Up 6 minutes                0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker start todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS         PORTS                                             NAMES
edb127bc313a   7f3c2055332e   "python app.py"          16 hours ago   Up 3 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp       todo-container
54c8b99e245c   mongo:7        "docker-entrypoint.s…"   11 days ago    Up 6 minutes   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker pause todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                   PORTS                                             NAMES
edb127bc313a   7f3c2055332e   "python app.py"          16 hours ago   Up 19 seconds (Paused)   0.0.0.0:5000->5000/tcp                            todo-container
54c8b99e245c   mongo:7        "docker-entrypoint.s…"   11 days ago    Up 7 minutes             0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker unpause todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker stop todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker rm-todo-container
docker: unknown command: docker rm-todo-container

Run 'docker --help' for more information
PS D:\College\CBAD\Mini Project\dockerized-todo> docker rm todo-container
todo-container
PS D:\College\CBAD\Mini Project\dockerized-todo> docker compose up --build
#1 [internal] load local bake definitions
#1 reading from stdin 561B done
#1 DONE 0.0s

#2 [internal] load build definition from Dockerfile
#2 transferring dockerfile: 199B 0.0s done
#2 DONE 0.0s

#3 [auth] library/python:pull token for registry-1.docker.io
#3 DONE 0.0s

#4 [internal] load metadata for docker.io/library/python:3.12-slim
#4 DONE 2.2s

#5 [internal] load .dockerignore
#5 transferring context: 159B 0.0s done
#5 DONE 0.0s

#6 [internal] load build context
#6 transferring context: 330B done
#6 DONE 0.0s

#7 [1/5] FROM docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea
#7 resolve docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea 0.0s done
#7 DONE 0.0s

#8 [4/5] RUN pip install --no-cache-dir -r requirements.txt
#8 CACHED

#9 [2/5] WORKDIR /app
#9 CACHED

#10 [3/5] COPY requirements.txt .
#10 CACHED

#11 [5/5] COPY . .
#11 CACHED

#12 exporting to image
#12 exporting layers done
#12 exporting manifest sha256:d809954263ede0caeac599fe03565d94913b11b160d8d64c6721bad6ad5ba83b 0.0s done
#12 exporting config sha256:c7657a6696baa3f7f9fa7aff118db60bdcb80a44d0ed0c92014e144bf05c9f2e
#12 exporting config sha256:c7657a6696baa3f7f9fa7aff118db60bdcb80a44d0ed0c92014e144bf05c9f2e 0.0s done
#12 exporting attestation manifest sha256:26ea9dd2c54c19341c134e58d76c023798aa01d60545cedf0cbc152c22ee98ea 0.0s done
#12 exporting manifest list sha256:23bcef428b8da56fde0d382426095e9410878f59b66d32948a0ad66f476f375b 0.0s done
#12 naming to docker.io/library/todo-app:1.0 done
#12 unpacking to docker.io/library/todo-app:1.0 0.0s done
#12 DONE 0.2s

#13 resolving provenance for metadata file
#13 DONE 0.0s
[+] up 2/2
 ✔ Image todo-app:1.0       Built                                                                                 3.1s
 ✔ Container todo-container Created                                                                               0.1s
Attaching to todo-container
todo-container  |  * Serving Flask app 'app'
todo-container  |  * Debug mode: on
todo-container  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
todo-container  |  * Running on all addresses (0.0.0.0)
todo-container  |  * Running on http://127.0.0.1:5000
todo-container  |  * Running on http://172.18.0.2:5000
todo-container  | Press CTRL+C to quit
todo-container  |  * Restarting with stat
todo-container  |  * Debugger is active!
todo-container  |  * Debugger PIN: 474-037-842
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:04:57] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:04:57] "GET /static/style.css HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:04:57] "GET /static/script.js HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:04:58] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:00] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:01] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:01] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:01] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:01] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:02] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:02] "GET /static/style.css HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:02] "GET /static/script.js HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:02] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /api/tasks HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET / HTTP/1.1" 200 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/style.css HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /static/script.js HTTP/1.1" 304 -
todo-container  | 172.18.0.1 - - [02/Sep/2026 06:05:03] "GET /api/tasks HTTP/1.1" 200 -
PS D:\College\CBAD\Mini Project\dockerized-todo> docker compose down
[+] down 2/2
 ✔ Container todo-container        Removed                                                                        0.5s
 ✔ Network dockerized-todo_default Removed                                                                        0.3s
PS D:\College\CBAD\Mini Project\dockerized-todo> docker build -t todo-app .
[+] Building 1.5s (10/10) FINISHED                                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                             0.0s
 => => transferring dockerfile: 199B                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                              1.1s
 => [internal] load .dockerignore                                                                                0.0s
 => => transferring context: 159B                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9  0.0s
 => [internal] load build context                                                                                0.0s
 => => transferring context: 330B                                                                                0.0s
 => CACHED [2/5] WORKDIR /app                                                                                    0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                         0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                              0.0s
 => CACHED [5/5] COPY . .                                                                                        0.0s
 => exporting to image                                                                                           0.1s
 => => exporting layers                                                                                          0.0s
 => => exporting manifest sha256:18b9d385afe4a44faf627e084e4eebc7bea363d8408fa40b99cb7e68e4ef8dfd                0.0s
 => => exporting config sha256:c12036da38534fe3187b6f75bc37751e6bf1db7d8bf819899b15d5ace17c981b                  0.0s
 => => exporting attestation manifest sha256:93626dd54fa3cd5181a3c2abdd9aebef7b9102467541b3eb28c81d690cde7902    0.0s
 => => exporting manifest list sha256:07f9a223aca235784819139796d116f233a5c00aefc5e2d0479a9eb09c29012b           0.0s
 => => naming to docker.io/library/todo-app:latest                                                               0.0s
 => => unpacking to docker.io/library/todo-app:latest                                                            0.0s
PS D:\College\CBAD\Mini Project\dockerized-todo> docker login
Authenticating with existing credentials... [Username: zeeshanwasim12]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
PS D:\College\CBAD\Mini Project\dockerized-todo> docker tag todo-app zeeshanwasim12/todo-app:1.0
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE                         ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:7                       b6421fd6d1c5       1.18GB          299MB    U   
todo-app:1.0                  23bcef428b8d        209MB         51.2MB        
todo-app:latest               07f9a223aca2        209MB         51.2MB        
zeeshanwasim12/todo-app:1.0   07f9a223aca2        209MB         51.2MB        
PS D:\College\CBAD\Mini Project\dockerized-todo> docker push zeeshanwasim12/todo-app:1.0
The push refers to repository [docker.io/zeeshanwasim12/todo-app]
58271ffe9341: Pushed 
44136fa355b3: Already exists 
dbd0b7849e6c: Layer already exists 
6310eb16bf42: Layer already exists 
1560cfed01dc: Layer already exists 
56235e424563: Layer already exists 
f11ea0d01df4: Layer already exists 
34adf8adef00: Pushed 
82b875c851b8: Pushed 
29cb3dc1d3a6: Pushed 
1.0: digest: sha256:07f9a223aca235784819139796d116f233a5c00aefc5e2d0479a9eb09c29012b size: 856
PS D:\College\CBAD\Mini Project\dockerized-todo> docker pull zeeshanwasim/todo-app:1.0
Error response from daemon: pull access denied for zeeshanwasim/todo-app, repository does not exist or may require 'docker login'
PS D:\College\CBAD\Mini Project\dockerized-todo> docker pull zeeshanwasim/todo-app:1.0
Error response from daemon: pull access denied for zeeshanwasim/todo-app, repository does not exist or may require 'docker login'
PS D:\College\CBAD\Mini Project\dockerized-todo> docker login
Authenticating with existing credentials... [Username: zeeshanwasim12]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE                         ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:7                       b6421fd6d1c5       1.18GB          299MB    U   
todo-app:1.0                  23bcef428b8d        209MB         51.2MB        
todo-app:latest               07f9a223aca2        209MB         51.2MB        
zeeshanwasim12/todo-app:1.0   07f9a223aca2        209MB         51.2MB        
PS D:\College\CBAD\Mini Project\dockerized-todo> docker tag todo-app zeeshanwasim/todo-app:1.0
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE                         ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:7                       b6421fd6d1c5       1.18GB          299MB    U   
todo-app:1.0                  23bcef428b8d        209MB         51.2MB        
todo-app:latest               07f9a223aca2        209MB         51.2MB        
zeeshanwasim/todo-app:1.0     07f9a223aca2        209MB         51.2MB        
zeeshanwasim12/todo-app:1.0   07f9a223aca2        209MB         51.2MB        
PS D:\College\CBAD\Mini Project\dockerized-todo> docker pull zeeshanwasim/todo-app:1.0
Error response from daemon: pull access denied for zeeshanwasim/todo-app, repository does not exist or may require 'docker login'
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS          PORTS                                             NAMES
54c8b99e245c   mongo:7   "docker-entrypoint.s…"   11 days ago   Up 13 minutes   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   campusone-mongo
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE                         ID             DISK USAGE   CONTENT SIZE   EXTRA
mongo:7                       b6421fd6d1c5       1.18GB          299MB    U   
todo-app:1.0                  23bcef428b8d        209MB         51.2MB        
todo-app:latest               07f9a223aca2        209MB         51.2MB        
zeeshanwasim/todo-app:1.0     07f9a223aca2        209MB         51.2MB        
zeeshanwasim12/todo-app:1.0   07f9a223aca2        209MB         51.2MB        
PS D:\College\CBAD\Mini Project\dockerized-todo> docker rm -f $(docker ps -aq)
54c8b99e245c
PS D:\College\CBAD\Mini Project\dockerized-todo> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images -q | ForEach-Object { docker rmi -f $_ }
Untagged: todo-app:latest
Untagged: zeeshanwasim/todo-app:1.0
Untagged: zeeshanwasim12/todo-app:1.0
Deleted: sha256:07f9a223aca235784819139796d116f233a5c00aefc5e2d0479a9eb09c29012b
Error response from daemon: No such image: 07f9a223aca2:latest
Error response from daemon: No such image: 07f9a223aca2:latest
Untagged: todo-app:1.0
Deleted: sha256:23bcef428b8da56fde0d382426095e9410878f59b66d32948a0ad66f476f375b
Untagged: mongo:7
Deleted: sha256:b6421fd6d1c5ded6377b397d8983e2f82e2100dc5123332dcfda2065a472be5b
PS D:\College\CBAD\Mini Project\dockerized-todo> docker images
                                                                                                  i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
PS D:\College\CBAD\Mini Project\dockerized-todo> docker system prune -a
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Images:
untagged: sha256:ff7e75068a43a3f13f4a5a4be060b3d824d36d43e84422a8bd54052b94f2326b
deleted: sha256:ff7e75068a43a3f13f4a5a4be060b3d824d36d43e84422a8bd54052b94f2326b
deleted: sha256:c63afb31e9b01b69d8fe24097a12916259494b4003dd15d655ebcb4d8ca416d9
deleted: sha256:89024470dd7795b71c3c67ad21ba85f1647824a03e119b73518a5eafc75efab1

Deleted build cache objects:
w8x5dyml8nhoviec3rmlrahg4
zrimudexslbft2srwg0cl4gou
7shps7tcsz3rclbrqpad55tok
se3v8ih6rnr8zj3af91rbc2k3
4gskjxuialed5sz2udh097dd7
qoovjz2zxnv3o54chn4waalnm
n8at2e2tha6wn4da0af9a4txd
s77uuzg0wtvchrnnvlilfjfxi
h1b8vy3ruywauahqfacxz9wv6
wejkwmba2ynvfier00zcu224n
hxrjcg1nbctbc7imezg3as5ir
z9z9r5waclz3uss9o3fyfsa0o
rh6hz7l2tfaqeog4d3ibahmot
va337b5dntcxknmly6npm6oxm

Total reclaimed space: 244.8MB
PS D:\College\CBAD\Mini Project\dockerized-todo> 