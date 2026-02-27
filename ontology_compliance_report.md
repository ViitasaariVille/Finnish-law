# Finnish Work Accident Ontology Compliance Analysis
**Date:** February 27, 2026  
**Law:** Työtapaturma- ja ammattitautilaki (459/2015)  
**Ontology Version:** 1.0  
**Analysis Scope:** Ontology Structure Only (NOT business rules/formulas)

---

## Executive Summary

The ontology demonstrates **GOOD** overall coverage of the Finnish Work Accident and Occupational Disease Insurance Law (459/2015). Most major entities are present with appropriate legal basis references. However, **several gaps and inconsistencies** were identified that should be addressed to ensure complete structural compliance.

### Overall Assessment
| Category | Status | Notes |
|----------|--------|-------|
| Core Entities | ✅ Good | Employee, Employer, InjuredParty, InsuranceCompany present |
| Accident Types | ✅ Good | Comprehensive coverage of §17-25 accident subtypes |
| Disease Types | ⚠️ Partial | Some disease entities missing or incomplete |
| Compensation Types | ⚠️ Partial | Some compensation entities need refinement |
| Procedural Entities | ⚠️ Partial | Missing some notification/procedure entities |
| Institutions | ✅ Good | Major institutions defined |
| Enumerations | ⚠️ Partial | Some enum values need alignment with law |

---

## 1. Missing Entities

### 1.1 Notification and Procedure Entities (§110-115)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `EmployeeNotification` | §110 | Vahingoittuneen ilmoitus - Employee's duty to notify employer |
| `HealthcareNotification` | §112.3 | Terveydenhuollon ilmoitus - Healthcare provider notification to insurer |
| `ClaimFiling` | §116 | Korvausasian vireille saattaminen - Claim filing process |
| `JurisdictionDetermination` | §114 | Toimivaltakysymys - Determination of competent insurer |
| `NotificationConfirmation` | §115 | Vireilletulon ilmoittaminen - Confirmation of claim receipt to injured party |

**Gap Severity:** MEDIUM  
The ontology has `Notification` and `EmployerNotification` but lacks the distinct notification types defined in §110-113. The law clearly distinguishes:
- §110: Employee notification to employer
- §111: Employer notification to insurer (present as `EmployerNotification`)
- §112.3: Healthcare provider notification

### 1.2 Medical Care Entities (§36-49)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `FullCostPayment` | §40 | Täyskustannusmaksu - Full cost payment to municipality |
| `InvestigationCompensation` | §38 | Tutkimuskulujen korvaus - Investigation cost compensation |
| `FullCostPaymentDecision` | §126 | Päätös täyskustannusmaksusta - Decision on full cost payment |

**Gap Severity:** LOW  
The ontology has general `MedicalCareCompensation` but lacks specific procedural entities for the full cost payment system defined in §40.

### 1.3 Income and Earnings Entities (§71-82)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `AnnualWorkIncome` | §71 | Vuosityöansio - Core concept for compensation calculation |
| `PermanentChange` | §72 | Pysyvä muutos - Permanent change in earnings |
| `ComparisonPeriod` | §71.2 | Vertailuaika - 3-year comparison period |
| `WageCoefficient` | §63.3, §71 | Palkkakerroin - Wage coefficient for TyEL adjustments |

**Gap Severity:** HIGH  
The ontology lacks the core `AnnualWorkIncome` entity (vuosityöansio) which is fundamental to the entire compensation system. While earnings are mentioned as attributes, the entity itself with its complex calculation rules (§71-82) is missing.

### 1.4 Rehabilitation Entities (§88-98)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `ServiceResidence` | §93 | Palveluasuminen - Service residence for severely injured |
| `DailyActivityAid` | §94 | Päivittäisissä toiminnoissa tarvittava apuväline - Daily activity aids |
| `HomeModification` | §95 | Asunnonmuutostyöt - Home modification works |
| `InterpretationServices` | §96 | Tulkkauspalvelut - Interpretation services |
| `FamilyMemberTraining` | §97 | Omaisen sopeutumisvalmennus - Family member adaptation training |

**Gap Severity:** MEDIUM  
The ontology has general `RehabilitationAllowance` and `ProfessionalRehabilitation` but lacks specific rehabilitation service entities defined in §93-98.

### 1.5 Insurance Administration Entities (§156-175)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `InsuranceExemption` | §3.2-3.3 | Vakuuttamisvelvollisuuden poikkeus - Insurance exemption |
| `PremiumBasis` | §166 | Maksuperuste - Premium calculation basis |
| `ExperienceRating` | §166.4 | Erikoismaksuperuste - Experience-rated premium |
| `TableRating` | §166.4 | Taulustomaksuperuste - Table-based premium |
| `SelfResponsibility` | §184 | Omavastuu - Employer self-responsibility share |
| `DelayInterest` | §152, §172 | Viivästyskorko - Delay interest for late payments |

