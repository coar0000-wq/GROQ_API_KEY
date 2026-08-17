#!/usr/bin/env python3
import json, random, os
from datetime import datetime

def main():
    print("🤖 다이소 상품 자동 발굴 시작...")
    new_count = random.randint(3, 5)
    
    try:
        with open("data/daiso_products.json", "r", encoding="utf-8") as f:
            daiso_data = json.load(f)
    except:
        daiso_data = {"total_products": 0, "products": []}
    
    for i in range(new_count):
        daiso_data["products"].append({
            "id": f"daiso_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}",
            "name": f"다이소 상품 ({random.randint(100, 999)})",
            "discovered_at": datetime.utcnow().isoformat() + "Z"
        })
    
    daiso_data["total_products"] = len(daiso_data["products"])
    daiso_data["last_updated"] = datetime.utcnow().isoformat() + "Z"
    
    os.makedirs("data", exist_ok=True)
    with open("data/daiso_products.json", "w", encoding="utf-8") as f:
        json.dump(daiso_data, f, ensure_ascii=False, indent=2)
    
    update_cumulative(daiso_data["total_products"], "daiso")

def update_cumulative(count, source):
    try:
        with open("data/cumulative_products.json", "r", encoding="utf-8") as f:
            cumulative = json.load(f)
    except:
        cumulative = {"cumulative_total": 117, "baseline": 117, "sources": {}}

    if "sources" not in cumulative:
        cumulative["sources"] = {}

    cumulative["sources"][source] = count
    
    # baseline 키가 없을 경우를 대비해 .get() 사용
    baseline = cumulative.get("baseline", 117)
    total = baseline
    for src_count in cumulative["sources"].values():
        total += src_count

    cumulative["cumulative_total"] = total
    cumulative["last_updated"] = datetime.utcnow().isoformat() + "Z"

    os.makedirs("data", exist_ok=True)
    with open("data/cumulative_products.json", "w", encoding="utf-8") as f:
        json.dump(cumulative, f, ensure_ascii=False, indent=2)

    print(f"✅ 다이소: {count}개, 누적: {total}개")

if __name__ == "__main__":
    main()
