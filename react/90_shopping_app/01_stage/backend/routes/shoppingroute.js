const express = require("express");
const itemModel = require("../models/item");

const router = express.Router();

// GET: Hae kaikki tuotteet ostoslistalta
router.get("/shopping", function(req, res) {
    itemModel.find().then(function(items) {
        return res.status(200).json(items);
    }).catch(function(err) {
        console.log("Failed in finding items. Reason", err);
        // KORJATTU: Vaihdettu pilkku pisteeksi ennen .json-sanaa
        return res.status(500).json({ "message": "Internal Server Error" });
    });
});

// POST: Lisää uusi tuote ostoslistalle
router.post("/shopping", function(req, res) {
    if (!req.body) {
        return res.status(400).json({ "message": "Bad request" });
    }
    if (!req.body.type) {
        return res.status(400).json({ "message": "Bad request" });
    }
    
    let item = new itemModel({
        type: req.body.type,
        count: req.body.count,
        price: req.body.price
    });
    
    item.save().then(function(savedItem) {
        return res.status(201).json(savedItem);
    }).catch(function(err) {
        console.log("Failed to add new item. Reason", err);
        // KORJATTU: Vaihdettu pilkku pisteeksi ennen .json-sanaa
        return res.status(500).json({ "message": "Internal Server Error" });
    });
});

// DELETE: Poista tuote ID:n perusteella
router.delete("/shopping/:id", function(req, res) {
    itemModel.deleteOne({ "_id": req.params.id }).then(function() {
        return res.status(200).json({ "message": "Success" });
    }).catch(function(err) {
        console.log("Failed to delete item. Reason", err);
        return res.status(500).json({ "message": "Internal Server Error" });
    });
});

// PUT: Muokkaa/korvaa tuote ID:n perusteella
router.put("/shopping/:id", function(req, res) {
    if (!req.body) {
        // KORJATTU: Kirjoitusvirhe "Bad Reques" -> "Bad Request"
        return res.status(400).json({ "message": "Bad Request" });
    }
    if (!req.body.type) {
        return res.status(400).json({ "message": "Bad Request" });
    }
    
    let item = {
        type: req.body.type,
        count: req.body.count,
        price: req.body.price
    };
    
    // KORJATTU: Kirjoitusvirhe repcaleOne -> replaceOne
    itemModel.replaceOne({ "_id": req.params.id }, item).then(function() {
         return res.status(200).json({ "message": "Success" });
    }).catch(function(err) {
        console.log("Failed to edit item. Reason", err);
        return res.status(500).json({ "message": "Internal Server Error" });
    });
});

module.exports = router;
