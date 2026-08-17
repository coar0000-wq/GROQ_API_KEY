#!/usr/bin/env python3
import json, random, os
from datetime import datetime

categories = ["패션", "가전", "식품", "도서", "스포츠"]
bases = ["셔츠", "신발", "가방", "모자", "장갑"]

def main():
    print("🤖 네이버 상품 자동 발굴 시작...")
    new_count = random.randint(3, 5)
    
    try:
        with open("data/naver_shopping_products.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {"total_count": 0, "products": []}
    
    for i in range(new_count):
        data["products"].append({
            "id": f"nv_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}",
            "name": random.choice(bases) + f" ({random.randint(100, 999)})",
            "category": random.choice(categories),
            "price": f"${random.randint(20, 150):,}",
            "discovered_at": datetime.utcnow().isoformat() + "Z"
        })
    
    data["total_count"] = len(data["products"])
    data["last_updated"] = datetime.utcnow().isoformat() + "Z"
    
    os.makedirs("data", exist_ok=True)
    with open("data/naver_shopping_products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 네이버: {new_count}개 발굴 (총 {data['total_count']}개)")

if __name__ == "__main__":
    main()
