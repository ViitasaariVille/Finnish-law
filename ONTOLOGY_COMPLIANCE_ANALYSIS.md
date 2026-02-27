# Finnish Work Accident Ontology Compliance Analysis
## Ontology Structure Review vs. Työtapaturma- ja ammattitautilaki (459/2015)

**Analysis Date:** 2026-02-27  
**Law Version:** 459/2015 (in force 2016-01-01)  
**Ontology Version:** 1.0  

---

## Executive Summary

The ontology demonstrates **good coverage** of the Finnish Work Accident Law's core entities and relationships. However, **several ontology-level gaps** have been identified that require GitHub issues for proper tracking and resolution.

**Overall Assessment:**
- ✅ **Entities:** ~85% coverage - Core entities present
- ⚠️ **Attributes:** ~80% coverage - Some legal attributes missing
- ⚠️ **Relations:** ~75% coverage - Key relationships need strengthening
- ⚠️ **Hierarchy:** ~80% coverage - Some inheritance issues
- ⚠️ **Enumerations:** ~85% coverage - Some enum values incomplete

---

## 1. ENTITY GAPS IDENTIFIED

### 1.1 Missing Core Entities

#### A. **Vahinkotapahtuma (DamageEvent)** - §15
**Status:** ❌ MISSING AS DISTINCT ENTITY
**Severity:** HIGH

**Law Reference:** §15 - "Korvattavat vahinkotapahtumat"
- Defines "vahinkotapahtuma" as the compensable event (work accident or occupational disease)
- "Vahinkopäivällä tarkoitetaan työtapaturman sattumispäivää ja 31 §:n mukaista ammattitaudin ilmenemispäivää"

**Current Ontology Issue:**
The ontology has `Vahinko` (Damage) and various accident types, but **no distinct `Vahinkotapahtuma` (DamageEvent) entity** that represents the event itself, which is the central legal concept for determining:
- When the claim filing deadline starts (§116)
- Which insurance company is liable (§32)
- The vahinkopäivä (damage day) concept

**Required Entity:**
```
### Vahinkotapahtuma (DamageEvent)
- **Description**: The compensable event - work accident or occupational disease occurrence
- **Legal Basis**: §15
- **Attributes**:
  - eventDate (vahinkopäivä) - §15.2
  - eventType: enum [work_accident, occupational_disease]
  - liabilityDeterminationDate
  - relatedInsurancePolicy
```

---

#### B. **Työkyvyttömyys (Incapacity)** - §56, §63
**Status:** ❌ MISSING AS DISTINCT ENTITY
**Severity:** HIGH

**Law Reference:** §56 - "Oikeus päivärahaan" - requires incapacity to work

**Current Ontology Issue:**
The ontology has `DailyAllowance` and `DisabilityPension` but **no `Työkyvyttömyys` (Incapacity) entity** to represent the state of being unable to work, which is:
- The trigger for daily allowance (§56)
- Required to be "at least 3 consecutive days" for waiting period (§56.3)
- Distinct from "työkyvyn heikentymä" (work capacity reduction) which is for pension

**Required Entity:**
```
### Incapacity (Työkyvyttömyys)
- **Description**: State of being unable to perform work due to injury/disease
- **Legal Basis**: §56
- **Attributes**:
  - incapacityType: enum [total, partial]
  - startDate
  - endDate
  - consecutiveDaysCount
  - medicalCertification: reference to MedicalCertificate
```

---

#### C. **Kuntoutustarve (RehabilitationNeed)** - §88, §89
**Status:** ❌ MISSING
**Severity:** MEDIUM

**Law Reference:** §88, §89 - Occupational rehabilitation requirements

The law requires insurance companies to investigate rehabilitation need. This should be a distinct entity with:
- Assessment date
- Need determination (boolean)
- Next assessment deadline
- Type of rehabilitation needed

---

#### D. **Omaisuusvahinko (PropertyDamage)** - §54
**Status:** ⚠️ PARTIALLY PRESENT (as enum in PropertyDamageApplication)
**Severity:** MEDIUM

**Law Reference:** §54 - "Eräiden henkilökohtaisessa käytössä olleiden esineiden korvaaminen"

