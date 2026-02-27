# Finnish Work Accident and Occupational Disease Insurance Ontology

## Overview

| Property | Value |
|----------|-------|
| **Name** | Finnish Work Accident and Occupational Disease Insurance Ontology |
| **Version** | 1.0 |
| **Based On** | Työtapaturma- ja ammattitautilaki (459/2015) |
| **Language** | English |
| **Effective Date** | 2016-01-01 |
| **Source** | https://www.finlex.fi/fi/laki/alkup/2015/20150459 |

---

## 1. Person Entities

### Employee
- **Description**: Person working in employment relationship under employment contract, public service, or similar
- **Legal Basis**: Section 8

### Student (Opiskelija)
- **Description**: Person whose primary occupation is studying
- **Legal Basis**: §70, §76, §77
- **Attributes**: studentType, studyProgram, enrollmentDate, expectedGraduationDate, isFullTime, actualEarningsAtInjury
- **studentType values**: higher_education, vocational, basic_secondary
- **Related Compensation**: §70 (full incapacity if injury prevents studying), §76 (future earnings estimate), §77 (minimum 2x for pupils)

### Entrepreneur  
- **Description**: Self-employed person with YEL insurance
- **Legal Basis**: Sections 188-190

### InjuredParty
- **Description**: Person who suffered a work accident or occupational disease
- **Legal Basis**: §15-16, §111.2
- **Attributes**: 
  - injuryDate (tapaturmapäivä) - §111.2.1 REQUIRED
  - injuryType (vamman laatu) - §111.2.1 REQUIRED
  - severity (vakavuus)
  - medicalFindings (lääketieteelliset löydökset)
  - personId (henkilötunnus) - REQUIRED
  - name (nimi)
  - contactInformation (yhteystiedot) - §111.2.1
  - injuryCause (tapaturman syy) - §111.2.1
  - injuryTime (tapaturman ajankohta) - §111.2.1
  - injuryLocation (tapaturman paikka) - §111.2.1
  - otherEmployment (muu työsuhde) - §111.2.5
  - otherEntrepreneurWork (muu yrittäjätyö) - §111.2.5
  - witnesses (todistajat) - §111.2.3
  - employerNotification (työnantajan ilmoitus) - reference to EmployerNotification

### Beneficiary (Edunsaaja)
- **Description**: Person entitled to family pension (perhe-eläke) after death - legal term per §99-109
- **Legal Basis**: §99-109
- **Subclasses**: 
  - Leski (WidowEquivalent)
    - Aviopuoliso (StatutorySpouse)
    - Avopuoliso (CohabitingPartner) - conditions: §100.2 continuous cohabitation, marriage-like conditions, common child or notarized support agreement, deceased not married at death
  - LapseneläkkeenSaaja (ChildPensionRecipient)
  - Dependent

### Party (Asianosainen)
- **Description**: Legal party to compensation case with procedural rights
- **Legal Basis**: §117
- **Includes**: Vahingoittunut (InjuredParty), Edunsaaja (Beneficiary)
- **Explicitly Excluded**: Employer, HealthcareProvider, Municipality

### FamilyMember (Perheenjäsen)
- **Description**: Family member as defined for ownership calculation and benefit purposes
- **Legal Basis**: §9, §100
- **Attributes**: 
  - relationshipType: enum [spouse, cohabiting_partner, direct_ascendant, direct_descendant]
  - sharesHousehold: boolean
  - relationshipStartDate: date
  - isForOwnershipCalculation: boolean
  - isForBenefitPurposes: boolean
  - ownershipPercentage: number - percentage of company ownership (0-100)
  - maxOwnership30Percent: boolean - individual cannot exceed 30% ownership per §9.1
  - familyMaxOwnership50Percent: boolean - family total cannot exceed 50% ownership per §9.1
  - ownershipCalculationDate: date - date when ownership was calculated
- **Ownership Rules** (§9.1):
  - Individual family member: maximum 30%
  - Total family ownership: maximum 50%
- **Related Rules**: Max 30% individual ownership, max 50% family ownership (§9.1)

### ClaimFilingDeadline (Korvausasian vireille saattamisen määräaika)
- **Description**: Time limit for filing compensation claim
- **Legal Basis**: §116
- **Attributes**: standardDeadlineYears, standardDeadlineStarts, occupationalDiseaseDeadlineStarts, lateFilingPermitted, lateFilingConditions
- **standardDeadlineYears**: 5
- **standardDeadlineStarts**: accidentDate (työtapaturma) OR firstMedicalAssessmentDate (ammattitauti)
- **lateFilingConditions**: not_claimants_fault, unreasonable_to_deny (§116.2)

### VakuuttamatonTyo (UninsuredWork)
- **Description**: Work performed without mandatory insurance coverage
- **Attributes**: workType, exemptionReason, liabilityEntity
- **workType values**: non-mandatory, below-threshold, exempt
- **exemptionReason values**: €1200-threshold, state-employer, other
- **liabilityEntity**: Tapaturmavakuutuskeskus (when uninsured)
- **Legal Basis**: §2.4, §3, §209.2.1

### Employer
- **Description**: Entity with mandatory insurance obligation
- **Legal Basis**: §3, §111.2.2, §159
- **Attributes**: 
  - businessId, companyName, annualPayroll, isExemptFromInsurance, exemptionType, annualPayrollEUR
  - exemptionReason: enum [none, below_threshhold_1200, state_employer, other_statutory_exemption]
  - exemptionStartDate: date - when exemption became effective
  - exemptionEndDate: date - when exemption ends (null if ongoing)
  - exemptionDocumentation: reference to documentation supporting exemption
  - contactInformation (yhteystiedot) - REQUIRED in notification
  - industrySector (toimiala) - §159.1
  - workStartDate (työn alkamisaika) - §159.1
  - ownershipStructure (omistussuhteet) - §159.1
- **exemptionType values**: none, below-threshold-1200, state-employer
- **Legal Basis**: §3.2 (exemption when annual payroll <= €1,200), §3.3 (state employer exemption)

