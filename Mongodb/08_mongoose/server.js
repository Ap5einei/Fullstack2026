require('dotenv').config();
const express = require("express");
const mongoose = require("mongoose");

const app = express();

//Remote Access to mongo atlas

const mongo_user = process.env.MONGODB_USER;
const mongo_password = process.env.MONGODB_PASSWORD

const url = "mongodb+srv://" + mongo_user + ":" + mongo_password + "@devben.egqvjjs.mongodb.net/local_contact_db?retryWrites=true&w=majority";
//const url = "mongodb://localhost"

// Both version
mongoose.connect(url).then(
    ()=> console.log("Connected to MongoDB"),
    (err) => console.log("Failed To connect to MongoDB.Reson", err)
)
app.listen(3000);
console.log("Running in port 3000");