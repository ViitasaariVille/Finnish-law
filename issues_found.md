# Issues Found: Business Rules vs. Liikennevakuutuslaki (460/2016)

## Issue #1: [CRITICAL] Missing time limits: claim filing, investigation, payment deadlines

### Problem
The DMN rules are missing critical time limits from Liikennevakuutuslaki (460/2016):

| Section | Requirement | Current DMN |
|---------|-------------|-------------|
| §61 | Claim filing: 3 years from knowledge | ❌ Missing |
| §61 | Absolute max: 10 years from accident | ❌ Missing |
| §62 | Investigation start: 7 business days | ❌ Missing |
| §62 | Payment deadline: 1 month from complete docs | ❌ Missing |
| §79 | Court action: 3 years from decision | ❌ Missing |

### Impact
Without these rules, the system cannot enforce statutory deadlines for claims handling.

### Suggested Fix
Add TIME-001 through TIME-007 rules from GAP_ANALYSIS_3rd_10x.md to main DMN rules file.

### References
- laws/liikennevakuutuslaki.txt §§61, 62, 79
- liikennevakuutuslaki/analysis/GAP_ANALYSIS_3rd_10x.md

---

## Issue #2: [CRITICAL] Missing property damage maximum: €5,000,000 cap

### Problem
The DMN rules do not include the statutory maximum for property damage compensation.

**Law (§38):** Esinevahinkona korvataan enintään **5 000 000 euroa** kutakin vahingosta vastuussa olevaa liikennevakuutusta kohden.

**Current DMN:** E8 (Property Damage Compensation) has no maximum amount check.

### Impact
System may calculate compensation exceeding legal maximum.

### Suggested Fix
Add AMT-001 rule from GAP analysis to main DMN:
- Add maximum compensation check: 5,000,000 EUR per insurance
- Add pro-rata distribution if claims exceed maximum

### References
- laws/liikennevakuutuslaki.txt §38
- liikennevakuutuslaki/analysis/GAP_ANALYSIS_3rd_10x.md (AMT-001)

---

## Issue #3: [HIGH] Alcohol thresholds incomplete: missing exact BAC limits from §48

### Problem
DMN rules N9, N11, N17 simplify alcohol impairment rules but miss exact thresholds from law.

**Law (§48):**
- **≥1.2‰ BAC** (or ≥0.53mg/L breath): Denial or significant reduction
- **0.5-1.19‰ BAC** (or 0.22-0.52mg/L breath): Proportional reduction

**Current DMN:** Uses explicit BAC values but missing:
- Breathalyzer equivalents (mg/L)
- Drug impairment language (tuntuvasti huonontunut)
- Combined alcohol+drug effects

### Impact
May not correctly handle all impairment scenarios per statute.

### Suggested Fix
Update N9, N11, N17 to include:
1. Exact BAC thresholds (blood and breath)
2. Drug impairment conditions
3. Combined effects rule

### References
- laws/liikennevakuutuslaki.txt §48
- liikennevakuutuslaki/rules/car_insurance_dmn_rules.md (N9, N11, N17)

---

## Issue #4: [HIGH] Missing medical treatment procedure rules (§§53-59)

### Problem
DMN rules lack detailed medical treatment compensation procedures required by law.

**Law requirements (§§53-59):**
- §53: Treatment must be necessary and from authorized providers
- §54: Public healthcare = customer fee only
- §55: Full cost payment to municipality (täyskustannusmaksu)
- §56: **4 business days** notification deadline
- §57: Insurer right to direct to specific treatment facility (maksusitoumus)
- §58-59: Private healthcare requires prior approval (except emergency)

**Current DMN:** Only basic E5 (Medical Expense Compensation) exists.

### Impact
Cannot properly validate medical expense claims or enforce notification deadlines.

### Suggested Fix
Add rules for:
1. Treatment authorization workflow
2. Public vs private healthcare paths
3. 4-day notification requirement
4. Maksusitoumus requirement for private care

### References
- laws/liikennevakuutuslaki.txt §§53-59

---

## Issue #5: [MEDIUM] Missing index adjustment for continuous compensation (§35)

### Problem
DMN rules do not include annual index adjustment for ongoing compensation payments.

**Law (§35):** 
Jatkuvat korvaukset tarkistetaan kalenterivuosittain työntekijän eläkelain 98 §:ssä tarkoitetulla työeläkeindeksillä.

(Current DMN: FIN-003 exists in GAP analysis but not in main rules)

### Impact
Continuous compensation calculations will become inaccurate over time.

### Suggested Fix
Add FIN-003 to main DMN rules or create calculation rule for annual index adjustment.

### References
- laws/liikennevakuutuslaki.txt §35
- liikennevakuutuslaki/analysis/GAP_ANALYSIS_3rd_10x.md (FIN-003)

---

## Issue #6: [MEDIUM] Missing procedural rules: claims handling, certificates, appeals (§§60-72)

### Problem
DMN rules lack claims procedure rules required for operational implementation.

**Missing from §§60-72:**
- §60: Direct claim right to insurer
- §19: Claims history certificate within **15 days**
- §63: Decision justification requirements
- §65: Right to request Liikennevahinkolautakunta opinion
- §67: Delay interest calculation (Interest Act + increase)

### Impact
System cannot support full claims handling workflow.

### Suggested Fix
Add procedural rules to DMN or document as out-of-scope for business rules.

### References
- laws/liikennevakuutuslaki.txt §§60-72, §19

---

## Summary

| Priority | Issue | Sections |
|----------|-------|----------|
| 🔴 Critical | Time limits missing | §§61, 62, 79 |
| 🔴 Critical | €5M property damage cap | §38 |
| 🟡 High | Alcohol thresholds incomplete | §48 |
| 🟡 High | Medical treatment rules | §§53-59 |
| 🟢 Medium | Index adjustment | §35 |
| 🟢 Medium | Procedural rules | §§60-72, 19 |

*Created by MerriMoltBot on 2026-02-26*
