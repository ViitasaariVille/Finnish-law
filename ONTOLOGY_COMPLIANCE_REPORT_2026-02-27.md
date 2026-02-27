# Finnish Work Accident Ontology Compliance Report
**Date:** February 27, 2026  
**Law:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Ontology File:** `tyotapaturma_ammattitautilaki/ontology/work_accident_ontology.md`

## Executive Summary

This report analyzes the ontology structure against the Finnish Work Accident and Occupational Disease Insurance Act. **4 critical/high severity ontology gaps** were identified and GitHub issues created.

### GitHub Issues Created
1. **#222** - Missing critical compensation type entities (CRITICAL)
2. **#227** - Survivor entity hierarchy incomplete (HIGH)
3. **#228** - Missing Vakuutuksenottaja entity and insurance classification (HIGH)
4. **#230** - Insurable event hierarchy incomplete (CRITICAL)

---

## Detailed Findings

### 1. Missing Critical Compensation Entities (CRITICAL)

**Law References:** §50-53

The ontology is missing standard compensation types that are core to work accident claims:

| Missing Entity | Law Section | Description | Key Attributes |
|---------------|-------------|-------------|----------------|
| **Hoitotuki** | §51 | Care allowance for assistance needs | 3 levels (perus/korotettu/ylin) with fixed amounts |
| **Vaatelisä** | §52 | Clothing allowance for assistive devices | 2 levels (standard/korotettu) |
| **Kodinhoidon lisäkustannukset** | §53 | Household additional costs | Max 1 year from accident |
| **Matka- ja majoituskulut** | §50 | Travel and accommodation | Public transport, private car rates, companion |

**Impact:** These are standard compensations in virtually every serious work accident claim. Their absence makes the ontology unsuitable for claim processing.

---

### 2. Survivor Entity Hierarchy Incomplete (HIGH)

**Law References:** §99-104

The current ontology defines `Survivor` with subclasses `Widow, Child, Dependent`, but this oversimplifies the legal definitions:

#### Leski (Widow/Widower) - §100
The law distinguishes:
- **Aviopuoliso** (spouse) - automatic entitlement
- **Avopuoliso** (domestic partner) - requires:
  - Continuous cohabitation in shared household
  - Marriage-like conditions (avioliitonomaiset olosuhteet)
  - Shared child OR notarized maintenance agreement
  - Deceased was not married at time of death

#### Lapsi (Child) - §101
Eligibility extends beyond age 18:
- Under 18: automatic entitlement
- 18-25: if studying full-time (päätoimisesti opiskelee)
- 18+: if disabled/ unable to support self
- Special orphan provisions (täysorpo) - §104 adds 15% pension share

#### Missing Marriage Duration Requirement - §102
Post-accident marriage only qualifies if:
- Marriage produced a child, OR
- Marriage lasted at least 3 years

---

### 3. Missing Vakuutuksenottaja Entity (HIGH)

**Law References:** §156-158, §188-190

The ontology conflates `Työnantaja` (Employer) with `Vakuutuksenottaja` (PolicyHolder), but the law distinguishes these:

| Scenario | Vakuutuksenottaja | Työnantaja |
|----------|------------------|------------|
| Employee insurance | Työnantaja | Työnantaja |
| Entrepreneur insurance | Yrittäjä (themselves) | N/A (self-employed) |

#### Missing Insurance Type Classification - §158
The ontology doesn't capture the critical distinction between:
- **Jatkuva vakuutus** (Continuous insurance) - calendar year periods, continues until terminated
- **Määräaikainen vakuutus** (Fixed-term insurance) - max 1 year for specific work/project

---

### 4. Insurable Event Hierarchy Incomplete (CRITICAL)

**Law References:** §15, §17, §20, §26, §33-35

#### Missing: Työliikekipeytyminen - §33
A critical gap - muscle/tendon strain from single strenuous work movement:
- NOT a tapaturma (accident) - no external sudden event
- Compensated similarly to accidents
- Maximum 6 weeks compensation
- Must exclude pre-existing conditions

#### Recommended Hierarchy

