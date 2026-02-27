# Finnish Work Accident Ontology Compliance Analysis
## Työtapaturma- ja ammattitautilaki (459/2015) Structural Compliance Report

**Analysis Date:** 2026-02-27
**Ontology Version:** 1.0
**Law Version:** 459/2015 (effective 2016-01-01)
**Analysis Type:** ONTOLOGY STRUCTURE ONLY (excludes business rules/formulas)

---

## 1. EXECUTIVE SUMMARY

### Overall Compliance Status: **PARTIALLY COMPLIANT** ⚠️

The ontology captures the majority of core entities from Työtapaturma- ja ammattitautilaki, but contains **significant structural gaps** that would impede accurate legal compliance checking. Key issues include missing entities, incomplete enumerations, attribute mismatches, and incorrect hierarchical relationships.

| Category | Status | Notes |
|----------|--------|-------|
| Core Entities | ⚠️ Partial | Missing key legal entities |
| Attributes | ⚠️ Partial | Several attributes misaligned with law |
| Relations | ⚠️ Partial | Some relationships incorrect |
| Hierarchy | ❌ Non-compliant | Several class hierarchy issues |
| Enumerations | ⚠️ Partial | Multiple enum values missing |

### Critical Gaps Summary
- **13 missing entities** identified from law sections §2, §9, §70-77, §95-96, §107, §229-232
- **5 incorrect hierarchies** - entities placed under wrong superclasses
- **9 incomplete enumerations** - missing valid values defined in law
- **3 missing institution types** - appeal bodies incorrectly modeled

---

## 2. DETAILED FINDINGS BY SECTION

### 2.1 PERSON ENTITIES (Chapter 2, §8-12)

#### 2.1.1 Missing Entities

| Law Section | Entity Name | Description | Severity |
|-------------|-------------|-------------|----------|
| §9.4 | **Perheenjäsen** (FamilyMember - Narrower) | Law defines: spouse, cohabiting partner, direct ascendant/descendant living in same household | HIGH |
| §2.8 | **Kolmas valtio** (ThirdCountry) | State not covered by EU social security regulations | MEDIUM |
| §10 | **Yrittäjä** (Entrepreneur - Full definition) | Law §188-190 specific types missing from ontology | MEDIUM |
| §11 | **Maatalousyrittäjä** (AgriculturalEntrepreneur) | Explicitly excluded from this law per §11 | LOW |

**Ontology Gap:** FamilyMember exists but §9.4 defines specific calculation rules for ownership (30% individual, 50% family) that require additional attributes.

#### 2.1.2 Incorrect Attributes

**Employee Entity (§8):**
- ❌ **Missing:** employmentContractType enumeration (employment contract, maritime employment, public service, municipal service, church service, parliamentary service, other public law service)
- ❌ **Missing:** isLeadingPosition boolean (§9 johtava asemassa oleva)
- ❌ **Missing:** ownershipPercentage for leading position employees

**Student Entity (§70-77):**
- ❌ **Missing:** studentStatus enumeration (päätoiminen opiskelija, perusopetus, lukio)
- ⚠️ **Partial:** studentType values don't match law categories
- ❌ **Missing:** estimatedFutureEarnings attribute (§76 tuleva ansio)

#### 2.1.3 Hierarchy Issues

```
CURRENT (INCORRECT):
  Person
    ├── Employee
    ├── Student  
    ├── Entrepreneur
    └── InjuredParty

REQUIRED (CORRECT per §2):
  Työntekijä (Employee) §8
    ├── EmploymentContractEmployee
    ├── MaritimeEmployee  
    ├── PublicServant
    ├── MunicipalOfficial
    ├── ChurchOfficial
    ├── ParliamentaryOfficial
    └── OtherPublicLawEmployee
    
  Yrittäjä (Entrepreneur) §10
    ├── YEL-InsuredEntrepreneur §188
    └── Non-YELEntrepreneur (excluded)
    
  Vahingoittunut (InjuredParty) §15-16
    ├── Can be Employee OR Entrepreneur
    └── Has specific attributes per §111.2
```

### 2.2 INSURABLE EVENTS (Chapters 5-7, §17-35)

#### 2.2.1 Missing Event Types

