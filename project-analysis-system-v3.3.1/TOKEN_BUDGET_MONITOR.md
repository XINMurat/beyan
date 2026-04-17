# Token Budget Monitor - Real-time Context Window Tracking

**Module**: System Management  
**Priority**: P1  
**Version**: 1.0  
**Last Updated**: 20 Aralık 2024

---

## �??� Amaç

Kullanıcıya **hangi modüllerin aktif oldu�?unu** ve **ne kadar token kullanıldı�?ını** göstermek. Context window dolmadan önce uyarı vermek.

**Problem**: Kullanıcı hangi analizlerin çalı�?tı�?ını bilmiyor, sistem sessizce modül atlıyor.

**�?özüm**: Real-time dashboard ve akıllı uyarılar.

---

## �??? Dashboard Format

### Minimal Version (Her Raporda)

```markdown
## �??� Loaded Modules

**Active**: 7/10 modules  
**Token Usage**: 18,500 / 30,000 (62%)  
**Status**: �??� Healthy

�?? Loaded:
- file_structure_analysis (2,000 tokens)
- performance_analysis (2,500 tokens)
- security_analysis (2,800 tokens)
- api_design_analysis (2,000 tokens)
- database_analysis (2,500 tokens)
- hidden_gems_deep_scan (2,500 tokens)
- ui_ux_analysis (3,000 tokens)

⏭️ Skipped (budget limit):
- accessibility_analysis (would exceed budget)
- seo_analysis (P3, not requested)
- analytics_analysis (P3, not requested)

�??? Auto-loaded dependencies: 1
- hidden_gems_deep_scan �?? file_structure_analysis
```

---

### Detailed Version (On Request)

```markdown
## �??? Token Budget Report

**Budget**: 30,000 tokens  
**Used**: 18,500 tokens (62%)  
**Available**: 11,500 tokens (38%)  
**Status**: �??� Healthy (>25% free)

### Module Breakdown

| Module | Tokens | Priority | Status | Reason |
|--------|--------|----------|--------|--------|
| BASE_PROMPT.md | 5,000 | SYSTEM | �?? Loaded | Always loaded |
| file_structure_analysis | 2,000 | P0 | �?? Loaded | Auto-load |
| performance_analysis | 2,500 | P0 | �?? Loaded | web_app detected |
| ui_ux_analysis | 3,000 | P0 | �?? Loaded | web_app detected |
| security_analysis | 2,800 | P1 | �?? Loaded | production detected |
| database_analysis | 2,500 | P1 | �?? Loaded | backend detected |
| api_design_analysis | 2,000 | P1 | �?? Loaded | api detected |
| hidden_gems_deep_scan | 2,500 | P1 | �?? Loaded | auto_load: true |
| accessibility_analysis | 2,200 | P2 | ⏭️ Skipped | Budget limit |
| seo_analysis | 1,500 | P3 | ⏭️ Skipped | Not requested |
| analytics_analysis | 1,200 | P3 | ⏭️ Skipped | Not requested |

### Token Distribution

```
�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�?? 62% Used (18,500)
�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�?? 38% Free (11,500)

P0 modules:  7,500 tokens (41%)
P1 modules:  9,800 tokens (53%)
P2 modules:  0 tokens (0%)
P3 modules:  0 tokens (0%)
SYSTEM:      5,000 tokens (27%)
```

### Recommendations

�??� **You can still load**:
- accessibility_analysis (2,200 tokens) - will use 69% total
- testing_strategy (2,000 tokens) - will use 68% total

�?�️ **Cannot load without dropping**:
- All P0 + P1 + P2 modules (would exceed 30K)

�??� **For full coverage**:
- Current: 7/10 requested modules
- To load all 10: Need 32,700 tokens (would exceed budget by 2,700)
- Solution: Drop 1 P1 module (e.g., hidden_gems_deep_scan)
```

---

## �??� Warning Levels

### �??� Healthy (<75% used)
```markdown
�??? Token Budget: 18,500 / 30,000 (62%) �??� Healthy
```

**Action**: None, all good

---

