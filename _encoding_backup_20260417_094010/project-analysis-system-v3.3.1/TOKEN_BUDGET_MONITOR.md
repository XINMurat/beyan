# Token Budget Monitor - Real-time Context Window Tracking

**Module**: System Management  
**Priority**: P1  
**Version**: 1.0  
**Last Updated**: 20 AralÄ±k 2024

---

## ðŸŽ¯ AmaÃ§

KullanÄ±cÄ±ya **hangi modÃ¼llerin aktif olduÄŸunu** ve **ne kadar token kullanÄ±ldÄ±ÄŸÄ±nÄ±** gÃ¶stermek. Context window dolmadan Ã¶nce uyarÄ± vermek.

**Problem**: KullanÄ±cÄ± hangi analizlerin Ã§alÄ±ÅŸtÄ±ÄŸÄ±nÄ± bilmiyor, sistem sessizce modÃ¼l atlÄ±yor.

**Ã‡Ã¶zÃ¼m**: Real-time dashboard ve akÄ±llÄ± uyarÄ±lar.

---

## ðŸ“Š Dashboard Format

### Minimal Version (Her Raporda)

```markdown
## ðŸ“¦ Loaded Modules

**Active**: 7/10 modules  
**Token Usage**: 18,500 / 30,000 (62%)  
**Status**: ðŸŸ¢ Healthy

âœ… Loaded:
- file_structure_analysis (2,000 tokens)
- performance_analysis (2,500 tokens)
- security_analysis (2,800 tokens)
- api_design_analysis (2,000 tokens)
- database_analysis (2,500 tokens)
- hidden_gems_deep_scan (2,500 tokens)
- ui_ux_analysis (3,000 tokens)

â­ï¸ Skipped (budget limit):
- accessibility_analysis (would exceed budget)
- seo_analysis (P3, not requested)
- analytics_analysis (P3, not requested)

ðŸ”— Auto-loaded dependencies: 1
- hidden_gems_deep_scan â†’ file_structure_analysis
```

---

### Detailed Version (On Request)

```markdown
## ðŸ“Š Token Budget Report

**Budget**: 30,000 tokens  
**Used**: 18,500 tokens (62%)  
**Available**: 11,500 tokens (38%)  
**Status**: ðŸŸ¢ Healthy (>25% free)

### Module Breakdown

| Module | Tokens | Priority | Status | Reason |
|--------|--------|----------|--------|--------|
| BASE_PROMPT.md | 5,000 | SYSTEM | âœ… Loaded | Always loaded |
| file_structure_analysis | 2,000 | P0 | âœ… Loaded | Auto-load |
| performance_analysis | 2,500 | P0 | âœ… Loaded | web_app detected |
| ui_ux_analysis | 3,000 | P0 | âœ… Loaded | web_app detected |
| security_analysis | 2,800 | P1 | âœ… Loaded | production detected |
| database_analysis | 2,500 | P1 | âœ… Loaded | backend detected |
| api_design_analysis | 2,000 | P1 | âœ… Loaded | api detected |
| hidden_gems_deep_scan | 2,500 | P1 | âœ… Loaded | auto_load: true |
| accessibility_analysis | 2,200 | P2 | â­ï¸ Skipped | Budget limit |
| seo_analysis | 1,500 | P3 | â­ï¸ Skipped | Not requested |
| analytics_analysis | 1,200 | P3 | â­ï¸ Skipped | Not requested |

### Token Distribution

```
â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 62% Used (18,500)
â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘ 38% Free (11,500)

P0 modules:  7,500 tokens (41%)
P1 modules:  9,800 tokens (53%)
P2 modules:  0 tokens (0%)
P3 modules:  0 tokens (0%)
SYSTEM:      5,000 tokens (27%)
```

### Recommendations

ðŸ’¡ **You can still load**:
- accessibility_analysis (2,200 tokens) - will use 69% total
- testing_strategy (2,000 tokens) - will use 68% total

âš ï¸ **Cannot load without dropping**:
- All P0 + P1 + P2 modules (would exceed 30K)

ðŸŽ¯ **For full coverage**:
- Current: 7/10 requested modules
- To load all 10: Need 32,700 tokens (would exceed budget by 2,700)
- Solution: Drop 1 P1 module (e.g., hidden_gems_deep_scan)
```

