frappe.ui.form.on('User', {
	refresh(frm) {
		// your code here
		frm.add_custom_button(
		    "Send welcome message",
		    function(){
		        frappe.msgprint("Message Sent!");
		    },
		    "Action"
		    );
	}
});
