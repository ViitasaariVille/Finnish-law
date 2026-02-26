# Finnish Law Compliance Check Report
**Date:** February 26, 2026, 4:14 PM UTC  
**Repository:** ViitasaariVille/Finnish-law  
**DMN Rules File:** liikennevakuutuslaki/rules/car_insurance_dmn_rules.md  
**Analyzer:** Agent (Maximal Thinking Mode)

---

## Executive Summary

| Category | Count |
|----------|-------|
| Issues to CLOSE (fixed in DMN) | 2 |
| DUPLICATE Issues | 2 |
| VALID Open Issues | 17 |
| NEW Discrepancies Found | 2 |

---

## 1. Automated Check Validation

The automated compliance script reported **time limits (§§61, 62, 79) as MISSING**, but this is **INCORRECT**. Upon detailed review:

| Law Section | DMN Location | Status |
|-------------|--------------|--------|
| §61 (3-year claim filing) | E12, T1 | ✅ **PRESENT** |
| §62 (7-day investigation, 1-month payment) | E12b, E12c, T2, T3, T3b | ✅ **PRESENT** |
| §79 (3-year court action, tolling) | E12c, T4 | ✅ **PRESENT** |

The DMN rules contain comprehensive time limit rules under sections E12/E12b/E12c and T1-T4.

---

## 2. Open GitHub Issues Analysis

### 2.1 Issues to CLOSE (Fixed in Recent DMN Update)

| Issue | Title | DMN Location | Fix Confirmed |
|-------|-------|--------------|---------------|
| #182 | Missing §40: Property damage exclusions | N18 (line 185) | ✅ **FIXED** |
| #183 | Missing §42: Work performance damage | N2a (line 107) | ✅ **FIXED** |

**#182 Details:** §40 rules exist as N18 "Owner/Holder Property Exclusion with Passenger Exception" including the passenger clothing/personal items exception and §40(3) special case.

**#183 Details:** §42 rules exist as N2a "Work Performance Damage" with complete decision table for stationary vehicle work exclusions.

---

### 2.2 DUPLICATE Issues

| Issue | Title | Duplicate Of | Action |
|-------|-------|--------------|--------|
| #186 | Missing §§69-72: Foreign representative | #191 (more detailed) | Close #186, keep #191 |
| #173 | Missing §9: Traficom reporting | #190 (§90 related) | Close #190 as duplicate, keep #173 |

**Recommendation:** Close #186 and #190 as duplicates. #191 and #173 have more complete descriptions.

---

### 2.3 VALID Open Issues (Still Missing from DMN)

| Issue | Title | Severity | Notes |
|-------|-------|----------|-------|
| #173 | Missing §9: Traficom reporting obligations | HIGH | No TRAF-001 rules found |
| #174 | Missing §10: 7-day liability termination | CRITICAL | E15 covers 7-day extension but not §10 reporting requirement |
| #175 | Missing §14: Information obligation violations | HIGH | Disclosure failure sanctions missing |
| #176 | Missing §15: Risk increase notification failure | HIGH | Premium adjustment rule missing |
| #177 | Missing §21: Claims history transfer | MEDIUM | 15-day transfer requirement missing |
| #178 | Missing §23: Premium refund minimum (€8) | MEDIUM | No refund threshold rules |
| #179 | Missing §24: Delay interest calculation | MEDIUM | Interest calculation rules missing |
| #180 | Missing §26: Premium claim limitation (5 years) | MEDIUM | Statute of limitations missing |
| #181 | Missing §27-28: Uninsured vehicle penalty fees | MEDIUM | P8/P9 exist for some but not complete |
| #184 | Missing §45-46: Guarantee fund coverage | CRITICAL | Partial (N7, N16) but needs enhancement |
| #185 | Missing §68: Beneficiary notification obligations | MEDIUM | Recipient notification rules missing |
| #187 | Missing §81: Municipality appeal rights | HIGH | Municipal appeal rights not in DMN |
| #188 | Missing §82-83: Information access rights | MEDIUM | Employer/medical data access missing |
| #189 | Missing §13(4): Finnish resident law election | MEDIUM | E3 exists but explicit election right missing |
| #190 | Missing §90: Traficom reporting obligations | HIGH | CUST-001 covers §91 Customs, not §90 Traficom |
| #191 | Incomplete §§69-72: Foreign claims representative | HIGH | Only FCR-001 (§70) exists; §69, §71, §72 missing |