| Law Section | Event Type | Current Status | Severity |
|-------------|------------|----------------|----------|
| §25 | **Kotona tehtävä työ** (WorkAtHome) | Missing | HIGH |
| §24.8 | **Majoitusolosuhteiden tapaturma** (AccommodationAccident) | Missing | MEDIUM |
| §35 | **Persoonallisuuden muutos** (PersonalityChange) | Missing | HIGH |
| §34 | **Tahallinen teko** (IntentionalAct) | Missing | MEDIUM |

#### 2.2.2 Incomplete Enumerations

**PsychologicalShock (§35):**
```
CURRENT ENUM values:
- AcuteStressReaction
- PTSD  
- PersonalityChange

MISSING per §35:
- Tuhoisaa kokemusta seuraava persoonallisuuden muutos (Destructive-experience-following personality change)
  * Has 6-month diagnostic window requirement
  * Requires direct involvement in event
```

**SpecialAccidentConditions (§18):**
```
CURRENT ENUM values (CORRECT):
- FrictionBlister ✓
- CorrosiveInjury ✓
- GasVaporInhalation ✓
- TemperatureInjury ✓
- RadiationInjury ✓
- PressureVariationInjury ✓

MISSING CONSTRAINTS:
- All require exposure within max 1 day before injury appears
- Must NOT be occupational disease
```

#### 2.2.3 Hierarchy Correction Required

```
CURRENT (INCORRECT):
  OccupationalAccident
    ├── WorkplaceAccident
    ├── CommuteAccident
    ├── BusinessTripAccident
    └── WorkRelatedActivityAccident

REQUIRED (CORRECT per §20-25):
  Työtapaturma (OccupationalAccident)
    ├── Tapaturma työssä (Accident at work) §21
    │   ├── Actual work
    │   ├── Trust representative duties
    │   ├── Employer business handling
    │   └── Work-related travel
    ├── Tapaturma työntekopaikan alueella (Accident at workplace) §22
    ├── Tapaturma työntekopaikan alueen ulkopuolella (Accident outside workplace) §23
    │   ├── Commute accident (with minor detour allowed)
    │   └── Break/meal near workplace
    ├── Tapaturma erityisissä olosuhteissa (Accident in special circumstances) §24
    │   ├── Training event
    │   ├── Recreation event (employer organized)
    │   ├── Work capacity maintenance activity
    │   ├── Medical appointment (work injury related)
    │   ├── Medical appointment (sudden illness)
    │   ├── Physical exercise during work time
    │   ├── Travel to/from above
    │   └── Accommodation with exceptional risk
    └── Tapaturma kotona (Accident at home) §25
        └── NOT covered by §22-23
```

### 2.3 COMPENSATION TYPES (Chapters 8-13, §36-109)

#### 2.3.1 Missing Compensation Entities

| Law Section | Entity | Description | Severity |
|-------------|--------|-------------|----------|
| §92 | **Kuntoutusraha koulutuksen jälkeen** (PostTrainingRehabilitationAllowance) | Specific to 6 months after training | MEDIUM |
| §93 | **Palveluasuminen** (AssistedLiving) | €46.82/day for severely injured | MEDIUM |
| §96 | **Tulkkauspalvelut** (InterpretationServices) | For severe vision/hearing/speech impairment | LOW |
| §97 | **Omaisen sopeutumisvalmennus** (FamilyAdaptationTraining) | Relative's adaptation training costs | LOW |
| §106 | **Kertasuoritus leskeneläkkeen sijaan** (WidowPensionLumpSum) | 3 years pension as lump sum | MEDIUM |

#### 2.3.2 Attribute Gaps

**DailyAllowance (§56-62):**
```
MISSING ATTRIBUTES:
- waitingPeriodStartDate (odotusajan alkamispäivä)
- waitingPeriodDays (fixed at 3 per §56.3)
- extensionReason (for beyond 1 year per §60)
- reductionReasonType: [alcohol_drugs, safety_violation, gross_negligence, criminal]
- reductionPercentage (max 50% per §61)
- isMinimumDailyAllowance (§60 vähimmäispäiväraha)
```

