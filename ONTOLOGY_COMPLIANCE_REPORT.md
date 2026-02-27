# Finnish Work Accident Ontology Compliance Report
**Date:** February 27, 2026  
**Law:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Ontology File:** `tyotapaturma_ammattitautilaki/ontology/work_accident_ontology.md`

---

## Executive Summary

### Critical Findings: 3
### High Priority Findings: 1  
### Medium Priority Findings: 1

**Status:** The ontology contains CRITICAL errors that were previously reported but NOT fixed. These errors misrepresent fundamental aspects of Finnish work accident law and could mislead claimants.

---

## CRITICAL Issues (Previously Reported but NOT Fixed)

### 1. DailyAllowance Duration Error [REPEAT of Issue #218]

**Location:** Section 4 - DailyAllowance

**Current (WRONG):**
```
DailyAllowance
- Not limited to 1 year - continues as long as work incapacity exists
```

**Law Actually Says (§56(1)):**
"Vahingoittuneella on oikeus päivärahaan **yhden vuoden ajan vahinkopäivästä lukien**"

(Right to daily allowance for **one year from accident date**)

**Impact:** Claimants may expect indefinite daily allowance when it actually converts to disability pension after exactly 1 year.

**Fix Required:**
```
DailyAllowance
- **Duration**: Maximum 1 year from accident date (vahinkopäivä) - §56(1)
- **After 1 year**: Converts to DisabilityPension (Tapaturmaeläke) - §63
```

---

### 2. Claim Filing Deadline Error [REPEAT of Issue #217]

**Location:** Section 5 - Key Relationships

**Current (WRONG):**
```
| InjuredParty | must_file_claim_within | 1 year | From date of knowledge |
| InjuredParty | must_file_claim_within | 10 years | Absolute maximum |
```

**Law Actually Says (§116(1)):**
"Korvausasia on saatettava vireille vakuutuslaitoksessa **viiden vuoden kuluessa vahinkopäivästä**"

(Claim must be filed within **5 years** from accident date)

**Impact:** Claimants relying on the ontology may:
- Miss their actual 5-year deadline
- Incorrectly believe they have 10 years

**Note on Time Limits:**
The ontology confuses different deadlines:
| Limit | Law Section | Purpose |
|-------|-------------|---------|
| 1 year | §128 | Cost reimbursement claims |
| 5 years | §116 | General claim filing |
| 10 years | §247 | Recovery of overpaid compensation |

**Fix Required:**
```
| InjuredParty | must_file_claim_within | 5 years | From accident date - §116 |
| InjuredParty | must_claim_costs_within | 1 year | From cost incurrence - §128 |
```

---

### 3. Missing Insurance Exemptions [REPEAT of Issue #219]

**Location:** Section 2 - MandatoryInsurance

**Current (INCOMPLETE):**
```
MandatoryInsurance
- Description: Compulsory insurance that employers must obtain
```

**Missing from Law (§3):**
- **€1,200 threshold**: No insurance required if annual payroll ≤ €1,200 (§3(2))
- **State employer exemption**: State pays from state funds, not insurance (§3(3))

**Impact:** 
- Small employers may unnecessarily purchase insurance
- State employees may not know claims go through Valtiokonttori

**Fix Required:**
```
MandatoryInsurance
- **Applies to**: Private employers with annual payroll > €1,200
- **Does NOT apply to**:
  - Employers with payroll ≤ €1,200 (§3(2))
  - State employers (§3(3))
```

---

## NEW Findings (Not Previously Reported)

### 4. HIGH: Missing Key Entities

The following entities are defined in law but missing from ontology:

| Entity | Legal Basis | Importance |
|--------|-------------|------------|
| **AccidentDay (Vahinkopäivä)** | §15 | Anchor date for ALL time calculations |
| **Workplace (Työntekopaikka)** | §22 | Determines accident compensability |
| **UninsuredWork** | §2(4), §6 | Special handling rules apply |
| **FamilyMember** | §9 | Used for ownership calculations |
| **CohabitingPartner (Avopuoliso)** | §9, §100 | Same rights as spouse |
| **Beneficiary (Edunsaaja)** | §117 | Party to death proceedings |
| **Guardian (Edunvalvoja)** | §118 | Legal representation |
| **CloseRelative (Lähiomainen)** | §118 | Can represent injured party |

