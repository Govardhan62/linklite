import frappe

from frappe.website.path_resolver import resolve_path as original_resolve_path

def path_resolver(path: str):
    #if we want to handle the short link
    #frappe.redirect("https://www.google.com/")
    if frappe.db.exists("ShortLink", {"short_link":path}):
        #we want to redirect
        destination =frappe.db.get_value("ShortLink",{"short_link":path},"destination_url")
        frappe.redirect(destination)


    #else pass it on!
    return original_resolve_path(path)