The ontology lists item types in `PropertyDamageApplication` but **no distinct `Omaisuusvahinko` entity** for property damage claims.

---

### 1.2 Entity Attribute Gaps

#### A. **InjuredParty (Vahingoittunut)** - §2.6, §111
**Missing Attributes:**
1. **sotu/henkilötunnus** format validation - §111 requires "henkilötunnus"
2. **opiskelija status** - §70-77 special rules for students
3. **eläke status** - §56.4, §73, §74 for retirees
4. **muu työsuhde** (other employment) - §111.2.5 required in notification
5. **muu yrittäjätyö** (other entrepreneur work) - §111.2.5 required in notification

---

#### B. **Employer (Työnantaja)** - §3, §111
**Missing Attributes:**
1. **payroll threshold status** - §3.2 (€1,200 exemption)
2. **state employer status** - §3.3
3. **vakuutuskelpoinen status** - §156-160
4. **maksuperuste type** - §166 (erikoismaksuperusteinen vs taulustomaksuperusteinen)

---

#### C. **InsurancePolicy (Vakuutussopimus)** - §156-160
**Missing Attributes:**
1. **policyType**: enum [mandatory, voluntary_work_time, voluntary_free_time]
2. **maksuperuste**: enum [table_based, experience_rated, fixed]
3. **selfResponsibilityAmount** - §184
4. **transferHistory** - §162

---

## 2. RELATIONSHIP GAPS

### 2.1 Missing Key Relations

#### A. **Vahinkotapahtuma → Insurance Company Liability** - §32, §113
**Status:** ❌ MISSING

The law at §32 specifies how to determine which employer/insurer is liable when:
- Multiple employers
- Multiple insurance periods
- Occupational disease manifestation after employment ended

**Required Relation:**
```
Vahinkotapahtuma -- liableInsuranceCompany --> InsuranceCompany
Vahinkotapahtuma -- liableEmployer --> Employer
Vahinkotapahtuma -- primaryExposureEmployer --> Employer (for occupational diseases)
```

---

#### B. **DailyAllowance → WaitingPeriod** - §56.3
**Status:** ⚠️ PARTIAL

Current ontology has both entities but **no explicit relation** linking a DailyAllowance to its WaitingPeriod.

**Required:**
```
DailyAllowance -- hasWaitingPeriod --> WaitingPeriod
WaitingPeriod -- mustBeConsecutiveDays --> Integer (3 days per §56.3)
```

---

#### C. **Työtapaturma → CommuteAccident/BusinessTripAccident hierarchy**
**Status:** ❌ INCORRECT HIERARCHY

Current ontology:
```
OccupationalAccident
├── WorkplaceAccident
├── CommuteAccident
├── BusinessTripAccident
└── WorkRelatedActivityAccident
```

**Law-based hierarchy should be:**
```
Vahinkotapahtuma (DamageEvent)
├── Työtapaturma (WorkAccident) - §20
│   ├── TyössäSattunut (AtWork) - §21
│   ├── TyöntekopaikanAlueella (WorkplaceArea) - §22
│   ├── TyöntekopaikanUlkopuolella (OutsideWorkplace) - §23
│   │   ├── CommuteAccident (§23.1)
│   │   └── BreakAccident (§23.2)
│   └── ErityisissäOlosuhteissa (SpecialCircumstances) - §24
├── Ammattitauti (OccupationalDisease) - §26
└── Työliikekipeytyminen (WorkMotionStrain) - §33
```

---

### 2.2 Missing Entity-to-Law-Section Mappings

Many entities lack explicit mapping to the legal sections that define them. For ontology compliance tracking, each entity should have:
- `definedInSection` attribute
- `amendedBySections` array (for future law changes)

---

## 3. HIERARCHY ISSUES

### 3.1 **Beneficiary (Edunsaaja) Hierarchy** - §99-109

**Current Ontology:**
```
Beneficiary
├── Leski (WidowEquivalent)
│   ├── Aviopuoliso (StatutorySpouse)
│   └── Avopuoliso (CohabitingPartner)
├── LapseneläkkeenSaaja (ChildPensionRecipient)
└── Dependent
```

