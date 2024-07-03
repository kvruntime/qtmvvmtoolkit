FROM python:3.10-slim-bullseye as dev

RUN apt-get update && apt-get install -y \
    python3-pil python3-tk \
    python3-pil.imagetk libgl1-mesa-dev \
    "libxkbcommon*" "libglib*" "xcb*" "libxcb*"