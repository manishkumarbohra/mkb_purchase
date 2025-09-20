# Bulk Unlock Purchase Orders

Unlock multiple locked Purchase Orders in one go from the Purchase Orders list view.

---

## Features

- Adds an **Action ▸ Unlock Purchase Orders** option in the Purchase Orders list view.
- Select several locked purchase orders at once and unlock them in bulk.
- Respects standard Odoo access rights and workflow.

---

## Compatibility

- Odoo: 16.0 / 17.0 / 18.0 (adjust if different)

---

## Dependencies

- `purchase`
- `purchase_stock` (if you use stock integration)

---

## Installation

1. Copy this module into your Odoo `addons` path.
2. Update the app list: **Apps ▸ Update Apps List**.
3. Install **Bulk Unlock Purchase Orders**.

---

## Usage

1. Go to **Purchase ▸ Orders**.
2. Switch to the **list** (tree) view.
3. Select the locked Purchase Orders you want to unlock.
4. Click **Action ▸ Unlock Purchase Orders**.
5. The selected Purchase Orders will be unlocked immediately.

> Notes:  
> - Only orders in the **Locked** state will be unlocked.  
> - Orders already unlocked remain unchanged.  
> - Standard Odoo permissions apply.  

---

## Access Rights

- Users need Purchase Orders access rights (`purchase_user` or above).  
- The bulk action is only available for users allowed to unlock orders individually.  

---

## Known Limitations

- Draft RFQs or already unlocked orders are skipped.  
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

## License

This module is licensed under the same terms as Odoo Community addons unless specified otherwise. Update this section if you use a different license.
