FROM debian:stable-slim AS base

RUN apt-get update -qq
RUN apt-get install --no-install-recommends -y curl
RUN apt-get install --no-install-recommends -y libjemalloc2
RUN apt-get install --no-install-recommends -y libvips
RUN apt-get install --no-install-recommends -y libpq-dev
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives

CMD ["echo", "Whalecome!"]