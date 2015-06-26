db.products.aggregate([
    {$group:
        {_id:"$category",
        num_products:{$sum:1}
        }
    }
])