---

## 3. NEW Discrepancies Found

During this analysis, 2 additional law sections were identified as not fully covered in the DMN rules:

### 3.1 Missing §4: Liikennevakuutuskeskus (Traffic Insurance Centre)

**Law Reference:** §4 - Liikennevakuutuskeskus

**Requirements:**
- Defines LVK as the entity covering damages when:
  - Foreign vehicle causes damage in Finland
  - Vehicle exempt from insurance requirement causes damage
  - Unknown vehicle causes damage
  - Insurance obligation is neglected
- LVK applies when 9, 11, 12, 14, 15, 20, 24, 25, 33-39, 49-52, 55-68, 73, 79-85, 95 § provisions apply

**Current DMN Status:** ❌ NOT IMPLEMENTED
- LVK is mentioned in various rules but no dedicated §4 decision table exists

**Suggested Severity:** HIGH

---

### 3.2 Missing §6: Insurance Obligation Start (Vakuuttamisvelvollisuuden alkaminen)

**Law Reference:** §6 - Vakuuttamisvelvolliset ja vakuuttamisvelvollisuuden alkaminen

**Requirements:**
1. Owner AND holder are BOTH obligated to insure vehicle from ownership/holdership transfer date
2. If multiple obligated parties → joint liability (yhteisvastuu)
3. Exception: Vehicle from another EEA country to Finland → obligation starts immediately when buyer accepts delivery, even if not yet registered

**Current DMN Status:** ⚠️ PARTIAL
- E1 and E4 reference insurance requirements
- Joint liability of owner AND holder is not explicitly modeled
- EEA import immediate coverage rule not explicitly in DMN

**Suggested Severity:** HIGH

---

## 4. Compliance Score

| Category | Covered | Partial | Missing | Score |
|----------|---------|---------|---------|-------|
| Core Coverage (§§31-52) | 18 | 2 | 2 | 90% |
| Time Limits (§§61, 62, 79) | 3 | 0 | 0 | 100% |
| Medical Treatment (§§53-59) | 4 | 0 | 0 | 100% |
| Procedural (§§60-72, 19) | 5 | 3 | 4 | 65% |
| Premium/Financial (§§20-30) | 3 | 2 | 5 | 50% |
| International (§§7, 13, 69-72) | 3 | 2 | 3 | 60% |
| LVK/Guarantee Fund (§§4, 43-46, 74) | 2 | 2 | 3 | 50% |

**Overall Compliance Score: ~72%**

---

## 5. Recommendations

### Immediate Actions:
1. **Close Issues #182 and #183** - Already fixed in DMN
2. **Close Issues #186 and #190** - Duplicates of #191 and #173
3. **Prioritize CRITICAL issues:** #174, #184
4. **Address HIGH severity issues:** #173, #175, #176, #187, #191

### New Issues to Create:
1. **§4 LVK Definition Rules** - Define LVK's role and when it applies
2. **§6 Insurance Obligation Start** - Joint owner/holder liability + EEA import rule

### DMN Enhancement Priorities:
1. Complete §§69-72 foreign representative rules (FCR-002, FCR-003, FCR-004)
2. Add §9 Traficom reporting obligations
3. Add §10 7-day liability termination rule
4. Enhance §45-46 guarantee fund coverage rules
5. Add §14-15 disclosure/risk notification violations

---

*Report generated by compliance check agent - February 26, 2026*
*For review by @VilleMoltBot*
