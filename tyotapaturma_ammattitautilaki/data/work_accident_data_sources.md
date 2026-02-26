# Work Accident Insurance (Työtapaturma- ja ammattitautilaki 459/2015) - Data Sources

This file maps each data point to potential **data sources** - where the data can be obtained from.

---

## Data Point → Source Mapping

### Person Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| person.type | Työnantaja / Työpaikka | Employment contract | HR system |
| person.employment_status | Työnantaja | HR records | Payroll |

### Event Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| event.type | Työpaikka / Poliisi | Accident investigation | Employer / Police |
| event.location | Työpaikka | Accident investigation | Employer |
| event.timing | Työpaikka / Potilastiedot | Accident investigation | Employer |

### Injury Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| injury.type | Terveydenhuolto | Medical records | Kanta / Patient data |
| injury.severity | Terveydenhuolto / Lääkärikeskus | Medical assessment | Doctor certificate |
| injury.duration | Terveydenhuolto | Medical certificate | Sick leave |

### Compensation Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| compensation.type | Vakuutusyhtiö | Claim assessment | Internal |
| income.annual | Verohallinto | Tax records | Tulorekisteri |

### Work Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| work_ability.reduced | Terveydenhuolto | Medical certificate | Doctor |
| work_ability.lost_percentage | Terveydenhuolto | Medical certificate | Doctor |

### Treatment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| treatment.type | Terveydenhuolto | Medical prescription | Kanta |
| treatment.necessity | Terveydenhuolto | Medical recommendation | Doctor |
| treatment.provider | Terveydenhuolto | Healthcare register | THL |

### Rehabilitation Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| rehabilitation.medical_recommendation | Terveydenhuolto | Doctor recommendation | Medical records |

### Claim Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| claim.type | Vakuutusyhtiö | Claim system | Customer application |
| injury.timing | Terveydenhuolto / Poliisi | Records | Medical / Police |

### Employer Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| employer.industry_risk | Tilastokeskus / Toimialaluokitus | Industry classification | Statistics |
| employer.payroll | Verohallinto | Tax records | Tulorekisteri |
| employer.claims_history | Vakuutusyhtiö / Tapaturmavakuutuskeskus | Claims register | Internal / TVK |

### Decision Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| decision.type | Vakuutusyhtiö | Decision system | Internal |
| claimant.disagreement | Vakuutusyhtiö | Appeal application | Customer |

### Survivor Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| survivor.relationship | Väestörekisteri | Population register | DVV |
| survivor.age | Väestörekisteri | Population register | DVV |
| deceased.contributory | Verohallinto | Tax records | Tax |

---

## Data Source Summary by Authority

### Government Registers

| Authority | Register | Data Points |
|-----------|----------|-------------|
| **DVV** (Väestörekisterikeskus) | Population register | survivor.relationship, survivor.age |
| **Verohallinto** | Tax records | income.annual, deceased.contributory, employer.payroll |
| **Tilastokeskus** | Industry classification | employer.industry_risk |
| **Poliisi** | Police records | event.type, injury.timing |

### Insurance Industry

| Organization | Database | Data Points |
|-------------|----------|-------------|
| **Tapaturmavakuutuskeskus (TVK)** | Claims database | employer.claims_history |
| **Vakuutusyhtiöt** | Policy/Claims systems | compensation.type, claim.type, decision.type |

### Healthcare

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **SOTE** (Social and health services) | Patient records (Kanta) | injury.type, treatment.type |
| **Lääkärikeskukset** | Medical certificates | injury.severity, work_ability.*, treatment.necessity |

---

## API Integration Potential

### Real-Time APIs

| API | Provider | Data Points |
|-----|----------|-------------|
| Kanta (eHealth) | THL | injury.*, treatment.* |
| Population Register API | DVV | survivor.* |
| Tulorekisteri | Verohallinto | income.annual, employer.payroll |
| Employer Register | YTJ | employer.* |

### Batch Data

| Source | Update Frequency | Data Points |
|--------|------------------|-------------|
| Claims history (TVK) | Monthly/Annual | employer.claims_history |
| Industry classification | Annual | employer.industry_risk |

---

## Data Quality Considerations

### Critical Data Points (Must Have)
- injury.type - From medical records
- income.annual - From tax records
- work_ability.lost_percentage - From medical certificate

### Important (Should Have)
- event.type - From accident investigation
- employer.industry_risk - From statistics
- employer.claims_history - From TVK

### Nice to Have
- treatment.provider - From healthcare register
- survivor.age - From population register