### Vakuutuksenottaja (PolicyHolder)
- **Description**: Entity that takes out insurance policy (can be different from Employer)
- **Attributes**: policyHolderId, policyHolderType, reportingObligations
- **policyHolderType values**: employer, entrepreneur, other
- **Legal Basis**: §156-160

### InsurancePeriod (Vakuutuskausi)
- **Description**: Period of insurance coverage
- **Attributes**: startDate, endDate, periodType, premiumBasis
- **periodType values**: annual, quarterly, monthly
- **premiumBasis values**: payroll-based, flat-rate, mixed
- **Legal Basis**: §156-160

### VakuutettuTyo (InsuredWork)
- **Description**: Work performed with mandatory insurance coverage
- **Attributes**: workType, coverageLevel, insurancePolicy
- **coverageLevel values**: full, partial
- **Legal Basis**: §3

### Edunsaaja (Beneficiary)
- **Description**: Person entitled to receive insurance benefits
- **Attributes**: beneficiaryType, relationshipToInsured, benefitEntitlement
- **beneficiaryType values**: primary, contingent, statutory
- **Legal Basis**: §99-109

### Asianosainen (Party)
- **Description**: Party to an insurance matter or dispute
- **Attributes**: partyType, role, legalStatus
- **partyType values**: claimant, respondent, third-party, intervener
- **Legal Basis**: §226-228

---

## 1.1. Representatives & Experts

### AccidentRepresentative (Tapaturma-asiamies)
- **Description**: Representative for accident victims
- **Attributes**: representativeType, authorization, scopeOfRepresentation
- **representativeType values**: legal-counsel, family-member, organizational
- **Legal Basis**: §119

### MedicalExpert (Lääkäriasiantuntija)
- **Description**: Medical expert providing professional opinions
- **Attributes**: expertType, specialization, certification
- **expertType values**: treating-physician, independent-examiner, occupational-health
- **Legal Basis**: §111

### Physician (Lääkäri)
- **Description**: Doctor providing medical treatment
- **Attributes**: licenseNumber, specialization, affiliation
- **Legal Basis**: §36-49

### HealthcareProvider (Terveydenhuollon palveluntarjoaja)
- **Description**: Healthcare service provider
- **Attributes**: providerType, authorization, region
- **providerType values**: public, private, occupational-health
- **Legal Basis**: §36-49, §252
- **Subclasses**:
  - PublicHealthcareUnit (Julkinen terveydenhuollon toimintayksikkö) - §252
  - PrivateHealthcareProvider (Yksityinen palveluntarjoaja)
  - RehabilitationProvider (Kuntoutuspalveluntarjoaja) - §89

## 2. Insurance Types

### MandatoryInsurance
- **Description**: Compulsory insurance that employers must obtain
- **Legal Basis**: Section 3

### VoluntaryWorkTimeInsurance
- **Description**: Voluntary insurance for entrepreneurs covering work hours
- **Legal Basis**: Sections 188-198
- **Eligibility**: Entrepreneur with YEL insurance

### VoluntaryFreeTimeInsurance
- **Description**: Voluntary insurance for leisure time accidents
- **Legal Basis**: Sections 199-203

### InsuranceDuration (Vakuutuksen kesto)
- **Description**: Duration of insurance coverage period
- **Attributes**: durationType, renewalTerms, terminationConditions
- **durationType values**: fixed-term, indefinite, continuous
- **Legal Basis**: §156-160

### PremiumBasis (Vakuutusmaksuperuste)
- **Description**: Basis for calculating insurance premium
- **Attributes**: calculationMethod, rateType, adjustmentFactors
- **calculationMethod values**: payroll-based, per-capita, risk-based
- **rateType values**: fixed-rate, percentage, hybrid
- **Legal Basis**: §161-168

### RiskClassification (Riskiluokitus)
- **Description**: Classification system for work accident and occupational disease risk maintained by Accident Insurance Centre
- **Legal Basis**: §171
- **Purpose**: Used for premium calculation for table-based employers (taulustomaksuperusteinen vakuutuksenottaja)
- **Based On**: Information from the Work Accident and Occupational Disease Register (§235) regarding industry or work performed
- **Maintained By**: Tapaturmavakuutuskeskus (Accident Insurance Centre)
- **Data Requirement**: Insurance companies must organize their statistics to provide required data to Accident Insurance Centre (§257.1-3)
- **Attributes**: riskCategory, industryCode, occupationalCategory, accidentRate, diseaseRate

### WorkAccidentRegister (Työtapaturmarekisteri)
- **Description**: National register of work accidents and occupational diseases maintained by Tapaturmavakuutuskeskus
- **Legal Basis**: §235
- **Purpose**: Collects data on work accidents and occupational diseases for statistics, risk classification, and prevention
- **Attributes**:
  - registerId, collectionStartDate, dataProvider
  - accidentData: annual accident count, injury type, severity, industryCode
  - occupationalDiseaseData: disease code, exposure type, latency period
  - statisticsPublished: boolean - annual statistics publication per §235.2
- **Data Sources**: Insurance companies, employers (§111), healthcare providers
- **Related Entities**:
  - RiskClassification: Uses register data for premium calculation
  - Tapaturmavakuutuskeskus: Register administrator

### WorkSafetyPrevention (Työturvallisuustyö)
- **Description**: Employer's documented preventive occupational safety work considered in premium calculation
- **Legal Basis**: §166.5
- **Application**: Only applies to table-based employers (taulustomaksuperusteinen vakuutuksenottaja)
- **Purpose**: Employer documented preventive safety work is taken into account when determining insurance premium
- **Note**: For experience-rated employers (erikoismaksuperusteinen), claims and full cost charges are already considered in premium
- **Attributes**: documentationDate, safetyMeasures, trainingPrograms, riskAssessment, incidentHistory

### Omavastuu (EmployerSelfResponsibility)
- **Description**: Employer's own responsibility share of insurance premiums per §184
- **Legal Basis**: §184
- **Purpose**: Employers participate in bearing the costs of work accidents and occupational diseases through a mandatory self-responsibility component
- **Attributes**:
  - selfResponsibilityType: enum [fixed_amount, percentage_based, combined]
  - baseAmount: fixed base per §184.1 (€1,250 minimum)
  - percentageRate: percentage of premium (§184.1)
  - calculationYear: year for which self-responsibility is calculated
  - employerCategory: enum [table_based, experience_rated, new_employer]
  - reductionApplied: boolean - reductions may apply for good safety record
  - documentation: reference to required documentation
