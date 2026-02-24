# Work Accident Insurance (Työtapaturma- ja ammattitautilaki 459/2015) - Data Points for Business Rules

This file documents the **data points needed** to calculate each business rule in the DMN decision tables.

---

## 1. InsuranceObligation

**Decision:** Determine if employer has mandatory insurance obligation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| person.type | Enum | Employment contract | Section 8 |
| person.employment_status | Enum | HR records | Section 3 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: InsuranceObligation

---

## 2. CompensableEvent

**Decision:** Determine if event is compensable under the law

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| event.type | Enum | Accident report | Sections 17-35 |
| event.location | Enum | Accident investigation | Sections 17-25 |
| event.timing | Enum | Accident report | Sections 17-25 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: CompensableEvent

---

## 3. CompensationType

**Decision:** Determine type of compensation based on injury

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.type | Enum | Medical diagnosis | Sections 17-35 |
| injury.severity | Enum | Medical assessment | Section 83 |
| injury.duration | Enum | Medical certificate | Sections 55-62 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: CompensationType

---

## 4. CompensationAmount

**Decision:** Calculate compensation amount

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| compensation.type | Enum | Injury assessment | Sections 36-109 |
| income.annual | Decimal | Tax records / Payslips | Section 56 |
| injury.severity | Enum | Medical assessment | Section 83 |
| work_ability.lost_percentage | Integer | Medical certificate | Section 56 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: CompensationAmount

---

## 5. MedicalCareCoverage

**Decision:** Determine medical care coverage

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| treatment.type | Enum | Medical prescription | Sections 36-54 |
| treatment.necessity | Boolean | Medical recommendation | Sections 36-54 |
| treatment.provider | Enum | Healthcare provider | Section 37 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: MedicalCareCoverage

---

## 6. ClaimTimeLimit

**Decision:** Determine claim submission time limit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| claim.type | Enum | Claim type | Section 110 |
| injury.timing | Date | Accident/diagnosis date | Section 110 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: ClaimTimeLimit

---

## 7. RehabilitationEligibility

**Decision:** Determine rehabilitation eligibility

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.severity | Enum | Medical assessment | Section 88 |
| work_ability.reduced | Boolean | Medical certificate | Section 88 |
| rehabilitation.medical_recommendation | Boolean | Doctor recommendation | Section 88 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: RehabilitationEligibility

---

## 8. InsurancePremium

**Decision:** Calculate insurance premium

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| employer.industry_risk | Enum | Industry classification | Section 166 |
| employer.payroll | Decimal | Tax records | Section 166 |
| employer.claims_history | Integer | Insurance records | Sections 171-176 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: InsurancePremium

---

## 9. AppealsProcess

**Decision:** Determine appeals process

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| decision.type | Enum | Insurance decision | Sections 237-247 |
| claimant.disagreement | Boolean | Appeal application | Section 237 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: AppealsProcess

---

## 10. SurvivorBenefits

**Decision:** Determine survivor benefit eligibility

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| survivor.relationship | Enum | Population register | Sections 99-109 |
| survivor.age | Integer | Population register | Section 103 |
| deceased.contributory | Boolean | Tax records | Section 99 |

### Rule Reference
- `work_accident_dmn_rules.json` - Decision: SurvivorBenefits

---

## Summary: All Data Points

### Person Data
- person.type
- person.employment_status

### Event Data
- event.type
- event.location
- event.timing

### Injury Data
- injury.type
- injury.severity
- injury.duration

### Compensation Data
- compensation.type
- income.annual

### Work Data
- work_ability.reduced
- work_ability.lost_percentage

### Treatment Data
- treatment.type
- treatment.necessity
- treatment.provider

### Rehabilitation Data
- rehabilitation.medical_recommendation

### Claim Data
- claim.type
- injury.timing

### Employer Data
- employer.industry_risk
- employer.payroll
- employer.claims_history

### Decision Data
- decision.type
- claimant.disagreement

### Survivor Data
- survivor.relationship
- survivor.age
- deceased.contributory
