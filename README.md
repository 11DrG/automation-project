# Automation Project

UI and API test automation project built with Playwright and Python.

## Tech Stack
- Python
- Playwright
- Pytest
- Requests
- Page Object Model
- python-dotenv

## Project Structure
automation_project/
├── api_tests/
│   └── test_api_users.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── header_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_multiple_items.py
│   ├── test_sorting.py
│   └── test_filtering_and_logout.py
├── conftest.py
├── pytest.ini
└── .env (not committed - contains sensitive data)

## Test Coverage
- Login (valid, invalid, empty credentials)
- Cart (add, remove, multiple items)
- Checkout (complete flow, missing details)
- Sorting (price, name)
- Logout
- API (GET, POST, PUT, DELETE, chaining)

## How to Run

### All tests
```powershell