# Finnish Law Compliance Check Report
**Date:** February 26, 2026
**Repository:** ViitasaariVille/Finnish-law
**Branch:** master

---

## Executive Summary

This compliance check analyzed the Finnish Traffic Insurance Act (Liikennevakuutuslaki 460/2016) against the DMN business rules in `car_insurance_dmn_rules.md`.

### Key Findings:
- **24 law sections** are NOT covered by any DMN rule
- **11 local issue files** identify missing rules that are still valid
- **6 GitHub open issues** are all still valid and unfixed
- **1 GitHub issue** (194) appears to be already fixed/invalid

---

## 1. GitHub Issues Analysis

### OPEN Issues Status

| Issue | Title | Status | Reason |
|-------|-------|--------|--------|
| #194 | [BUG] E8 Property Damage table column misalignment | **CLOSE** | Already fixed - table columns align correctly |
| #195 | [TYPO] Duplicate section numbering 2.7 | **VALID** | Two sections labeled 2.7 exist (lines ~501 and ~900+) |
| #196 | [TYPO] Duplicate section numbering 0.2 | **VALID** | Two sections labeled 0.2 exist |
| #197 | Duplicate section number 2.8 appears 4 times | **VALID** | Sections 2.8, 2.8, 2.8, 2.8 should be 2.8-2.11 |
| #198 | Duplicate section numbers 2.15 and 2.15b | **VALID** | 2.15b should be 2.16 |
| #199 | Metadata says 35 decisions but actually has 91 | **VALID** | Metadata count needs updating |

**Recommendation:** Close issue #194 as already fixed. Leave others open for @VilleMoltBot to fix.

---

## 2. Local Issue Files Analysis

All 11 local issue files identify **VALID** gaps that are still missing from the DMN rules:

| File | Law Section | Description | Severity |
|------|-------------|-------------|----------|
| issue-001-section-10.md | §10(3) | 7-day liability termination rule | HIGH |
| issue-002-section-51.md | §51 | Multi-insurer liability apportionment | HIGH |
| issue-003-section-58.md | §58 | Emergency care without maksusitoumus | HIGH |
| issue-004-section-09.md | §9 | Insurer reporting to Traficom | HIGH |
| issue-005-section-13.md | §13(4) | Finnish resident law election right | HIGH |
| issue_29_penalty_procedure.md | §29 | Penalty decision procedure | CRITICAL |
| issue_30_use_prohibition.md | §30 | Vehicle use prohibition when uninsured | HIGH |
| issue_78_portfolio_transfer.md | §78 | Portfolio transfer effects on distribution | MEDIUM |
| issue_80_court_proceedings.md | §80 | Court proceedings and legal costs | CRITICAL |
| issue_86_88_info_center.md | §§86-88 | LVK information center operations | LOW |
| issue_93_94_insolvency.md | §§93-94 | Insolvency additional premium/joint guarantee | MEDIUM |

**All issues remain valid - no DMN rules exist for these sections.**

---

## 3. Comprehensive Law Section Coverage Analysis

### Sections NOT Covered (24 total):

**Chapters 1-2 (General/Insurance):**
- ❌ §1 - Application scope
- ❌ §2 - Definitions
- ❌ §11 - Insurance certificate and terms
- ❌ §13 - Insurance coverage area
- ❌ §14 - Disclosure obligation violation
- ❌ §15 - Risk increase notification failure
- ❌ §21 - Claims history data transfer
- ❌ §23 - Premium refund on termination
- ❌ §24 - Late payment interest
- ❌ §25 - Liability continuation

**Chapter 3 (Compensation):**
- ❌ §29 - Penalty procedure (CRITICAL - has issue file)
- ❌ §30 - Vehicle use prohibition (HIGH - has issue file)
- ❌ §31 - Compensation regardless of liability
- ❌ §33 - Multi-vehicle accident liability
- ❌ §51 - Insurer apportionment (HIGH - has issue file)

**Chapter 4 (Medical):**
- ❌ §9 - Insurer reporting (HIGH - has issue file)
- ❌ §13(4) - Law election right (HIGH - has issue file)
- ❌ §58 - Emergency care exception (HIGH - has issue file)
- ❌ §64 - Traffic Damage Board (mentioned but no rule)

**Chapter 5 (Procedure):**
- ❌ §80 - Court proceedings (CRITICAL - has issue file)

**Chapter 7 (Miscellaneous):**
- ❌ §84 - Insurer information sharing
- ❌ §86 - Information Center (LOW - has issue file)
- ❌ §87 - LVK additional duties (LOW - has issue file)
- ❌ §88 - Data sharing with LVK (LOW - has issue file)
- ❌ §93 - Additional premium (MEDIUM - has issue file)
- ❌ §94 - Joint guarantee (MEDIUM - has issue file)
- ❌ §95 - Official liability