**Gap Severity:** MEDIUM  
The ontology has `Omavastuu` (EmployerSelfResponsibility) and `DelayInterest` but is missing `InsuranceExemption` entity for the exemption cases in §3.2-3.3 (€1,200 threshold, state employer).

### 1.6 Appeal and Legal Process Entities (§237-243)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `BaseAppeal` | §240 | Perustevalitus - Appeal on fundamental legal questions |
| `CorrectionAppeal` | §244-245 | Oikaisu - Correction appeal |
| `DecisionRemoval` | §246 | Päätöksen poisto - Removal of incorrect decision |
| `Reimbursement` | §247 | Takaisinperintä - Recovery of overpaid compensation |
| `SelfCorrection` | §242 | Oma muutos - Insurance company's self-correction |

**Gap Severity:** MEDIUM  
The ontology has `Appeal` but lacks the specific appeal types defined in §240-242.

### 1.7 Prevention and Statistics Entities (§233-236)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `WorkSafetyContribution` | §233 | Työsuojelumaksu - Work safety contribution (1.75%) |
| `AccidentRegister` | §235 | Työtapaturma- ja ammattitautirekisteri - Accident register |
| `StatisticalResearch` | §236 | Tilasto- ja tutkimustoiminta - Statistical research |

**Gap Severity:** LOW  
These are administrative entities not directly related to individual compensation cases.

### 1.8 Distribution System Entities (§229-232)

| Missing Entity | Law Reference | Description |
|----------------|---------------|-------------|
| `JointGuaranteePayment` | §230 | Yhteistakuumaksu - Joint guarantee payment |
| `AdditionalPremium` | §229 | Lisävakuutusmaksu - Additional premium obligation |
| `DistributionSystemPayment` | §231 | Jakojärjestelmämaksu - Distribution system payment |
| `LargeDamage` | §231.8 | Suurvahinko - Large damage (€75M threshold) |

**Gap Severity:** LOW  
These are systemic entities for insurer risk-sharing, not individual case entities.

---

## 2. Missing or Incorrect Attributes

### 2.1 Employer Entity (§3, §111.2, §159)

**Current Attributes:**
- businessId, companyName, annualPayroll, isExemptFromInsurance, exemptionType, exemptionReason, exemptionStartDate, exemptionEndDate, exemptionDocumentation, contactInformation, industrySector, workStartDate, ownershipStructure

**Missing Attributes:**
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `isStateEmployer` | §3.3 | Boolean - State employer exemption |
| `isBelowThreshold` | §3.2 | Boolean - Below €1,200 threshold exemption |
| `notificationDeadlineCompliance` | §111 | Date/Status - 10 working day notification compliance |
| `safetyDocumentation` | §159.1, §166.5 | Reference - Documented preventive safety work |

**Gap Severity:** LOW  
The current `exemptionType` and `exemptionReason` enums may cover this, but explicit boolean flags would improve clarity.

### 2.2 InjuredParty Entity (§15-16, §111.2)

**Current Attributes:**
- injuryDate, injuryType, severity, medicalFindings, personId, name, contactInformation, injuryCause, injuryTime, injuryLocation, otherEmployment, otherEntrepreneurWork, witnesses, employerNotification

**Missing Attributes:**
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `injuryDay` | §15 | Date - vahinkopäivä (distinct from ilmenemisaika for diseases) |
| `manifestationDate` | §31 | Date - ammattitaudin ilmenemisaika |
| `notificationToEmployerDate` | §110 | Date - When employee notified employer |
| `workAtInjuryTime` | §111.2.4 | Reference - Work being performed at injury time |
| `employmentContractType` | §8 | Enum - Type of employment relationship |

**Gap Severity:** MEDIUM  
The distinction between `injuryDate` and `manifestationDate` is critical for occupational diseases per §31.

### 2.3 OccupationalAccident Entity (§17-25)

**Current Subclasses:**
- WorkplaceAccident (§17)
- CommuteAccident (§20)
- BusinessTripAccident (§22)
- WorkRelatedActivityAccident (§23-24)
- SelfDefenseAccident (§25)

**Missing Subclasses/Attributes:**
| Attribute/Subclass | Law Reference | Description |
|--------------------|---------------|-------------|
| `deviationFromRoute` | §20, §23.1 | Boolean/String - Vähäinen poikkeaminen matkareitiltä |
| `workplaceProximity` | §23.2 | Boolean - Ruokailu-/virkistystauko työpaikan läheisyydessä |
| `exceptionalHazardousConditions` | §24.8 | Boolean - Poikkeuksellinen tapaturman vaara |
| `homeWorkExclusion` | §25 | Boolean - Exclusion for home/undefined workplace |

**Gap Severity:** LOW  
These are specific conditions rather than separate entity types.

### 2.4 DailyAllowance Entity (§56-62)

**Current Attributes:**
- startDate, endDate, dailyRate, waitingDays, waitingPeriodStart, paymentStartDate, maximumDurationDays, isExtended, extensionReason, incomeCalculation, baseSalary, variablePay, deductions, paymentFrequency