### �??� Warning (75-85% used)
```markdown
�?�️ Token Budget: 24,000 / 30,000 (80%) �??� Warning

You're approaching the limit. Consider:
- Skip P3 modules
- Use quick_scan strategy instead of full_audit
```

**Action**: Suggest optimization

---

### �??� Critical (85-95% used)
```markdown
�??� Token Budget: 27,000 / 30,000 (90%) �??� Critical

Budget almost full! Automatically dropped:
- P3 modules (seo_analysis, analytics_analysis)
- Lower priority P2 (browser_compatibility)

Still loaded: P0, P1, critical P2
```

**Action**: Auto-drop P3, warn user

---

### �??� Exceeded (>95% used)
```markdown
�? Token Budget: 29,500 / 30,000 (98%) �??� EXCEEDED

Cannot load all requested modules. Dropping lowest priority:
1. �? Dropped: analytics_analysis (P3)
2. �? Dropped: seo_analysis (P3)
3. �? Dropped: browser_compatibility (P2)

Loaded: P0, P1 only
```

**Action**: Emergency drop, keep P0/P1 only

---

## �???️ Smart Budget Management

### Strategy 1: Priority-Based Dropping

```yaml
if budget_exceeded:
  drop_order:
    1. P3 modules (lowest priority)
    2. P2 optional modules
    3. SPECIALIZED modules (unless project-specific)
    4. P1 non-critical
  preserve:
    - All P0 modules (critical)
    - Required dependencies
    - Explicitly requested modules
```

### Strategy 2: User Choice

```markdown
�??� Budget limit reached!

You requested 12 modules, but budget allows only 9.

Which modules are most important?

High Priority (will load):
�?? file_structure_analysis (P0)
�?? performance_analysis (P0)
�?? security_analysis (P1)

Medium Priority (your choice - pick 6):
[ ] ui_ux_analysis (3,000 tokens)
[ ] api_design_analysis (2,000 tokens)
[ ] database_analysis (2,500 tokens)
[ ] accessibility_analysis (2,200 tokens)
[ ] testing_strategy (2,000 tokens)
[ ] hidden_gems_deep_scan (2,500 tokens)

Low Priority (will skip):
⏭️ seo_analysis (P3)
⏭️ analytics_analysis (P3)
```

**User Input**: Select 6 checkboxes �?? System loads only those

---

## �??? Token Tracking During Execution

### Progressive Loading

```markdown
�??? Loading modules...

[�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??] 40% - Loaded BASE_PROMPT (5,000)
[�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??] 60% - Loaded file_structure (7,000 cumulative)
[�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??] 80% - Loaded performance (9,500 cumulative)
[�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??�??] 100% - All modules loaded (18,500 total)

�?? Ready for analysis!
```

---

### Mid-Analysis Warning

```markdown
�?�️ Token budget update:

Started: 18,500 / 30,000 (62%)
Current: 26,000 / 30,000 (87%) �??�

Reason: Large project files analyzed
Action: Skipping P3 modules for response
```

---

## �??� Module Selection Helper

### Interactive Mode

```markdown
�??� Module Selection Helper

Your project type: Web App (React + TypeScript)
Auto-detected modules: 8
Token budget: 30,000

Recommendations:

Must Have (P0):
�?? file_structure_analysis
�?? performance_analysis
�?? ui_ux_analysis

Highly Recommended (P1):
�?? react_typescript_analysis
�?? security_analysis
[ ] api_design_analysis (skip if no backend API)

Nice to Have (P2):
[ ] accessibility_analysis (government/public sites)
[ ] testing_strategy (if coverage >50%)
[ ] state_management_analysis (large apps)

Optional (P3):
[ ] seo_analysis
[ ] analytics_analysis

Current selection: 18,500 tokens (62%) �??�

Want to:
[A] Load all recommended (21,300 tokens - 71%)
[B] Customize selection
[C] Load only must-have (10,000 tokens - 33%)
```

---

## �??� Optimization Tips

### Tip 1: Use Loading Strategies

