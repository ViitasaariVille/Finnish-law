# Patient Insurance (Potilasvakuutuslaki 948/2019) - Data Sources

This file maps each data point to potential **data sources** - where the data can be obtained from.

---

## Data Point → Source Mapping

### Organization Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| organization.type | Yritys- ja yhteisötietojärjestelmä (YTJ) | Business register | PRH |
| organization.is_free | SOTE / Palveluntuottaja | Service records | Healthcare |
| organization.has_employer | Työnantaja / HR | Employment records | Internal |

### Injury Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| injury.type | Terveydenhuolto | Patient records | Kanta |
| injury.condition_met | Terveydenhuolto / Potilasvakuutuskeskus | Medical investigation | PVK |
| injury.result | Terveydenhuolto | Medical assessment | Kanta |
| injury.causation | Potilasvakuutuskeskus | Investigation | PVK |

### Claim Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| claim.knowledge_date | Potilasvakuutuskeskus | Claim application | PVK |
| claim.event_date | Terveydenhuolto | Patient records | Kanta |
| claim.stage | Potilasvakuutuskeskus | Workflow system | PVK |
| claim.type | Potilasvakuutuskeskus | Claim system | Customer |

### Patient Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| patient.status | Terveydenhuolto | Patient records | Kanta |

### Payment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| payment.status | Potilasvakuutuskeskus | Payment system | PVK |
| payment.amount | Potilasvakuutuskeskus | Payment system | PVK |

### Work Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| work_ability.affected | Terveydenhuolto | Medical certificate | Doctor |
| future.affect_probable | Terveydenhuolto | Medical prognosis | Doctor |

### Decision Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| decision.type | Potilasvakuutuskeskus | Decision system | PVK |
| timeline | Potilasvakuutuskeskus | Case management | PVK |

### Compensation Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| compensation.type | Potilasvakuutuskeskus | Assessment | PVK |

---

## Data Source Summary by Authority

### Government Registers

| Authority | Register | Data Points |
|-----------|----------|-------------|
| **PRH** (Patentti- ja rekisterihallitus) | YTJ (Business register) | organization.type |
| **Väestörekisteri (DVV)** | Population register | patient.status |

### Healthcare

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **SOTE** (Social and health services) | Patient records (Kanta) | injury.type, injury.event_date, patient.status, work_ability.* |
| **Lääkärikeskukset** | Medical certificates | injury.condition_met, injury.result |
| **Terveyspalvelut** | Treatment records | injury.result |

### Insurance

| Organization | Database | Data Points |
|-------------|----------|-------------|
| **Potilasvakuutuskeskus (PVK)** | Claims system | claim.knowledge_date, claim.stage, claim.type, decision.type, payment.*, compensation.type |
| **Vakuutusyhtiöt** | Policy systems | organization.is_free |

---

## API Integration Potential

### Real-Time APIs

| API | Provider | Data Points |
|-----|----------|-------------|
| Kanta (eHealth) | THL | injury.type, injury.event_date, patient.status |
| Population Register API | DVV | patient.status |
| YTJ Business Register | PRH | organization.type |

### Batch Data

| Source | Update Frequency | Data Points |
|--------|------------------|-------------|
| Claims system (PVK) | Real-time | claim.*, decision.*, payment.* |

---

## Data Quality Considerations

### Critical Data Points (Must Have)
- injury.type - From medical records (Kanta)
- injury.condition_met - From medical investigation
- claim.knowledge_date - From claim application

### Important (Should Have)
- injury.result - From medical assessment
- organization.type - From business register
- work_ability.affected - From medical certificate

### Nice to Have
- payment.amount - From payment system
- timeline - From case management
