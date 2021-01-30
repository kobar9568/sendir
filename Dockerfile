FROM alpine:latest

LABEL maintainer="Ryota Kobayashi <38117745+kobar9568@users.noreply.github.com>"

RUN apk --update add --no-cache \
    git \
    make \
    gcc \
    libc-dev \
    libusb-dev \
    python3 && \
    git clone https://github.com/Drunkar/bto_ir_advanced_cmd.git && \
    cd bto_ir_advanced_cmd/ && \
    make && \
    make install