**Issues:**
1. **Missing:** `Rintaperillinen` (intestate heir) - §99 general concept
2. **Missing:** Beneficiary priority order (leski > lapset > other dependents)
3. **Missing:** Leski vs CohabitingPartner mutual exclusivity per §100.3

### 3.2 **Compensation Types Missing from Hierarchy**

**Missing in hierarchy (all in Chapter 10):**
- `Ansionmenetyskorvaus` (EarningsLossCompensation) - parent of DailyAllowance, DisabilityPension
- `Päiväraha` hierarchy needs §56-§62 subclasses for calculation methods

---

## 4. ENUMERATION GAPS

### 4.1 **InjuryType** (Vammatyyppi)
**Status:** ⚠️ INCOMPLETE

Current ontology has `InjuryType` but should include §18 special conditions:
- `friction_blister` (§18.1)
- `corrosive_contact` (§18.2)
- `gas_vapor_inhalation` (§18.3)
- `temperature_injury` (§18.4)
- `radiation_injury` (§18.5)
- `pressure_variation` (§18.6)

### 4.2 **NegligenceType** (Myötävaikutus) - §61
**Current:** `[alcohol_drugs, safety_violation, gross_negligence, criminal]`

**Should include per §61.1:**
- `alcohol_or_drug_influence` (alkoholin tai huumausaineen vaikutuksenalaisuus)
- `medicine_misuse` (lääkeaineen väärinkäyttö)
- `intentional_safety_violation` (tahallinen menettely)
- `grossly_negligent_safety_violation` (törkeän huolimaton menettely)
- `other_gross_negligence` (muu törkeä huolimattomuus)
- `criminal_activity` (rikollinen toiminta)

### 4.3 **Missing: AsianosaisenRooli** (PartyRole) - §117
**Law Reference:** §117 defines who are asianosaiset (parties)

```
PartyRole:
- vahingoittunut (injured party)
- edunsaaja (beneficiary - in death cases)
- NOT: työnantaja (explicitly excluded per §117)
- NOT: terveydenhuollon ammattihenkilö (excluded)
- NOT: kunta/kuntayhtymä (excluded for compensation cases)
```

---

## 5. INSTITUTIONAL ENTITY GAPS

### 5.1 **Missing: Tapaturma-asioiden muutoksenhakulautakunta** - §237
**Status:** ❌ MISSING

The ontology has `AccidentAppealsBoard` but also references `ClaimAppealBoard` (Tapaturma-asiain korvauslautakunta) from §226.

**Two distinct bodies:**
1. **Tapaturma-asiain korvauslautakunta** (§226-228) - advisory body, NOT appeal body
2. **Tapaturma-asioiden muutoksenhakulautakunta** (§237) - actual appeal body

These are **different entities** and both should be in the ontology.

### 5.2 **Missing: Vakuutusoikeus** (Insurance Court) - §237
**Status:** ⚠️ PRESENT but needs clarification

The ontology lists `InsuranceCourt` but should verify it's the same as "vakuutusoikeus" in §237.

### 5.3 **Missing: Käräjäoikeus** (District Court) - §228
**Status:** ❌ MISSING

§228 allows disputes to be taken to District Court as first instance.

---

## 6. PROCEDURAL DOCUMENTATION GAPS

### 6.1 **Ilmoitus (Notification) Hierarchy** - §110-113

**Current:** Single `Notification` entity with subclasses

**Should be:**
```
Ilmoitus (Notification)
├── TyöntekijänIlmoitus (EmployeeNotification) - §110
│   └── to: Employer
│   └── deadline: "immediately when possible"
├── TyönantajanIlmoitus (EmployerNotification) - §111
│   └── to: InsuranceCompany
│   └── deadline: "10 working days"
│   └── requiredFields: [personId, name, contact, employerInfo, ...]
├── TerveydenhuollonIlmoitus (HealthcareNotification) - §41
│   └── to: InsuranceCompany
│   └── deadline: "without delay"
└── VahingoittuneenIlmoitus (InjuredPartyNotification) - §112.2
    └── to: InsuranceCompany
    └── when: When employer fails to notify
```

---

## 7. RECOMMENDED GIT ISSUES TO CREATE

