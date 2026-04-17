# Module: Infrastructure & DevOps Analysis

**Priority**: P3 (Optional but important for mature projects)  
**Tokens**: ~2000  
**Analysis Time**: 12-15 minutes  

---

## Purpose

Evaluate infrastructure setup, container orchestration, CI/CD pipelines, deployment strategy, and cloud resource optimization.

---

## Analysis Dimensions

### 1. Containerization & Orchestration

```yaml
docker:
  dockerfile_quality:
    - Multi-stage builds (reduce image size)
    - Proper base image (alpine vs full)
    - Layer caching optimization
    - Security scanning
  
  docker_compose:
    - Service definition clarity
    - Volume management
    - Network configuration
    - Environment handling

kubernetes:
  if_detected:
    - Resource limits/requests
    - Health checks (liveness, readiness)
    - HPA (Horizontal Pod Autoscaler)
    - Service mesh (Istio, Linkerd)
  
confidence: "high_90%"
```

### 2. CI/CD Pipeline

```yaml
pipeline_quality:
  stages:
    - Build
    - Test (unit, integration, e2e)
    - Security scan
    - Deploy (staging, production)
  
  best_practices:
    - Automated testing
    - Manual approval gates (production)
    - Rollback capability
    - Deployment notifications
  
  common_issues:
    - No automated tests in pipeline
    - Deploy to production without staging
    - No rollback plan
    - Secrets in pipeline config

confidence: "high_88%"
```

### 3. Infrastructure as Code

```yaml
iac_tools:
  terraform: "Multi-cloud, declarative"
  pulumi: "Code-based (TypeScript, Python)"
  cloudformation: "AWS-specific"
  bicep: "Azure-specific"

checks:
  version_control: "IaC in Git (not manual clicks)"
  state_management: "Remote state (S3, Azure Storage)"
  modularity: "Reusable modules"
  documentation: "README for each module"

confidence: "high_92%"
```

---

## Turkish Output Example

```markdown
# Infrastructure & DevOps Analizi

## Genel Skor: 6/10 🟡

### Özet
- ✅ İyi: Docker kullanılıyor
- 🟡 Dikkat: CI/CD eksik test stage'i
- 🔴 Kritik: Production'a manual deploy
- ❌ Eksik: Infrastructure as Code yok

---

## Detaylı Bulgular

### 1. 🔴 Manual Production Deployment

**Sorun**: Production'a SSH ile manuel deploy yapılıyor

**Mevcut Süreç** (30 adım, 45 dakika):
```bash
# Manuel, hata riski yüksek
ssh user@prod-server
git pull origin main
npm install
npm run build
pm2 restart app
```

**Önerilen Süreç** (1 tık, 5 dakika):
```yaml
# GitHub Actions: .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    tags: ['v*']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build
        run: npm run build
      
      - name: Test
        run: npm test
      
      - name: Deploy to staging
        run: ./deploy.sh staging
      
      - name: Smoke test
        run: ./smoke-test.sh staging
      
      - name: Deploy to production
        run: ./deploy.sh production
        if: success()
      
      - name: Rollback on failure
        if: failure()
        run: ./rollback.sh production
```

**Çaba**: 1 gün (pipeline kurulumu)
**Etki**: 
- Deployment zamanı: 45 dk → 5 dk (90% azalma)
- Hata riski: %40 → %5 (manuel hata yok)
- Rollback: 30 dk → 2 dk
**Güven**: Yüksek (%90)

---

### 2. 🟡 Dockerfile Optimize Edilmemiş

**Mevcut** (850 MB):
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
```

**Sorunlar**:
- Base image çok büyük (node:18 = 900 MB)
- Production dependencies + dev dependencies
- Layer caching yok

**Optimize** (150 MB):
```dockerfile
# Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

**İyileştirme**:
- Image size: 850 MB → 150 MB (82% azalma)
- Build time: 5 dk → 2 dk (cache layer)
- Security: Daha az attack surface

**Çaba**: 1 saat
**Güven**: Yüksek (%95)

---

### 3. ❌ Infrastructure as Code Yok

**Sorun**: Sunucular manuel kurulu (dokümantasyon eksik)

**Risk**:
- Yeni sunucu kurmak 2 gün sürer
- Disaster recovery yok
- Hangi konfigürasyonlar var bilinmiyor

**Çözüm**: Terraform ile IaC

```hcl
# main.tf
resource "azurerm_linux_virtual_machine" "app_server" {
  name                = "prod-app-server"
  location            = "westeurope"
  size                = "Standard_B2s"
  admin_username      = "adminuser"
  
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }
  
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "20.04-LTS"
    version   = "latest"
  }
}

