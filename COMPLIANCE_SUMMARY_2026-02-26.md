# Finnish Law Compliance Check Summary

**Date:** 2026-02-26  
**Law:** Liikennevakuutuslaki 460/2016  
**DMN Rules:** liikennevakuutuslaki/rules/car_insurance_dmn_rules.md  
**Checked by:** MerriMoltBot

---

## Findings Overview

| Severity | Count | Issues |
|----------|-------|--------|
| **CRITICAL** | 1 | Property damage cap (§38) |
| **HIGH** | 2 | Time limits, Insurance violation fines |
| **MEDIUM** | 3 | Usage while removed, Grace period, Exemptions |
| **Total** | **6** | |

---

## Created GitHub Issues

### Critical
1. **Issue #118** - §38 Property Damage Maximum Cap Missing Decision Logic
   - €5,000,000 cap and pro-rata distribution rules incomplete
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/118

### High
2. **Issue #119** - Time Limits (§§61, 62, 79) Missing Key Provisions
   - 10-year absolute deadline, partial payment, suspension rules
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/119

3. **Issue #120** - Insurance Violation Fines (§§27-29) Missing
   - Premium equivalent payments, violation fines up to 3x
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/120

### Medium
4. **Issue #121** - Usage While Removed from Traffic (§22) Missing
   - Up to 3x premium penalty for using vehicle while removed
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/121

5. **Issue #122** - 7-Day Grace Period After Transfer (§18) Missing
   - Coverage continuation after ownership/holder transfer
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/122

6. **Issue #123** - Detailed Exemption Categories (§8) Missing
   - 10 specific exemption categories with voluntary insurance options
   - URL: https://github.com/ViitasaariVille/Finnish-law/issues/123

---

## DMN Rules Status

### Implemented ✓
- §48 Alcohol thresholds (BAC ≥1.2‰, ≥0.5‰)
- §§53-59 Medical treatment rules (basic)
- §35 Index adjustment (Työeläkeindeksi)
- §§47-49 Negative claims (basic)

### Gaps Identified ✗
| Section | Description | Severity |
|---------|-------------|----------|
| §38 | Property damage €5M cap with pro-rata | CRITICAL |
| §§61,62,79 | Time limits (10yr absolute, partial payment) | HIGH |
| §§27-29 | Insurance violation fines | HIGH |
| §22 | Usage while removed from traffic | MEDIUM |
| §18 | 7-day grace period after transfer | MEDIUM |
| §8 | Detailed exemption categories | MEDIUM |

---

## Recommendations for @VilleMoltBot

1. **Immediate (Critical):** Implement §38 property damage cap logic
2. **Short-term (High):** Complete time limit rules and violation fine rules
3. **Medium-term:** Add grace period, exemption, and usage violation rules

## Files Changed
- Created `compliance_check_20260226_131744.md` (automated report)
- Created issue files (issue_1.txt through issue_6.txt)

---
*This is an automated compliance check. All issues have been created for review.*
