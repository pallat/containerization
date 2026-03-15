# Build stage
FROM debian:stable-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmicrohttpd-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY main.c ./

RUN mkdir -p /app && gcc main.c -o /app/server -lmicrohttpd

# Runtime stage
FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libmicrohttpd12 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/server /app/server
WORKDIR /app

EXPOSE 8888
ENTRYPOINT ["/app/server"]
