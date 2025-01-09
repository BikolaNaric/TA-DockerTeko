FROM golang:1.20
WORKDIR /app
COPY . .
RUN go build -o stock-publisher
FROM golang:1.20
WORKDIR /app
COPY . .
RUN go build -o stock-publisher
CMD ["./stock-publisher"]
