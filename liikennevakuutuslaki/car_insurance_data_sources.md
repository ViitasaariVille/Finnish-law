# Car Insurance (Liikennevakuutuslaki 460/2016) - Data Sources for Each Data Point

This file maps each data point to potential **data sources** - where the data can be obtained from.

---

## Data Point → Source Mapping

### Vehicle Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| vehicle.permanent_location | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Traficom / Findian |
| vehicle.type | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Traficom / Finnish Transport and Communications Agency |
| vehicle.owner.exists | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Owner lookup |
| vehicle.holder.exists | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Holder lookup |
| vehicle.ownership_transferred | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Transfer date |
| vehicle.registered | Liikenne- ja viestintävirasto (Traficom) | Vehicle register API | Registration certificate |
| vehicle.value | Autovälittäjät / Katsastuskonttori | Market data / Appraisal | Dealer data / Inspection |

### Driver Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| driver.age | Liikenne- ja viestintävirasto (Traficom) | License register | License lookup |
| driver.intent | Poliisi (Police) | Accident report | Police investigation |
| driver.drunkenness | Poliisi / Laboratoriot | Blood test / Breathalyzer | Police / Medical |

### Usage Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| vehicle.purpose | Vakuutusyhtiö | Insurance application form | Customer input |
| usage.purpose | Vakuutusyhtiö | Insurance application form | Customer input |

### Accident Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| accident.date | Poliisi / Onnettomuustietopalvelu (OTI) | Accident register | Police / Insurance |
| accident.country | Poliisi | Accident report | Police |
| accident.location | Poliisi / Liikennevirasto | Accident coordinates | GPS / Police |
| damage.type | Vakuutusyhtiö / Korjaamo | Damage assessment | Insurance claim |
| damage.severity | Vakuutusyhtiö / Korjaamo | Damage assessment | Expert evaluation |

### Injury Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| injury.type | Terveyspalvelut (SOTE) | Medical records | Patient data / Kanta |
| injury.permanent | Terveyspalvelut / KELA | Medical assessment | Doctor certificate |
| injury.percentage | Vakuutusyhtiö / Lääkärikeskus | Disability evaluation | Medical expert |
| injury.person.injured | Terveyspalvelut / Poliisi | Medical records | Patient data |

### Treatment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| treatment.type | Terveyspalvelut (SOTE) | Medical records | Patient data / Kanta |
| treatment.necessity | Terveyspalvelut / Lääkärikeskus | Medical recommendation | Doctor certificate |
| treatment.provider | Terveyspalvelut (SOTE) | Healthcare register | THL / Kanta |

### Income Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| income.type | Verohallinto / Työnantaja | Tax records / Payslips | Tulorekisteri |
| income.amount | Verohallinto | Tax return / Payslips | Tulorekisteri |

### Work Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| work_ability.lost_days | Terveyspalvelut / KELA | Medical certificate | Doctor sick note |

### Pain Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| pain.level | Terveyspalvelut | Medical assessment | Doctor evaluation |

### Survivor Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| survivor.relationship | Väestörekisteri (Digital and Population Data Services Agency) | Population register | DVV |
| survivor.dependent | KELA / Väestörekisteri | Household register | DVV / KELA |

### Property Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| property.type | Vakuutusyhtiö | Claim assessment | Customer report |
| property.value | Vakuutusyhtiö / Korjaamo | Appraisal / Receipts | Expert / Receipt |
| property.damaged | Vakuutusyhtiö | Damage assessment | Claim |

### Claim Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| claim.type | Vakuutusyhtiö | Claim system | Customer application |
| claim.pending | Vakuutusyhtiö | Claims system | Internal |

### Claims History

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| claims.history | Vakuutusyhtiö / Liikennevakuutuskeskus | Claims database | Internal / LVK |

### Insurance Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| insurer.status | Finanssivalvonta (FIN-FSA) | Financial register | Supervision |
| policy.active | Vakuutusyhtiö | Policy system | Internal |

---

## Data Source Summary by Authority

### Government Registers

| Authority | Register | Data Points |
|-----------|----------|-------------|
| **Traficom** (Liikenne- ja viestintävirasto) | Vehicle register | permanent_location, type, owner, holder, registered |
| **Traficom** | License register | driver.age |
| **DVV** (Väestörekisterikeskus) | Population register | survivor.relationship, dependent |
| **Verohallinto** | Tax records | income.type, income.amount |
| **KELA** | Social benefits | injury.permanent, survivor.dependent |
| **Poliisi** | Police records | accident.date, accident.country, driver.intent, driver.drunkenness |
| **THL** (Terveyden ja hyvinvoinnin laitos) | Health register | treatment.provider |
| **Finanssivalvonta** | Financial register | insurer.status |

### Insurance Industry

| Organization | Database | Data Points |
|-------------|----------|-------------|
| **Liikennevakuutuskeskus (LVK)** | Claims database | claims.history |
| **Vakuutusyhtiöt** (Insurance companies) | Policy system | policy.active, claim.pending, claim.type, usage.purpose, property data |
| **Korjaamot** (Repair shops) | Repair records | damage.type, damage.severity, property.value |

### Healthcare

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **SOTE** (Social and health services) | Patient records (Kanta) | injury.type, treatment.type, injury.person.injured |
| **Lääkärikeskukset** (Medical centers) | Medical certificates | treatment.necessity, injury.percentage, pain.level, work_ability.lost_days |

---

## API Integration Potential

### Real-Time APIs

| API | Provider | Data Points |
|-----|----------|-------------|
| Traficom Vehicle API | Traficom | vehicle.* |
| Population Register API | DVV | survivor.* |
| Kanta (eHealth) | THL | injury.*, treatment.* |
| Accident Register | OTI | accident.* |

### Batch Data

| Source | Update Frequency | Data Points |
|--------|------------------|-------------|
| Claims history (LVK) | Monthly/Annual | claims.history |
| Tax records (Tulorekisteri) | Real-time | income.* |
| FIN-FSA register | Daily | insurer.status |

---

## Data Quality Considerations

### Critical Data Points (Must Have)
- vehicle.permanent_location - From official register
- driver.age - From license register
- accident.date - From police/insurance
- income.amount - From tax records

### Important (Should Have)
- damage.severity - Expert assessment
- injury.percentage - Medical certificate
- claims.history - Industry database

### Nice to Have
- vehicle.value - Market data
- pain.level - Subjective assessment
