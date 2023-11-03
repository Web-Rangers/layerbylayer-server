FROM ubuntu:latest
LABEL authors="bel"

ENTRYPOINT ["top", "-b"]