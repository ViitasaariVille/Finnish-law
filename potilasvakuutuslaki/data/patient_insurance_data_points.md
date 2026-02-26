# Patient Insurance (Potilasvakuutuslaki 948/2019) - Data Points for Business Rules

This file documents the **data points needed** to calculate each business rule in the DMN decision tables.

---

## 1. InsuranceObligation

**Decision:** Determine if organization has patient insurance obligation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| organization.type | Enum | Business register | Section 6 |
| organization.is_free | Boolean | Service records | Section 6 |
| organization.has_employer | Boolean | HR records | Section 6 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: InsuranceObligation

---

## 2. CompensableInjury

**Decision:** Determine if patient injury is compensable

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.type | Enum | Medical records | Section 23 |
| injury.condition_met | Boolean | Medical investigation | Section 23 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: CompensableInjury

---

## 3. ClaimTimeLimit

**Decision:** Determine claim time limit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| claim.knowledge_date | Date | Claim application | Section 31 |
| claim.event_date | Date | Medical records | Section 31 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: ClaimTimeLimit

---

## 4. CompensationType

**Decision:** Determine type of compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.result | Enum | Medical assessment | Section 24 |
| patient.status | Enum | Medical records | Section 24 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: CompensationType

---

## 5. ProcessingDeadline

**Decision:** Determine processing deadline

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| claim.stage | Enum | Internal workflow | Section 33 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: ProcessingDeadline

---

## 6. LatePaymentInterest

**Decision:** Determine late payment interest

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| payment.status | Enum | Payment system | Section 42 |
| payment.amount | Decimal | Payment records | Section 42 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: LatePaymentInterest

---

## 7. RehabilitationEligibility

**Decision:** Determine rehabilitation eligibility

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| work_ability.affected | Boolean | Medical certificate | Section 25 |
| future.affect_probable | Boolean | Medical prognosis | Section 25 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: RehabilitationEligibility

---

## 8. SubrogationRight

**Decision:** Determine subrogation rights

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| claimant.type | Enum | Claim type | Sections 45-47 |
| injury.causation | Enum | Investigation | Section 45 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: SubrogationRight

---

## 9. AppealProcess

**Decision:** Determine appeal path

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| decision.type | Enum | Insurance decision | Section 38 |
| timeline | Date | Appeal deadline | Section 38 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: AppealProcess

---

## 10. IndexAdjustment

**Decision:** Determine if compensation is index-adjusted

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| compensation.type | Enum | Compensation type | Section 28 |

### Rule Reference
- `patient_insurance_dmn_rules.json` - Decision: IndexAdjustment

---

## Summary: All Data Points

### Organization Data
- organization.type
- organization.is_free
- organization.has_employer

### Injury Data
- injury.type
- injury.condition_met
- injury.result
- injury.causation

### Claim Data
- claim.knowledge_date
- claim.event_date
- claim.stage
- claim.type

### Patient Data
- patient.status

### Payment Data
- payment.status
- payment.amount

### Work Data
- work_ability.affected
- future.affect_probable

### Decision Data
- decision.type
- timeline

### Compensation Data
- compensation.type
