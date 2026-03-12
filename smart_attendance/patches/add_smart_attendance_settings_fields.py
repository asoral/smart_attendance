import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Smart Attendance Settings": [
            {
                "fieldname": "anti_spoofing_section",
                "fieldtype": "Section Break",
                "label": "Anti-Spoofing & Matching",
                "insert_after": "colour_mode"
            },
            {
                "fieldname": "texture_score_limit",
                "fieldtype": "Float",
                "label": "Texture Score Limit",
                "default": "8.0",
                "description": "Lower means more relaxed texture checking.",
                "insert_after": "anti_spoofing_section"
            },
            {
                "fieldname": "organic_variance_limit",
                "fieldtype": "Float",
                "label": "Organic Variance Limit",
                "default": "0.20",
                "description": "Lower means more relaxed lighting check.",
                "insert_after": "texture_score_limit"
            },
            {
                "fieldname": "digital_grid_sharpness",
                "fieldtype": "Float",
                "label": "Digital Grid Sharpness Limit",
                "default": "0.25",
                "description": "Higher means more relaxed screen reflection check.",
                "insert_after": "organic_variance_limit"
            },
            {
                "fieldname": "match_tolerance",
                "fieldtype": "Float",
                "label": "Face Match Tolerance",
                "default": "0.52",
                "description": "Higher number means more tolerant face matching.",
                "insert_after": "digital_grid_sharpness"
            },
            {
                "fieldname": "cooldown_seconds",
                "fieldtype": "Int",
                "label": "Check-in Cooldown Seconds",
                "default": "10",
                "description": "Seconds to wait before a second check-in can be created.",
                "insert_after": "match_tolerance"
            }
        ]
    }
    create_custom_fields(custom_fields)
    
    # After creating fields, ensure the document has default values set, especially if it was already created but fields are 0
    try:
        doc = frappe.get_doc("Smart Attendance Settings")
        updated = False
        
        if doc.texture_score_limit in [0, 0.0, None]:
            doc.texture_score_limit = 8.0
            updated = True
            
        if doc.organic_variance_limit in [0, 0.0, None]:
            doc.organic_variance_limit = 0.20
            updated = True
            
        if doc.digital_grid_sharpness in [0, 0.0, None]:
            doc.digital_grid_sharpness = 0.25
            updated = True
            
        if doc.match_tolerance in [0, 0.0, None]:
            doc.match_tolerance = 0.52
            updated = True
            
        if doc.cooldown_seconds in [0, None]:
            doc.cooldown_seconds = 10
            updated = True
            
        if updated:
            doc.save(ignore_permissions=True)
            frappe.db.commit()
    except Exception:
        pass