- **Application** (§184.1): 
  - Mandatory component in premium calculation
  - Minimum €1,250 or percentage of premium, whichever is higher
  - Purpose: Incentivize workplace safety
- **Note**: Different rules apply to table-based (taulustomaksuperusteinen) vs experience-rated (erikoismaksuperusteinen) employers

### InsuranceTransfer (Vakuutuksen siirto)
- **Description**: Transfer of insurance policy from one insurance company to another
- **Legal Basis**: §162
- **Attributes**:
  - **transferRequestDate**: Date of transfer request
  - **effectiveTransferDate**: Date when transfer takes effect
  - **previousInsuranceCompany**: Company being transferred from
  - **newInsuranceCompany**: Company being transferred to
  - **policyNumber**: Insurance policy being transferred
  - **transferReason**: Reason for transfer
  - **statisticalHistoryProvided**: Boolean - whether §167 statistics provided
  - **statisticalHistoryYears**: Number of years of history (typically 5 years per §167)
  - **payrollData**: Payroll information for transferred policy
  - **accidentData**: Historical accident data
  - **compensationData**: Historical compensation data
  - **deliveryDeadline**: 14 days from final transfer date per §162
  - **transferType**: Type of transfer (full_portfolio, partial, merger_division)
- **Requirements**: 
  - Statistical history must be provided within 14 days (§162.1)
  - Must include complete payroll and compensation data for 5 years (§167)

---

## 2.1. Procedural Documentation

### ClaimApplication (Korvaushakemus)
- **Description**: Application for compensation
- **Attributes**: submissionDate, completeness, attachments
- **Legal Basis**: §128
- **Subclasses**:
  - WageCompensationApplication - §48-49
  - TravelCostApplication - §50
  - CareCostApplication - §53
  - PropertyDamageApplication - §54
- **Enumeration Values per Claim Type**:
  - **TravelCostApplication** (§50):
    - **transportMethod**: enum [public_transport, private_car, special_vehicle]
    - **accommodationRequired**: boolean
    - **companionUsed**: boolean
    - **rateCalculation**: enum [actual_cost, tax_free_km_allowance_50_percent]
  - **CareCostApplication** (§51):
    - **careLevel**: enum [perus (8.70€), korotettu (19.55€), ylin (23.41€)]
  - **ClothingAllowanceApplication** (§52):
    - **allowanceLevel**: enum [basic (0.58€), elevated (2.31€)]
    - **minimumDurationMet**: boolean - requires 3 months continuous
  - **HouseholdCostsApplication** (§53):
    - **householdTasks**: enum array [cleaning, laundry, shopping, childcare]
    - **maxDurationDays**: 365 (1 year from accident)
  - **PropertyDamageApplication** (§54):
    - **itemTypes**: enum array [glasses, hearing_aid, dental_prosthesis, support, prosthetic, clothing, ring, artificial_limb, artificial_joint, artificial_organ, support_binder, support_vest, corset]

### Notification (Ilmoitus)
- **Description**: Formal notification of accident
- **Legal Basis**: §110-113
- **Attributes**: notificationDate, notificationType, deadlineStatus
- **Subclasses**:
  - EmployeeNotification (§110) - to employer
  - EmployerNotification (§111) - to insurer, 10 working days deadline
  - HealthcareNotification (§112.3) - healthcare provider's notification to insurer

### HealthcareNotification (Terveydenhuollon ilmoitus)
- **Description**: Healthcare provider's notification to insurance company per §112.3 - triggers claim filing automatically
- **Legal Basis**: §112.3, §41
- **Attributes**:
  - notificationDate: date - when healthcare notified insurer
  - treatmentStartDate: date - when treatment began
  - injuryType: enum [physical_injury, occupational_disease, psychological_injury]
  - employerName: string - employer name for claim filing purposes
  - injuredPartyName: string - name of injured party
  - injuryDescription: string - brief description of injury/disease
- **Relationships**:
  - injuredParty: InjuredParty
  - insuranceCompany: InsuranceCompany
  - employer: Employer
  - healthcareProvider: HealthcareProvider
- **Triggers**: Automatic claim filing per §112.3 - must include injured party identification and employer information

### AnnualWorkIncome (Vuosityöansio)
- **Description**: Annual work income basis for compensation calculation - fundamental to entire compensation system
- **Legal Basis**: §71-82
- **Attributes**:
  - baseAmount: monetary amount - §71.1 previous year earnings
  - comparisonPeriodAmount: monetary amount - §71.2 3-year average
  - comparisonPeriodUsed: boolean - whether 3-year average was applied
  - deviationPercentage: number - >20% triggers comparison period per §71.2
  - permanentChangeApplied: boolean - §72 permanent earnings change
  - wageCoefficient: number - §63.3, §71 TyEL wage coefficient (palkkakerroin)
  - minimumThresholdApplied: boolean - §79 €13,680 minimum threshold
  - excludedIncomeTypes: enum array - §81-82 excluded income types
  - calculationMethod: enum [standard, comparison_period, permanent_change, student_estimate, pupil_minimum, young_person]
  - incomeType: enum [employee, entrepreneur, student, pupil, young_worker]
- **Calculation Methods** (§71-78):
  - standard (§71.1): Previous year earnings as base
  - comparison_period (§71.2): 3-year average when deviation >20%
  - permanent_change (§72): Adjustment for permanent earnings change
  - student_estimate (§76): Estimated future earnings for students
  - pupil_minimum (§77): 2x minimum annual earnings for school pupils
  - young_person (§78): Special rules for young workers
- **Related Entities**:
  - DailyAllowance (§56-62) - uses AnnualWorkIncome for rate calculation
  - DisabilityPension (§63-68) - uses AnnualWorkIncome for pension calculation
  - FamilyPension (§99-109) - uses deceased's AnnualWorkIncome
  - PermanentDamageCompensation (§83-87) - may reference AnnualWorkIncome