**DisabilityPension (§63-68):**
```
MISSING ATTRIBUTES:
- pensionStartType: [fixed_term, indefinite]
- lumpSumIncreaseYear (kertakorotusvuosi per §67)
- lumpSumIncreasePercentage (16% → 0.462% based on age)
- pensionAdjustmentIndex (työeläkeindeksi per §66)
- pensionEndAge65: boolean (pension reduces to 70% at 65)
```

**PermanentDamageCompensation (§83-87):**
```
MISSING ATTRIBUTES:
- isPermanent (determined when no medical probability of improvement)
- permanencyAssessmentDate (earliest 1 year from injury date)
- isLumpSum (classes 1-5 per §87.1)
- isContinuous (classes 6-20 per §87.1)
- painLevel: [none, moderate, severe] (affects class per §84.2)
- combinedDisabilityFormula (A × B / 20 calculation per §84.4)
```

#### 2.3.3 Incorrect Enumerations

**Haittaluokka (DisabilityClass) §86:**
```
CURRENT: Percentages provided

MISSING CONSTRAINTS per §87:
- Classes 1-5: Paid as lump sum (kertakaikkinen)
- Classes 6-20: Paid continuously (jatkuva)
- Rapidly fatal diseases: Class 10 equivalent lump sum even if higher class
```

### 2.4 PROCEDURAL ENTITIES (Chapters 14-18, §110-155)

#### 2.4.1 Missing Procedural Entities

| Law Section | Entity | Description | Severity |
|-------------|--------|-------------|----------|
| §110 | **Työntekijän ilmoitus** (EmployeeNotification) | To employer immediately | HIGH |
| §111 | **Työnantajan ilmoitus** (EmployerNotification) | To insurer within 10 working days | HIGH |
| §113 | **Ilmoitus vakuutusyhtiölle** (NotificationToInsurer) | Specific notification routing | MEDIUM |
| §114 | **Toimivaltakiista** (CompetenceDispute) | When insurers disagree | LOW |
| §115 | **Vireilletuloilmoitus** (CaseOpeningNotification) | To injured party | MEDIUM |
| §119 | **Selvittämisvelvollisuus** (InvestigationObligation) | 7 working days to start | MEDIUM |
| §123 | **Lautakunnan lausuntopyyntö** (BoardOpinionRequest) | For principled questions | LOW |
| §138 | **Ennakkomaksu** (AdvancePayment) | Without final decision | MEDIUM |
| §150 | **Takautuva korvaus** (RetroactiveCompensation) | After processing suspension | MEDIUM |

#### 2.4.2 ClaimFilingDeadline Issues (§116)

```
CURRENT ATTRIBUTES:
- standardDeadlineYears: 5 ✓
- standardDeadlineStarts: accidentDate OR firstMedicalAssessmentDate ✓
- lateFilingPermitted: boolean ✓
- lateFilingConditions: [not_claimants_fault, unreasonable_to_deny] ✓

MISSING ATTRIBUTES:
- deadlineCalculationBase: [vahinkopäivä, first_medical_assessment]
- isOccupationalDisease: boolean (different deadline calculation)
- extendedFilingGrounds: [not_claimants_fault, unreasonable_to_deny] §116.2
```

### 2.5 INSTITUTIONS (Chapters 27-29, §205-228)

#### 2.5.1 Institution Hierarchy Issues

```
CURRENT (INCORRECT):
  Institutions
    ├── InsuranceCompany
    ├── StateTreasury
    ├── AccidentInsuranceCentre
    ├── ClaimAppealBoard  ← WRONG: Not an appeal body!
    ├── AccidentAppealsBoard
    ├── InsuranceCourt
    └── DistrictCourt

REQUIRED (CORRECT per §226-237):
  Vakuutuslaitokset (Insurance Institutions)
    ├── Vakuutusyhtiö (InsuranceCompany) §205
    ├── Valtiokonttori (StateTreasury) §207
    └── Tapaturmavakuutuskeskus (AccidentInsuranceCentre) §209
    
  Muutoksenhakuelimet (Appeal Bodies) §237
    ├── Tapaturma-asioiden muutoksenhakulautakunta (AccidentAppealsBoard)
    ├── Vakuutusoikeus (InsuranceCourt)
    └── Korkein oikeus (SupremeCourt)
    
  Asiantuntijaelimet (Expert Bodies)
    └── Tapaturma-asiain korvauslautakunta §226  ← Advisory only!
      * Issues recommendations/lausunnot
      * NOT an appeal body
      * 1 chairperson, 3 legal members, 4 labor market members, 5+ medical experts
```

