import frappe

def get_context(context):
    hash = frappe.request.args.get('id')
    context.member = verify_member(hash)
    return context

def verify_member(hash):
    member = frappe.get_all("Member",
        fields=['member_name', 'status', 'designation', 'membership_valid_till', 'club', 'zone', 'dues_paid'], 
        filters={"verification_hash": hash})
    if member:
        return member[0]
    else:
        return None