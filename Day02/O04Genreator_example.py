import random

# Generate a dataset of 1000 records
def generate_dataset(n = 500):
    for i in range(1, n+1):
        record = {
            "id": i,
            "user": f"user_{random.randint(1, 100)}",
            "amount": round(random.uniform(10, 500), 2),
            "status": random.choice(["Success", "failed", "Pending"])
        }
        yield record

dataset = generate_dataset()
print(next(dataset))
print(next(dataset))


# assignment - yield 50 records at a time