```
Vahinkotapahtuma (InsurableEvent)
│
├── Työtapaturma (WorkAccident)
│   ├── Tapaturma (Accident) §17
│   │   └── Sudden external event causing injury
│   ├── Työliikekipeytyminen (Strain Injury) §33
│   │   └── Single strenuous work movement
│   ├── Pahoinpitely/Tahallinen teko §34
│   │   └── Violence/intentional act related to work duties
│   └── Henkinen järkytysreaktio §35
│       ├── Akuutti stressireaktio
│       ├── Traumaperäinen stressihäiriö (PTSD)
│       └── Persoonallisuuden muutos
│
└── Ammattitauti (OccupationalDisease) §26
    ├── Luettelon mukainen sairaus §27
    ├── Yläraajan jännetulehdus §28
    ├── Rannekanavaoireyhtymä §29
    └── Muun vamman/sairauden paheneminen §30
```

#### Critical Missing Attribute
**Vahinkopäivä** (Date of Injury) - §15:
- For accidents: the day of occurrence
- For occupational diseases: day first seeking medical care

---

## Additional Observations

### Entities Present and Correctly Defined ✓

| Entity | Law Basis | Status |
|--------|-----------|--------|
| Employee (Työntekijä) | §2, §8 | Present with basic definition |
| Entrepreneur (Yrittäjä) | §2, §188-190 | Present |
| Employer (Työnantaja) | §2, §3 | Present |
| MandatoryInsurance | §3 | Present |
| VoluntaryWorkTimeInsurance | §188-198 | Present |
| OccupationalAccident | §20 | Present (hierarchy incomplete) |
| OccupationalDisease | §26 | Present |
| InsuranceCompany | §205 | Present |
| StateTreasury (Valtiokonttori) | §207 | Present |
| AccidentInsuranceCentre | §209 | Present |
| ClaimAppealBoard | §226 | Present |

### Partially Correct Entities ⚠️

| Entity | Issue | Recommendation |
|--------|-------|----------------|
| PsychologicalShock | Missing legal conditions from §35 | Add attributes for 6-month manifestation rule, direct involvement requirement |
| Survivor | Over-simplified hierarchy | Restructure with proper legal subclasses |
| DailyAllowance | Present but lacks relation to specific calculation types | Add päiväraha classification |

---

## Ontology Coverage Summary

| Category | Coverage | Gaps |
|----------|----------|------|
| **Person Entities** | 60% | Missing Vakuutuksenottaja, detailed survivor types |
| **Insurance Types** | 70% | Missing jatkuva/määräaikainen distinction |
| **Insurable Events** | 65% | Missing Työliikekipeytyminen, incomplete hierarchy |
| **Compensation Types** | 50% | Missing Hoitotuki, Vaatelisä, Kodinhoidon kulut |
| **Institutions** | 90% | Well covered |
| **Relations** | 55% | Many key relations not modeled |

---

## Recommendations

### Immediate Actions (Critical)
1. Add Työliikekipeytyminen as distinct insurable event type
2. Add Hoitotuki, Vaatelisä, Kodinhoidon lisäkustannukset entities
3. Add Vahinkopäivä attribute to all injury events
4. Distinguish Vakuutuksenottaja from Työnantaja

### Short-term Actions (High Priority)
1. Refactor Survivor hierarchy with legal subclasses
2. Add insurance type classification (jatkuva/määräaikainen)
3. Complete psychological shock conditions
4. Add travel/accommodation compensation entity

### Long-term Improvements
1. Add relations for all legal obligations
2. Model claim filing deadlines (§116)
3. Model appeal procedures
4. Add jurisdiction/geographic scope entities (§13-14)

---

## Compliance Status: **PARTIAL**

The ontology covers basic concepts but has significant gaps in:
- Standard compensation types (§50-53)
- Detailed survivor classifications (§99-104)
- Insurance policyholder modeling (§156-158)
- Complete insurable event hierarchy (§15-35)

**Recommendation:** Address CRITICAL issues before using ontology for claim processing systems.

---

*Report generated by OpenClaw Agent - Finnish Law Compliance Check*  
*Model: Gemini with maximal thinking*