**CRITICAL ERROR:** The ontology incorrectly models `ClaimAppealBoard` (Tapaturma-asiain korvauslautakunta) as an appeal body. Per §226, this is an **advisory body** that issues recommendations (suosituksia, lausuntoja) - it does NOT handle appeals.

#### 2.5.2 Missing Institution Entities

| Law Section | Entity | Description | Severity |
|-------------|--------|-------------|----------|
| §7 | **Lain soveltamisen ratkaisu** (ApplicationDeterminationBody) | Determines if law applies to specific work | HIGH |
| §114 | **Tapaturma-asioiden muutoksenhakulautakunta** (AccidentAppealsBoard) | First instance appeal body | HIGH |
| §237 | **Vakuutusoikeus** (InsuranceCourt) | Appellate body | HIGH |
| §237 | **Korkein oikeus** (SupremeCourt) | Final appeal with permission | MEDIUM |
| §230 | **Yhteistakuumaksu** (JointGuaranteePayment) | Shared liability mechanism | LOW |

### 2.6 INSURANCE STRUCTURE (Chapters 20-22, §156-187)

#### 2.6.1 Missing Insurance Entities

| Law Section | Entity | Description | Severity |
|-------------|--------|-------------|----------|
| §156 | **Vakuutuksenottaja** (PolicyHolder) | Entity taking out insurance | HIGH |
| §158 | **Jatkuva vakuutus** (ContinuousInsurance) | Calendar year based | MEDIUM |
| §158 | **Määräaikainen vakuutus** (FixedTermInsurance) | Max 1 year for specific work | MEDIUM |
| §163 | **Konkurssipesä** (BankruptcyEstate) | Takes over insurance obligation | LOW |
| §171 | **Riskiluokitus** (RiskClassification) | Maintained by Accident Insurance Centre | HIGH |
| §166.5 | **Työturvallisuustyö** (WorkSafetyPrevention) | Documented preventive work | MEDIUM |

#### 2.6.2 InsuranceTransfer Issues (§162)

```
CURRENT ATTRIBUTES (PARTIAL):
- transferRequestDate ✓
- effectiveTransferDate ✓
- previousInsuranceCompany ✓
- newInsuranceCompany ✓
- statisticalHistoryYears: 5 ✓
- deliveryDeadline: 14 days ✓

MISSING ATTRIBUTES:
- transferQuarter: [march, june, september, december]
- noticeDeadline: 3 months before quarter end
- transferValidity: [first_transfer_valid, multiple_transfers_handled]
- isFirstPolicyPeriod: boolean (cannot transfer before first period ends)
```

### 2.7 DEATH BENEFITS (Chapter 13, §99-109)

#### 2.7.1 Survivor Benefits Structure

```
CURRENT (INCORRECT):
  Beneficiary
    ├── Leski (WidowEquivalent)
    │   ├── Aviopuoliso (StatutorySpouse)
    │   └── Avopuoliso (CohabitingPartner)
    ├── LapseneläkkeenSaaja (ChildPensionRecipient)
    └── Dependent

REQUIRED (CORRECT per §99-104):
  Perhe-eläke (FamilyPension) §99
    ├── Leskeneläke (WidowPension) §100
    │   ├── Aviopuoliso (StatutorySpouse) §100.1
    │   └── Avopuoliso (CohabitingPartner) §100.2
    │       * Continuous cohabitation
    │       * Marriage-like conditions
    │       * Common child OR notarized support agreement
    │       * Deceased NOT married at death
    │       * OR divorce proceedings pending (separate living)
    │
    ├── Lapseneläke (ChildPension) §101
    │   ├── Under 18 years
    │   ├── 18-25 years if studying
    │   ├── 18-25 years if disabled
    │   └── Also applies to cohabiting partner's child §101.2
    │       (if deceased supported them)
    │
    └── Perhe-eläkkeen määrä §104
        ├── Maximum 70% of annual work income
        ├── Spouse share: 40% → 15% (based on child count)
        └── Child share: 25% → 55% (based on child count)
            * Plus 15% for full orphans
```

