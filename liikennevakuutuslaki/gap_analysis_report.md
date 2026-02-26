# Gap Analysis Report: Finnish Traffic Insurance Act vs DMN Rules
## Liikennevakuutuslaki 460/2016

**Analysis Date:** 2026-02-26  
**Law Version:** 460/2016 (648 lines)  
**DMN Rules Version:** car_insurance_dmn_rules.md (1368 lines)

---

## 1. SUMMARY STATISTICS

| Metric | Count |
|--------|-------|
| Total Sections in Law | 99 sections (excluding §41a which doesn't exist in law) |
| Sections Fully Implemented | ~45 sections |
| Sections Partially Implemented | ~12 sections |
| Sections NOT Implemented | ~42 sections |
| **Critical Gaps** | **8 sections** |
| **High Priority Gaps** | **12 sections** |
| **Medium/Low Priority Gaps** | **22 sections** |

---

## 2. CRITICAL GAPS (Require Immediate Attention)

### §61 - Claim Filing Time Limits ⏰ CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
- Claims must be filed within **3 years** from when claimant learned of damage
- Absolute deadline: **10 years** from damage occurrence
- "Erityisen painava syy" (particularly weighty reason) allows late processing

**DMN Implementation (E12, T1):**
- ✓ Basic 3-year and 10-year deadlines implemented
- ✗ "Erityisen painava syy" exception not fully modeled
- ✗ Claim filing notification rinnastaminen (equivalence) not implemented

**Severity:** CRITICAL - Time bar affects fundamental rights

---

### §62 - Payment Time Limits ⏰ CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
1. Investigation must start within **7 business days** of claim receipt
2. Payment must be made within **1 month** of receiving sufficient documentation
3. If disputed, **undisputed portion** must still be paid within 1 month
4. If liability unclear, **justified response** within **3 months**

**DMN Implementation (E12b, T2, T3, T3b):**
- ✓ 7-day investigation start deadline
- ✓ 1-month payment deadline  
- ✓ Undisputed portion rule (T3b)
- ✗ 3-month justified response for unclear liability NOT implemented
- ✗ Viivästyskorotus (delay interest) calculation details missing

**Severity:** CRITICAL - Procedural deadlines are mandatory

---

### §79 - Court Action Time Limit ⏰ CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
- Court action within **3 years** of written decision notification
- **Tolling** when filed with Vakuutuslautakunta/Liikennevahinkolautakunta
- If proceedings end prematurely: **minimum 1-year extension**
- **Extension can only be used ONCE** (§79(4))

**DMN Implementation (E12c, T4):**
- ✓ 3-year deadline implemented
- ✓ Tolling rule implemented
- ✓ 1-year safety net mentioned
- ✗ "Only once" limitation NOT explicitly enforced
- ✗ Consumer dispute body tolling partially covered

**Severity:** CRITICAL - Affects access to justice

---

### §38 - €5M Property Damage Cap 💰 CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
- Property damage cap: **€5,000,000 per insurance policy**
- Pro-rata distribution if claims exceed cap
- **Late claimant protection** (§38(3)): Even if cap exceeded, late claimants get their proportional share

**DMN Implementation (E8b, E8c, E8d):**
- ✓ €5M cap implemented
- ✓ Pro-rata distribution implemented
- ✓ Late claimant protection mentioned
- ✗ Late claimant protection logic not fully detailed

**Severity:** CRITICAL - Financial cap affects all property damage claims

---

### §48 - Alcohol Thresholds 🍺 HIGH→CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
**Blood Alcohol Concentration (BAC):**
- **≥1.2‰** (blood) OR **≥0.53 mg/L** (breath): Compensation only for other circumstances' contribution
- **≥0.5‰** (blood) OR **≥0.22 mg/L** (breath): Proportional reduction
- **Drugs**: "tuntuvasti huonontunut" (significantly impaired) = same as ≥1.2‰

**DMN Implementation (N9, N11, N17):**
- ✓ BAC thresholds correctly implemented
- ✓ Breath alcohol levels correctly implemented
- ✓ Drug impairment mentioned
- ✗ "Tuntuvasti huonontunut" (significant impairment) standard not quantified
- ✗ Combined alcohol + drug effects mentioned but not detailed

**Severity:** HIGH (elevated to CRITICAL due to frequent applicability)

---

### §66 - Mandatory Liikennevahinkolautakunta Consultation 📋 CRITICAL
**Status:** Partially Implemented

**Law Requirements:**
**MUST request opinion for:**
1. Continuous compensation for permanent loss OR death
2. Increase/decrease of continuous compensation
3. Severe disability compensation
4. Correction of erroneous decision against claimant's interest

**Exceptions:**
- Obvious error from party's own conduct
- Clerical/calculation error

**DMN Implementation (MOP-001, P4b):**
- ✓ Mandatory triggers listed
- ✓ Exceptions mentioned
- ✗ Detailed workflow not implemented
- ✗ §66(3) requirement to attach opinion if differing not enforced

**Severity:** CRITICAL - Mandatory procedural requirement

---

## 3. HIGH PRIORITY GAPS

### §§53-59 - Medical Treatment Procedures 🏥 HIGH
**Status:** Partially Implemented

**Law Requirements:**

| Section | Requirement | Implementation Status |
|---------|-------------|----------------------|
| §53 | Treatment must be "vahingon vuoksi tarpeellinen" | ✓ Partially |
| §54 | Public healthcare = customer fee only | ✓ Partially |
| §55 | Full cost payment (täyskustannusmaksu) to municipality | ✗ Not fully |
| §56 | **4 business day notification** requirement | ✗ Missing |
| §57 | Maksusitoumus (treatment authorization) system | ✓ Partially |
| §58 | Emergency private care without prior approval | ✓ Implemented |
| §59 | Non-emergency private care requires maksusitoumus | ✓ Partially |

**Missing Details:**
- Täyskustannusmaksu calculation methodology
- 4-day notification enforcement mechanism
- Long-term care (>3 months) exclusion from täyskustannusmaksu

**Severity:** HIGH - Healthcare compensation is major claim category

---

### §§67-68 - Delay Interest and Notification Obligations ⏱️ HIGH
**Status:** Partially Implemented

**§67 Missing:**
- Detailed viivästyskorotus calculation formula
- €7.28 minimum threshold adjustment (palkkakerroin)
- Force majeure exception handling
- Victim-caused delay exception

**§68 Missing:**
- Recipient notification obligation workflow
- Specific reportable changes list

**Severity:** HIGH - Affects payment processing

---

### §§69-72 - Claims Representatives and Information Rights 📄 HIGH
**Status:** NOT Implemented

**§69 - Claims Representative:**
- Appointment requirements for foreign insurers
- Representative's authorization requirements
- Notification to information centres

**§70 - Foreign Representative 3-Month Deadline:**
- **Critical:** Representative must respond within **3 months**
- Must pay or make justified offer
- Missing: Complete workflow

**§71 - LVK Takes Over if Delayed:**
- If no response in 3 months, victim can demand from LVK
- LVK must start processing within **2 months**

**§72 - Information Rights:**
- Vehicle owner/holder information from LVK
- 7-year limitation for foreign accident information

**Severity:** HIGH - Cross-border claims are common

---

### §73-74 - Subrogation/Recourse Rights ⚖️ HIGH
**Status:** Partially Implemented

**§73 - Insurer Subrogation:**
- ✓ Implemented for individuals vs corporations
- ✗ Detailed recovery workflow missing

**§74 - LVK Recourse:**
- ✓ Basic scenarios covered
- ✗ Complete recourse chain not modeled
- ✗ International fund-to-fund recourse

**Severity:** HIGH - Financial recovery mechanism

---

### §§75-78 - Large Loss Distribution System 📊 HIGH
**Status:** Partially Implemented

**§75 Missing:**
- €75M threshold monitoring
- 9-year waiting period for healthcare costs
- Pro-rata calculation formula details

**§76-78:**
- Distribution system payment calculation
- Advance estimate requirements
- Portfolio transfer effects

**Severity:** HIGH - Catastrophic loss handling

---

### §§80, 81, 84 - Court Process and Appeals ⚖️ HIGH
**Status:** NOT Implemented

**§80 - Court Processing:**
- Direct claim against liable party rules
- Court summons to insurer (14 days)
- Insurer's right to appeal

**§81 - Municipality Appeal Rights:**
- Municipality NOT party to victim compensation claims
- CAN appeal täyskustannusmaksu decisions

**§84 - Insurer Information Disclosure:**
- Right to disclose to healthcare providers
- For maksusitoumus and expert opinions

**Severity:** HIGH - Legal procedure requirements

---

### §§82-83, 85-88 - Information Access and Retention 📁 HIGH
**Status:** NOT Implemented

**§82 - Information Access:**
- Employer information rights
- Medical information rights
- LVK enforcement information access

**§83 - Technical Connection:**
- Automated data retrieval
- Traffic register access
- Vehicle registry access

**§85 - Document Retention:**
- **100 years** for personal injury claims
- **50 years** for appeal documents
- **10 years** for other documents

**§§86-88:**
- Information centre operations
- LVK data collection duties
- Statistics and risk research

**Severity:** HIGH - Compliance requirements

---

### §§90-91 - Customs and Border Insurance 🛃 HIGH
**Status:** Partially Implemented

**§90 - Traffic Safety Agency:**
- Notification of permanent removal
- Insurance transfer notification
- Owner/holder change notification
- Traffic use commencement/removal

**§91 - Customs Duties:**
- ✓ Border insurance enforcement partially covered
- ✗ Premium collection at border
- ✗ Certificate issuance
- ✗ Export validation

**Severity:** HIGH - Border enforcement

---

## 4. MEDIUM/LOW PRIORITY GAPS

### Chapter 1 - General Provisions
| Section | Title | Status | Notes |
|---------|-------|--------|-------|
| §1 | Scope | ✓ | Covered in general |
| §2 | Definitions | ✓ | Mostly covered |
| §4 | Traffic Insurance Centre | ✓ | Partially covered |

### Chapter 2 - Insurance and Premium (Partial Coverage)
| Section | Title | Status | Notes |
|---------|-------|--------|-------|
| §9 | Info to Traffic Safety Agency | ✗ | Administrative |
| §11 | Policy document | ✗ | Procedural |
| §13 | Coverage area | ✓ | Partially covered |
| §14-15 | Disclosure failures | ✗ | Penalty-related |
| §18 | Ownership transfer | ✓ | Partially covered |
| §21 | Claims history transfer | ✗ | Administrative |
| §23 | Premium refund | ✗ | Financial |
| §24 | Late payment interest | ✗ | Financial |
| §25 | Enforceability | ✗ | Legal |
| §26 | Limitation | ✗ | Time limit |
| §29-30 | Penalty assessment | ✗ | Administrative |

### Chapter 3 - Compensation (Additional)
| Section | Title | Status | Notes |
|---------|-------|--------|-------|
| §32 | Valtiokonttori liability | ✗ | State vehicle specific |
| §35 | Index adjustment details | ✓ | Partially covered |
| §36 | Work accident coordination | ✗ | Coordination rule |
| §51 | Inter-insurer apportionment | ✗ | Multi-vehicle claims |

### Chapter 7 - Miscellaneous (Lower Priority)
| Section | Title | Status | Notes |
|---------|-------|--------|-------|
| §89 | Financial Supervision stats | ✗ | Regulatory |
| §92 | Insolvency | ✓ | Partially covered |
| §93 | Additional payment obligation | ✗ | Insolvency-related |
| §94 | Joint guarantee | ✗ | Insolvency-related |
| §95 | Official liability | ✗ | Criminal |

### Chapter 8 - Entry into Force
| Section | Title | Status | Notes |
|---------|-------|--------|-------|
| §§96-99 | Transitional provisions | N/A | Historical |

---

## 5. RECOMMENDED ISSUES TO CREATE

### Priority 1 (Critical - Create Issues Immediately)

1. **Issue #1: §62 Complete Payment Deadline Implementation**
   - 7-day investigation start (✓ exists, verify enforcement)
   - 1-month payment deadline (✓ exists, verify enforcement)
   - **3-month justified response for unclear liability** (MISSING)
   - Undisputed portion payment (✓ exists)

2. **Issue #2: §61 Complete Time Limit Rules**
   - "Erityisen painava syy" exception modeling
   - Claim filing equivalence notification

3. **Issue #3: §66 Mandatory Lautakunta Consultation Workflow**
   - Mandatory consultation triggers
   - Opinion attachment requirement
   - Exception handling

4. **Issue #4: §38 Late Claimant Protection**
   - Complete §38(3) implementation
   - Pro-rata recalculation logic

### Priority 2 (High - Create Issues Soon)

5. **Issue #5: §§56-59 Medical Treatment Procedures**
   - 4-business-day notification enforcement
   - Täyskustannusmaksu calculation
   - Long-term care exclusion

6. **Issue #6: §§69-72 Claims Representatives**
   - 3-month foreign representative deadline
   - LVK takeover workflow
   - Information rights

7. **Issue #7: §67 Complete Delay Interest**
   - Detailed calculation formulas
   - Minimum threshold adjustments
   - Exception handling

8. **Issue #8: §§75-78 Large Loss Distribution**
   - €75M threshold monitoring
   - Distribution calculations

9. **Issue #9: §§82-83, 85 Information Access & Retention**
   - Document retention periods
   - Technical connection rules
   - Access rights

10. **Issue #10: §§90-91 Customs Integration**
    - Complete border insurance workflow
    - Premium collection
    - Certificate management

### Priority 3 (Medium - Backlog)

11. **Issue #11: §§80-81 Court Process Integration**
12. **Issue #12: Chapter 2 Administrative Provisions**
13. **Issue #13: §§93-94 Insolvency Procedures**

---

## 6. IMPLEMENTATION QUALITY ASSESSMENT

### Well-Implemented Areas ✅

1. **Negative Claims (Exclusions)** - Comprehensive coverage
2. **Basic Eligibility** - Core coverage rules
3. **Alcohol Thresholds** - Correct BAC levels
4. **International Coverage** - Green Card, EEA rules
5. **Basic Time Limits** - 3-year, 10-year deadlines

### Needs Improvement ⚠️

1. **Procedural Deadlines** - Missing 3-month response
2. **Medical Procedures** - Incomplete täyskustannusmaksu
3. **Cross-Border Claims** - Missing representative rules
4. **Information Access** - Technical connections not modeled
5. **Document Retention** - Compliance requirements missing

### Critical Missing 🔴

1. **Mandatory Consultation** - §66 workflow
2. **Late Claimant Protection** - §38(3) details
3. **Court Action Tolling** - §79 "once only" rule
4. **LVK Takeover** - §71 procedure
5. **Customs Integration** - §91 enforcement

---

## 7. CONCLUSION

The DMN rules provide a **solid foundation** for traffic insurance claim processing, covering approximately **45%** of the law's provisions comprehensively. However, there are **significant gaps** in:

1. **Procedural deadlines** (§62, §79) - Critical for compliance
2. **Medical treatment workflows** (§§53-59) - High-volume claims
3. **Cross-border procedures** (§§69-72) - International obligations
4. **Mandatory consultation** (§66) - Legal requirement
5. **Information management** (§§82-88) - Compliance and operations

**Recommended Action:** Prioritize creating issues for the 10 identified high-priority gaps, with immediate attention to the 4 critical gaps affecting fundamental claim processing rights and deadlines.
