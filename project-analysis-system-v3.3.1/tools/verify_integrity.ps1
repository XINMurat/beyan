<#
.SYNOPSIS
Project Analysis System Integrity Verifier

.DESCRIPTION
Bu script Project Analysis System'in (v3.3.1+) bütünlüğünü kontrol eder:
1. Encoding kontrolü (Bozuk/Mojibake karakter kontrolü)
2. Kırık link / referans kontrolü
3. MANIFEST.yaml senkronizasyon kontrolü

.USAGE
.\verify_integrity.ps1
#>

$ErrorActionPreference = "Stop"
$systemRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Definition)
Set-Location $systemRoot

$exitCode = 0
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Project Analysis System - Integrity    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Encoding Check
Write-Host "`n[1/3] Encoding Kontrolü (Mojibake tespiti)..." -ForegroundColor Yellow
$mdFiles = Get-ChildItem -Path "." -Filter "*.md" -Recurse
$encodingErrors = 0

foreach ($file in $mdFiles) {
    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        # Sık görülen mojibake karakterleri
        if ($content -match "Ã|\xEF\xBF\xBD") {
            Write-Host "  ❌ BOZUK ENCODING: $($file.Name)" -ForegroundColor Red
            $encodingErrors++
        }
    } catch {
        Write-Host "  ❌ OKUMA HATASI: $($file.Name)" -ForegroundColor Red
        $encodingErrors++
    }
}

if ($encodingErrors -eq 0) {
    Write-Host "  ✅ Tüm .md dosyalarının kodlaması temiz." -ForegroundColor Green
} else {
    $exitCode = 1
}

# 2. Kırık Referans Kontrolü
Write-Host "`n[2/3] Kırık Referans Kontrolü..." -ForegroundColor Yellow
$refErrors = 0
$knownFiles = $mdFiles | Select-Object -ExpandProperty Name

foreach ($file in $mdFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Basit bir regex ile .md linklerini bul
    $matches = [regex]::Matches($content, "\[.*?\]\((.*?.md)\)")
    foreach ($match in $matches) {
        $target = $match.Groups[1].Value
        # Path içeriyorsa sadece dosya adını al (basit kontrol için)
        $targetFile = Split-Path $target -Leaf
        
        if ($targetFile -notin $knownFiles) {
            Write-Host "  ❌ KIRIK LINK: $($file.Name) -> $target" -ForegroundColor Red
            $refErrors++
        }
    }
}

if ($refErrors -eq 0) {
    Write-Host "  ✅ Tüm içi bağlantılar sağlam." -ForegroundColor Green
} else {
    $exitCode = 1
}

# 3. MANIFEST.yaml Senkronizasyonu
Write-Host "`n[3/3] MANIFEST.yaml Senkronizasyonu..." -ForegroundColor Yellow
$manifestPath = "MANIFEST.yaml"
if (Test-Path $manifestPath) {
    $manifestContent = Get-Content $manifestPath -Raw -Encoding UTF8
    $modulesDir = "modules"
    $actualModules = Get-ChildItem -Path $modulesDir -Filter "*.md" -Recurse | Select-Object -ExpandProperty Name
    $missingInManifest = 0
    
    foreach ($mod in $actualModules) {
        if ($manifestContent -notmatch $mod) {
            Write-Host "  ⚠️ UYARI: $mod fiziksel olarak var ama MANIFEST'te tanımlı değil." -ForegroundColor Yellow
            $missingInManifest++
        }
    }
    
    if ($missingInManifest -eq 0) {
        Write-Host "  ✅ MANIFEST ile fiziksel modüller senkronize." -ForegroundColor Green
    }
} else {
    Write-Host "  ❌ HATA: MANIFEST.yaml bulunamadı!" -ForegroundColor Red
    $exitCode = 1
}

Write-Host "`n==========================================" -ForegroundColor Cyan
if ($exitCode -eq 0) {
    Write-Host "SONUÇ: BAŞARILI (System Integrity OK)" -ForegroundColor Green
} else {
    Write-Host "SONUÇ: BAŞARISIZ (Lütfen hataları düzeltin)" -ForegroundColor Red
}
Write-Host "==========================================" -ForegroundColor Cyan

exit $exitCode
