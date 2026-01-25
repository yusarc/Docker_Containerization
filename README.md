# Docker_Containerization

This repository contains a simple example of containerizing an application using Docker and Docker Compose.

## What it does

- Builds a Docker image for the application.
- Runs the application inside a container.
- Optionally uses Docker Compose to start containers with a single command.

## Main files

- `Dockerfile`  
  - Defines the base image.  
  - Copies the application source code.  
  - Installs dependencies and configures the entrypoint/command.

- `docker-compose.yml` 
  - Describes how to run one or more services (containers).  
  - Configures ports, environment variables, volumes, etc.

- Application source files (for example `app.py`, `src/`, etc.).

## Build and run with Docker

```bash
# Build the image
docker build -t my-app-image .

# Run the container in the foreground
docker run --rm -p 8080:8080 my-app-image

# Run the container in the background (detached)
docker run -d -p 8080:8080 --name my-app-container my-app-image

# List running containers
docker ps

# Stop and remove the container
docker stop my-app-container
docker rm my-app-container


Run with Docker Compose
bash
# Create and start containers in the background using docker-compose.yml
docker compose up -d

# (Legacy syntax, if needed)
docker-compose up -d

# Stop and remove containers, networks, etc.
docker compose down
