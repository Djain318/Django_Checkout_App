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

## Architecture: Model-View-Template (MVT)

- Overview:
Django follows the Model-View-Template (MVT) architectural pattern, which is a variant of the more common Model-View-Controller (MVC) pattern. In Django, the "Template" replaces the "View" in the MVC architecture, which means that the Django pattern is a bit different.

Here's a breakdown of each component in the MVT pattern used in this project:

1. Model (Data Layer):
The Model represents the data structure and the business logic of the application. In Django, models are Python classes that define the structure of the database.

Models define the fields (attributes) and behaviors (methods) that the data will have. In our API, this is where you would define things like pricing rules, item types, and any other data you need to store or process.

2. View (Business Logic Layer):
The View is responsible for handling the user request and returning the appropriate response. In Django, views are Python functions or classes that process requests and return responses.

In this project, the CheckoutAPIView class is the view that handles the POST request. The view validates the data, processes the checkout logic, calculates the total price, and returns the response.

3. Template (Presentation Layer):
The Template is responsible for rendering the content that the user sees. In Django, templates are HTML files that are rendered and returned to the client.

For this API, templates are not used in the traditional sense, since it's a backend API. Instead, we send back JSON responses directly to the client.

- How MVT Works in Django:
User Request: The user sends an HTTP request to the server.

View Processing: The request is routed to the corresponding view based on the URL configuration. The view processes the request, interacts with the model if necessary, and prepares the response.

Template Rendering: If the view requires presenting HTML, it uses a template to generate HTML content.

Response: The view sends the generated content (in this case, JSON) back to the user.

In this project, the primary interaction happens between the View (API logic in the CheckoutAPIView), Model (business rules or data like pricing), and the Template (though in this case, the response is JSON, not HTML).

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