Based on this analysis, the following GitHub issues should be created:

### Issue #1: [ONTOLOGY] Create Vahinkotapahtuma (DamageEvent) entity
- **Priority:** HIGH
- **Law Ref:** §15
- **Description:** Create distinct DamageEvent entity to represent the compensable event itself, separate from Vahinko (Damage consequence)

### Issue #2: [ONTOLOGY] Create Työkyvyttömyys (Incapacity) entity
- **Priority:** HIGH
- **Law Ref:** §56
- **Description:** Add Incapacity entity to represent work inability state that triggers daily allowance

### Issue #3: [ONTOLOGY] Fix Työtapaturma entity hierarchy
- **Priority:** HIGH
- **Law Ref:** §20-§25
- **Description:** Reorganize accident type hierarchy to match legal structure with Vahinkotapahtuma as root

### Issue #4: [ONTOLOGY] Add missing attributes to InjuredParty
- **Priority:** MEDIUM
- **Law Ref:** §111.2
- **Description:** Add muuTyösuhde, muuYrittäjätyö, studentStatus, pensionStatus attributes

### Issue #5: [ONTOLOGY] Create distinct Muutoksenhakulautakunta entity
- **Priority:** MEDIUM
- **Law Ref:** §237
- **Description:** Separate Tapaturma-asioiden muutoksenhakulautakunta (appeal body) from Korvauslautakunta (advisory body)

### Issue #6: [ONTOLOGY] Complete Ilmoitus hierarchy
- **Priority:** MEDIUM
- **Law Ref:** §110-§113
- **Description:** Create full notification type hierarchy with deadlines and recipients

### Issue #7: [ONTOLOGY] Add Käräjäoikeus to institutions
- **Priority:** LOW
- **Law Ref:** §228
- **Description:** Add District Court as possible dispute resolution venue

### Issue #8: [ONTOLOGY] Create SyyYhteys entity for causation
- **Priority:** MEDIUM
- **Law Ref:** §16
- **Description:** Add CausalConnection entity for medical causation assessment

---

## 8. POSITIVE FINDINGS ✅

The ontology correctly captures:

1. ✅ **§2 Definitions** - Core terms defined
2. ✅ **§3 Insurance obligation** - Employer mandatory insurance
3. ✅ **§8-9 Employee scope** - Employment relationship definitions
4. ✅ **§17-20 Accident definitions** - Core accident concepts
5. ✅ **§26-32 Occupational disease** - Disease types and conditions
6. ✅ **§36-49 Medical care** - Healthcare compensation types
7. ✅ **§51 Care allowance levels** - Perus/Korotettu/Ylin enumeration
8. ✅ **§52 Clothing allowance levels** - Basic/Elevated enumeration
9. ✅ **§83-87 Permanent damage** - Haittaluokat 1-20 enumeration
10. ✅ **§99-109 Survivor benefits** - Family pension structure
11. ✅ **§209 Tapaturmavakuutuskeskus** - Central institution defined
12. ✅ **§226 ClaimAppealBoard** - Advisory body present
13. ✅ **§235 Work Accident Register** - Registry entity defined

---

## 9. CONCLUSION

The Finnish Work Accident Ontology provides a **solid foundation** with approximately 80-85% coverage of the legal concepts at the structural level. The identified gaps are primarily:

1. **Missing root entity** (`Vahinkotapahtuma`) that is central to the legal framework
2. **Missing state entity** (`Työkyvyttömyys`) for incapacity tracking
3. **Hierarchy issues** in accident classification
4. **Missing institutional entities** for appeals process
5. **Incomplete notification hierarchy**

These gaps should be addressed through the recommended GitHub issues to achieve full ontology-level compliance with the law before proceeding to DMN business rules implementation.

**Next Steps:**
1. Create GitHub issues for HIGH priority gaps
2. Review and merge attribute additions
3. Refine entity hierarchy
4. Add missing institutional entities
5. Validate enumeration completeness

---

*Analysis completed using Gemini maximal reasoning mode*
*Source: Työtapaturma- ja ammattitautilaki (459/2015)*
*Ontology: tyotapaturma_ammattitautilaki/ontology/work_accident_ontology.md*
