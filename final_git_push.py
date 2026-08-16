#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 JARVIS: 최종 Git 동기화 (모든 데이터 파일)
"""

import subprocess
import os
from datetime import datetime

os.chdir(r'C:\Users\Desktop\Claude\Projects\kms')

print("\n" + "="*70)
print("🚀 JARVIS: 최종 Git 동기화 시작")
print("="*70)
print(f"⏰ 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📍 경로: {os.getcwd()}")

# 1️⃣ Git status 확인
print("\n[1/3] 현재 Git 상태 확인...")
subprocess.run(['git', 'status'], timeout=30)

# 2️⃣ 모든 파일 추가
print("\n[2/3] 모든 변경사항 스테이징...")
subprocess.run(['git', 'add', '.'], timeout=30)

# 3️⃣ 커밋
print("\n[3/3] 커밋 및 푸시...")
subprocess.run(['git', 'commit', '-m', '🤖 JARVIS LUNA 대시보드 데이터 모두 푸시 (작업로그+프로젝트+팀원+활동)'], timeout=30)

# 4️⃣ 푸시
subprocess.run(['git', 'push', 'origin', 'main'], timeout=60)

print("\n" + "="*70)
print("✅ 모든 작업 완료!")
print("="*70)
print("📱 대시보드 확인: https://coar0000-wq.github.io/jarvis-luna/")
print("⏱️  업데이트 시간: 1-2분 (캐시 반영)")
print("🔄 강력 새로고침: Ctrl+Shift+R")
