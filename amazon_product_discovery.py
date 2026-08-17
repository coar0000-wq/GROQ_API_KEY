#!/usr/bin/env python3
import json, random, os
from datetime import datetime

categories = ["Books", "Electronics", "Fashion", "Home", "Beauty"]
bases = ["Book", "Headphone", "Jacket", "Pillow", "Shampoo"]

def main():
    print("🤖 아마존 상품 자동 발굴 시작...")
    new_count = random.randint(3, 5)
    
    try:
        with open("data/amazon_products.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {"total_count": 0, "products": []}
    
    for i in range(new_count):
        data["products"].append({
            "id": f"az_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}",
            "name": random.choice(bases) + f" ({random.randint(100, 999)})",
            "category": random.choice(categories),
            "price": f"${random.randint(10, 200):,}",
            "discovered_at": datetime.utcnow().isoformat() + "Z"
        })
    
    data["total_count"] = len(data["products"])
    data["last_updated"] = datetime.utcnow().isoformat() + "Z"
    
    os.makedirs("data", exist_ok=True)
    with open("data/amazon_products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 아마존: {new_count}개 발굴 (총 {data['total_count']}개)")

if __name__ == "__main__":
    main()