### CompensationDecision (Korvauspäätös)
- **Description**: Written decision on compensation
- **Legal Basis**: §124-127
- **Attributes**: decisionDate, decisionType, amount, reasoning, appealInstructions
- **decisionType values**: grant, deny, partial
- **Deadline**: 30 days from sufficient documentation (§127)

### PaymentCommitment (Maksusitoumus)
- **Description**: Insurance company commitment to pay for treatment
- **Legal Basis**: §42, §45
- **Purpose**: Directs injured to specific healthcare provider

### MedicalCertificate (Lääketieteellinen todistus)
- **Description**: Medical certificate documenting injury or disease
- **Attributes**: certificateType, issuingPhysician, expirationDate
- **certificateType values**: initial, follow-up, final
- **Legal Basis**: §111

### AccidentReport (Tapaturmailmoitus)
- **Description**: Report of work accident or occupational disease
- **Attributes**: reportDate, reporter, incidentDetails
- **Legal Basis**: §107

### InsurancePolicy (Vakuutussopimus)
- **Description**: Insurance policy document
- **Attributes**: policyNumber, coverageTerms, exclusions
- **Legal Basis**: §156-160

### Decision (Päätös)
- **Description**: Compensation decision document
- **Attributes**: decisionDate, decisionMaker, appealInstructions
- **Legal Basis**: §112-116

---

## 3. Insurable Events

### OccupationalAccident (Työtapaturma)
- **Legal Basis**: Sections 17-25
- **Description**: Work accident defined as injury suffered in circumstances covered by the law
- **Subclasses** (per §17-§25):
  - **WorkplaceAccident (Työpaikkatapaturma)** - §17, injury at workplace during work
  - **CommuteAccident (Työmatkatapaturma)** - §20, injury on journey to/from work
  - **BusinessTripAccident (Työmatkatapaturma ja muu työliikenne)** - §22, injury during work-related travel
  - **WorkRelatedActivityAccident** - §23-§24, sports/rehabilitation activities
  - **SelfDefenseAccident (Itsensä puolustustyötapaturma)** - §25, self-defense and rescue operations
- **Attributes**:
  - accidentDate (tapaturmapäivä)
  - accidentLocation (tapaturmapaikka)
  - circumstances (olosuhteet)
  - causationAssessment (syy-yhteys)

### SpecialAccidentConditions (§18)
- **Description**: Additional injuries and illnesses considered as caused by accident under special conditions
- **Legal Basis**: §18
- **Conditions**: Exposure to causative factor must occur within max 1 day before injury/illness appears; not occupational disease
- **Types**:
  - FrictionBlister (Hankauksen aiheuttama ihon hiertymä) - §18.1
  - CorrosiveInjury (Syövyttävän aineen kosketus) - §18.2
  - GasVaporInhalation (Kaasun, höyryn tai huurun hengittäminen) - §18.3
  - TemperatureInjury (Paleltuma, hypotermia, palovamma, lämpösairaus) - §18.4
    - **Condition**: Caused by abnormal thermal environment
  - RadiationInjury (Säteilyn aiheuttama vamma tai sairaus) - §18.5
  - PressureVariationInjury (Huomattava fysikaalisen paineen vaihtelu) - §18.6

### OccupationalDisease
- **Legal Basis**: Sections 26-32
- **Attributes**: diseaseCode, exposureDuration, latencyPeriod
- **Subclasses**:
  - AmmattitautiluetteloSairaus (StatutoryListDisease) - diseases on official occupational disease list
  - YlaraajanJannetulehdus (UpperLimbTendonInflammation) - §28, condition: repetitive, unusual upper limb movements
  - Rannekanavaoireyhtyma (CarpalTunnelSyndrome) - §29, condition: repetitive, forceful, wrist-bending movements
  - TyostaAiheutunutPaheneminen (WorkRelatedDeterioration) - §30, essential worsening of pre-existing condition

### PreExistingConditionDeterioration (Olemassa olevan tilan paheneminen)
- **Description**: Significant worsening of pre-existing injury or illness due to work accident or occupational disease
- **Legal Basis**: §19 (accident-related), §30 (occupational disease-related)
- **Subclasses**:
  - AccidentRelatedDeterioration (Tapaturman aiheuttama paheneminen) - §19
    - **Description**: Essential worsening of non-work-related injury/illness caused by work accident
    - **Conditions**: Accident causation mechanism, energy intensity, timing relationship, pre-existing condition contribution
    - **Maximum Duration**: 6 months from accident (may be extended if recovery delayed by treatment choices/waiting)
    - **Causation Threshold**: Not paid if accident had only minor causal contribution
  - OccupationalDiseaseRelatedDeterioration (Ammattitaudista aiheutunut paheneminen) - §30
    - **Description**: Essential worsening of pre-existing condition primarily caused by occupational exposure to physical, chemical, or biological factors
    - **Conditions**: Same exposure factor as the pre-existing condition; compensated for duration of essential worsening
    - **Causation**: Must be probable that exposure was the primary cause
- **Attributes**: causationAssessment, preExistingCondition, worseningDegree, duration, causalContribution

### WorkMotionStrain (Työliikekipeytyminen)
- **Legal Basis**: Section 33
- **Description**: Acute muscle/tendon strain from single strenuous work movement (NOT repetitive)
- **Note**: Maximum 6 weeks (42 days) compensation per §33
- **Attributes**: 
  - strainLocation, workActivityDuringStrain, onsetDate
  - **isSingleMovement**: boolean - distinguishes from repetitive strain (REQUIRED)
  - **maximumDurationDays**: 42 - 6 weeks per §33
  - **priorInjuryExists**: boolean - checks for prior injury (aikaisempi vamma)
  - **priorIllnessExists**: boolean - checks for prior illness (sairaus)
  - **exclusionApplies**: boolean - whether exclusion condition applies
  - **exclusionReason**: enum - [prior_injury, prior_illness, tissue_damage_only_from_accident]
  - **isCompensable**: boolean - derived attribute based on all conditions
