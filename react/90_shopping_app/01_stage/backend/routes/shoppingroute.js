const express = require("express");
const itemModel = require("../models/item");



const router = express.Router();

router.get("/shopping",function(req,res){
    itemModel.find().then(function(items){
        return res.status(200).json(items);
    }).catch(function(err){
        console.log("Failed in finding items. Reason",err);
        return res.status(500),json({"message":"Internal Server Error"})
    })
})

router.post("/shopping",function(req,res){
    if(!req.body){
        return res.status(400).json({"message":"Bad request"});
    }
     if(!req.body.type){
        return res.status(400).json({"message":"Bad request"});
    }
    let item = new itemModel({
        type:req.body.type,
        count:req.body.count,
        price:req.body.price
    })
    item.save().then(function(item){
        return res.status(201).json(item);

    }).catch(function(err){
        console.log("Failed to add new item. Reason",err);
        return res.status(500),json({"message":"Internal Server Error"})
    });
})

router.delete("/shopping/:id",function(req,res) {
	itemModel.deleteOne({"_id":req.params.id}).then(function() {
		return res.status(200).json({"message":"Success"});
	}).catch(function(err) {
		console.log("Failed to delete item. Reason",err);
		return res.status(500).json({"message":"Internal Server Error"})
	})
})

router.put("/shopping/:id",function(req,res){
    if(!req.body){
        return res.status(400).json({"message":"Bad Reques"});
    }
    if(!req.body.type){
        return res.status(400).json({"message":"Bad Reques"});
    }
    let item ={
        type:req.body.type,
        count:req.body.count,
        price:req.body.price
    }
    itemModel.repcaleOne({"_id":req.params.id},item).then(function(){
         return res.status(200).json({"message":"Success"});
    }).catch(function(err){
        console.log("Failed to edit itme. Reason",err);
        return res.status(500).json({"message":"Internal Server Error"});
    })
})

module.exports = router;