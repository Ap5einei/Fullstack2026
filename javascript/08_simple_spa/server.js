const express = require('express');

const app = express();

app.use("/",express.static("frontend"));

app.use(express.json());

//DATABASE

let database = [];
let id = 100;