- **Compensability Criteria** (§33):
  - Must be single movement (NOT repetitive)
  - Must occur during work (§21) or approved fitness activity (§24.1.6)
  - NOT compensable if due to prior injury, prior illness, or tissue damage that could ONLY occur from accident

### ViolenceDamage
- **Legal Basis**: Section 34
- **Condition**: Must be related to work duties

### PsychologicalShock
- **Legal Basis**: Section 35
- **Subclasses**: AcuteStressReaction, PTSD, PersonalityChange

---

## 4. Compensation Types

### MedicalCareCompensation
- **Legal Basis**: Sections 36-49
- **Subclasses**: PublicHealthcare, PrivateHealthcare, ForeignHealthcare, Medicine

### TravelAndAccommodationCosts
- **Legal Basis**: Section 50
- **Description**: Transportation costs for treatment and accommodation costs when treatment requires overnight stay away from home
- **Subclasses**: TransportationCosts, AccommodationCosts

### CareAllowance (Hoitotuki)
- **Legal Basis**: Section 51
- **Description**: Compensation provided when injured party requires care assistance
- **Levels**:
  - Perus (Basic): 8,70€/day
  - Korotettu (Elevated): 19,55€/day
  - Ylin (Highest): 23,41€/day

### ClothingAllowance (Vaatelisä)
- **Legal Basis**: Section 52
- **Description**: Compensation for clothing damage due to treatment/prosthetics
- **Levels**:
  - Basic: 0,58€/day
  - Elevated: 2,31€/day

### HouseholdAdditionalCosts (Kodinhoidon lisäkustannukset)
- **Legal Basis**: Section 53
- **Description**: Covers additional costs for household management due to injury
- **Maximum Duration**: 1 year from accident date

### WaitingPeriod (Odotusaika)
- **Description**: Waiting period before daily allowance becomes payable
- **Legal Basis**: §56.3
- **Attributes**:
  - **waitingDays**: integer - fixed at 3 per §56.3
  - **waitingPeriodStart**: date - when the waiting period begins (accident date or first day of incapacity)
  - **paymentStartDate**: date - date when payments begin after waiting period is satisfied
  - **isSatisfied**: boolean - whether the waiting period has been completed
  - **consecutiveDaysRequired**: integer - must be 3 consecutive days of incapacity
- **Note**: Daily allowance is not paid for first 3 consecutive days of incapacity (excluding accident day)

### Työkyvyttömyys (Incapacity)
- **Legal Basis**: §56
- **Description**: Work incapacity - core concept for daily allowance eligibility. Incapacity means inability to work due to injury or disease.
- **Attributes**:
  - **incapacityType** (työkyvyttömyyden laatu): enum [full, partial]
    - full: unable to perform any work
    - partial: able to perform some work but with reduced capacity
  - **startDate** (alkamisajankohta): date - when incapacity began
  - **endDate** (päättymisajankohta): date - when incapacity ended (null if ongoing)
  - **durationDays**: number - total days of incapacity
  - **medicalCertificate** (lääketieteellinen todistus): reference to MedicalCertificate
  - **assessmentBasis** (arviointiperuste): enum [initial, follow_up, final]
  - **cause** (syy): enum [occupational_accident, occupational_disease, commuting_accident]
  - **isWorkRelated** (työperäinen): boolean - whether related to work
  - **relatedInjury** (liittyvä vamma): reference to Vahinko
- **Related Entities**:
  - **DailyAllowance**: Työkyvyttömyys is the basis for daily allowance compensation (§56-62)
  - **WaitingPeriod**: 3-day waiting period before daily allowance starts (§56.3)
  - **WorkCapacityReduction**: Used to determine degree of incapacity

### DailyAllowance
- **Legal Basis**: Sections 56-62
- **Maximum Duration**: 1 year from accident date
- **Attributes**:
  - **startDate**: First day of incapacity
  - **endDate**: Last day of incapacity or 1 year max
  - **dailyRate**: Daily compensation amount (§57-59)
  - **waitingDays**: 3 consecutive days (§56.3)
  - **waitingPeriodStart**: Date waiting period begins
  - **paymentStartDate**: Date payments begin after waiting period
  - **maximumDurationDays**: 365 days from accident date
  - **isExtended**: Boolean - whether extended beyond 1 year per §60
  - **extensionReason**: Reason for extension if applicable
  - **incomeCalculation**: Method for calculating daily rate (§57-59)
  - **baseSalary**: Injured party's regular earnings
  - **variablePay**: Overtime, bonuses included in calculation
  - **deductions**: Tax and other deductions
  - **paymentFrequency**: How often paid (monthly, bi-weekly)
- **WaitingPeriod (Odotusaika)**: 3 consecutive days (§56.3)
  - **Description**: Daily allowance is not paid for the first 3 consecutive days of incapacity (excluding the accident day)
  - **Legal Basis**: §56.3
  - **Waiting Days**: 3
  - **Application**: Applies from accident day onwards; compensation starts from day 4 of incapacity
- **NegligenceReduction (Myötävaikutus vähennys)**: §61

### WaitingPeriod (Odotusaika)
- **Legal Basis**: §56.3
- **Description**: Mandatory waiting period before daily allowance payments begin. Daily allowance is not paid for the first 3 consecutive days of incapacity (excluding the accident day).
- **Attributes**:
  - **waitingDays**: number - fixed at 3 per §56.3
  - **waitingPeriodStart**: date - when waiting period begins (accident day)
  - **paymentStartDate**: date - day 4, when payments begin
  - **isSatisfied**: boolean - whether 3 consecutive days of incapacity occurred
  - **consecutiveDaysRequired**: number - always 3 per law
  - **excludesAccidentDay**: boolean - waiting period starts from day after accident
- **Related Entities**:
  - DailyAllowance: hasWaitingPeriod relationship
  - Injury: affects workCapacityDuringWaitingPeriod
  - **negligenceType values**: alcohol_drugs, safety_violation, gross_negligence, criminal
  - **reductionPercentage**: max 50% per §61
  - **isReductionApplied**: boolean
- **Relation to MedicalCertificate**: Requires medical certification of incapacity

