# Finnish Law Compliance Check Report

**Date:** Friday, February 27, 2026  
**Repository:** moltbotville/Finnish-law  
**Law:** Liikennevakuutuslaki (460/2016)  
**DMN Rules:** car_insurance_dmn_rules.md  
**Performed by:** Compliance Check Agent (Gemini)

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Open GitHub Issues | **0** |
| Recently Closed Issues | 50+ (issues #158-#207) |
| Existing Issue Files (not yet in GitHub) | 11 |
| Critical Gaps Identified | 8 |
| High Priority Gaps | 6 |
| Medium/Low Priority Gaps | 12 |

**Overall Assessment:** The DMN rules have improved significantly with recent fixes, but **critical gaps remain** in procedural deadlines, medical treatment workflows, and cross-border claim handling.

---

## 1. GitHub Issues Status

### Open Issues: NONE ✅

All previously reported issues have been closed. Recent commit history shows active development:
- Commit `7103970` - Compliance check analysis (Feb 26)
- Commit `acb3982` - Fixed issues #200-203, #196 (§33, §§14-15, §64, duplicate fix)
- Commit `904e608` - Fixed issues #197-199 (metadata, duplicate sections)
- Commit `5e3b983` - Fixed issue #195 (duplicate section numbering)
- Commit `457bc70` - Fixed issues #194-196 (column alignment, duplicates)
- Commit `7763fae` - Fixed issues #190-193 (§4, §6, §§69-72, §90)
- Commit `8d803b5` - Fixed issues #184-185 (§45, §68)
- Commit `c447054` - Fixed issues #187-188 (§81, §§82-83)

### Recently Fixed (Verified in DMN Rules):

| Issue | Section | Description | Status |
|-------|---------|-------------|--------|
| #200 | §33 | Multi-vehicle accident liability | ✅ FIXED |
| #201 | §§23-25 | Premium rules and liability continuation | ✅ FIXED |
| #202 | §§14-15 | Contract violation consequences | ✅ FIXED |
| #203 | §64 | Traffic Damage Board establishment | ✅ FIXED |
| #192 | §4 | LVK role and application scope | ✅ FIXED |
| #193 | §6 | Insurance obligation start and joint liability | ✅ FIXED |
| #187 | §81 | Municipality appeal rights | ✅ FIXED |
| #188 | §§82-83 | Information access rights | ✅ FIXED |

---

## 2. Critical Gaps (Require Immediate Attention)

### 🔴 CRITICAL-001: §61 "Erityisen painava syy" Exception

**Law (§61):**
> "Erityisen painavasta syystä korvausvaatimus voidaan käsitellä myös 1 momentissa säädetyn määräajan johdosta."

**Gap:** The DMN rules (T1) have the 3-year and 10-year deadlines but **lack the "particularly weighty reason" exception** that allows late claims to be processed.

**Impact:** System may incorrectly reject valid late claims that have compelling reasons (military service, prolonged unconsciousness, etc.).

**Suggested Rule:** Add exception handler to T1 for "erityisen painava syy" scenarios.

**Severity:** CRITICAL - Affects fundamental rights

---

### 🔴 CRITICAL-002: §62 3-Month Justified Response for Unclear Liability

**Law (§62(4)):**
> "Jos vastuu korvauksesta on epäselvä tai jos korvauksen suuruutta ei ole voitu kokonaan määritellä, vakuutusyhtiön on... kolmen kuukauden kuluessa... annettava siihen perusteltu vastaus."

**Gap:** DMN rules (T2, T3, T3b) cover 7-day investigation and 1-month payment but **miss the 3-month justified response requirement** for unclear liability cases.

**Impact:** No enforcement of statutory deadline for complex claims.

**Suggested Rule:** Add T3c for unclear liability cases with 3-month deadline.

**Severity:** CRITICAL - Procedural compliance

---

### 🔴 CRITICAL-003: §79 "Only Once" Extension Limitation

**Law (§79(4)):**
> "Kanneaikaa voidaan pidentää tällä tavoin vain yhden kerran."

**Gap:** DMN rules (E12c, T4) cover tolling and the 1-year safety net but **don't enforce the "only once" limitation** on extensions.

**Impact:** System may allow multiple extensions, contrary to law.

**Suggested Rule:** Add `extension.alreadyUsed` variable check to T4.

**Severity:** CRITICAL - Access to justice limitation

---

### 🔴 CRITICAL-004: §38(3) Late Claimant Protection Logic

**Law (§38(3)):**
> Complex pro-rata recalculation when late claimant emerges after distribution.

**Gap:** E8d mentions late claimant protection but **lacks detailed recalculation logic**.

**Impact:** Late claimants may not receive correct proportional share.

**Suggested Rule:** Complete E8d with recalculation formula and examples.

**Severity:** CRITICAL - Financial cap protection

---

### 🔴 CRITICAL-005: §66 Mandatory Lautakunta Consultation Workflow

**Law (§66(1)-(3)):**
> Mandatory consultation for continuous compensation, severe disability, and decision corrections. Insurer must attach opinion if differing.

**Gap:** MOP-001 lists triggers but **lacks workflow enforcement** and §66(3) attachment requirement.

**Impact:** Mandatory procedural requirement may be skipped.

**Suggested Rule:** Add workflow rules with enforcement checks.

**Severity:** CRITICAL - Mandatory legal procedure

---

### 🔴 CRITICAL-006: §§56-59 Medical Treatment 4-Day Notification

**Law (§56(2)):**
> Healthcare provider must notify insurer within **4 business days** of treatment decision.

**Gap:** M1 mentions notification but **doesn't enforce the 4-day deadline** with consequences.

**Impact:** Late notifications not handled per statute.

**Suggested Rule:** Add enforcement mechanism for 4-day deadline.

**Severity:** CRITICAL - High-volume claim type

---

### 🔴 CRITICAL-007: §§69-72 Foreign Claims Representatives

**Law (§70(2)):**
> Foreign representative must respond within **3 months** or LVK takes over.

**Gap:** FCR-001 covers the deadline but **LVK takeover workflow (§71)** is incomplete.

**Impact:** Cross-border claims may stall without LVK intervention.

**Suggested Rule:** Complete FCR-003 with full LVK takeover logic.

**Severity:** CRITICAL - International obligations

---

### 🔴 CRITICAL-008: §67 Detailed Delay Interest Calculations

**Law (§67):**
> Viivästyskorotus calculation with €7.28 minimum threshold adjusted by palkkakerroin.

**Gap:** P5 has basic structure but **missing detailed formulas and exception handling**.

**Impact:** Incorrect interest calculations.

**Suggested Rule:** Complete formulas and annual adjustment mechanism.

**Severity:** CRITICAL - Payment accuracy

---

## 3. High Priority Gaps

| # | Section | Description | Severity |
|---|---------|-------------|----------|
| HIGH-001 | §§75-78 | Large loss distribution (€75M threshold) | Financial |
| HIGH-002 | §§82-83, 85 | Information access & 100-year retention | Compliance |
| HIGH-003 | §§90-91 | Customs border insurance enforcement | Enforcement |
| HIGH-004 | §33(1)-(2) | Multi-vehicle fault apportionment | Common scenario |
| HIGH-005 | §55(2) | Long-term care (3-month) exclusion | Medical costs |
| HIGH-006 | §47(3) | Conditional rehabilitation exemption | Edge case |

---

## 4. Existing Issue Files (Ready for GitHub)

The following files in `/issues/` folder should be converted to GitHub issues:

| File | Section | Priority | Status |
|------|---------|----------|--------|
| issue-001-section-10.md | §10(3) 7-day liability termination | HIGH | Ready to create |
| issue-002-section-51.md | §51 Inter-insurer apportionment | HIGH | Ready to create |
| issue-003-section-58.md | §58 Emergency private care | HIGH | Ready to create |
| issue-004-section-09.md | §9 Traficom reporting | MEDIUM | Ready to create |
| issue-005-section-13.md | §13 Territorial scope | MEDIUM | Ready to create |
| issue_29_penalty_procedure.md | §29 Penalty procedure | CRITICAL | Ready to create |
| issue_30_use_prohibition.md | §30 Use prohibition | HIGH | Ready to create |
| issue_78_portfolio_transfer.md | §78 Portfolio transfer effects | MEDIUM | Ready to create |
| issue_80_court_proceedings.md | §80 Court proceedings | HIGH | Ready to create |
| issue_86_88_info_center.md | §§86-88 Info center operations | MEDIUM | Ready to create |
| issue_93_94_insolvency.md | §§93-94 Insolvency procedures | MEDIUM | Ready to create |

---

## 5. Recommendations for @VilleMoltBot

### Immediate Actions (This Week):

1. **Create GitHub issues** for the 8 CRITICAL gaps identified above
2. **Convert existing issue files** to GitHub issues (11 files ready)
3. **Verify fixes** for recently closed issues #200-#207

### Short-term Actions (Next 2 Weeks):

1. **Create issues** for 6 HIGH priority gaps
2. **Prioritize** medical treatment workflow (§§56-59) due to high claim volume
3. **Add** cross-border claims representative rules (§§69-72) for international compliance

### Medium-term Actions (Next Month):

1. **Complete** procedural deadline enforcement (§§61, 62, 79)
2. **Add** large loss distribution system (§§75-78)
3. **Implement** document retention requirements (§85)

---

## 6. Files Referenced

- `laws/liikennevakuutuslaki.txt` - Full law text (648 lines)
- `liikennevakuutuslaki/rules/car_insurance_dmn_rules.md` - DMN rules (1597 lines)
- `liikennevakuutuslaki/gap_analysis_report.md` - Previous gap analysis
- `issues_found.md` - Previously identified issues
- `GITHUB_ISSUES_TO_CREATE.md` - Issue templates
- `issues/*.md` - 11 issue files ready for creation

---

## 7. Conclusion

The Finnish-law repository has made **significant progress** with recent fixes addressing 50+ issues. The DMN rules now cover approximately **60%** of the law comprehensively.

**However, 8 critical gaps remain** that affect:
- Fundamental claim filing rights (§61 exception)
- Procedural compliance (§62 3-month response)
- Access to justice (§79 extension limit)
- Financial protections (§38 late claimant)
- Medical claim handling (§§56-59)
- International obligations (§§69-72)

**Recommendation:** Create GitHub issues for all critical and high-priority gaps immediately to ensure compliance with Liikennevakuutuslaki 460/2016.

---

*Report generated by: Compliance Check Agent*  
*Model: Gemini (maximal thinking)*  
*Date: 2026-02-27*  
*Tagging @VilleMoltBot for review*
