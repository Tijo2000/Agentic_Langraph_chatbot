#Agentic_Langraph_chatbot
#Built using langraph , fast api and stream lit
#Hosted on streamlit : https://tijo-langchat.streamlit.app/

/n
(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker build -t docker build -t langgraph-streamlit-app .
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker build -t langgraph-streamlit-app .                
[+] Building 129.4s (10/10) FINISHED                                                                  docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                  0.1s
 => => transferring dockerfile: 544B                                                                                  0.0s 
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                    4.6s 
 => [auth] library/python:pull token for registry-1.docker.io                                                         0.0s
 => [internal] load .dockerignore                                                                                     0.1s
 => => transferring context: 2B                                                                                       0.0s 
 => [internal] load build context                                                                                     0.3s 
 => => transferring context: 42.88kB                                                                                  0.2s 
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:bb8009c87ab69e751a1dd2c6c7f8abaae3d9fce8e072802d4a23c95594d  22.9s 
 => => resolve docker.io/library/python:3.9-slim@sha256:bb8009c87ab69e751a1dd2c6c7f8abaae3d9fce8e072802d4a23c95594d1  0.0s
 => => sha256:c876ae22765e4a125855eb121718c3f8f07bd8b00dae0ad4e68e716571961f37 249B / 249B                            0.2s
 => => sha256:4f4cb1a24c66f1a92f204ba0bbd6d2a7c941a853c83161ffa38bbfa121448861 14.93MB / 14.93MB                      6.8s 
 => => sha256:1da0723265ec311debcf6bec17d4fae5f1e5f7809fca4378aac265cdef238f1c 3.51MB / 3.51MB                        3.0s
 => => sha256:af302e5c37e9dc1dbe2eadc8f5059d82a914066b541b0d1a6daa91d0cc55057d 28.21MB / 28.21MB                     21.6s 
 => => extracting sha256:af302e5c37e9dc1dbe2eadc8f5059d82a914066b541b0d1a6daa91d0cc55057d                             0.6s 
 => => extracting sha256:1da0723265ec311debcf6bec17d4fae5f1e5f7809fca4378aac265cdef238f1c                             0.1s 
 => => extracting sha256:4f4cb1a24c66f1a92f204ba0bbd6d2a7c941a853c83161ffa38bbfa121448861                             0.3s 
 => => extracting sha256:c876ae22765e4a125855eb121718c3f8f07bd8b00dae0ad4e68e716571961f37                             0.0s 
 => [2/4] COPY . /app/                                                                                                0.1s
 => [3/4] WORKDIR /app                                                                                                0.1s 
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                         74.8s 
 => exporting to image                                                                                               26.5s 
 => => exporting layers                                                                                              21.6s 
 => => exporting manifest sha256:786af94b51c6c3f6a8f8b74024604121396ffe143575166f1929a40f6ce04d63                     0.0s 
 => => exporting config sha256:79ec081d0c228c170aa23c0b3cb08c832de7c070b86ff3b8ed09298e74466734                       0.0s 
 => => exporting attestation manifest sha256:83cfc1fe7570418107ea49b7bc64656092c971af7979a8a5b8ebeb42581b9314         0.0s 
 => => exporting manifest list sha256:03a4323e241da09a3fbd9f901b9ae5abecb8a693bd15a1d1d246014adf9fddef                0.0s 
 => => naming to docker.io/library/langgraph-streamlit-app:latest                                                     0.0s 
 => => unpacking to docker.io/library/langgraph-streamlit-app:latest                                                  4.8s 

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker run -d -p 8000:8000 -p 8501:8
501 --name langgraph-streamlit-container langgraph-streamlit-app .
ecc36d31b7b7112f0b0b5416047ad870c0e98287104df85234599597e51ccbb4
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: ".": executable file not found in $PATH: unknown.        

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker run -d -p 8000:8000 -p 8501:8501 --name langgraph-streamlit-container langgraph-streamlit-app
docker: Error response from daemon: Conflict. The container name "/langgraph-streamlit-container" is already in use by container "ecc36d31b7b7112f0b0b5416047ad870c0e98287104df85234599597e51ccbb4". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker rm -f langgraph-streamlit-container
langgraph-streamlit-container

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker run -d -p 8000:8000 -p 8501:8501 --name langgraph-streamlit-container langgraph-streamlit-app
5db760b740932943b413ee7cb55274aed4b27ba799b8c55afdda0d07e3fa38b4

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker login
Authenticating with existing credentials...
Login Succeeded

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker tag langgraph-streamlit-app Tijo001/langgraph-streamlit-app:latest  

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker push Tijo001/langgraph-streamlit-app:latest
The push refers to repository [Tijo001/langgraph-streamlit-app]
47ac7dc13aee: Waiting
af302e5c37e9: Waiting
1da0723265ec: Waiting
4f4fb700ef54: Waiting
597790b2e14a: Waiting
0c045ed10513: Waiting
4f4cb1a24c66: Waiting
c876ae22765e: Waiting
failed to do request: Head "https://Tijo001/v2/langgraph-streamlit-app/blobs/sha256:47ac7dc13aee18eb53a8476d06aed103f3e29775cc55695d1b67fddb60b9d51d": dialing Tijo001:443 container via direct connection because static system has no HTTPS proxy: connecting to Tijo001:443: dial tcp: lookup Tijo001: no such host

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker tag langgraph-streamlit-app docker.io/Tijo001/langgraph-streamlit-app:latest
Error parsing reference: "docker.io/Tijo001/langgraph-streamlit-app:latest" is not a valid repository/tag: invalid reference format: repository name (Tijo001/langgraph-streamlit-app) must be lowercase

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker tag langgraph-streamlit-app docker.io/tijo001/langgraph-streamlit-app:latest 

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker push docker.io/Tijo001/langgraph-streamlit-app:latest
invalid reference format: repository name (Tijo001/langgraph-streamlit-app) must be lowercase

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker push docker.io/tijo001/langgraph-streamlit-app:latest  
The push refers to repository [docker.io/tijo001/langgraph-streamlit-app]
c876ae22765e: Pushed
0c045ed10513: Pushed
597790b2e14a: Pushed
4f4cb1a24c66: Pushed
47ac7dc13aee: Pushed
af302e5c37e9: Pushed
4f4fb700ef54: Pushed
1da0723265ec: Pushed
latest: digest: sha256:03a4323e241da09a3fbd9f901b9ae5abecb8a693bd15a1d1d246014adf9fddef size: 856

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker pull tijo001/langgraph-streamlit-app       
Using default tag: latest
latest: Pulling from tijo001/langgraph-streamlit-app
Digest: sha256:03a4323e241da09a3fbd9f901b9ae5abecb8a693bd15a1d1d246014adf9fddef
Status: Image is up to date for tijo001/langgraph-streamlit-app:latest
docker.io/tijo001/langgraph-streamlit-app:latest

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker run -d -p 8000:8000 -p 8501:8501 --name new langgraph-streamlit-container tijo001/langgraph-streamlit-app                          
Unable to find image 'langgraph-streamlit-container:latest' locally
require 'docker login'.
See 'docker run --help'.

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker run -d -p 8000:8000 -p 8501:8501 --name new_langgraph-streamlit-container tijo001/langgraph-streamlit-app
9b27867a2f7459f1248df2ada119eb2f3944801806e67e73cd9a070d98f8b9c8

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                                            NAMES    
9b27867a2f74   tijo001/langgraph-streamlit-app   "sh -c 'uvicorn app:…"   9 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp, 0.0.0.0:8501->8501/tcp   new_langgraph-streamlit-container

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Dockerfile
        app.py
        requirements.txt
        ui.py

nothing added to commit but untracked files present (use "git add" to track)

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>git add .

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>git commit -m "First commit" 
[main 9182a99] First commit
 4 files changed, 133 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 app.py
 create mode 100644 requirements.txt
 create mode 100644 ui.py

(langchat) D:\Data Science Projects\Agentic Langraph chat bot\Agentic_Langraph_chatbot>git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.93 KiB | 2.93 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Tijo2000/Agentic_Langraph_chatbot.git
   7686522..9182a99  main -> main
