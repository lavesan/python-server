const http = require("http");

const options = {
  socketPath: "localhost",
  path: "/login"
};

const callback = res => {
  console.log(`STATUS: ${res.statusCode}`);
  res.setEncoding("utf8");
  res.on("data", data => console.log(data));
  res.on("error", data => console.error(data));
};

const clientRequest = http.request(options, callback);
console.log("rodando o código");
console.log(clientRequest);
clientRequest.end();

document.getElementById("nome").addEventListener("click", function() {
  console.log("cliquei");
});
