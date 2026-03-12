import frappe

def execute():
    # Fetch the document, set defaults if they are 0 or not set
    doc = frappe.get_single("Smart Attendance Settings")
    
    updated = False
    
    if getattr(doc, "texture_score_limit", 0) == 0:
        doc.texture_score_limit = 8.0
        updated = True
        
    if getattr(doc, "organic_variance_limit", 0) == 0:
        doc.organic_variance_limit = 0.20
        updated = True
        
    if getattr(doc, "digital_grid_sharpness", 0) == 0:
        doc.digital_grid_sharpness = 0.25
        updated = True
        
    if getattr(doc, "match_tolerance", 0) == 0:
        doc.match_tolerance = 0.52
        updated = True
        
    if getattr(doc, "cooldown_seconds", 0) == 0:
        doc.cooldown_seconds = 10
        updated = True
        
    if updated:
        doc.save(ignore_permissions=True)
        frappe.db.commit()
    print("Defaults set!")