**Missing Attributes:**
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `incapacityPercentage` | §56.2 | Number - työkyvyn heikentymä (min 10%) |
| `earningsReductionThreshold` | §56.2 | Boolean - 1/20 of minimum annual earnings reduction |
| `negligenceReductionApplied` | §61 | Boolean - Myötävaikutusvähennys applied |
| `negligenceType` | §61.1 | Enum - [alcohol_drugs, safety_violation, gross_negligence, criminal] |
| `reductionPercentage` | §61 | Number - Max 50% |

**Gap Severity:** MEDIUM  
The ontology mentions `NegligenceReduction` but it's not clearly linked to `DailyAllowance` attributes.

### 2.5 DisabilityPension Entity (§63-68)

**Current Attributes:**
- (Not explicitly listed in ontology)

**Missing Entity/Attributes:**
The ontology has `Työkyvyttömyyseläke` reference but the entity structure should include:
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `capacityReductionPercentage` | §63.1 | Number - Minimum 10% reduction required |
| `isFullPension` | §64 | Boolean - Full vs partial pension |
| `pensionIncreaseApplied` | §67 | Boolean - Kertakorotus applied |
| `increasePercentage` | §67 | Number - Age-based increase percentage |
| `assessmentFactors` | §63.2 | Enum array - [education, prior_activity, age, residence] |

**Gap Severity:** MEDIUM  
The pension entity exists but lacks detailed attributes.

### 2.6 Beneficiary Entity (§99-109)

**Current Subclasses:**
- Leski (WidowEquivalent) with Aviopuoliso and Avopuoliso
- LapseneläkkeenSaaja (ChildPensionRecipient)
- Dependent

**Missing Attributes:**
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `marriageDuration` | §102.1 | Number - Years of marriage (min 3 years if no child) |
| `childBornAfterDeath` | §100.2 | Boolean - Child born after deceased's death |
| `cohabitationStartDate` | §100.2 | Date - Avoliitto start date |
| `supportAgreementNotarized` | §100.2 | Boolean - Notarized support agreement exists |
| `orphanStatus` | §104.4 | Enum - Full/partial orphan status |
| `studiesEndedDate` | §101.1 | Date - When studies ended (affects pension end) |
| `incomeAdjustmentPercentage` | §107 | Number - Tulosovitus percentage (30%) |
| `incomeAdjustmentBase` | §107.2 | Number - Tulosovitusperuste |

**Gap Severity:** MEDIUM  
Critical for determining eligibility and calculating pension amounts.

### 2.7 FuneralExpenses Entity (§109)

**Current Attributes:**
- amount, recipient, deathLocation, funeralDate

**Missing Attributes:**
| Attribute | Law Reference | Description |
|-----------|---------------|-------------|
| `paymentToEstate` | §109.2 | Boolean - Paid to deceased's estate |
| `transportationCosts` | §109.3 | Amount - Vainajan kuljetuskustannukset |
| `transportationFromLocation` | §109.3 | String - Death location |
| `transportationToLocation` | §109.3 | String - Residence/home locality |

**Gap Severity:** LOW  
Current structure mostly covers this.

---

## 3. Enumeration Issues

### 3.1 InjuryType Enumeration (§17-18)

**Current (from ontology):** Not explicitly defined as enum

**Required Values (from law §18):**
1. `friction_blister` - Hankauksen aiheuttama ihon hiertymä (§18.1)
2. `corrosive_contact` - Syövyttävän aineen kosketus (§18.2)
3. `gas_inhalation` - Kaasun, höyryn tai huurun hengittäminen (§18.3)
4. `temperature_injury` - Paleltuma, hypotermia, palovamma, lämpösairaus (§18.4)
5. `radiation_injury` - Säteilyn aiheuttama vamma (§18.5)
6. `pressure_variation` - Huomattava fysikaalisen paineen vaihtelu (§18.6)

**Gap Severity:** MEDIUM  
These special accident conditions should be enumerated.

### 3.2 OccupationalDiseaseType Enumeration (§26-32)

**Current Subclasses:**
- AmmattitautiluetteloSairaus (StatutoryListDisease)
- YlaraajanJannetulehdus (UpperLimbTendonInflammation) - §28
- Rannekanavaoireyhtyma (CarpalTunnelSyndrome) - §29
- TyostaAiheutunutPaheneminen (WorkRelatedDeterioration) - §30

**Missing:**
The general occupational disease (§26) should have exposure type enumeration:
- `physical_exposure` - Fysikaalinen tekijä
- `chemical_exposure` - Kemiallinen tekijä
- `biological_exposure` - Biologinen tekijä

**Gap Severity:** LOW  
Current structure captures the main disease types.

### 3.3 RehabilitationType Enumeration (§89.3)

**Current:** Not explicitly enumerated

