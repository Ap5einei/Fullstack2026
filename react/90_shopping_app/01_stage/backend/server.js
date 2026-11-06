require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const shoppingRoute = require("./routes/shoppingroute");

const app = express();

app.use(express.json());

const mongo_user = process.env.MONGODB_USER;
const mongo_password = process.env.MONGODB_PASSWORD;

const url = "mongodb+srv://" + mongo_user + ":" + mongo_password + "@devben.egqvjjs.mongodb.net/local_contact_db?retryWrites=true&w=majority";

mongoose.connect(url).then(
	() => console.log("Connected to Mongodb"),
	(err) => console.log("Failed to connect to Mongodb. Reason",err)
)

app.use("/api",shoppingRoute);

app.listen(3000);

console.log("Running in port 3000");