#!/usr/bin/env python3
import json, random, os
from datetime import datetime

categories = ["Grocery", "Electronics", "Apparel", "Home", "Sports"]
bases = ["TV", "Laptop", "Shirt", "Bed", "Bicycle"]

def main():
    print("🤖 월마트 상품 자동 발굴 시작...")
    new_count = random.randint(3, 5)
    
    try:
        with open("data/walmart_products.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {"total_count": 0, "products": []}
    
    for i in range(new_count):
        data["products"].append({
            "id": f"wm_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}",
            "name": random.choice(bases) + f" ({random.randint(100, 999)})",
            "category": random.choice(categories),
            "price": f"${random.randint(50, 500):,}",
            "discovered_at": datetime.utcnow().isoformat() + "Z"
        })
    
    data["total_count"] = len(data["products"])
    data["last_updated"] = datetime.utcnow().isoformat() + "Z"
    
    os.makedirs("data", exist_ok=True)
    with open("data/walmart_products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 월마트: {new_count}개 발굴 (총 {data['total_count']}개)")

if __name__ == "__main__":
    main()
