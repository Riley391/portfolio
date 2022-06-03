const fastify = require("fastify")();
const fs = require("fs");
const { print } = require("./module");

fastify.get("/", (request, reply) => {
    const path = __dirname + "/index.html"
    const stream = fs.createReadStream(path);
    reply
        .code(200)
        .header("Content-Type", "text/html; charset=utf-8")
        .send(stream);
});

fastify.get("/plants", (request, reply) => {
    const path = __dirname + "/ui-ux-demo.html"
    const stream = fs.createReadStream(path);
    reply
        .code(200)
        .header("Content-Type", "text/html; charset=utf-8")
        .send(stream);
});

fastify.get("/search", (request, reply) => {
    reply
        .code(200)
        .header("Content-Type", "text/html; charset=utf-8")
        .send("<h1>Hello World</h1>");
});

fastify.get("*", (request, reply) => {
    reply
        .code(404)
        .header("Content-Type", "application/json; charset=utf-8")
        .send({ status: "Page not found" });
});

const listenIP = "localhost";
const listenPort = 8080;
fastify.listen(listenPort, listenIP, (err, address) => {
    if (err) {
        print(err);
        process.exit(1);
    }
    print(`Server listening on ${address}`);
});