#### 2.7.2 Missing Death-Related Entities

| Law Section | Entity | Description | Severity |
|-------------|--------|-------------|----------|
| §102 | **Avioliiton jälkeen syntynyt eläkeoikeus** (PostMarriagePensionRight) | Marriage after accident - 3 years or child required | MEDIUM |
| §103.3 | **Leskeneläkkeen lakkaaminen** (WidowPensionTermination) | Remarriage or new cohabitation | MEDIUM |
| §104.5 | **Täysorpo** (FullOrphan) | Child with no surviving parents - 15% addition | MEDIUM |
| §106 | **Kertasuoritus** (LumpSumPayment) | 3 years pension as lump sum on remarriage | MEDIUM |
| §107 | **Tulolaskelma** (IncomeCalculation) | For widow pension adjustment | LOW |

### 2.8 OTHER COMPENSATION ENTITIES

#### 2.8.1 Recourse Rights (§95-96)

```
MISSING ENTITIES:
- Takautumisoikeus (RecourseRight) §95-96
  * Subrogation right against third party
  * Amount limited to compensation paid
  
- Vahingonaiheuttaja (DamageCauser) §95-96
  * Third party causing damage
  * Liability basis
  * Fault level
```

#### 2.8.2 Distribution System (§231)

```
CURRENT: DistributionSystem exists

MISSING ATTRIBUTES:
- distributionSystemYear (jakojärjestelmävuosi)
- ratioCoefficient (suhdeluku by May 31)
- preliminaryEstimate (ennakkoarvio by May 31)
- finalSettlement (lopullinen vahvistus following May 31)
- interestRate (reference rate from Interest Act §12)
- majorDamageThreshold: 75,000,000 EUR (suurvahinkoraja)
```

---

## 3. ENUMERATION COMPLIANCE MATRIX

| Enumeration | Law Section | Current Values | Missing Values | Status |
|-------------|-------------|----------------|----------------|--------|
| studentType | §70-77 | higher_education, vocational, basic_secondary | päätoiminen_opiskelu, perusopetus, lukio, alle_18 | ⚠️ |
| beneficiaryType | §99-109 | primary, contingent, statutory | leski, lapsi, täysorpo | ❌ |
| accidentType | §17-25 | workplace, commute, business_trip | kotona_tehtävä_työ, majoitusolosuhteet | ⚠️ |
| injuryType | §18 | 6 types | All present | ✅ |
| pensionType | §63-68 | disability | määräaikainen, toistaiseksi | ❌ |
| disabilityClass | §86 | 1-20 percentages | kertakaikkinen/jatkuva distinction | ⚠️ |
| notificationType | §110-113 | Not specified | työntekijän_ilmoitus, työnantajan_ilmoitus, terveydenhuollon_ilmoitus | ❌ |
| partyType | §117 | claimant, respondent, third-party, intervener | vahingoittunut, edunsaaja | ❌ |
| representativeType | §119 | legal-counsel, family-member, organizational | lähiomainen, huolehtinut_henkilö | ⚠️ |
| appealBodyType | §237 | Not specified | muutoksenhakulautakunta, vakuutusoikeus, korkein_oikeus | ❌ |

---

## 4. RECOMMENDED GITHUB ISSUES

### Issue #1: [CRITICAL] Fix Institution Hierarchy - Separate Advisory from Appeal Bodies
**Title:** `[STRUCTURE] Correct ClaimAppealBoard entity - advisory NOT appeal body`

**Body:**
```
## Problem
The current ontology incorrectly models ClaimAppealBoard (Tapaturma-asiain korvauslautakunta) 
as an appeal body. Per §226, this is an ADVISORY body that issues recommendations, not decisions.

## Law Reference
§226: " edistämään tämän lain mukaisen korvauskäytännön yhtenäisyyttä antamalla yleisohjeita ja lausuntoja"
(English: promote uniform compensation practice by issuing general guidelines and opinions)

## Required Changes
1. Rename ClaimAppealBoard → AccidentCompensationAdvisoryBoard
2. Add description: "Issues recommendations and opinions, NOT appeal decisions"
3. Add composition attributes per §227:
   - chairperson: 1 (Ministry of Social Affairs representative)
   - legalMembers: 3
   - laborMarketMembers: 4 (2 employer, 2 employee reps)
   - medicalExperts: 5+
4. Create new AccidentAppealsBoard entity per §237
   - First instance appeal body
   - Appeal deadline: 30 days
5. Create InsuranceCourt entity per §237
6. Create SupremeCourt entity (with permission requirement)

## Severity: CRITICAL
This misclassification could lead to incorrect procedural modeling.
```

