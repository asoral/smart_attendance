import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def add_fields():
    doc = frappe.get_doc("DocType", "Smart Attendance Settings")
    new_fields = [
        {"fieldname": "anti_spoofing_section", "fieldtype": "Section Break", "label": "Anti-Spoofing & Matching"},
        {"fieldname": "texture_score_limit", "fieldtype": "Float", "label": "Texture Score Limit", "default": "8"},
        {"fieldname": "organic_variance_limit", "fieldtype": "Float", "label": "Organic Variance Limit", "default": "0.20"},
        {"fieldname": "digital_grid_sharpness", "fieldtype": "Float", "label": "Digital Grid Sharpness Limit", "default": "0.25"},
        {"fieldname": "match_tolerance", "fieldtype": "Float", "label": "Face Match Tolerance", "default": "0.52"},
        {"fieldname": "cooldown_seconds", "fieldtype": "Int", "label": "Check-in Cooldown Seconds", "default": "10"}
    ]
    
    # Check if they exist
    existing_fields = [f.fieldname for f in doc.fields]
    for field in new_fields:
        if field["fieldname"] not in existing_fields:
            doc.append("fields", field)
            
    doc.save()
    from frappe.modules.export_file import export_to_files
    export_to_files(record_list=[["DocType", "Smart Attendance Settings"]], record_module="Smart Attendance")

if __name__ == "__main__":
    add_fields()
