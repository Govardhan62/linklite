import frappe

from frappe.website.path_resolver import resolve_path as original_resolve_path

def path_resolver(path: str):
    #if we want to handle the short link
    #frappe.redirect("https://www.google.com/")
    if frappe.db.exists("ShortLink", {"short_link":path}):
        #we want to redirect
        short_link =frappe.db.get_value("ShortLink",{"short_link":path}, ["destination_url", "name"], as_dict=True )

        click =frappe.new_doc("Short Link Click")

        request_headers =frappe.request.headers
        click.ip =request_headers.get("X-Real-IP")
        click.user_agent =request_headers.get("User-Agent")
        click.referer =request_headers.get("Referer")

        click.link =short_link.name
        click.insert().submit()
        frappe.db.commit() #TO REMOVE ONCE  MYISAM


        frappe.redirect(short_link.destination_url)


    #else pass it on!
    return original_resolve_path(path)