### Covered Sections (71 total):

See full list in detailed analysis. Key covered sections include:
- ✅ §3 - Mandatory provisions (VAL-001)
- ✅ §4 - LVK scope (LVK-000)
- ✅ §5-8 - Insurance requirements, exemptions, border traffic
- ✅ §10 - Vehicle identification (partial - §10(3) missing)
- ✅ §12 - Insurance validity period
- ✅ §16 - Policy termination (TERM-001, TERM-002)
- ✅ §18 - Coverage during transfer (E15)
- ✅ §34-38 - Compensation calculation (E6, E7, E8 series)
- ✅ §39 - Rescue assistance (N19)
- ✅ §40-50 - Exclusions and denials (N1-N19)
- ✅ §52 - Rail-road liability (RAIL-001, RAIL-002)
- ✅ §53-59 - Medical treatment (E5, M1, M2 - §58 partially missing)
- ✅ §60-63, 65-79 - Time limits and procedures (E12, T1-T4)
- ✅ §81 - Municipality appeal rights
- ✅ §82-83 - Information access rights
- ✅ §85 - Document retention
- ✅ §89-92 - Premium calculation, insolvency protection

---

## 4. New Issues to Create

Based on compliance check, the following NEW issues should be created:

### Critical Priority:

**Issue: [MISSING] §33 Multi-Vehicle Accident Liability**
- **Description:** §33 defines liability in multi-vehicle accidents based on negligence, traffic violations, and vehicle condition. Currently only §51 (insurer apportionment) is flagged, but §33 (liability determination) is also missing.
- **Law Reference:** §33
- **Suggested Rule:** Create `MULTI-001: Multi-Vehicle Liability Determination (§33)`
- **Severity:** CRITICAL

### High Priority:

**Issue: [MISSING] §§23-25 Premium and Liability Rules**
- **Description:** Missing rules for premium refunds, late payment interest, and liability continuation when premium unpaid.
- **Law Reference:** §§23-25
- **Severity:** HIGH

**Issue: [MISSING] §§14-15 Contract Violation Consequences**
- **Description:** Missing rules for consequences of disclosure obligation violations and risk increase notification failures.
- **Law Reference:** §§14-15
- **Severity:** HIGH

### Medium Priority:

**Issue: [MISSING] §64 Traffic Damage Board Procedure**
- **Description:** §64 establishes the Traffic Damage Board (Liikennevahinkolautakunta). While mentioned in §66, no specific rule exists for Board procedures.
- **Law Reference:** §64
- **Severity:** MEDIUM

**Issue: [MISSING] §84 Insurer Information Sharing Rights**
- **Description:** §84 governs insurer rights to share information with healthcare providers for maksusitoumus and expert opinions.
- **Law Reference:** §84
- **Severity:** MEDIUM

**Issue: [MISSING] §95 Official Liability**
- **Description:** §95 establishes criminal and civil liability for insurer personnel and board members.
- **Law Reference:** §95
- **Severity:** MEDIUM

### Low Priority:

**Issue: [MISSING] §§1-2 General Definitions**
- **Description:** Basic application scope and definitions. May not need explicit DMN rules.
- **Law Reference:** §§1-2
- **Severity:** LOW

---

## 5. Recommendations

### Immediate Actions:
1. **Close GitHub issue #194** - already fixed
2. **Prioritize CRITICAL issues:** §29, §33, §80
3. **Address HIGH priority gaps:** §10(3), §14-15, §23-25, §30, §51, §58

### DMN Rule Development Priority:
1. **Critical:** §29, §33, §80 (court proceedings, penalties, multi-vehicle)
2. **High:** §10(3), §30, §51, §58 (liability termination, use prohibition, apportionment, emergency care)
3. **Medium:** §78, §84, §93-94, §95 (portfolio transfer, information sharing, insolvency, liability)
4. **Low:** §§86-88, §§1-2 (information center ops, general definitions)

### Quality Improvements:
1. **Fix section numbering:** Issues #195-198
2. **Update metadata:** Issue #199 (decision count)
3. **Add cross-references:** Link related sections (e.g., §33 to §51)

---

## 6. Compliance Metrics

| Metric | Value |
|--------|-------|
| Total Law Sections | 95 |
| Sections with DMN Rules | 71 (75%) |
| Sections Missing | 24 (25%) |
| Critical Missing | 3 (§29, §33, §80) |
| High Priority Missing | 7 |
| GitHub Open Issues | 6 |
| Local Issue Files | 11 |
| New Issues to Create | 7 |

---

*Report generated by law-compliance-check cron job*
*@VilleMoltBot tagged for review*
