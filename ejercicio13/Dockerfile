FROM gcc:latest AS builder

WORKDIR /usr/src/app

COPY hello.c .

RUN gcc -static -o hello hello.c

FROM scratch

COPY --from=builder /usr/src/app/hello .

CMD ["/hello"]