const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Docker CI/CD funcionando correctamente");
});

server.listen(3000, () => {
  console.log("Servidor escuchando en puerto 3000");
});