### DisabilityPension
- **Legal Basis**: Sections 63-68
- **Requirement**: Minimum 10% work capacity reduction

### Kertakorotus (PensionIncrease)
- **Description**: One-time increase to disability pension per §67
- **Legal Basis**: §67
- **Attributes**:
  - increasePercentage: 20% (twenty percent increase per §67.1)
  - baseAmount: reference to base disability pension
  - effectiveDate: date when increase begins
  - reason: enum [age_60, age_65, vocational_rehabilitation_failure]
  - applicationDate: date of application
- **Conditions** (§67.1): 
  - Recipient has reached age 60, OR
  - Recipient has reached age 65 with no vocational rehabilitation opportunity
- **Note**: Applies to full disability pension, not partial

### RehabilitationAllowance
- **Legal Basis**: Sections 69, 88-98

### ServiceResidence (Palveluasuminen)
- **Description**: Service residence compensation for severely injured persons under §93
- **Legal Basis**: §93
- **Attributes**:
  - **dailyAllowance**: number - Fixed at €46.82 per day per §93
  - **eligibility**: enum [vaikeasti_vahingoittunut] - Severely injured only
  - **startDate**: date
  - **endDate**: date
  - **serviceProvider**: string - Provider of service residence
- **Note**: Only for "vaikeasti vahingoittunut" (severely injured) per §93

### DailyActivityAid (Päivittäisissä toiminnoissa tarvittava apuväline)
- **Description**: Aids for daily activities for severely injured persons under §94 (non-medical aids)
- **Legal Basis**: §94
- **Attributes**:
  - **aidType**: enum [mobility, hearing, vision, speech, daily_living, other]
  - **costAmount**: number - Actual cost (reimbursed if reasonable and necessary)
  - **necessity**: boolean - Required for daily activities
  - **exclusionReference**: reference - Not applicable if covered under §37.3 (medical rehabilitation aids)
- **Note**: Different from §37.3 medical rehabilitation aids

### HomeModification (Asunnonmuutostyöt)
- **Description**: Home modification works and equipment for severely injured persons under §95
- **Legal Basis**: §95
- **Attributes**:
  - **modificationType**: enum [structural, bathroom, kitchen, accessibility, safety, other]
  - **costAmount**: number - Actual cost (reimbursed if reasonable and necessary)
  - **frequencyLimit**: string - "Max once per 5 years" per §95
  - **outPatientCarePossible**: boolean - Not applicable if outpatient care not possible
  - **permanentResidence**: boolean - Must be permanent residence
- **Note**: §95 states compensation is for permanent residence modifications, max once per 5 years

### InterpretationServices (Tulkkauspalvelut)
- **Description**: Interpretation services for persons with severe sensory disabilities under §96
- **Legal Basis**: §96
- **Attributes**:
  - **serviceType**: enum [visual_impairment, hearing_impairment, speech_impairment]
  - **maxAmount**: number - Capped at Kela's interpretation service rate
  - **eligibility**: enum [vaikea_nakovamma, vaikea_kuulovamma, vaikea_puhevamma]
  - **necessity**: boolean - Required due to injury-related disability
- **Note**: For severe vision, hearing, or speech disabilities caused by the injury

### FamilyMemberAdaptationTraining (Omaisen sopeutumisvalmennus)
- **Description**: Family member participation in adaptation training under §97
- **Legal Basis**: §97
- **Attributes**:
  - **familyMember**: FamilyMember - Family member who participated
  - **trainingType**: string - Type of adaptation training
  - **travelCosts**: TravelCost[] - Reimbursable travel costs per §97
  - **accommodationCosts**: AccommodationCost[] - Reimbursable accommodation per §97
  - **incomeLoss**: number - Compensation for lost earnings per §97
- **Note**: Covers family member or person actually caring for injured party

### PermanentDamageCompensation
- **Legal Basis**: Sections 83-87
- **Classes**: 1-20 based on severity
- **Base Amount**: €12,440
- **Haittaluokka (DisabilityClass) Enumeration** (per §86):
  - Class 1: 1.15%
  - Class 2: 2.27%
  - Class 3: 3.36%
  - Class 4: 4.42%
  - Class 5: 5.45%
  - Class 6: 6.45%
  - Class 7: 7.42%
  - Class 8: 8.36%
  - Class 9: 9.27%
  - Class 10: 10.15%
  - Class 11: 13%
  - Class 12: 16%
  - Class 13: 19%
  - Class 14: 22%
  - Class 15: 25%
  - Class 16: 32%
  - Class 17: 39%
  - Class 18: 46%
  - Class 19: 53%
  - Class 20: 60%

### DisabilityClassification (Haittaluokitus)
- **Description**: System for classifying permanent damage/disability
- **Attributes**: classificationDate, evaluator, classificationLevel
- **classificationLevels**: 1-20 (Haittaluokka)
- **Legal Basis**: §83-87

### WorkCapacity (Työkyky)
- **Description**: Work capacity assessment
- **Attributes**: assessmentDate, capacityPercentage, assessmentBasis
- **capacityLevels**: full, partial, none
- **Legal Basis**: §63-68, §88-98

### WorkCapacityReduction (Työkyvyn heikentymä)
- **Description**: Reduction in work capacity as defined in §63 - core concept for disability pension eligibility
- **Legal Basis**: §63-68
- **Attributes**:
  - **reductionPercentage**: number - minimum 10% required per §63.1
  - **earningCapacityBefore**: MonetaryAmount - pre-injury earning capacity (adjusted with wage coefficient per TyEL §96)
  - **earningCapacityAfter**: MonetaryAmount - post-injury earning capacity
  - **causationVerified**: boolean - must establish connection between injury and reduced work capacity
  - **assessmentFactors**: enum array [education, prior_activity, age, residence] - factors to consider per §63.2
  - **wageCoefficientApplied**: number - wage coefficient (palkkakerroin) per TyEL §96
  - **minimumThresholdMet**: boolean - at least 10% reduction AND at least 1/20 of minimum annual work income reduction per §63.1
- **Related**: DisabilityPension (§63-68)

