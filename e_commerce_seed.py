# seed.py  —  run with: python manage.py shell < seed.py

from e_commerce.models import Category, Product  # adjust 'your_app' to your app name

# ── 1. Clean up existing data ──────────────────────────────────────────────────
Product.objects.all().delete()
Category.objects.all().delete()
print("Cleared existing data.")

# ── 2. Create Categories ───────────────────────────────────────────────────────
categories_data = ["Laptops", "Smartphones", "Accessories", "Monitors", "Audio"]

categories = {
    name: Category.objects.create(name=name) for name in categories_data
}
print(f"Created {len(categories)} categories.")

# ── 3. Create Products ─────────────────────────────────────────────────────────
products_data = [
    # Laptops
    {
        "name": "MacBook Pro 14",
        "category": categories["Laptops"],
        "price": "1999.99",
        "discount": 0.05,
        "stock": 15,
        "condition": "new",
    },
    {
        "name": "Dell XPS 15",
        "category": categories["Laptops"],
        "price": "1599.99",
        "discount": 0.10,
        "stock": 8,
        "condition": "new",
    },
    {
        "name": "Lenovo ThinkPad X1",
        "category": categories["Laptops"],
        "price": "899.99",
        "discount": 0.0,
        "stock": 0,
        "condition": "refurbished",
    },
    # Smartphones
    {
        "name": "iPhone 15 Pro",
        "category": categories["Smartphones"],
        "price": "1099.99",
        "discount": 0.0,
        "stock": 30,
        "condition": "new",
    },
    {
        "name": "Samsung Galaxy S24",
        "category": categories["Smartphones"],
        "price": "899.99",
        "discount": 0.08,
        "stock": 22,
        "condition": "new",
    },
    {
        "name": "Google Pixel 7",
        "category": categories["Smartphones"],
        "price": "499.99",
        "discount": 0.15,
        "stock": 5,
        "condition": "used",
    },
    # Accessories
    {
        "name": "Logitech MX Master 3 Mouse",
        "category": categories["Accessories"],
        "price": "99.99",
        "discount": 0.0,
        "stock": 50,
        "condition": "new",
    },
    {
        "name": "Keychron K2 Keyboard",
        "category": categories["Accessories"],
        "price": "89.99",
        "discount": 0.05,
        "stock": 18,
        "condition": "new",
    },
    {
        "name": "USB-C Hub 7-in-1",
        "category": categories["Accessories"],
        "price": "45.99",
        "discount": 0.0,
        "stock": 0,
        "condition": "new",
    },
    # Monitors
    {
        "name": "LG UltraWide 34\"",
        "category": categories["Monitors"],
        "price": "749.99",
        "discount": 0.12,
        "stock": 10,
        "condition": "new",
    },
    {
        "name": "Dell 27\" 4K Monitor",
        "category": categories["Monitors"],
        "price": "499.99",
        "discount": 0.0,
        "stock": 7,
        "condition": "refurbished",
    },
    # Audio
    {
        "name": "Sony WH-1000XM5",
        "category": categories["Audio"],
        "price": "349.99",
        "discount": 0.10,
        "stock": 25,
        "condition": "new",
    },
    {
        "name": "AirPods Pro 2nd Gen",
        "category": categories["Audio"],
        "price": "249.99",
        "discount": 0.0,
        "stock": 40,
        "condition": "new",
    },
    {
        "name": "Bose QuietComfort 45",
        "category": categories["Audio"],
        "price": "279.99",
        "discount": 0.20,
        "stock": 3,
        "condition": "used",
    },
]

products = [Product.objects.create(**data) for data in products_data]
print(f"Created {len(products)} products.")

# ── 4. Summary ─────────────────────────────────────────────────────────────────
print("\n── Seed complete ──")
for category in Category.objects.all():
    product_count = category.products.count()
    print(f"  {category.name} — {product_count} product(s)")