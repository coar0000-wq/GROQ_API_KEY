# ?¤– Gemini API Key ?ë™ ?±ë¡ ê°€?´ë“œ

## ë°©ë²• 1: GitHub CLI ?¬ìš© (ê¶Œì¥) â­?
### 1?¨ê³„: GitHub CLI ?¤ì¹˜
```bash
# Windows (PowerShell ê´€ë¦¬ì ëª¨ë“œ)
choco install gh

# ?ëŠ” ì§ì ‘ ?¤ìš´ë¡œë“œ
# https://github.com/cli/cli/releases
```

### 2?¨ê³„: GitHub ë¡œê·¸??```bash
gh auth login
```
- ? íƒ: GitHub.com
- ?„ë¡œ? ì½œ: HTTPS
- ?¸ì¦ ë°©ì‹: Personal access token ?ëŠ” ë¸Œë¼?°ì? ë¡œê·¸??
### 3?¨ê³„: Secrets ?±ë¡ (??ì¤?ëª…ë ¹??
```bash
echo "[YOUR_GEMINI_API_KEY]" | gh secret set GEMINI_API_KEY -R coar0000/kms
```

**ê²°ê³¼:**
```
??Set secret GEMINI_API_KEY for coar0000/kms
```

---

## ë°©ë²• 2: GitHub ??UI (?˜ë™)

### 1?¨ê³„: GitHub ?€?¥ì†Œ ?‘ì†
```
https://github.com/coar0000/kms/settings/secrets/actions
```

### 2?¨ê³„: "New repository secret" ?´ë¦­

### 3?¨ê³„: ?•ë³´ ?…ë ¥
```
Name:   GEMINI_API_KEY
Secret: [YOUR_GEMINI_API_KEY]
```

### 4?¨ê³„: "Add secret" ?´ë¦­

---

## ë°©ë²• 3: Windows PowerShell ?ë™??
### 1?¨ê³„: PowerShell ?¤í¬ë¦½íŠ¸ ?ì„±
?Œì¼ëª? `setup_gemini.ps1`

```powershell
# GitHub Personal Access Token ?…ë ¥
$token = Read-Host "GitHub Token"
$repo = "coar0000/kms"
$apiKey = "[YOUR_GEMINI_API_KEY]"

# Base64 ?¸ì½”??$bytes = [System.Text.Encoding]::UTF8.GetBytes($apiKey)
$base64 = [Convert]::ToBase64String($bytes)

# API ?¸ì¶œ
$headers = @{
    "Authorization" = "token $token"
    "Accept" = "application/vnd.github.v3+json"
}

# ê³µê°œ ??ì¡°íšŒ
$keyUrl = "https://api.github.com/repos/$repo/actions/secrets/public-key"
$keyResponse = Invoke-RestMethod -Uri $keyUrl -Headers $headers

Write-Host "??ê³µê°œ ???ë“ ?„ë£Œ"

# Secrets ?±ë¡
$secretUrl = "https://api.github.com/repos/$repo/actions/secrets/GEMINI_API_KEY"
$body = @{
    "encrypted_value" = $base64
    "key_id" = $keyResponse.key_id
} | ConvertTo-Json

Invoke-RestMethod -Uri $secretUrl -Method Put -Headers $headers -Body $body -ContentType "application/json"

Write-Host "??GEMINI_API_KEY ?±ë¡ ?„ë£Œ!"
```

### 2?¨ê³„: ?¤í–‰
```powershell
# PowerShell ê´€ë¦¬ì ëª¨ë“œ?ì„œ
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\setup_gemini.ps1
```

---

## ???±ë¡ ?•ì¸

### 1?¨ê³„: GitHub ?€?¥ì†Œ Settings ?•ì¸
```
https://github.com/coar0000/kms/settings/secrets/actions
```

### 2?¨ê³„: GEMINI_API_KEYê°€ ë³´ì´?”ì? ?•ì¸
- ???œì‹œ?˜ë©´ ?±ê³µ

### 3?¨ê³„: GitHub Actions ?•ì¸
```
https://github.com/coar0000/kms/actions
```

- JARVIS-Core-Automation.yml ?¤í–‰ ?¬ë? ?•ì¸
- ??10ë¶????ë™ ?¤í–‰ ?œì‘

---

## ?? ?±ë¡ ???ˆìƒ ê²°ê³¼

### 1ë¶???
- ??GitHub Actions ?Œí¬?Œë¡œ???œì‘
- ?“Š 5ê°??Œë«???í’ˆ ?™ì‹œ ë°œêµ´

### 10ë¶???
- ??cumulative_products.json ?…ë°?´íŠ¸
- ??scheduler_log.json ? ê·œ ??ª©
- ??Obsidian ?ë™ ?™ê¸°??
### ë§?10ë¶?
- ?”„ ?ë™ ë°˜ë³µ ?¤í–‰
- ?“ˆ ?„ì  ?í’ˆ ??ì¦ê?
- ?“ ?‘ì—… ë¡œê·¸ ê¸°ë¡

---

## ?› ï¸??¸ëŸ¬ë¸”ìŠˆ??
### "GitHub Token??? íš¨?˜ì? ?ŠìŒ"
??Personal Access Token ?¬ë°œê¸???https://github.com/settings/tokens

### "ê¶Œí•œ ë¶€ì¡? ?¤ë¥˜
??Token ?ì„± ??"repo" ê¶Œí•œ ? íƒ
???€?¥ì†Œ ?„ì²´ ?‘ê·¼ ê¶Œí•œ ?„ìš”

### "Secrets ?±ë¡??????
???€?¥ì†Œëª??•ì¸: coar0000/kms
??Token ê¶Œí•œ ?¬í™•??????UI?ì„œ ?˜ë™ ?±ë¡ ?œë„

---

## ?“‹ ì²´í¬ë¦¬ìŠ¤??
- [ ] GitHub CLI ?¤ì¹˜ (ë°©ë²• 1) ?ëŠ” ??UI (ë°©ë²• 2)
- [ ] GitHub ?¸ì¦ ?„ë£Œ
- [ ] GEMINI_API_KEY ?±ë¡ ?„ë£Œ
- [ ] ?±ë¡ ?•ì¸ (Settings?ì„œ ë³´ì„)
- [ ] ??10ë¶???GitHub Actions ?¤í–‰ ?•ì¸
- [ ] cumulative_products.json ?…ë°?´íŠ¸ ?•ì¸

---

**?‰ ?„ë£Œ! JARVIS ?ë™???œìŠ¤?œì´ ?¤í–‰ ì¤‘ì…?ˆë‹¤.**