### Issue #2: [HIGH] Add Missing Person Entities
**Title:** `[ENTITIES] Add missing person types per §9, §25, §188-190`

**Body:**
```
## Missing Entities
1. **WorkAtHomeWorker** (§25) - "kotona tehtävä työ" 
   - Special rules: §22-23 don't apply
   
2. **ThirdCountry** (§2.8) - "kolmas valtio"
   - State not covered by EU social security regulations
   - Affects foreign healthcare coverage (§47)
   
3. **YEL-InsuredEntrepreneur** (§188)
   - Must have YEL insurance
   - Annual work income = confirmed YEL work income
   
4. **Post68Entrepreneur** (§189)
   - Continues working past 68
   - Different income calculation

## Attributes Required
- WorkAtHomeWorker: workLocationType = home, undefined_location
- ThirdCountry: euSocialSecurityApplies = false
- YEL-InsuredEntrepreneur: yelInsuranceNumber, confirmedWorkIncome
- Post68Entrepreneur: continuationAge, actualWorkIncome

## Severity: HIGH
Missing entities prevent complete coverage modeling.
```

### Issue #3: [HIGH] Complete Death Benefit Hierarchy
**Title:** `[HIERARCHY] Restructure survivor benefits per §99-109`

**Body:**
```
## Current Issues
1. Beneficiary hierarchy incomplete
2. Missing full orphan (täysorpo) concept
3. Missing post-marriage pension rights
4. Missing lump sum on remarriage

## Required Structure
```
FamilyPension §99
├── WidowPension §100
│   ├── StatutorySpouse §100.1
│   └── CohabitingPartner §100.2
│       * Must have: continuous cohabitation, marriage-like conditions
│       * Must have: common child OR notarized support agreement
│       * Must NOT: deceased married at death (unless divorce pending)
├── ChildPension §101
│   ├── Under18
│   ├── Student18to25
│   └── Disabled18to25
│   └── CohabitingPartnerChild (if deceased supported)
├── FullOrphanAddition §104.4 (+15%)
└── PostMarriagePension §102 (3 years OR child required)
```

## Missing Attributes
- WidowPension: incomeAdjustmentStartDate (13th month after death)
- WidowPension: remarriageLumpSum (3 years equivalent)
- ChildPension: orphanType [one_parent, full_orphan]
- FamilyPension: totalMaximumPercentage (70%)

## Severity: HIGH
Death benefits are significant part of law.
```

### Issue #4: [MEDIUM] Add Missing Compensation Types
**Title:** `[ENTITIES] Add missing compensation entities from Chapters 8-13`

**Body:**
```
## Missing Entities (per law section)

### §92 - PostTrainingRehabilitationAllowance
- Available up to 6 months after training ends
- Only if annual earnings < pre-injury earnings
- Amount: partial daily allowance → partial disability pension

### §93 - AssistedLiving (Palveluasuminen)
- €46.82/day maximum
- For severely injured (vaikeasti vahingoittunut)

### §96 - InterpretationServices (Tulkkauspalvelut)
- For severe vision/hearing/speech impairment
- Limited to amount Kela would provide

### §97 - FamilyAdaptationTraining (Omaisen sopeutumisvalmennus)
- Travel and accommodation for relative
- Loss of earnings compensation

### §106 - WidowPensionLumpSum (Kertasuoritus)
- 3 years pension as lump sum
- When widow's right ends due to remarriage

## Attributes Required
See detailed attribute list in compliance report.

## Severity: MEDIUM
Entities exist but are not exhaustive.
```

### Issue #5: [MEDIUM] Fix Disability Class Enumeration
**Title:** `[ENUM] Add payment type distinction to DisabilityClass`

