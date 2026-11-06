const mongoose = require("mongoose");

const Schema = mongoose.Schema({
    type:String,
    count:Number,
    price:Number
})

module.export = mongoose.model("Item",Schema);