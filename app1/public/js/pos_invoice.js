frappe.ui.form.on("POS Invoice", {

}),

frappe.ui.form.on("POS Invoice Item", {
    item_code(frm, cdt , cdn){
        let item = locals[cdt][cdn]
        if(item.item_code){
            item.use_serial_batch_fields = 1
        }
        

    }

})