### Takautumisoikeus (RecourseRight)
- **Description**: Right of recourse - insurer's right to claim compensation from liable third party
- **Attributes**: 
  - recourseType: enum [subrogation, contribution, indemnification]
  - liableParty: reference to DamageCauser
  - claimAmount: monetary amount
  - exclusionApplies: boolean
  - exclusionReason: enum [none, employer_liability_excluded, intentional_self_injury, unrelated_third_party]
- **Exclusion Logic**:
  - **NOT applicable** when: Employer is liable (§93.1 - employer cannot claim from themselves)
  - **NOT applicable** for: Intentional self-injury by injured party (§94)
  - **NOT applicable** when: Third party is not legally liable for the damage
  - **Applies** when: Third party (other than employer) is liable for damage causing the insured event
- **Legal Basis**: §95-96

### DamageCauser (Vahingonaiheuttaja)
- **Description**: Party causing the damage/accident - distinct from employer who may be liable but not necessarily the causer
- **Attributes**: 
  - causationType: enum [direct, indirect, contributory]
  - liabilityBasis: enum [strict_liability, fault_based, contractual, statutory]
  - faultLevel: enum [none, slight, moderate, gross, intentional]
  - partyType: enum [employer, third_party, colleague, self, unknown]
  - isIdentified: boolean
  - insuranceStatus: enum [insured, uninsured, unknown]
- **Legal Basis**: §95-96

### Vahinkotapahtuma (DamageEvent)
- **Legal Basis**: §15
- **Description**: The damage event - the occurrence that causes damage/injury. This is the triggering event for insurance compensation.
- **Attributes**:
  - **eventId**: unique identifier
  - **eventType** (tapahtuman laatu): enum [occupational_accident, occupational_disease, commuting_accident, work_related_activity]
  - **eventDate** (tapahtumapäivä): date - when the event occurred
  - **eventTime** (tapahtuma-aika): time
  - **eventLocation** (tapahtumapaikka): string - where the event occurred
  - **description** (kuvaus): string - detailed description of circumstances
  - **insuredPerson** (vakuutettu): reference to InjuredParty
  - **employer** (työnantaja): reference to Employer
  - **workActivity** (työtoiminta): enum [main_work, commuting, business_trip, rehabilitation, sports]
  - **witnesses** (todistajat): array of strings
  - **reportedToEmployer** (ilmoitettu työnantajalle): boolean
  - **employerNotificationDate** (työnantajan ilmoituspäivämäärä): date
  - **insuranceNotificationDate** (vakuutuksenantajan ilmoituspäivämäärä): date
- **Related Entities**:
  - **Vahinko (Damage)**: The consequence of the event
  - **SyyYhteys (CausalConnection)**: Links event to damage
  - **InjuredParty**: The person affected

### Vahinko (Damage)
- **Description**: Damage as a consequence of a vahinkotapahtuma (damage event) - the actual injury/illness resulting from the insured event
- **Legal Basis**: §2.3, §15-16
- **Attributes**:
  - damageType: enum [physical_injury, occupational_disease, psychological_injury, death]
  - severity: enum [minor, moderate, severe, total]
  - bodyPartAffected: string
  - medicalDiagnosis: string
  - causationToEvent: reference to SyyYhteys
  - manifestationDate: date
  - isPermanent: boolean
- **Causal Chain**: Vahinkotapahtuma (Event) → Vahinko (Damage) → Korvaus (Compensation)
- **Related**: §83-87 (disability classification depends on damage consequence)

### SyyYhteys (CausalConnection)
- **Description**: Causal connection between work accident/occupational disease and the damage/injury
- **Legal Basis**: §16, §19, §30
- **Attributes**:
  - connectionType: enum [direct_cause, contributing_cause, aggravation]
  - assessmentDate: date
  - assessor: string (medical expert)
  - medicalOpinion: string
  - workContribution: number (percentage 0-100)
  - preExistingCondition: boolean
  - deteriorationType: reference to PreExistingConditionDeterioration
- **Assessment Criteria** (§16): Damage must be caused by work accident or occupational disease
- **Required for**: All compensation claims except funeral expenses

### StatisticHistory (Tilastohistoria)
- **Description**: Statistical history data for insurance transfers per §167
- **Legal Basis**: §167
- **Attributes**: payrollData, accidentEventData, compensationData, yearsCovered, sourceInsuranceCompany, targetInsuranceCompany
- **yearsCovered**: 5 years per §167
- **Purpose**: Required when transferring insurance or requesting offers with payroll >€150,000

### InsuranceRegister (Vakuutusrekisteri)
- **Description**: Insurance register maintained by Tapaturmavakuutuskeskus for compliance monitoring
- **Legal Basis**: §178
- **Attributes**: employerName, businessId, insuranceCompany, policyStartDate, policyEndDate, registrationDate
- **Purpose**: Monitor insurance compliance, combat gray economy

### DelayInterest (Viivästyskorko)
- **Description**: Interest charged for delayed payments
- **Legal Basis**: §152 (compensation delay), §172 (premium delay)
- **Attributes**: interestType, baseAmount, delayStartDate, interestRate, minimumThreshold
- **interestType values**: compensation_delay, premium_delay
- **minimumThreshold**: €7.28 per §152.4

### DeathCompensation
- **Legal Basis**: Sections 99-109
- **Includes**: SurvivorsPension, FuneralExpenses

### FuneralExpenses (Hautausapu)
- **Description**: Compensation for funeral expenses and transportation of deceased
- **Legal Basis**: §109
- **Amount**: €4,760
- **Payment To**: Deceased's estate (kuolinpesä) if funeral costs paid from estate; otherwise to those who arranged funeral
- **Maximum**: Amount that would have been paid to estate
- **Additional**: Reasonable transportation costs from death location to residence/home locality also covered
- **Attributes**: amount, recipient, deathLocation, funeralDate

---

## 5. Key Relationships

| Subject | Predicate | Object | Condition |
|---------|-----------|--------|-----------|
| Employee | has_right_to | Compensation | When suffering occupational accident |
| Employer | must_obtain | MandatoryInsurance | For all employees |
| InsuranceCompany | must_pay | Compensation | When insured event occurs |
| InjuredParty | must_file_claim_within | 5 years | From accident/disease date |
| Survivor | has_right_to | DeathCompensation | When injured party dies |