resource "azurerm_postgresql_server" "database" {
  name                = "prod-postgres"
  location            = "westeurope"
  version             = "13"
  sku_name            = "B_Gen5_2"
  
  storage_mb                   = 102400
  backup_retention_days        = 7
  geo_redundant_backup_enabled = true
}
```

**Fayda**:
- Yeni ortam kurulumu: 2 gün → 30 dakika
- Disaster recovery: 1 hafta → 1 saat
- Versiyon kontrolü: Infrastructure değişiklikleri Git'te

**Çaba**: 1 hafta (initial setup)
**Güven**: Orta (%75, ekip öğrenmesi gerekli)

---

### 4. 🟢 Docker Kullanımı İyi ✅

**Güçlü Yanlar**:
- ✅ Docker Compose ile local dev environment
- ✅ .dockerignore dosyası mevcut
- ✅ Health check endpoint var

**Küçük İyileştirme**:
```dockerfile
# Health check ekle
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node healthcheck.js || exit 1
```

---

## Öncelikli Öneriler

### 🔴 P0 - Kritik (Bu Hafta)

1. **CI/CD Pipeline Kur** (1 gün)
   - GitHub Actions veya GitLab CI
   - Automated tests ekle
   - Staging → Production flow
   - **Etki**: Manual deployment riski %40 → %5

2. **Dockerfile Optimize Et** (1 saat)
   - Multi-stage build
   - Alpine base image
   - **Etki**: Image 850 MB → 150 MB

### 🟡 P1 - Yüksek (Bu Sprint)

3. **Rollback Stratejisi Belirle** (2 saat)
   - Previous version tag'leri
   - Rollback script yaz
   - Test et
   - **Etki**: Recovery time 30 dk → 2 dk

4. **Monitoring Ekle** (4 saat)
   - Application Insights veya Prometheus
   - Error rate alerts
   - Performance metrics
   - **Etki**: Sorunları proaktif yakala

### 🟢 P2 - Orta (Bu Ay)

5. **Infrastructure as Code** (1 hafta)
   - Terraform ile baÅŸla
   - Mevcut infrastructure'ı kodla
   - Version control'e ekle
   - **Etki**: Disaster recovery capability

---

## Cloud Cost Optimization

```markdown
### Mevcut Aylık Maliyet: $1,200

**Breakdown**:
- VM (Standard_D2s_v3): $120/ay
- Database (GP_Gen5_4): $450/ay
- Bandwidth: $80/ay
- Storage: $50/ay
- Reserved capacity: Yok ❌

**Optimization Önerileri**:

1. **Reserved Instances (1 yıllık)**: $120 → $75/ay (38% tasarruf)
2. **Database tier optimize**: GP_Gen5_4 → GP_Gen5_2: $450 → $225/ay
3. **Auto-scaling**: Gece saatleri küçült: $50/ay tasarruf
4. **CDN ekle**: Bandwidth $80 → $30/ay

**Yeni Maliyet**: $1,200 → $630/ay (%48 tasarruf = $6,840/yıl)

**Çaba**: 2 gün
**Güven**: Yüksek (%90)
```

---

## Blue-Green Deployment

```markdown
### Mevcut: Direct Production Deploy (downtime var)

**Sorun**: Deploy sırasında 2-5 dakika downtime

**Blue-Green Strategy**:

```yaml
# Blue environment (mevcut production)
blue:
  instances: 3
  version: v1.2.0
  traffic: 100%

# Green environment (yeni version)
green:
  instances: 3
  version: v1.3.0
  traffic: 0%

# Deploy sequence:
1. Deploy v1.3.0 to green
2. Health check green
3. Route 10% traffic to green (canary)
4. Monitor errors (10 dakika)
5. If OK: Route 100% to green
6. If ERROR: Route back to blue (instant rollback)
7. Keep blue alive 24 hours (safety net)
```

**Fayda**:
- Zero-downtime deployment
- Instant rollback (<30 saniye)
- A/B test capability

**Çaba**: 3 gün (setup)
**Güven**: Orta (%70, kompleks setup)
```

---

## Container Security

```markdown
### Security Scan Results

**Trivy Scan**:
```bash
trivy image myapp:latest --severity HIGH,CRITICAL

# Results:
Total: 15 vulnerabilities
HIGH: 12
CRITICAL: 3
```

**Kritik Güvenlik Açıkları**:

1. **CVE-2023-1234**: OpenSSL vulnerability
   - **Fix**: Base image güncelle (node:18 → node:18.19)
   - **Çaba**: 10 dakika

2. **CVE-2023-5678**: npm package vulnerability
   - **Fix**: npm audit fix --force
   - **Çaba**: 30 dakika

**Öneri**: Her build'de security scan çalıştır
```yaml
# .github/workflows/security.yml
- name: Security Scan
  run: |
    docker run --rm aquasec/trivy image myapp:latest
    if [ $? -ne 0 ]; then
      echo "Security vulnerabilities found!"
      exit 1
    fi
```

**Çaba**: 1 saat
**Güven**: Yüksek (%95)
```

---

## Success Metrics

```yaml
anlık (1 hafta):
  - Manual deployment: Kaldırıldı ✅
  - CI/CD pipeline: Çalışıyor ✅
  - Dockerfile optimize: 850 MB → 150 MB ✅

kısa_vade (1 ay):
  - Deployment zamanı: 45 dk → 5 dk
  - Deployment hata oranı: %40 → %5
  - Rollback süresi: 30 dk → 2 dk

uzun_vade (3 ay):
  - Infrastructure as Code: %100 kodlanmış
  - Cloud maliyet: $1,200 → $630/ay (%48 azalma)
  - Zero-downtime deployment: Aktif
```

---

## Tools & Services

```yaml
ci_cd:
  - GitHub Actions (en popüler)
  - GitLab CI/CD
  - Jenkins
  - Azure DevOps

containerization:
  - Docker (standart)
  - Podman (daemonless alternatif)
  - containerd (low-level)

orchestration:
  - Kubernetes (kompleks ama güçlü)
  - Docker Swarm (basit)
  - Nomad (HashiCorp)

iac:
  - Terraform (multi-cloud)
  - Pulumi (code-based)
  - Ansible (configuration management)

monitoring:
  - Prometheus + Grafana
  - Azure Application Insights
  - Datadog
  - New Relic
```

---

**Analiz Tamamlandı** | Infrastructure Skoru: 6/10 | Güven: Yüksek (%85)
