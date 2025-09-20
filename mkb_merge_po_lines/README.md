# Merge Duplicate Purchase Order Lines

This module adds a button on the Purchase Order form to automatically merge duplicate purchase order lines into a single line.

---

## Features

- Adds a **Merge Duplicate PO Lines** button in the Purchase Order form header.
- Automatically merges duplicate lines that have:
  - The same **Product**
  - The same **Unit Price**
  - The same **Taxes**
- The quantities of duplicate lines are summed into a single line.
- Available only when the Purchase Order is in **Draft** state.

---

## Compatibility

- Odoo: 19.0

---

## Dependencies

- `purchase`
- `purchase_stock` (optional, if your flow depends on stock integration)

---

## Installation

1. Copy this module into your Odoo `addons` directory.
2. Update the Apps list from **Apps ▸ Update Apps List**.
3. Search for **Merge Duplicate Purchase Order Lines** and install it.

---

## Usage

1. Navigate to **Purchase ▸ Orders**.
2. Open any Purchase Order in **Draft** state.
3. Click the **Merge Duplicate PO Lines** button in the form header.
4. Duplicate lines will be merged automatically, and quantities will be updated.

> **Notes**  
> - Only duplicates (same product, price, and taxes) are merged.  
> - The action is available only in Draft purchase orders.  
> - If no duplicates are found, the order remains unchanged.  

---

## Access Rights

- Available to any user with access to Purchase Orders (`purchase_user` or higher).  

---

## Known Limitations

- Does not consider differences in **UoM** (Unit of Measure). If the same product is entered with different UoMs, lines will not merge.  
- Custom workflows or third-party modules may override default line handling.  

---

## Changelog

### v1.0.0
- Initial release: Added button to merge duplicate Purchase Order lines.  

---

## Author

- **Manish Kumar Bohra**

## Developer

- **Manish Kumar Bohra** — <manishkumarbohra@outlook.com>