---

## ðŸš¨ Warning Levels

### ðŸŸ¢ Healthy (<75% used)
```markdown
ðŸ“Š Token Budget: 18,500 / 30,000 (62%) ðŸŸ¢ Healthy
```

**Action**: None, all good

---

### ðŸŸ¡ Warning (75-85% used)
```markdown
âš ï¸ Token Budget: 24,000 / 30,000 (80%) ðŸŸ¡ Warning

You're approaching the limit. Consider:
- Skip P3 modules
- Use quick_scan strategy instead of full_audit
```

**Action**: Suggest optimization

---

### ðŸŸ  Critical (85-95% used)
```markdown
ðŸš¨ Token Budget: 27,000 / 30,000 (90%) ðŸŸ  Critical

Budget almost full! Automatically dropped:
- P3 modules (seo_analysis, analytics_analysis)
- Lower priority P2 (browser_compatibility)

Still loaded: P0, P1, critical P2
```

**Action**: Auto-drop P3, warn user

---

### ðŸ”´ Exceeded (>95% used)
```markdown
âŒ Token Budget: 29,500 / 30,000 (98%) ðŸ”´ EXCEEDED

Cannot load all requested modules. Dropping lowest priority:
1. âŒ Dropped: analytics_analysis (P3)
2. âŒ Dropped: seo_analysis (P3)
3. âŒ Dropped: browser_compatibility (P2)

Loaded: P0, P1 only
```

**Action**: Emergency drop, keep P0/P1 only

---

## ðŸŽ›ï¸ Smart Budget Management

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
ðŸš¨ Budget limit reached!

You requested 12 modules, but budget allows only 9.

Which modules are most important?

High Priority (will load):
âœ… file_structure_analysis (P0)
âœ… performance_analysis (P0)
âœ… security_analysis (P1)

Medium Priority (your choice - pick 6):
[ ] ui_ux_analysis (3,000 tokens)
[ ] api_design_analysis (2,000 tokens)
[ ] database_analysis (2,500 tokens)
[ ] accessibility_analysis (2,200 tokens)
[ ] testing_strategy (2,000 tokens)
[ ] hidden_gems_deep_scan (2,500 tokens)

Low Priority (will skip):
â­ï¸ seo_analysis (P3)
â­ï¸ analytics_analysis (P3)
```

**User Input**: Select 6 checkboxes â†’ System loads only those

---

## ðŸ“ˆ Token Tracking During Execution

### Progressive Loading

```markdown
ðŸ”„ Loading modules...

[â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘] 40% - Loaded BASE_PROMPT (5,000)
[â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘] 60% - Loaded file_structure (7,000 cumulative)
[â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘] 80% - Loaded performance (9,500 cumulative)
[â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ] 100% - All modules loaded (18,500 total)

âœ… Ready for analysis!
```

---

### Mid-Analysis Warning

```markdown
âš ï¸ Token budget update:

Started: 18,500 / 30,000 (62%)
Current: 26,000 / 30,000 (87%) ðŸŸ 

Reason: Large project files analyzed
Action: Skipping P3 modules for response
```

---

## ðŸ” Module Selection Helper

### Interactive Mode

```markdown
ðŸŽ¯ Module Selection Helper

Your project type: Web App (React + TypeScript)
Auto-detected modules: 8
Token budget: 30,000

Recommendations:

Must Have (P0):
âœ… file_structure_analysis
âœ… performance_analysis
âœ… ui_ux_analysis

Highly Recommended (P1):
âœ… react_typescript_analysis
âœ… security_analysis
[ ] api_design_analysis (skip if no backend API)

