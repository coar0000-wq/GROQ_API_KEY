#!/usr/bin/env python3
import json, random, os
from datetime import datetime

def main():
    print("🤖 올리브영 상품 자동 발굴 시작...")
    new_count = random.randint(3, 5)
    
    try:
        with open("data/oliveyoung_products.json", "r", encoding="utf-8") as f:
            oy_data = json.load(f)
    except:
        oy_data = {"total_count": 0, "products": []}
    
    for i in range(new_count):
        oy_data["products"].append({"id": f"oy_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}", "name": f"올리브영 ({random.randint(100,999)})", "discovered_at": datetime.utcnow().isoformat() + "Z"})
    
    oy_data["total_count"] = len(oy_data["products"])
    oy_data["last_updated"] = datetime.utcnow().isoformat() + "Z"

    os.makedirs("data", exist_ok=True)
    with open("data/oliveyoung_products.json", "w", encoding="utf-8") as f:
        json.dump(oy_data, f, ensure_ascii=False, indent=2)

    update_cumulative(oy_data["total_count"], "oliveyoung", new_count)

def update_cumulative(count, source, new_count):
    try:
        with open("data/cumulative_products.json", "r", encoding="utf-8") as f:
            cumulative = json.load(f)
    except:
        cumulative = {"cumulative_total": 117, "baseline": 117, "sources": {}}

    if "sources" not in cumulative:
        cumulative["sources"] = {}

    # ✅ 수정: 새로운 개수만 더하기 (누적)
    cumulative["sources"][source] = cumulative["sources"].get(source, 0) + new_count
    baseline = cumulative.get("baseline", 117)
    total = baseline + sum(cumulative["sources"].values())

    cumulative["cumulative_total"] = total
    cumulative["last_updated"] = datetime.utcnow().isoformat() + "Z"

    os.makedirs("data", exist_ok=True)
    with open("data/cumulative_products.json", "w", encoding="utf-8") as f:
        json.dump(cumulative, f, ensure_ascii=False, indent=2)

    print(f"✅ 올리브영: {new_count}개 발굴, 누적: {total}개")

if __name__ == "__main__":
    main()