---

## 6. Institutions

### InsuranceCompany
- **Legal Basis**: Section 205
- Authorized to provide insurance

### StateTreasury (Valtiokonttori)
- **Legal Basis**: Section 207
- Pays compensation for state employees

### AccidentInsuranceCentre (Tapaturmavakuutuskeskus)
- **Legal Basis**: Sections 209-225
- Central coordinating organization

### ClaimAppealBoard (Tapaturma-asiain korvauslautakunta)
- **Legal Basis**: Sections 226-228
- **Description**: Advisory body for uniform compensation practice - issues recommendations and opinions
- **NOT an appeal body** - provides expert opinions to insurers

### AccidentAppealsBoard (Tapaturma-asiainratkaisulautakunta / Muutoksenhakulautakunta)
- **Legal Basis**: §237
- **Description**: First instance appeal body for vakuutuslaitos decisions - distinct from ClaimAppealBoard (§226-228)
- **Appeal deadline**: 30 days (§241)
- **Attributes**: 
  - boardName (Finnish: Tapaturma-asiainratkaisulautakunta)
  - finnishName: "Tapaturma-asioiden muutoksenhakulautakunta"
  - jurisdiction
  - decisionMakingProcess
  - isDistinctFromClaimAppealBoard: boolean - true (separate body per §226-228 vs §237)
- **Subclasses**:
  - InsuranceCompanyDecisionAppeal (§237) - Appeal against insurance company decision
  - PremiumAssessmentAppeal (§238) - Appeal against premium calculation

### Appeal (Valitus)
- **Description**: Formal appeal against insurance company decision
- **Legal Basis**: §237-243
- **Attributes**:
  - appealType: enum [regular, premium, correction]
  - filingDate, deadline, status
  - groundsForAppeal: string - factual/legal basis
  - supportingDocuments: array
  - decisionDeadline: 30 days per §241
- **Subclasses**:
  - RegularAppeal (Tavallinen valitus) - §237, standard appeal against compensation decision
  - PremiumAppeal (Maksuperustevalitus) - §238, appeal against premium assessment
  - BaseAppeal (Perustevalitus) - §240, appeal on fundamental legal questions

### AppealDecision (Valituspäätös)
- **Description**: Decision on appeal by Accident Appeals Board or court
- **Legal Basis**: §242-243
- **Attributes**: decisionDate, decisionType, reasoning, appealInstructions
- **decisionType values**: upheld, reversed, remanded, dismissed

### SelfCorrection (Oma muutos)
- **Description**: Insurance company's right to self-correct decisions
- **Legal Basis**: §242
- **Attributes**: originalDecisionDate, correctionDate, correctedAmount, correctionReason
- **Trigger**: New information or error discovery

### DecisionRemoval (Päätöksen poisto)
- **Description**: Removal of incorrect decision
- **Legal Basis**: §246
- **Attributes**: removalReason, originalDecision, effectiveDate
- **Conditions**: Decision was clearly incorrect, may be initiated by insurer or court

### ReimbursementRight (Takaisinperintäoikeus)
- **Description**: Right to recover overpaid compensation
- **Legal Basis**: §247
- **Attributes**:
  - overpaymentAmount, originalPaymentDate, recoveryDate
  - recoveryReason: enum [error, fraudulent_claim, changed_circumstances, deceased]
  - recoveryProcedure: enum [voluntary, deduction, court_proceedings]
  - statuteOfLimitations: 5 years per §247.3
  - interestRate: reference to §152 delay interest
- **Limitations**:
  - Cannot recover if claimant not at fault and would cause unreasonable hardship (§247.2)
  - Maximum recovery period: 5 years from overpayment (§247.3)
- **Related**: DelayInterest (§152)

### ApplicationDeterminationBody (Lain soveltaminen)
- **Legal Basis**: §7
- **Description**: Determines if law applies to specific work
- **Function**: Ratkaisee lain soveltamisesta

### InsuranceCourt (Vakuutusoikeus)
- **Legal Basis**: Section 227
- Appellate body for insurance decisions

### DistrictCourt (Käräjäoikeus)
- **Legal Basis**: Section 228
- **First instance court for disputes

### DistributionSystem (Jakojarjestelma)
- **Description**: Shared risk distribution system among insurance companies for workers' compensation
- **Legal Basis**: §231
- **Purpose**: System for distributing claims costs and administrative responsibilities among insurance companies
- **Attributes**:
  - **systemType**: Type of distribution system (risk_pool, administrative_pool, combined)
  - **participantCompanies**: List of participating insurance companies
  - **companyShares**: Each company's share of system costs
  - **distributionKey**: Method for allocating costs (premium_share, claims_share,混合)
  - **annualContribution**: Annual payment to/from system per company
  - **systemBalance**: Current system surplus/deficit
  - **adjustmentFactor**: Annual adjustment factor per §231.4
  - **advanceEstimate**: Preliminary estimate per §231.4
  - **finalSettlement**: Final settlement amounts per §231.5
  - **largeDamageThreshold**: €8.4 million per §231.1 (threshold for extraordinary cost distribution)
  - **largeDamagePool**: Separate pool for costs exceeding threshold
- **Related Entities**:
  - **Tapaturmavakuutuskeskus**: System administrator
  - **InsuranceCompany**: System participants
  - **InsuranceTransfer**: Affects system participation (§231.4)
- **Calculations**:
  - Risk-based distribution of claims
  - Administrative cost sharing
  - Annual reconciliation process

---

## 5.1. Procedural Documentation

- **Effective Date**: 2016-01-01
- **Replaced Laws**:
  - Tapaturmavakuutuslaki (608/1948)
  - Ammattitautilaki (1343/1988)
  - Tapaturmavakuutuslain mukainen kuntoutuslaki (625/1991)
  - Valtion virkamiesten tapaturmakorvaukset (449/1990)

---

## 8. Coverage

- **Geographical**: Finland primarily, extended to EU/agreement countries
- **Personal Scope**: Employees, entrepreneurs (voluntary), certain other groups