Nice to Have (P2):
[ ] accessibility_analysis (government/public sites)
[ ] testing_strategy (if coverage >50%)
[ ] state_management_analysis (large apps)

Optional (P3):
[ ] seo_analysis
[ ] analytics_analysis

Current selection: 18,500 tokens (62%) ðŸŸ¢

Want to:
[A] Load all recommended (21,300 tokens - 71%)
[B] Customize selection
[C] Load only must-have (10,000 tokens - 33%)
```

---

## ðŸ’¡ Optimization Tips

### Tip 1: Use Loading Strategies

```markdown
Instead of: "analyze my project" (loads 8+ modules)

Try:
- "quick_scan" â†’ 1 module (7,000 tokens)
- "frontend_focus" â†’ 5 modules (15,000 tokens)
- "backend_focus" â†’ 4 modules (12,000 tokens)

This saves tokens for deeper analysis!
```

### Tip 2: Sequential Analysis

```markdown
Run 1: "quick_scan" â†’ Get overview (7K tokens)
Run 2: "security review" â†’ Deep dive (2.8K tokens)
Run 3: "performance analysis" â†’ Optimize (2.5K tokens)

Total: 12.3K tokens across 3 runs
vs. 
Full audit: 25K tokens in 1 run

Benefit: More targeted, clearer results
```

### Tip 3: Module Caching (Future)

```markdown
ðŸ’¡ Idea for v3.4:

First run: Load all modules â†’ Cache results
Next runs: Reuse cached modules, only re-analyze changed files

Token savings: ~60% on subsequent runs
```

---

## ðŸŽ¯ User Preferences

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

## ðŸ“Š Statistics & Reporting

### Summary Stats

```markdown
## ðŸ“ˆ Token Usage Statistics

**Last 7 Days**:
- Average usage: 19,200 tokens (64%)
- Peak usage: 27,500 tokens (92%) - Dec 15
- Most loaded module: security_analysis (7 times)
- Most skipped module: analytics_analysis (5 times)

**Optimization Score**: 8/10 ðŸŸ¢
- You're using budget efficiently
- Consider using loading strategies more often
```

---

## ðŸ§ª Testing

### Test Scenarios

```markdown
Scenario 1: Budget OK
Input: 10 modules, 18K tokens
Expected: All loaded, ðŸŸ¢ status

Scenario 2: Budget Warning
Input: 12 modules, 25K tokens
Expected: All loaded, ðŸŸ¡ warning

Scenario 3: Budget Exceeded
Input: 15 modules, 32K tokens
Expected: Drop 3 lowest priority, ðŸŸ  critical

Scenario 4: User Preference
Input: 10 modules, user prefers security
Expected: Load security first, drop others if needed
```

---

## ðŸ”— Integration

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
4. Check token budget â† TOKEN_BUDGET_MONITOR
5. Drop lowest priority if needed
6. Load modules
7. Show dashboard â† TOKEN_BUDGET_MONITOR
8. Analyze
9. Report
```

---

## ðŸŽ“ FAQs

**Q: Why was my module skipped?**  
A: Check token budget. If >85% used, P3/P2 modules auto-drop.

**Q: Can I force-load a P3 module?**  
A: Yes, use "load seo_analysis" explicitly, or drop another module.

**Q: How do I increase budget?**  
A: Edit `.ai-budget-preferences.yml` but beware - larger context = slower responses.

**Q: What's the optimal budget?**  
A: 20-25K tokens gives best balance of coverage vs. speed.

---

**Ã–zet**: Token budget artÄ±k gÃ¶rÃ¼nÃ¼r ve kontrol edilebilir. KullanÄ±cÄ± her zaman ne olduÄŸunu bilir. ðŸ“Š

---

**Version**: 1.0  
**Next Feature**: Module caching (v3.4)  
**Feedback**: KullanÄ±cÄ±lar dashboard'u faydalÄ± buluyor mu?
