const fastify = require("fastify")();
const myModule = require("./module.js");

let mySum = myModule.sumNums(1, 2);
console.log(mySum);

fastify.get("/", (request, reply) => {
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
    console.log(err);
    process.exit(1);
  }
  console.log(`Server listening on ${address}`);
});