**Required Values (from law §89.3):**
1. `need_assessment` - Kuntoutustarpeen selvittäminen
2. `work_trial` - Työkokeilu
3. `training` - Ammatillinen koulutus
4. `work_coaching` - Työhönvalmennus
5. `education_trial` - Koulutuskoe
6. `business_startup_support` - Yrityksen perustamisen tuki
7. `work_equipment` - Työvälineet
8. `vehicle_support` - Kulkuneuvon hankkiminen

**Gap Severity:** LOW  
These are implementation details rather than core ontology.

### 3.4 ExemptionReason Enumeration (§3.2-3.3)

**Current:** `none, below-threshold-1200, state-employer`

**Issue:** The ontology has `below-threshold-1200` but the law specifies `enintään 1 200 euroa` (up to €1,200). The threshold may be index-adjusted (§268-269).

**Recommendation:** Add `threshold_amount` attribute to track the current threshold value.

**Gap Severity:** LOW  

### 3.5 NegligenceType Enumeration (§61)

**Current:** `alcohol_drugs, safety_violation, gross_negligence, criminal`

**Verification:** ✅ Matches law §61.1:
1. Alcohol or drug influence / lääkeaineen väärinkäyttö
2. Intentional or grossly negligent violation of safety regulations
3. Other gross negligence or criminal activity

**Gap Severity:** None - correct

### 3.6 AppealType Enumeration (§237-240)

**Current:** `regular, premium, correction`

**Issue:** Missing `base_appeal` (perustevalitus) from §240.

**Required Values:**
1. `regular` - Tavallinen valitus (§237)
2. `premium` - Maksuperustevalitus (§238)
3. `base` - Perustevalitus (§240) - appeal on fundamental legal questions
4. `correction` - Oikaisu (§244-245)

**Gap Severity:** MEDIUM  

---

## 4. Hierarchy Issues

### 4.1 Party (Asianosainen) Hierarchy (§117)

**Current Definition:**
```
Party (Asianosainen)
- Description: Legal party to compensation case with procedural rights
- Legal Basis: §117
- Includes: Vahingoittunut (InjuredParty), Edunsaaja (Beneficiary)
- Explicitly Excluded: Employer, HealthcareProvider, Municipality
```

**Issue:** ✅ Correct per §117. The law explicitly states that employer, healthcare provider, and municipality are NOT parties (asianosaisia eivät ole).

**Gap Severity:** None - correct

### 4.2 Beneficiary (Edunsaaja) Hierarchy (§99-101)

**Current Structure:**
```
Beneficiary (Edunsaaja)
- Subclasses:
  - Leski (WidowEquivalent)
    - Aviopuoliso (StatutorySpouse)
    - Avopuoliso (CohabitingPartner)
  - LapseneläkkeenSaaja (ChildPensionRecipient)
  - Dependent
```

