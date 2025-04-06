# Challenge Solutions

# 🟡 Solution 1 – Basic Query (All Fields)

Fetch all active products, ordering them by name.
This retrieves all fields from the database.

```python
products = Product.objects.filter(is_active=True).order_by("name")
```

This returns full model instances with all fields loaded.
Useful when you need access to the entire model or its methods.


# 🟢 Solution 2 – Use `.only()` to Limit Fields (Model Instances)


Fetch only selected fields: id, name, slug, description, price.
Still returns model instances, with only specified fields loaded.

```python
products = (
    Product.objects.filter(is_active=True)
    .only("id", "name", "slug", "description", "price")
    .order_by("name")
)
```

You still get model instances, but accessing any field outside of `.only()`
will trigger additional database queries (lazy loading).


# 🔵 Solution 3 – Use `.values()` to Return Raw Data


Fetch and return selected fields as dictionaries (not model instances).
```python
products = Product.objects.filter(is_active=True).values(
    "id", "name", "slug", "description", "price"
).order_by("name")

return Response(products)
```

