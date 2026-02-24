# Car Insurance (Liikennevakuutuslaki 460/2016) - Data Points for Business Rules

This file documents the **data points needed** to calculate each business rule in the DMN decision tables.

---

## 1. MandatoryInsuranceRequirement

**Decision:** Determine if vehicle requires mandatory traffic insurance

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| vehicle.permanent_location | String | Vehicle registration | Section 5 |
| vehicle.requires_insurance | Boolean | Vehicle type assessment | Section 5 |
| vehicle.type | Enum | Vehicle category | Section 5 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: MandatoryInsuranceRequirement

---

## 2. InsuranceObligationLiableParty

**Decision:** Determine who is liable for insurance obligation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| vehicle.owner.exists | Boolean | Vehicle registration | Section 6 |
| vehicle.holder.exists | Boolean | Vehicle registration | Section 6 |
| vehicle.ownership_transferred | Boolean | Transfer date | Section 6 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: InsuranceObligationLiableParty

---

## 3. CoverageCompensation

**Decision:** Determine what is covered by traffic insurance

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| damage.type | Enum | Police report / Medical | Sections 12-16 |
| damage.person.injured | Boolean | Medical records | Section 12 |
| damage.property.damaged | Boolean | Damage assessment | Section 12 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: CoverageCompensation

---

## 4. Exclusions

**Decision:** Determine what is NOT covered by traffic insurance

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| driver.intent | Enum | Investigation | Section 17 |
| driver.drunkenness | Boolean | Blood test / Police | Section 18 |
| vehicle.purpose | Enum | Insurance application | Section 19 |
| accident.location | Enum | Police report | Section 20 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: Exclusions

---

## 5. MedicalExpenseCoverage

**Decision:** Determine medical expense compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.type | Enum | Medical diagnosis | Section 5 |
| treatment.necessity | Boolean | Medical recommendation | Sections 5a-5f |
| treatment.provider | Enum | Healthcare provider | Section 5a |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: MedicalExpenseCoverage

---

## 6. LostWagesCompensation

**Decision:** Calculate lost wages compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| income.type | Enum | Employment contract / Tax records | Section 4 |
| income.amount | Decimal | Payslip / Tax return | Section 4 |
| work_ability.lost_days | Integer | Medical certificate | Section 4 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: LostWagesCompensation

---

## 7. PainAndSufferingCompensation

**Decision:** Calculate pain and suffering compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| injury.permanent | Boolean | Medical assessment | Section 5 |
| injury.percentage | Enum | Disability evaluation | Section 5(2) |
| pain.level | Enum | Medical assessment | Section 5 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: PainAndSufferingCompensation

---

## 8. DeathCompensation

**Decision:** Calculate death compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| deceased.income.exists | Boolean | Tax records | Sections 7-8 |
| survivor.relationship | Enum | Civil status / Birth certificates | Sections 7-8 |
| survivor.dependent | Boolean | Household registration | Sections 7-8 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: DeathCompensation

---

## 9. PropertyDamageCompensation

**Decision:** Calculate property damage compensation

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| property.type | Enum | Damage assessment | Section 3 |
| property.value | Decimal | Market value / Receipts | Section 3 |
| damage.severity | Enum | Assessment report | Section 3 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: PropertyDamageCompensation

---

## 10. ClaimTimeLimit

**Decision:** Determine claim submission time limit

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| claim.type | Enum | Claim type | Section 74 |
| accident.date | Date | Police report | Section 74 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: ClaimTimeLimit

---

## 11. PremiumCalculation

**Decision:** Calculate insurance premium

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| vehicle.type | Enum | Vehicle registration | Sections 89-92 |
| driver.age | Integer | License / ID | Section 90 |
| claims.history | Integer | Claims history | Section 91 |
| usage.purpose | Enum | Insurance application | Section 89 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: PremiumCalculation

---

## 12. InternationalCoverage

**Decision:** Determine international coverage

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| accident.country | Enum | Police report | Sections 10-11 |
| green_card.valid | Boolean | Green Card / Insurance card | Section 10 |
| vehicle.registered | String | Registration | Section 10 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: InternationalCoverage

---

## 13. InsolvencyProtection

**Decision:** Protection when insurer becomes insolvent

### Input Variables (Data Points)
| Data Point | Type | Source | Legal Basis |
|-----------|------|--------|-------------|
| insurer.status | Enum | Financial Authority | Section 77 |
| policy.active | Boolean | Policy records | Section 76 |
| claim.pending | Boolean | Claims system | Section 77 |

### Rule Reference
- `car_insurance_dmn_rules.json` - Decision: InsolvencyProtection

---

## Summary: All Data Points

### Vehicle Data
- vehicle.permanent_location
- vehicle.requires_insurance
- vehicle.type
- vehicle.owner.exists
- vehicle.holder.exists
- vehicle.ownership_transferred
- vehicle.registered
- vehicle.value

### Driver Data
- driver.age
- driver.intent
- driver.drunkenness

### Usage Data
- vehicle.purpose
- usage.purpose

### Accident Data
- accident.date
- accident.country
- accident.location
- damage.type
- damage.severity

### Injury Data
- injury.type
- injury.permanent
- injury.percentage
- injury.person.injured

### Treatment Data
- treatment.type
- treatment.necessity
- treatment.provider

### Income Data
- income.type
- income.amount

### Work Data
- work_ability.lost_days

### Pain Data
- pain.level

### Survivor Data
- survivor.relationship
- survivor.dependent

### Property Data
- property.type
- property.value
- property.damaged

### Claim Data
- claim.type
- claim.pending

### Claims History
- claims.history

### Insurance Data
- insurer.status
- policy.active

### Legal Basis
- Sections: 3, 4, 5, 5a-5f, 6, 6a, 7-8, 10-11, 12-21, 74, 76-77, 89-92
