# MLOps Project Makefile
# Usage: make <target>

# Variables
IMAGE_NAME = my-mlops-project
CONTAINER_NAME = mlops-container

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make build     - Build Docker image"
	@echo "  make run       - Run Docker container"
	@echo "  make stop      - Stop running container"
	@echo "  make clean     - Remove containers and images"
	@echo "  make logs      - Show container logs"
	@echo "  make shell     - Open shell in container"
	@echo "  make test      - Run tests"
	@echo "  make install   - Install dependencies locally"

# Build Docker image
.PHONY: build
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .
	@echo "Image built successfully!"

# Run Docker container
.PHONY: run
run:
	@echo "Running Docker container..."
	docker run --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Run container in detached mode
.PHONY: run-detached
run-detached:
	@echo "Running Docker container in background..."
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop running container
.PHONY: stop
stop:
	@echo "Stopping container..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Clean up containers and images
.PHONY: clean
clean:
	@echo "Cleaning up..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME) || true
	@echo "Cleanup completed!"

# Show container logs
.PHONY: logs
logs:
	docker logs $(CONTAINER_NAME)

# Open shell in container
.PHONY: shell
shell:
	docker run -it --rm $(IMAGE_NAME) /bin/bash

# Run tests (if you have tests)
.PHONY: test
test:
	@echo "Running tests..."
	python -m pytest tests/ || echo "No tests found"

# Install dependencies locally
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -e .

# Development setup
.PHONY: dev-setup
dev-setup: install
	@echo "Development setup completed!"
	@echo "Run 'python project/src/main.py' to start the application" 

inst