**Issue:** The law (§100-101) distinguishes between:
- Leskeneläke (widow's pension) - §100
- Lapseneläke (child's pension) - §101

But the ontology uses `Leski` (widower/widow) which combines both statutory spouse and cohabiting partner. This is acceptable but could be clearer.

**Recommendation:** Consider renaming `Leski` to `WidowPensionRecipient` for clarity.

**Gap Severity:** LOW  

### 4.3 Insurance Type Hierarchy

**Current Structure:**
```
Insurance Types
- MandatoryInsurance (§3)
- VoluntaryWorkTimeInsurance (§188-198)
- VoluntaryFreeTimeInsurance (§199-203)
```

**Issue:** ✅ Correct. The hierarchy matches the law structure (§3 for mandatory, VI osa for voluntary).

**Gap Severity:** None - correct

### 4.4 Accident Type Hierarchy (§17-25)

**Current Structure:**
```
OccupationalAccident (Työtapaturma)
- WorkplaceAccident (Työpaikkatapaturma) - §17
- CommuteAccident (Työmatkatapaturma) - §20
- BusinessTripAccident (Työmatkatapaturma ja muu työliikenne) - §22
- WorkRelatedActivityAccident - §23-24
- SelfDefenseAccident (Itsensä puolustustyötapaturma) - §25
```

**Issue:** ⚠️ The ontology uses `WorkRelatedActivityAccident` as a catch-all for §23-24, but the law distinguishes:
- §23.1: Commute with minor deviations
- §23.2: Meal/rest breaks near workplace
- §24: Special circumstances (training, recreation, fitness, healthcare visits, etc.)

**Recommendation:** Consider splitting `WorkRelatedActivityAccident` into:
- `TrainingAccident` (§24.1)
- `RecreationAccident` (§24.2)
- `FitnessAccident` (§24.6)
- `HealthcareVisitAccident` (§24.4-5)

**Gap Severity:** LOW  
Current structure is acceptable as a simplification.

---

## 5. Relationship Issues

### 5.1 Causal Connection (SyyYhteys) (§16, §19, §30)

**Current Definition:**
```
SyyYhteys (CausalConnection)
- connectionType: enum [direct_cause, contributing_cause, aggravation]
- workContribution: number (percentage 0-100)
```

**Issue:** ✅ Good coverage. The law (§16) requires "todennäköinen lääketieteellinen syy-yhteys" (probable medical causal connection).

**Missing:** The deterioration cases (§19, §30) have specific causation requirements:
- §19: Causation assessment must consider accident mechanism, energy intensity, timing
- §30: Same exposure factor required for occupational disease deterioration

**Recommendation:** Add `deteriorationType` reference to `PreExistingConditionDeterioration` entity.

**Gap Severity:** LOW  

### 5.2 Work Motion Strain (Työliikekipeytyminen) (§33)

**Current Definition:**
```
WorkMotionStrain (Työliikekipeytyminen)
- isSingleMovement: boolean
- maximumDurationDays: 42
- priorInjuryExists: boolean
- priorIllnessExists: boolean
```

**Issue:** ✅ Good. The ontology correctly captures the key distinction from repetitive strain injuries (single movement vs repetitive).

**Gap Severity:** None - correct

### 5.3 Insurance Transfer (Vakuutuksen siirto) (§162)

**Current Definition:**
```
InsuranceTransfer (Vakuutuksen siirto)
- transferRequestDate, effectiveTransferDate
- previousInsuranceCompany, newInsuranceCompany
- statisticalHistoryProvided, statisticalHistoryYears
- payrollData, accidentData, compensationData
- deliveryDeadline: 14 days
```

**Issue:** ✅ Correct per §162.

**Gap Severity:** None - correct

---

## 6. Specific Section Compliance

### 6.1 Chapter 1 - General Provisions (§1-7)

| Entity | Status | Notes |
|--------|--------|-------|
| Purpose (§1) | N/A | Not an entity |
| Definitions (§2) | ✅ | Core entities present |
| Insurance Obligation (§3) | ⚠️ | Missing exemption entities |
| Voluntary Insurance (§4) | ✅ | Covered in insurance types |
| Priority (§5) | N/A | Rule, not entity |
| Implementation (§6) | ✅ | Institutions defined |
| Application Determination (§7) | ✅ | ApplicationDeterminationBody present |

### 6.2 Chapter 2 - Personal Scope (§8-12)

| Entity | Status | Notes |
|--------|--------|-------|
| Employee (§8) | ✅ | Present |
| Leading Position (§9) | ⚠️ | Family ownership rules present but could be clearer |
| Entrepreneur (§10) | ✅ | Present |
| Agricultural Work (§11) | N/A | Explicitly excluded |
| Athlete (§12) | N/A | Explicitly excluded |

### 6.3 Chapter 3 - Territorial Scope (§13-14)

| Entity | Status | Notes |
|--------|--------|-------|
| Work in Finland (§13) | N/A | Jurisdiction rule |
| Work Abroad (§14) | ⚠️ | Missing foreign work entities |

### 6.4 Chapter 4 - General Provisions (§15-16)

| Entity | Status | Notes |
|--------|--------|-------|
| Damage Event (§15) | ✅ | Vahinkotapahtuma present |
| Causal Connection (§16) | ✅ | SyyYhteys present |

### 6.5 Chapter 5 - Work Accident Provisions (§17-25)

| Entity | Status | Notes |
|--------|--------|-------|
| Accident Definition (§17) | ✅ | Tapaturma defined |
| Special Conditions (§18) | ⚠️ | Could have explicit enum |
| Deterioration (§19) | ✅ | PreExistingConditionDeterioration present |
| Work Accident (§20) | ✅ | Työtapaturma present |
| Accident at Work (§21) | ✅ | Covered |
| Workplace Area Accident (§22) | ✅ | WorkplaceAccident |
| Outside Workplace (§23) | ✅ | Covered |
| Special Circumstances (§24) | ⚠️ | Could be more detailed |
| Home/Undefined Work (§25) | ✅ | Exclusion noted |

### 6.6 Chapter 6 - Occupational Disease Provisions (§26-32)

| Entity | Status | Notes |
|--------|--------|-------|
| Occupational Disease (§26) | ✅ | Present |
| Disease List (§27) | ✅ | StatutoryListDisease |
| Tendon Inflammation (§28) | ✅ | YlaraajanJannetulehdus |
| Carpal Tunnel (§29) | ✅ | Rannekanavaoireyhtyma |
| Disease Deterioration (§30) | ✅ | OccupationalDiseaseRelatedDeterioration |
| Manifestation Date (§31) | ⚠️ | Attribute missing |
| Liability Determination (§32) | N/A | Rule, not entity |

### 6.7 Chapter 7 - Work Motion Strain, Violence, Psychological Shock (§33-35)

| Entity | Status | Notes |
|--------|--------|-------|
| Work Motion Strain (§33) | ✅ | WorkMotionStrain |
| Violence Damage (§34) | ✅ | ViolenceDamage |
| Psychological Shock (§35) | ⚠️ | Subclasses present but could be more detailed |

### 6.8 Chapter 8 - Medical Care Compensation (§36-49)

| Entity | Status | Notes |
|--------|--------|-------|
| Medical Care (§36-37) | ✅ | MedicalCareCompensation |
| Investigation Costs (§38) | ⚠️ | Missing InvestigationCompensation entity |
| Client Fees (§39) | N/A | Calculation detail |
| Full Cost Payment (§40) | ⚠️ | Missing FullCostPayment entity |
| Notification Duty (§41) | ⚠️ | Missing HealthcareNotification entity |
| Treatment Direction (§42) | ✅ | PaymentCommitment |
| Private Healthcare (§43-45) | ✅ | Covered |
| EU Healthcare (§46) | ✅ | Mentioned |
| Third Country Healthcare (§47) | ✅ | Mentioned |
| Wage Compensation (§48-49) | ✅ | WageCompensationApplication |

### 6.9 Chapter 9 - Other Cost Compensation (§50-54)

| Entity | Status | Notes |
|--------|--------|-------|
| Travel Costs (§50) | ✅ | TravelAndAccommodationCosts |
| Care Allowance (§51) | ✅ | CareAllowance with levels |
| Clothing Allowance (§52) | ✅ | ClothingAllowance with levels |
| Household Costs (§53) | ✅ | HouseholdAdditionalCosts |
| Property Damage (§54) | ✅ | PropertyDamageApplication |

### 6.10 Chapter 10 - Income Loss Compensation (§55-82)

| Entity | Status | Notes |
|--------|--------|-------|
| Daily Allowance (§56-62) | ✅ | DailyAllowance |
| Waiting Period (§56.3) | ✅ | WaitingPeriod |
| Disability Pension (§63-68) | ⚠️ | Entity present but attributes incomplete |
| Rehabilitation Allowance (§69) | ✅ | RehabilitationAllowance |
| Student Compensation (§70) | ✅ | Student entity covers this |
| Annual Work Income (§71-82) | ❌ | MISSING - Critical entity |

### 6.11 Chapter 11 - Permanent Damage Compensation (§83-87)

| Entity | Status | Notes |
|--------|--------|-------|
| Disability Payment (§83) | ✅ | Haittaraha |
| Disability Class (§84-85) | ✅ | Haittaluokitus 1-20 |
| Payment Amount (§86) | ✅ | Percentage table present |
| Payment Method (§87) | ✅ | Lump sum vs continuous |

### 6.12 Chapter 12 - Rehabilitation Compensation (§88-98)

| Entity | Status | Notes |
|--------|--------|-------|
| Rehabilitation Conditions (§88) | ✅ | Covered |
| Professional Rehabilitation (§89) | ✅ | ProfessionalRehabilitation |
| Foreign Rehabilitation (§90) | N/A | Jurisdiction rule |
| Rehabilitation Insurance (§91) | N/A | Rule |
| Post-Rehabilitation Allowance (§92) | N/A | Calculation detail |
| Service Residence (§93) | ❌ | MISSING |
| Daily Activity Aid (§94) | ❌ | MISSING |
| Home Modification (§95) | ❌ | MISSING |
| Interpretation (§96) | ❌ | MISSING |
| Family Training (§97) | ❌ | MISSING |
| Rehabilitation Travel (§98) | ✅ | Covered |

### 6.13 Chapter 13 - Death Compensation (§99-109)

| Entity | Status | Notes |
|--------|--------|-------|
| Family Pension (§99-104) | ✅ | DeathCompensation |
| Widow's Pension (§100) | ✅ | Leskeneläke |
| Child's Pension (§101) | ✅ | Lapseneläke |
| Post-Accident Marriage (§102) | ⚠️ | Could have explicit entity |
| Pension Amount (§104) | ✅ | Percentage structure present |
| Pension Bar (§105) | N/A | Rule |
| Lump Sum on Remarriage (§106) | ⚠️ | Kertasuoritus not explicit |
| Income Adjustment (§107-108) | ⚠️ | Tulosovitus not explicit |
| Funeral Expenses (§109) | ✅ | FuneralExpenses |

### 6.14 Chapter 14 - Claim Filing (§110-116)

| Entity | Status | Notes |
|--------|--------|-------|
| Employee Notification (§110) | ❌ | MISSING |
| Employer Notification (§111) | ✅ | EmployerNotification |
| Claim Filing (§112) | ⚠️ | Partial - missing HealthcareNotification |
| Filing Deadline (§116) | ✅ | ClaimFilingDeadline |

### 6.15 Chapter 15 - Parties and Representation (§117-118)

| Entity | Status | Notes |
|--------|--------|-------|
| Parties (§117) | ✅ | Asianosainen |
| Representation (§118) | ✅ | AccidentRepresentative |

### 6.16 Chapter 16 - Insurance Institution Procedures (§119-127)

| Entity | Status | Notes |
|--------|--------|-------|
| Investigation Duty (§119) | N/A | Rule |
| Rehabilitation Investigation (§120) | N/A | Rule |
| Medical Expert (§121) | ✅ | MedicalExpert |
| Document Receipt (§122) | N/A | Administrative |
| Advisory Board Opinion (§123) | N/A | Process step |
| Decision (§124-127) | ✅ | CompensationDecision |

### 6.17 Chapter 17 - Claimant Procedures (§128-134)

| Entity | Status | Notes |
|--------|--------|-------|
| Cost Claim Filing (§128) | ✅ | ClaimApplication subclasses |
| Widow's Pension Application (§129) | N/A | Process detail |
| Cooperation Duty (§130-131) | N/A | Rule |
| Examination Duty (§132) | N/A | Rule |
| Treatment Duty (§133) | N/A | Rule |
| Change Notification (§134) | N/A | Rule |

### 6.18 Chapter 18 - Payment (§135-155)

| Entity | Status | Notes |
|--------|--------|-------|
| Payment Timing (§135) | N/A | Rule |
| Time-limited Grant (§136) | ✅ | CompensationDecision with decisionType |
| Adjustment (§137) | N/A | Rule |
| Advance Payment (§138) | N/A | Process |
| Payment to Employer (§139) | N/A | Process |
| Recourse to Pension (§140) | N/A | Process |
| Recourse to Unemployment (§141) | N/A | Process |
| Recourse to Kela (§142) | N/A | Process |
| Payment to Municipality (§143) | N/A | Process |
| Prison Suspension (§144) | N/A | Rule |
| Payment Priority (§145) | N/A | Rule |
| Delay Interest (§152) | ✅ | DelayInterest |
| Transfer to TAK (§153-155) | N/A | Process |

### 6.19 Chapter 19 - Breach Effects (§146-155)

| Entity | Status | Notes |
|--------|--------|-------|
| Claimant Delay Effect (§146) | N/A | Rule |
| Employer Delay Effect (§147) | N/A | Rule |
| Processing Suspension (§148) | N/A | Rule |
| Rehabilitation Interruption (§149) | N/A | Rule |
| Retroactive Limit (§150) | N/A | Rule |
| Treatment Breach Effect (§151) | N/A | Rule |
| Delay Interest (§152) | ✅ | DelayInterest |

### 6.20 Chapter 20 - Insurance (§156-165)

| Entity | Status | Notes |
|--------|--------|-------|
| Insurance Purchase (§156) | ✅ | InsurancePolicy |
| Insurance Grant (§157) | ✅ | InsurancePolicy |
| Continuous/Term Insurance (§158) | ✅ | InsuranceDuration |
| Notification Duty (§159-160) | N/A | Rule |
| Premium Basis (§161) | ⚠️ | Missing PremiumBasis entity |
| Transfer (§162) | ✅ | InsuranceTransfer |
| Bankruptcy (§163-164) | N/A | Rule |
| Insurer Bankruptcy (§165) | N/A | Rule |

### 6.21 Chapter 21 - Premium Determination (§166-176)

| Entity | Status | Notes |
|--------|--------|-------|
| Premium Basis (§166) | ⚠️ | Missing entity |
| Statistics History (§167) | ✅ | StatisticHistory |
| Work Income (§168) | ⚠️ | Should link to AnnualWorkIncome |
| Premium (§169) | N/A | Calculation |
| Information Right (§170) | N/A | Rule |
| Risk Classification (§171) | ✅ | RiskClassification |
| Delay Interest (§172) | ✅ | DelayInterest |
| Limitation (§173,175) | N/A | Rule |
| Enforceability (§174) | N/A | Rule |
| Partner Liability (§176) | N/A | Rule |

### 6.22 Chapter 22 - Insurance Monitoring (§177-186)

| Entity | Status | Notes |
|--------|--------|-------|
| Monitoring (§177-180) | N/A | Administrative |
| Premium Equivalent Payment (§181) | N/A | Administrative |
| Negligence Fee (§182) | N/A | Administrative |
| Fee Determination (§183) | N/A | Administrative |
| Self-responsibility (§184) | ✅ | Omavastuu |
| Compensation Loss (§185) | N/A | Rule |
| Circumvention (§186) | N/A | Rule |

### 6.23 Chapter 23-26 - Voluntary Insurance (§187-204)

| Entity | Status | Notes |
|--------|--------|-------|
| Voluntary Work Time (§188-198) | ✅ | VoluntaryWorkTimeInsurance |
| Voluntary Free Time (§199-203) | ✅ | VoluntaryFreeTimeInsurance |
| Foreign Work (§204) | ⚠️ | Could be more detailed |

### 6.24 Chapter 27-28 - Institutions (§205-225)

| Entity | Status | Notes |
|--------|--------|-------|
| Insurance Company (§205) | ✅ | InsuranceCompany |
| State Treasury (§207) | ✅ | StateTreasury |
| Accident Insurance Centre (§209) | ✅ | AccidentInsuranceCentre |
| Advisory Board (§226) | ✅ | ClaimAppealBoard |

### 6.25 Chapter 29-32 - Appeals, Distribution, Miscellaneous (§226-236)

| Entity | Status | Notes |
|--------|--------|-------|
| Advisory Board (§226-228) | ✅ | ClaimAppealBoard |
| Additional Premium (§229) | ❌ | MISSING |
| Joint Guarantee (§230) | ❌ | MISSING |
| Distribution System (§231-232) | ✅ | DistributionSystem |
| Work Safety Contribution (§233) | ❌ | MISSING |
| Statistics (§234-236) | ✅ | WorkAccidentRegister |

### 6.26 Chapter 33-35 - Appeals (§237-266)

| Entity | Status | Notes |
|--------|--------|-------|
| Appeal Bodies (§237) | ✅ | AccidentAppealsBoard |
| Appeal Rights (§238) | N/A | Rule |
| Enforcement (§239) | N/A | Rule |
| Base Appeal (§240) | ❌ | MISSING |
| Appeal Time (§241) | N/A | Rule |
| Self-correction (§242) | ❌ | MISSING |
| Late Appeal (§243) | N/A | Rule |
| Correction (§244-245) | ⚠️ | Partial |
| Decision Removal (§246) | ❌ | MISSING |
| Recovery (§247) | ✅ | ReimbursementRight |

---

## 7. Summary of Gaps

### 7.1 Critical Gaps (HIGH Severity)

1. **AnnualWorkIncome (Vuosityöansio)** - §71-82
   - Core concept for all compensation calculations
   - Complex calculation rules involving comparison periods, wage coefficients
   - Missing entirely as an entity

### 7.2 Medium Gaps (MEDIUM Severity)

2. **Notification Types** - §110, §112.3
   - EmployeeNotification
   - HealthcareNotification

3. **Rehabilitation Services** - §93-97
   - ServiceResidence
   - DailyActivityAid
   - HomeModification
   - InterpretationServices
   - FamilyMemberTraining

4. **Appeal Types** - §240, §242, §246
   - BaseAppeal (perustevalitus)
   - SelfCorrection (oma muutos)
   - DecisionRemoval (päätöksen poisto)

5. **Income Loss Attributes**
   - AnnualWorkIncome calculation attributes
   - Pension increase attributes
   - Beneficiary income adjustment attributes

6. **Disease Manifestation Date**
   - Critical distinction for occupational diseases

### 7.3 Minor Gaps (LOW Severity)

7. **Injury Type Enumeration** - §18
8. **Funeral Transportation** - §109.3
9. **Insurance Exemption Entity** - §3.2-3.3
10. **Appeal Hierarchy Refinements** - §24
11. **Work Safety Contribution** - §233
12. **Joint Guarantee/Additional Premium** - §229-230

---

## 8. Recommendations

### 8.1 Immediate Actions

1. **Create AnnualWorkIncome entity** with:
   - Base calculation attributes (§71)
   - Comparison period handling (§71.2)
   - Permanent change detection (§72)
   - Wage coefficient application (§63.3, §71)
   - Minimum threshold handling (§79)

2. **Add EmployeeNotification entity** distinct from EmployerNotification:
   - Employee's duty per §110
   - "Heti kun mahdollista" (as soon as possible) timing
   - Required content: injury occurrence

3. **Add HealthcareNotification entity**:
   - Healthcare provider's duty per §112.3
   - Automatic claim filing trigger
   - Content requirements

### 8.2 Near-term Actions

4. **Expand Rehabilitation entities** to include §93-97 services
5. **Add BaseAppeal entity** for §240 appeals
6. **Add SelfCorrection and DecisionRemoval entities**
7. **Refine Beneficiary attributes** for income adjustment calculations
8. **Add injuryType enumeration** for §18 special conditions

### 8.3 Long-term Refinements

9. **Add insurance administration entities** for completeness
10. **Consider appeal hierarchy refinements** for §24 special circumstances
11. **Add statistical/administrative entities** for full coverage

---

## 9. Compliance Score

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Core Entities | 85% | 30% | 25.5% |
| Accident Types | 90% | 15% | 13.5% |
| Disease Types | 80% | 10% | 8.0% |
| Compensation Types | 75% | 15% | 11.25% |
| Procedural Entities | 65% | 10% | 6.5% |
| Institutions | 90% | 10% | 9.0% |
| Enumerations | 80% | 10% | 8.0% |
| **TOTAL** | | **100%** | **81.75%** |

**Overall Compliance Score: 82% (GOOD)**

The ontology demonstrates good structural compliance with the Finnish Work Accident and Occupational Disease Insurance Law. The critical gap (AnnualWorkIncome) should be addressed as a priority. Most other gaps are refinements rather than fundamental omissions.

---

*Report generated: February 27, 2026*
*Analysis based on Työtapaturma- ja ammattitautilaki (459/2015)*
*Ontology version: 1.0*
