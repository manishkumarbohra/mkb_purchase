# Bulk Reset Cancelled Purchase Orders to Draft

Reset multiple cancelled Purchase Orders back to **Draft** in one go from the Purchase Orders list view.

---

## Features

- Adds an **Action ▸ Reset Cancelled POs to Draft** option in the Purchase Orders list view.  
- Select several cancelled purchase orders at once and reset them in bulk.  
- Respects standard Odoo access rights and workflow.  

---

## Compatibility

- Odoo: 19.0  

---

## Dependencies

- `purchase`  
- `purchase_stock` (if you use stock integration)  

---

## Installation

1. Copy this module into your Odoo `addons` path.  
2. Update the app list: **Apps ▸ Update Apps List**.  
3. Install **Bulk Reset Cancelled POs**.  

---

## Usage

1. Go to **Purchase ▸ Orders**.  
2. Switch to the **list** (tree) view.  
3. Select the cancelled Purchase Orders you want to reset.  
4. Click **Action ▸ Reset Cancelled POs to Draft**.  
5. The selected Purchase Orders will immediately return to **Draft** status.  

> Notes:  
> - Only orders in the **Cancelled** state will be reset.  
> - Orders not in **Cancelled** state remain unchanged.  
> - Standard Odoo permissions apply.  

---

## Access Rights

- Users need Purchase Orders access rights (`purchase_user` or above).  
- The bulk action is only available for users allowed to reset orders individually.  

---

## Known Limitations

- Draft or Confirmed orders are skipped.  
- Custom workflows or third-party modules may alter behavior.  

---

## Support & Issues

If you encounter problems or want enhancements, please open an issue or contact the developer.  

---

## Author

- **Manish Kumar Bohra**

## Developer

- **Manish Kumar Bohra** — <manishkumarbohra@outlook.com>  

---
