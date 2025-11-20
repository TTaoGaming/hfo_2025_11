FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install system dependencies for Postgres and Graphviz (for Mermaid/NetworkX)
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client graphviz curl

# Install Temporal CLI
RUN curl -sSf https://temporal.download/cli.sh | sh

# Install Python dependencies
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Set the default shell to bash
ENV SHELL /bin/bash
