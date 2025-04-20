# Superstore Checkout API

This is a simple Django REST API that calculates the total price of items in a supermarket cart. The cart's total price takes into account individual prices and special offers for certain items.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-5.2-blue.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/Swagger-Enabled-green.svg" alt="Swagger">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

## Features:

- **Item Prices**: Each item has an individual price.
- **Special Offers**: Certain items have special offers (e.g., 3 items for Rs.130 ).
- **API**: A POST request accepts a string of item codes, processes the items, and returns the total price.

## Special Pricing:

| Item | Unit Price | Special Offer    |
| ---- | ---------- | ---------------- |
| A    | 50         | 3 for Rs.130     |
| B    | 30         | 2 for Rs.45      |
| C    | 20         | No special offer |
| D    | 15         | No special offer |

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Djain318/Django_Checkout_App.git
   cd Django_Checkout_App
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**

   ```bash
   python manage.py runserver
   ```

5. **Access Swagger API Docs:**

   Once the server is running, you can view the Swagger documentation at:

   - Swagger UI => http://127.0.0.1:8000/swagger/
   - ReDoc UI => http://127.0.0.1:8000/redoc/

## API Endpoint

- **POST /api/checkout/**: Calculate the total price based on the list of items.
- Example: http://127.0.0.1:8000/api/checkout/

### Example:

```
AABBC

"total_price: 165"
```

## Technologies Used

- **Django**: A Python web framework.
- **Django REST Framework**: A toolkit for building Web APIs.
- **drf-yasg**: A great tool to generate Swagger UI for the Django REST API.

---

## 🧾 Checkout API Logic

This Django REST API calculates the **total price** of items added to the shopping cart based on **unit prices** and **available discount deals**.

### 🔧 Pricing Rules:

- Each item (A, B, C, D) has a fixed **unit price**.
- Items **A** and **B** also have **bulk discount offers**:
  - `A: 3 for Rs. 130`
  - `B: 2 for Rs. 45`

### 📥 How It Works:

1. The API receives a string of characters (e.g., `"ABACBAD"`) representing items scanned by the customer.
2. It counts the quantity of each item.
3. It applies available deals:
   - If a deal exists for an item, it calculates how many deals apply and the remaining items at unit price.
   - If no deal exists, it simply multiplies count × unit price.
4. It sums up the total and returns it as JSON.

### 🧠 Example:

**Input:**

```
ABACBAD
```

**Breakdown:**

- A × 3 → Special: 3 for 130 → Total = 130
- B × 2 → Special: 2 for 45 → Total = 45
- C × 1 → No deal → 1 × 20 = 20
- D × 1 → No deal → 1 × 15 = 15

**✅ Final Output:**

```
"total_price: 210"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