**Body:**
```
## Current State
DisabilityClass 1-20 with percentages only

## Missing per §87
- Classes 1-5: Paid as LUMP SUM (kertakaikkinen)
- Classes 6-20: Paid CONTINUOUSLY (jatkuva)
- Rapidly fatal diseases: Class 10 lump sum even if higher class applies

## Proposed Changes
```python
DisabilityClass:
  class: 1-20
  percentage: per §86 table
  paymentType: [lump_sum, continuous]  # DERIVED from class
  
DiseaseType:
  isRapidlyFatal: boolean
  # If true AND disabilityClass > 10:
  # effectiveLumpSumClass = 10
```

## Severity: MEDIUM
Affects compensation calculation modeling.
```

### Issue #6: [MEDIUM] Add Procedural Notification Entities
**Title:** `[ENTITIES] Add missing notification and procedural entities`

**Body:**
```
## Missing Entities

### §110 - EmployeeNotification (Työntekijän ilmoitus)
- To employer immediately
- Must provide certificate on request

### §111 - EmployerNotification (Työnantajan ilmoitus)
- To insurer within 10 working days
- Required content per §111.2 (6 items)

### §115 - CaseOpeningNotification (Vireilletulon ilmoitus)
- To injured party immediately
- Must include data protection notice

### §119 - InvestigationObligation (Selvittämisvelvollisuus)
- Start within 7 working days
- Notify of 1-year claim deadline

### §123 - BoardOpinionRequest (Lautakunnan lausuntopyyntö)
- For principled legal/medical questions
- Before compensation decision

### §138 - AdvancePayment (Ennakkomaksu)
- When right undisputed but decision pending
- Deducted from final compensation

## Severity: MEDIUM
Procedural completeness affects case workflow modeling.
```

### Issue #7: [MEDIUM] Complete Insurance Transfer Attributes
**Title:** `[ATTRIBUTES] Complete InsuranceTransfer entity per §162`

**Body:**
```
## Missing Attributes

### Transfer Timing
- transferQuarter: [march, september, june, december]
- noticeDeadlineDate: 3 months before quarter end
- isFirstPolicyPeriod: boolean (cannot transfer if true)

### Statistical History
- statisticalHistoryType: [offer_request, actual_transfer]
- payrollData: structured
- accidentEventData: structured  
- compensationData: structured

### Transfer Validity
- transferValidity: [first_valid, multiple_received]
- isValidTransfer: boolean

## Severity: MEDIUM
Required for complete insurance lifecycle modeling.
```

### Issue #8: [LOW] Add Risk Classification and Safety Prevention
**Title:** `[ENTITIES] Add RiskClassification and WorkSafetyPrevention per §166.5, §171`

**Body:**
```
## RiskClassification (§171)
- Maintained by: Tapaturmavakuutuskeskus
- Based on: Työtapaturma- ja ammattitautirekisteri (§235)
- Used for: Table-based premium calculation

### Attributes
- riskCategory
- industryCode  
- occupationalCategory
- accidentRate
- diseaseRate

## WorkSafetyPrevention (§166.5)
- Applies only to: Table-based employers (taulustomaksuperusteinen)
- Purpose: Documented preventive work considered in premium
- Not for: Experience-rated employers (erikoismaksuperusteinen)

### Attributes
- documentationDate
- safetyMeasures[]
- trainingPrograms[]
- riskAssessment
- incidentHistory

## Severity: LOW
These are supporting entities for premium calculation.
```

### Issue #9: [LOW] Fix Student Entity Enumerations
**Title:** `[ENUM] Correct student type enumerations per §70-77`

**Body:**
```
## Current Values
- higher_education
- vocational  
- basic_secondary

## Required Values per Law
1. **päätoiminen_opiskelija** (full-time student) - §70
   - Right to full incapacity compensation if studying prevented
   - Future earnings estimate per §76

2. **perusopetus** (basic education) - §77
   - Minimum 2x annual work income

3. **lukio** (upper secondary) - §77
   - Minimum 2x annual work income

4. **ammattiin_opiskeleva** (vocational student) - §76
   - Future earnings: 3 years experience in profession

## Additional Attributes
- expectedGraduationDate
- actualEarningsAtInjury
- isFullTime

## Severity: LOW
Affects specific student compensation calculations.
```