```markdown
Instead of: "analyze my project" (loads 8+ modules)

Try:
- "quick_scan" �?? 1 module (7,000 tokens)
- "frontend_focus" �?? 5 modules (15,000 tokens)
- "backend_focus" �?? 4 modules (12,000 tokens)

This saves tokens for deeper analysis!
```

### Tip 2: Sequential Analysis

```markdown
Run 1: "quick_scan" �?? Get overview (7K tokens)
Run 2: "security review" �?? Deep dive (2.8K tokens)
Run 3: "performance analysis" �?? Optimize (2.5K tokens)

Total: 12.3K tokens across 3 runs
vs. 
Full audit: 25K tokens in 1 run

Benefit: More targeted, clearer results
```

### Tip 3: Module Caching (Future)

```markdown
�??� Idea for v3.4:

First run: Load all modules �?? Cache results
Next runs: Reuse cached modules, only re-analyze changed files

Token savings: ~60% on subsequent runs
```

---

## �??� User Preferences

```yaml
# .ai-budget-preferences.yml

token_budget:
  # Default budget
  max_tokens: 30000
  
  # Preferred buffer (don't use last X%)
  safety_buffer: 15%  # Keep 15% free
  
  # Auto-drop behavior
  auto_drop_enabled: true
  auto_drop_priority: ["P3", "P2_optional"]
  
  # User confirmation
  confirm_before_drop: true  # Ask before dropping modules
  
  # Favorite modules (never drop)
  always_load:
    - security_analysis
    - performance_analysis
  
  # Never load (unless explicitly requested)
  blacklist:
    - seo_analysis  # We don't care about SEO
```

---

## �??? Statistics & Reporting

### Summary Stats

```markdown
## �??? Token Usage Statistics

**Last 7 Days**:
- Average usage: 19,200 tokens (64%)
- Peak usage: 27,500 tokens (92%) - Dec 15
- Most loaded module: security_analysis (7 times)
- Most skipped module: analytics_analysis (5 times)

**Optimization Score**: 8/10 �??�
- You're using budget efficiently
- Consider using loading strategies more often
```

---

## �?�� Testing

### Test Scenarios

```markdown
Scenario 1: Budget OK
Input: 10 modules, 18K tokens
Expected: All loaded, �??� status

Scenario 2: Budget Warning
Input: 12 modules, 25K tokens
Expected: All loaded, �??� warning

Scenario 3: Budget Exceeded
Input: 15 modules, 32K tokens
Expected: Drop 3 lowest priority, �??� critical

Scenario 4: User Preference
Input: 10 modules, user prefers security
Expected: Load security first, drop others if needed
```

---

## �??? Integration

### With MANIFEST_V2.yaml

```yaml
# MANIFEST reads user preferences
token_budget: 
  read_from: ".ai-budget-preferences.yml"
  fallback: 30000
  
# Module loading respects budget
loading_strategies:
  standard_analysis:
    check_budget_before_load: true
    drop_if_exceeded: true
```

### With ORCHESTRATOR

```markdown
ORCHESTRATOR:
1. Read MANIFEST_V2.yaml
2. Detect project type
3. Select modules
4. Check token budget �?� TOKEN_BUDGET_MONITOR
5. Drop lowest priority if needed
6. Load modules
7. Show dashboard �?� TOKEN_BUDGET_MONITOR
8. Analyze
9. Report
```

---

## �??? FAQs

**Q: Why was my module skipped?**  
A: Check token budget. If >85% used, P3/P2 modules auto-drop.

**Q: Can I force-load a P3 module?**  
A: Yes, use "load seo_analysis" explicitly, or drop another module.

**Q: How do I increase budget?**  
A: Edit `.ai-budget-preferences.yml` but beware - larger context = slower responses.

**Q: What's the optimal budget?**  
A: 20-25K tokens gives best balance of coverage vs. speed.

---

**�?zet**: Token budget artık görünür ve kontrol edilebilir. Kullanıcı her zaman ne oldu�?unu bilir. �???

---

**Version**: 1.0  
**Next Feature**: Module caching (v3.4)  
**Feedback**: Kullanıcılar dashboard'u faydalı buluyor mu?
