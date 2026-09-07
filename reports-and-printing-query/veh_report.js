// Copyright (c) 2026, Moulis and contributors
// For license information, please see license.txt

frappe.query_reports["veh_report"] = {
    filters: [
        {
            fieldname: "vehicle",
            label: "Vehicle",
            fieldtype: "Link",
            options: "Vehicle"
        }
    ]
};
