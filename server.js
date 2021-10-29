const express = require("express");
const helmet = require("helmet");
const morgan = require("morgan");
const fs = require("fs");

const app = express();

app.use(helmet());
app.use(morgan("short"));

// C'est pour le retiré de git

function filterProducts(params) {
    let products = JSON.parse(fs.readFileSync('./amazon.json', {encoding: 'utf8'}));

    if (params?.price) {
        products = products.filter(product => product.prix == params.price)
    }

    if (params?.roundedPrice) {
        products = products.filter(product => Math.round(product.prix) == params.roundedPrice)
    }

    if(params?.search) {
        products = products.filter(product => product.nom.toLowerCase().includes(params.search.toLowerCase()))
    }

    return products
}

app.get('/products', (req, res) => {
    const params = req.query

    const products = filterProducts(params)

    res.json(products)
})

app.get('/products/random', (req, res) => {
    const params = req.query

    const products = filterProducts(params)

    const product = products[Math.floor(Math.random() * products.length)]

    res.json(product)
})

app.listen('6969')