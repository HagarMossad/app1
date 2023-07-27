data = {
    "custom_fields": {
        "Item": [
            {
                "fieldname": "code",
                "fieldtype": "Data",
                "insert_after": "item_name",
                "label": "Code"
            },
            {
                "fieldname": "barcode",
                "fieldtype": "Barcode",
                "insert_after": "code",
                "label": "Barcode"
            }
        ],
    },
}