**Suggested Addition:** Create new section "1b. Key Dates and Locations" and "1c. Related Persons"

---

### 5. MEDIUM-HIGH: Missing Attributes and Enumerations

#### 5a. DisabilityClass (Haittaluokka) Values

**Current (INCOMPLETE):**
```
PermanentDamageCompensation
- Classes: 1-20 based on severity
```

**Missing:** Specific percentages for each class (§86)

| Class | Percentage | Payment Type |
|-------|------------|--------------|
| 1-5 | 1.15% - 5.45% | Lump sum |
| 6-20 | 6.45% - 60% | Continuous |

**Base Amount:** €12,440

#### 5b. Survivor Subclass Details

**Current (INCOMPLETE):**
```
Survivor
- Subclasses: Widow, Child, Dependent
```

**Missing Attributes:**

**Widow:**
- Types: Spouse OR CohabitingPartner
- Conditions for cohabiting partner: shared child OR mutual support agreement
- Income adjustment (tulosovitus) after 13 months

**Child:**
- Age limit: Under 18, OR 18-25 if studying/disabled
- Cannot receive from more than 2 deceased simultaneously

#### 5c. Employer Attributes

**Current:**
```
Employer
- Attributes: businessId, companyName, annualPayroll
```

**Missing:**
- payrollThreshold: €1,200
- isExempt: boolean
- isStateEmployer: boolean
- familyOwnershipPercentages (for §9 calculations)

---

## Compliance Summary

| Category | Status | Count |
|----------|--------|-------|
| Critical Errors (Unfixed) | ❌ FAILED | 3 |
| Missing Entities | ⚠️ GAPS | 8 |
| Missing Attributes | ⚠️ GAPS | Multiple |
| Overall Ontology Quality | ⚠️ NEEDS WORK | - |

---

## Recommendations

### Immediate Actions (Critical)
1. **Fix DailyAllowance duration** - Change "Not limited to 1 year" to "Maximum 1 year"
2. **Fix claim filing deadline** - Change "1 year / 10 years" to "5 years"
3. **Add insurance exemptions** - Document €1,200 threshold and state employer exemption

### Short-term Actions (High Priority)
4. Add AccidentDay entity
5. Add Workplace entity with subclasses
6. Add Beneficiary entity
7. Add CohabitingPartner entity

### Medium-term Actions
8. Add DisabilityClass enumeration with percentages
9. Enhance Survivor subclasses with attributes
10. Add missing Employer attributes

---

## Law References

Key sections referenced in this report:
- §2(4) - Uninsured work definition
- §3 - Insurance obligation and exemptions
- §9 - Family member and cohabiting partner definitions
- §15 - Accident day definition
- §22 - Workplace accidents
- §56 - Daily allowance (1-year limit)
- §63 - Disability pension
- §86 - Haittaluokka percentages
- §100-101 - Survivor eligibility
- §116 - Claim filing deadline (5 years)
- §117-118 - Parties and representation

---

## Appendix: Ontology vs Law Comparison Table

| Ontology Section | Law Section | Status |
|------------------|-------------|--------|
| DailyAllowance duration | §56 | ❌ WRONG |
| Claim filing deadline | §116 | ❌ WRONG |
| MandatoryInsurance exemptions | §3 | ❌ MISSING |
| Survivor subclasses | §§100-101 | ⚠️ INCOMPLETE |
| PermanentDamageCompensation classes | §86 | ⚠️ INCOMPLETE |
| AccidentDay entity | §15 | ❌ MISSING |
| Workplace entity | §22 | ❌ MISSING |
| Beneficiary entity | §117 | ❌ MISSING |

---

**Report Generated By:** Finnish Work Accident Ontology Compliance Check  
**Model:** Gemini (maximal thinking mode)