### Issue #10: [LOW] Add Distribution System Attributes
**Title:** `[ATTRIBUTES] Complete DistributionSystem entity per §231`

**Body:**
```
## Missing Attributes

### Timing
- distributionSystemYear (jakojärjestelmävuosi)
- ratioCoefficientDeadline: May 31
- preliminaryEstimateDeadline: May 31  
- finalSettlementDeadline: following May 31

### Financial
- ratioCoefficient (suhdeluku)
- companySharePercentage
- annualContribution
- systemBalance (saldo)
- adjustmentFactor
- preliminaryEstimate (ennakkoarvio)
- finalSettlement (lopullinen)

### Major Damage
- majorDamageThreshold: 75,000,000 EUR
- isMajorDamage: boolean
- majorDamageShare

### Interest
- interestStartDate: July 1 of distribution year
- interestRate: reference rate (Interest Act §12)

## Severity: LOW
Internal insurance company mechanism.
```

---

## 5. SUMMARY OF SEVERITY DISTRIBUTION

| Severity | Count | Categories |
|----------|-------|------------|
| CRITICAL | 1 | Institution hierarchy error (appeal vs advisory) |
| HIGH | 4 | Missing core entities, death benefits, person types |
| MEDIUM | 9 | Compensation types, enumerations, procedures |
| LOW | 6 | Supporting entities, secondary attributes |
| **TOTAL** | **20** | |

---

## 6. RECOMMENDATIONS FOR ONTOLOGY IMPROVEMENT

### Priority 1 (Immediate - Blocks DMN)
1. Fix ClaimAppealBoard hierarchy - this is critical for appeal process modeling
2. Add missing core person entities (WorkAtHomeWorker, YEL-Entrepreneur)
3. Complete death benefit hierarchy

### Priority 2 (High - Significant Impact)
4. Add all procedural notification entities
5. Complete DailyAllowance and DisabilityPension attributes
6. Fix DisabilityClass enumeration with payment types

### Priority 3 (Medium - Completeness)
7. Add all compensation sub-types
8. Complete InsuranceTransfer attributes
9. Add RiskClassification and WorkSafetyPrevention

### Priority 4 (Low - Enhancement)
10. Fix Student enumerations
11. Add DistributionSystem attributes
12. Add remaining minor entities

---

## APPENDIX A: COMPLETE ENTITY GAP LIST

### A.1 Entities Completely Missing
1. WorkAtHomeWorker (§25)
2. ThirdCountry (§2.8)
3. Post68Entrepreneur (§189)
4. AccommodationAccident (§24.8)
5. IntentionalAct (§34)
6. PostTrainingRehabilitationAllowance (§92)
7. AssistedLiving (§93)
8. InterpretationServices (§96)
9. FamilyAdaptationTraining (§97)
10. WidowPensionLumpSum (§106)
11. FullOrphan (§104.5)
12. PostMarriagePensionRight (§102)
13. EmployeeNotification (§110)
14. CompetenceDispute (§114)
15. CaseOpeningNotification (§115)
16. InvestigationObligation (§119)
17. BoardOpinionRequest (§123)
18. AdvancePayment (§138)
19. RetroactiveCompensation (§150)
20. ContinuousInsurance (§158)
21. FixedTermInsurance (§158)
22. BankruptcyEstate (§163)
23. JointGuaranteePayment (§230)

### A.2 Entities Requiring Structural Changes
1. ClaimAppealBoard → AdvisoryBoard + add AccidentAppealsBoard
2. Beneficiary → Expand hierarchy per §99-104
3. Student → Correct enumerations per §70-77
4. DailyAllowance → Add missing attributes
5. DisabilityPension → Add missing attributes
6. PermanentDamageCompensation → Add payment type logic
7. InsuranceTransfer → Complete attributes

---

*Report generated by structural compliance analysis of Finnish Work Accident Ontology against Työtapaturma- ja ammattitautilaki (459/2015)*
*Focus: Entities, attributes, relations, hierarchy, enumerations ONLY*
*Business rules/formulas excluded from this analysis*
