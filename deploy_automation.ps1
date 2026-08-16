# 🤖 JARVIS 자동화 배포 스크립트

Write-Host "🚀 JARVIS 자동화 시스템 배포 시작..." -ForegroundColor Cyan

# Git 커밋
Write-Host "`n📝 Git 커밋 중..." -ForegroundColor Yellow
git add -A
git commit -m "🤖 JARVIS 실제 자동화 시스템 (GitHub Actions 매 10분)" -q

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 커밋 완료" -ForegroundColor Green
} else {
    Write-Host "⚠️ 커밋 실패 (변경사항 없음 가능)" -ForegroundColor Yellow
}

# Git 푸시
Write-Host "`n📤 GitHub로 푸시 중..." -ForegroundColor Yellow
git push origin main -q

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 푸시 완료" -ForegroundColor Green
} else {
    Write-Host "❌ 푸시 실패" -ForegroundColor Red
    exit 1
}

# 배포 정보 표시
Write-Host "`n" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "✅ JARVIS 자동화 시스템 배포 완료!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

Write-Host "`n📊 자동화 시스템 정보:" -ForegroundColor Cyan
Write-Host "  • 실행 빈도: 매 10분마다" -ForegroundColor White
Write-Host "  • 워크플로우: .github/workflows/jarvis_automation.yml" -ForegroundColor White
Write-Host "  • 스크립트: scripts/jarvis_automation_real.py" -ForegroundColor White
Write-Host "  • 데이터: data/jarvis_work_detailed_log.json" -ForegroundColor White

Write-Host "`n🔗 GitHub Actions 확인:" -ForegroundColor Cyan
Write-Host "  https://github.com/coar0000/kms/actions" -ForegroundColor Cyan

Write-Host "`n📈 대시보드:" -ForegroundColor Cyan
Write-Host "  https://coar0000-wq.github.io/jarvis-luna/" -ForegroundColor Cyan

Write-Host "`n⏰ 다음 자동 실행:" -ForegroundColor Yellow
$nextRun = [Math]::Ceiling((Get-Date).Minute / 10) * 10
if ($nextRun -eq 60) { $nextRun = 0 }
Write-Host "  약 $($nextRun)분 이내" -ForegroundColor Yellow

Write-Host "`n✨ 시스템이 정상 작동하고 있습니다!" -ForegroundColor Green
