# 🩸 The Blood (Injector)

> **Role**: Injector / Logistics
> **JADC2 Mapping**: Logistics
> **Gherkin Source**: `brain/gen50_core.feature`

## 🧬 Biological Function
The **Blood** handles **Logistics** and **Resources**. It provisions the environment, manages dependencies, spins up containers, and ensures the "nutrients" (compute/storage) are available for the Hands to work.

## 📂 Contents
*   **Setup Scripts**: `setup_env.sh`, `setup_hybrid.sh`.
*   **Infrastructure**: Docker configurations, Ray cluster setup.
*   **Dependency Management**: `requirements.txt` handling.

## 🤖 Agent Instructions
*   **Flow**: Keep the system running smoothly.
*   **Provision**: Ensure resources are available before agents start.
