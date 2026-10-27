const express = require('express');

const app = express();
app.use(express.static("frontend"));

app.listen(3000);
Console.log("Running on port 3000...");
