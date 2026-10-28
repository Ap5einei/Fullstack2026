const express = require('express');

const app = express();

app.use("/",express.static("frontend"));

app.use(express.json());

//DATABASE

let database = [];
let id = 100;

//REST API (CRUD)
//GET         /api/shopping      get all items
//POST        /api/shopping      post new item
//DELETE      /api/shopping/:id  remove item :id
//PUT         /api/shopping/:id  update item :id

//ITEM
//id Number
//type   String
//count Number
//price Number

//SHOPPING API

app.get("api/shopping",function(req,res) {
    return res.status(200).json(database);
})

app.post("/api/shopping",function(req,res){
    let item ={
        id:id,
        type:req.body.type,
        count:req.body.count,
        price:req.body.price
    }
    id++;
    database.push(itemm);
    return res.status(201).json(item);
})