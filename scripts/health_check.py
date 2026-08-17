#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏥 JARVIS 헬스 체크 스크립트
자동화 시스템이 정상 작동하는지 모니터링
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

def check_jarvis_health():
    """JARVIS 자동화 시스템 헬스 체크"""
    print("🏥 JARVIS 헬스 체크 시작...")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    issues = []

    # 1️⃣ 데이터 파일 확인
    print("1️⃣ 데이터 파일 확인...")
    log_file = Path('data/jarvis_work_detailed_log.json')

    if not log_file.exists():
        issues.append("❌ jarvis_work_detailed_log.json 파일 없음")
    else:
        try:
            with open(log_file) as f:
                data = json.load(f)

            # 타임스탐프 확인
            file_time = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
            now = datetime.now()
            time_diff = (now - file_time).total_seconds() / 60

            if time_diff > 30:  # 30분 이상
                issues.append(f"⚠️ 데이터 오래됨: {time_diff:.0f}분 전")
                print(f"   ⚠️ 마지막 업데이트: {time_diff:.0f}분 전")
            else:
                print(f"   ✅ 데이터 최신: {time_diff:.0f}분 전")

            # completed_today 확인
            if not data.get('completed_today'):
                issues.append("⚠️ completed_today 배열이 비어있음")
            else:
                print(f"   ✅ 완료된 작업: {len(data['completed_today'])}개")

        except Exception as e:
            issues.append(f"❌ 데이터 파일 읽기 실패: {str(e)}")

    # 2️⃣ 스크립트 파일 확인
    print("\n2️⃣ 스크립트 파일 확인...")
    scripts = [
        'scripts/collect_moe_papers.py',
        'scripts/youtube_moe_analysis.py',
        'scripts/youtube_dropshipping_analysis.py',
        'scripts/google_search_data_collection.py',
        'scripts/moe_neural_network.py',
        'scripts/moe_training.py'
    ]

    missing_scripts = []
    for script in scripts:
        if not Path(script).exists():
            missing_scripts.append(script)
            issues.append(f"❌ {script} 파일 없음")

    if not missing_scripts:
        print(f"   ✅ 모든 스크립트 있음 ({len(scripts)}개)")
    else:
        print(f"   ❌ 빠진 스크립트: {len(missing_scripts)}개")

    # 3️⃣ 워크플로우 파일 확인
    print("\n3️⃣ 워크플로우 파일 확인...")
    workflow_file = Path('.github/workflows/jarvis_final_automation.yml')

    if workflow_file.exists():
        print(f"   ✅ 워크플로우 파일 있음")
    else:
        issues.append("❌ 워크플로우 파일 없음")
        print(f"   ❌ 워크플로우 파일 없음")

    # 최종 보고
    print("\n" + "="*60)
    print("📊 헬스 체크 결과")
    print("="*60)

    if not issues:
        print("✅ 모든 시스템 정상! JARVIS 자동화가 제대로 작동 중입니다.")
    else:
        print(f"⚠️ 주의: {len(issues)}개 문제 발견")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")

    print("="*60)
    print()

    return len(issues) == 0


if __name__ == '__main__':
    success = check_jarvis_health()
    exit(0 if success else 1)
