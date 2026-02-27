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
- **Attributes**: 
  - studentType: enum [higher_education, vocational, basic_secondary]
  - studyProgram, enrollmentDate, expectedGraduationDate
  - isFullTime: boolean
  - actualEarningsAtInjury: MonetaryAmount
  - **Special Earnings Rules per §76, §77**:
    - **estimatedEarnings3YearsPostGraduation** (decimal): §76 for vocational students - estimated earnings 3 years after graduation
    - **isWithinOneYearOfCompletion** (boolean): §76 - applies within 1 year of study completion
    - **studyCompletionStatus** (enum): [ongoing, completed_within_year, completed_over_year_ago]
    - **minimumEarningsMultiplier** (decimal): §77 - 2.0x basic amount for pupils (€13,680 × 2)
    - **educationLevel** (enum): [basic_secondary, vocational, higher_education]
    - **actualEarningsCalculationMethod** (enum): [estimated_future, pupil_minimum, actual_earnings]
- **Related Compensation**: 
  - §70: Full incapacity if injury prevents studying
  - §76: Future earnings estimate for vocational students
  - §77: Minimum 2x basic amount (€13,680 × 2) for pupils

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
  - **Pension Status** (per §56.4, §60, §73-74):
    - pensionStatus: enum [none, old_age_pension, disability_pension] - §2.9, §2.10
    - receivesOldAgePension (boolean) - receiving old-age pension at time of accident (§56.4, §60, §73)
    - receivesDisabilityPension (boolean) - receiving disability pension at time of accident (§56.4, §74)
    - pensionStartDate (date) - when pension started (§56.4, §74)
    - pensionType (enum) - [old_age, disability, partial_disability, survivor]

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
- **Explicitly Excluded per §117**: Employer, HealthcareProvider, Municipality
- **Attributes**:
  - isExcludedParty (boolean): true if explicitly excluded from being a party per §117
  - exclusionReason (enum): [employer, healthcare_provider, healthcare_institution, municipality, joint_municipal_authority, compensation_recipient] - per §117 exclusions

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
- **Legal Basis**: 
  - §3.2: Exemption when annual payroll ≤ €1,200
  - §3.3: State employer exemption - compensation paid by StateTreasury (Valtiokonttori) per §207
- **Note**: When exemptionType = state-employer, compensation is paid by StateTreasury (Valtiokonttori), not an insurance company

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

### InvestigationObligation (Selvittämisvelvollisuus)
- **Description**: Insurance company's legal investigation obligations per §119-120
- **Legal Basis**: §119, §120
- **Attributes**:
  - investigationStartDeadline: integer - 7 working days per §119
  - rehabilitationAssessmentDeadline: integer - 3 months per §120
  - rehabilitationAssessmentInterval: integer - 3 months per §120
  - isInvestigationStarted: boolean
  - investigationStartDate: date
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
  - **CommuteAccident (Työmatkatapaturma)** - §20, §23, injury on journey to/from work
    - **isCustomaryRoute** (boolean): §23.1 - must be "tavanomainen" (customary) commute between home and work
    - **hasDeviation** (boolean): whether route deviated from direct path
    - **deviationReason** (enum): [childcare, grocery_shopping, other_comparable, none] - §23.1 minor deviations allowed
    - **deviationDurationMinutes** (int): duration of deviation
    - **isMealBreak** (boolean): §23.2 - normal meal breaks near workplace included
    - **isRestBreak** (boolean): §23.2 - rest breaks near workplace included
    - **proximityToWorkplace** (enum): [near_area, normal_route, other] - §23.2 area near workplace
    - **routeStartLocation**: string - typically home
    - **routeEndLocation**: string - typically workplace
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

### OccupationalDiseaseManifestation (Ammattitaudin ilmenemisaika)
- **Legal Basis**: §31
- **Description**: Date when occupational disease manifested - determines claim filing deadlines and insurance liability
- **Attributes**:
  - **manifestationDate** (date): date when disease first manifested per §31 (first medical exam for symptoms)
  - **firstMedicalExaminationDate** (date): date injured first sought medical examination for symptoms
  - **symptomOnsetDate** (date): date symptoms first appeared
  - **diagnosisDate** (date): date of formal diagnosis
  - **isManifestationDateSpecial** (boolean): whether "special reason" applies per §31
  - **specialReasonDescription** (text): explanation if special reason applies
  - **manifestationBasis** (enum): [first_medical_exam, symptom_onset, diagnosis_date] - basis for determination
- **Note**: Per §31, manifestation date is when injured first sought medical examination for symptoms (unless special reason requires different date)

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
- **Attributes**: 
  - causationAssessment, preExistingCondition, worseningDegree, duration
  - **deteriorationType** (enum): [accident_related, occupational_disease_related] - per §19 or §30
  - **maxDurationMonths** (int): 6 for accident-related per §19.2, null for occupational disease
  - **isExtended** (boolean): whether extension beyond 6 months granted
  - **extensionReason** (enum): [treatment_choice_delay, waiting_delay, none] - per §19.2
  - **extensionGrantedDate** (date): when extension was granted
  - **accidentDate** (date): for calculating 6-month deadline per §19.2
  - **sixMonthDeadlineDate** (date): deadline 6 months from accident

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
- **Legal Basis**: §34
- **Description**: Damage from assault or intentional act by another person - must be related to work duties
- **Attributes**:
  - causationType: enum [assault, intentional_act, threat]
  - liabilityBasis: enum [work_related, third_party_liable]
  - faultLevel: enum [intentional, negligent, unknown]
  - **exclusionType** (§34.2-34.3): enum [none, family_related, private_life, commute_activity, recreational_activity]
  - **isWorkRelatedCausation** (boolean): whether primarily related to work duties
  - **locationType** (enum): [workplace, commute_route, recreational_venue, other]
  - **primaryCauseRelation** (enum): [work_duty, family_relation, private_life, unknown]
- **Exclusions per §34.2-34.3**:
  - NOT covered if act primarily relates to family relations or private life
  - NOT covered if occurred during commute breaks (§23.2) or recreational activities (§24.1 paragraphs 2-8) unless intentional third-party damage related to work duties

### PsychologicalShock
- **Legal Basis**: §35
- **Description**: Psychological injury from shock or fear caused by work-related incident
- **Subclasses**: AcuteStressReaction, PTSD, PersonalityChange
- **Preconditions per §35**:
  - **diagnosisRequired**: boolean - must be diagnosed by qualified professional
  - **diagnosisDeadline**: date - PTSD/personality change requires diagnosis within 6 months of event
  - **causationRequirement**: incident must be sudden, unexpected, at work or commuting
  - **workConnection**: boolean - must be causally connected to work duties
  - **directInvolvement** (boolean): direct involvement in event per §35.4
  - **factualConnectionToWork** (boolean): tight factual connection to work per §35.4
  - **activityTypeAtIncident** (enum): work_activity, commute_activity, recreational_activity, training_activity
  - **isIntentionalThirdPartyDamage** (boolean): exception to exclusions per §35.5
- **Subclasses**:
  - **AcuteStressReaction** (Akuutti stressireaktio): immediate reaction, short duration
  - **PTSD** (Traumaperäinen stressihäiriö): requires diagnosis within 6 months per §35
  - **PersonalityChange** (Persoonallisuuden muutos): requires diagnosis within 6 months per §35

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
- **Description**: Waiting period before daily allowance becomes payable - structured entity for §56.3 rules
- **Legal Basis**: §56.3
- **Attributes**:
  - **waitingDays**: integer - fixed at 3 per §56.3
  - **waitingPeriodStartDate**: date - when the waiting period begins (accident day or first day of incapacity)
  - **waitingPeriodEndDate**: date - day 3 of incapacity when waiting period completes
  - **paymentStartDate**: date - date when payments begin after waiting period is satisfied (day 4)
  - **isConsecutiveDaysRequirementMet**: boolean - whether 3 consecutive days of incapacity requirement is met
  - **excludesAccidentDay**: boolean - true per §56.3 (accident day excluded from waiting period)
  - **relatedDailyAllowance**: reference to DailyAllowance - the daily allowance this waiting period applies to
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
  - **negligenceType values**: alcohol_drugs, medication_misuse, safety_violation, gross_negligence, criminal_conduct
  - **reductionPercentage**: max 50% per §61
  - **isReductionApplied**: boolean

### NegligenceReduction (Myötävaikutus)
- **Legal Basis**: §61
- **Description**: Reduction of daily allowance due to injured party's own contribution to the accident
- **Attributes**:
  - **negligenceType**: enum [alcohol_drugs, medication_misuse, safety_violation, gross_negligence, criminal_conduct]
    - **alcohol_drugs** (§61.1): Being under influence of alcohol or drugs
    - **medication_misuse** (§61.1): Medication misuse
    - **safety_violation** (§61.2): Intentional or grossly negligent violation of work safety regulations
    - **gross_negligence** (§61.3): Gross negligence
    - **criminal_conduct** (§61.3): Criminal conduct
  - **reductionPercentage**: number - max 50% per §61
  - **isReductionApplied**: boolean
  - **severity**: enum [minor, moderate, severe] - affects reduction amount
  - **evidenceRequired**: documentation of negligence

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
- **Legal Basis**: §69, §88-98
- **Description**: Compensation during rehabilitation to replace lost earnings
- **Attributes**:
  - **phase** (enum): [first_year, after_first_year] - §69.2
  - **calculationBasis** (enum): [daily_allowance_full, disability_pension_full, partial_capacity_based]
  - **includesVacationPeriods** (boolean): §69.3 - includes vacation periods during education
  - **vacationPeriodStart** (date): start of vacation period
  - **vacationPeriodEnd** (date): end of vacation period
  - **preventsSuitableWork** (boolean): whether rehabilitation prevents suitable work
  - **firstYearEndDate** (date): end of first year of rehabilitation
  - **yearlyAmount** (MonetaryAmount): full amount regardless of capacity reduction per §69.2
- **Calculation Rules per §69.2**:
  - First year: Full daily allowance regardless of capacity reduction
  - After first year: Full disability pension amount regardless of capacity
  - Exception: If rehabilitation doesn't prevent suitable work → calculated per §56-57 or §63-64

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

### DisabilityCombination (Haittaluokkien yhdistäminen)
- **Description**: Rules for combining multiple disability classes per §84 - formula for calculating combined disability when person has multiple disabilities
- **Legal Basis**: §84
- **Formula**: K = A + B - (A×B)/20 where A and B are individual disability class percentages
- **Attributes**:
  - **formula**: string - "A + B - (A×B)/20" per §84.4
  - **disabilityA**: integer - first disability class (1-20)
  - **disabilityB**: integer - second disability class (1-20)
  - **combinedDisability**: integer - calculated combined disability class using formula
  - **isPairOrgan**: boolean - exemption from formula per §84.5 for paired organs (eyes, ears, kidneys, limbs)
  - **isCombinedVisionHearing**: boolean - exemption from formula per §84.5 for combined vision and hearing disabilities
  - **exemptionReason**: enum [none, pair_organ, vision_hearing_combined] - reason if formula doesn't apply
- **Exemptions per §84.5**:
  - Paired organs (silmät, korvat, munuaiset, raajat): disabilities combined additively, not using formula
  - Combined vision and hearing: disabilities combined additively, not using formula
- **Related Entities**: PermanentDamageCompensation (§83-87), DisabilityClassification

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

### PartialWorkCapacity (Osittainen työkyky)
- **Legal Basis**: §57, §64
- **Description**: Partial work capacity calculation for daily allowance and disability pension - earnings reduction percentage rounded to nearest 5%
- **Attributes**:
  - **earningsReductionPercentage**: number - rounded to nearest 5% per §57, §64
  - **preAccidentEarnings**: MonetaryAmount - earnings before accident
  - **postAccidentEarnings**: MonetaryAmount - earnings after accident (with reduced capacity)
  - **comparisonMethod**: enum [same_employer, comparable_work, estimated_capacity] - how earnings compared
  - **appliesToDailyAllowance**: boolean - §57 applies to daily allowance
  - **appliesToDisabilityPension**: boolean - §64 applies to disability pension
  - **partialDisabilityType**: enum [earning_reduction, capacity_reduction] - type of partial disability
  - **roundingMethod**: enum [nearest_5, upward] - rounding per law
- **Calculation**: (preAccidentEarnings - postAccidentEarnings) / preAccidentEarnings * 100, rounded to nearest 5%
- **Related Entities**: DailyAllowance (§57), DisabilityPension (§64), WorkCapacity

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
  - **eventType** (tapahtuman laatu): enum [
    occupational_accident,
    occupational_disease,
    commuting_accident,
    work_related_activity,
    work_motion_strain,        # §33: Acute muscle/tendon strain from single work movement
    violence_damage,            # §34: Damage from assault related to work duties
    psychological_shock         # §35: Acute stress reaction, PTSD, personality change
    ]
  - **specialConditionType** (§18): enum [
    friction_blister,           # §18.1: Skin blister from friction
    corrosive_injury,           # §18.2: Contact with corrosive substance
    gas_vapor_inhalation,       # §18.3: Inhaling gas, vapor, or fumes
    temperature_injury,         # §18.4: Cold/heat injury, hypothermia, burns
    radiation_injury,           # §18.5: Radiation-induced injury
    pressure_variation_injury  # §18.6: Significant pressure variation injury
    ]
  - **exposureWindowHours** (§18): integer - max 24 hours per §18 condition
  - **notOccupationalDisease** (§18): boolean - must be true (exclusion from occupational disease)
  - **psychologicalShockSubtype** (§35): enum [acute_stress_reaction, ptsd, personality_change]
  - **ptsdDiagnosisWithin6Months** (boolean): §35.2 - PTSD diagnosis must be within 6 months of event
  - **immediateInvolvement** (boolean): §35.4 - injured was immediately involved in the event
  - **eventSubType**: enum [single_movement, cumulative_trauma] - distinguishes §33 from repetitive strain
  - **workLocationType** (§21-25): enum [at_work, workplace_area, outside_workplace, special_circumstances, at_home, undefined_location]
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
  - **causationType** (§16): enum [direct_causation, substantial_contribution, aggravation, acceleration]
    - direct_causation: Suora syy-yhteys
    - substantial_contribution: Olennainen myötävaikuttaminen
    - aggravation: Taudin paheneminen
    - acceleration: Taudin puhkeaminen
  - **causationStrength** (§16): enum [probable, possible, unlikely, no_connection]
    - probable: Todennäköinen
    - possible: Mahdollinen
    - unlikely: Epätodennäköinen
    - no_connection: Ei syy-yhteyttä
  - **burdenOfProof** (§16): enum [balance_of_probabilities, reasonable_certainty, medical_consensus]
  - **temporalConnection** (boolean): §16 - injury occurred during work time or work-related activity
  - **spatialConnection** (boolean): §16 - injury occurred at workplace or work-mandated location
  - **medicalEvidenceLevel** (enum): [conclusive, supportive, suggestive, insufficient]
  - connectionType: enum [direct_cause, contributing_cause, aggravation]
  - medicalFindings (string): §16 - lääketieteelliset löydökset ja havainnot
  - causationMechanism (string): §16 - vahingon sattumistapa (how injury occurred)
  - timingRelationship (string): §16 - ajallinen yhtös
  - priorInjuryContribution (number): §16 - aikaisempien vammojen myötävaikutus (0-100%)
  - priorIllnessContribution (number): §16 - aikaisempien sairauksien myötävaikutus (0-100%)
  - probableCausation (boolean): §16 - todennäköinen syy-yhteys established
  - assessmentBasis (enum): [medical_evidence, circumstances, combined] - per §16
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
- **Base Amount**: €4,760
- **Payment To** (§109.2): Deceased's estate (kuolinpesä) if funeral costs paid from estate; otherwise to those who arranged funeral up to estate amount
- **Additional**: Reasonable transportation costs from death location to residence/home locality also covered (§109.3)
- **Attributes**: 
  - amount: MonetaryAmount - base €4,760
  - recipient: string
  - **recipientType** (enum): [deceased_estate, funeral_arranger, other]
  - **paymentSource** (enum): [estate_funds, third_party]
  - **maxPayableAmount** (MonetaryAmount): limited to estate amount per §109.2
  - **transportationCostsCovered** (boolean): §109.3
  - **deathLocation** (string): where death occurred
  - **homeLocality** (string): deceased's home locality
  - **transportationCostAmount** (MonetaryAmount): reasonable transportation costs
  - **totalFuneralCosts** (MonetaryAmount): total cost of funeral
  - **estateAmount** (MonetaryAmount): estate amount for max calculation

---

## 4.1. Employer Duties & Occupational Disease Factors

### AccidentLogbook (Tapaturma- ja vaarailmoitusrekisteri)
- **Description**: Employer's mandatory record of work accidents and near-misses (§267)
- **Legal Basis**: §267
- **Attributes**:
  - employer: reference to Employer
  - accidentRecords: array of AccidentRecord
  - annualSummary: string - yearly summary submitted to Tapaturmavakuutuskeskus
  - recordRetentionYears: integer - minimum 10 years
- **AccidentRecord**:
  - accidentDate: date
  - injuredPerson: reference to InjuredParty
  - accidentType: enum [occupational_accident, commuting_accident, near_miss]
  - severity: enum [minor, serious, fatal, near_miss]
  - rootCauseAnalysis: string
  - preventiveMeasures: array of string
  - reportedToAuthority: boolean
  - authorityReportDate: date

### WorkLocationType (Työpaikan sijainti)
- **Description**: Classification of work location for insurance coverage determination (§21-25)
- **Legal Basis**: §21-25
- **Attributes**:
  - locationCategory: enum [
    fixed_workplace,           # §21: Regular place of work
    mobile_work,               # §21: Work involving travel between locations
    construction_site,        # §22: Temporary construction work site
    remote_work,               # §23: Work from home or remote location
    vehicle_work,              # §24: Work in or on vehicle
    vessel_work,               # §24: Work on ship or floating platform
    aircraft_work,             # §24: Work in aircraft
    offshore_installations,    # §25: Oil platforms, offshore structures
    underground_work,          # §25: Mining, tunnel work
    hazardous_area             # §25: Areas with special risks
    ]
  - isInsurable: boolean
  - coverageNotes: string
  - relatedSections: array of string

### ExposureFactor (Altistustekijä)
- **Description**: Factor contributing to occupational disease development (§26)
- **Legal Basis**: §26
- **Attributes**:
  - factorType: enum [
    chemical_agent,            # §26.1: Chemical substances (solvents, metals, etc.)
    biological_agent,          # §26.1: Bacteria, viruses, fungi
    physical_factor,           # §26.2: Noise, vibration, radiation, temperature
    ergonomic_factor,          # §26.3: Repetitive motion, posture, lifting
    psychological_factor,     # §26.4: Stress, harassment, violence
    dust_particle,            # §26.5: Mineral dust, asbestos, silica
    carcinogenic_agent        # §26.6: Known carcinogens
    ]
  - substanceName: string - specific agent name
  - exposureLevel: string - measured exposure amount
  - exposureDuration: duration
  - causalMechanism: string - how factor causes disease
  - diseaseReference: reference to occupationalDisease
  - thresholdLimit: string - occupational exposure limit
  - measurementDate: date
  - measurementMethod: string

### PensionStatus (Eläkestatus)
- **Description**: Status of pension recipient affecting compensation calculations (§2.9, §2.10, §56.4)
- **Legal Basis**: §2.9, §2.10, §56.4
- **Attributes**:
  - pensionType: enum [
    old_age_pension,          # §2.9: Vanhuuseläke - full old-age pension
    early_old_age_pension,    # §2.9: Varhennettu vanhuuseläke - reduced old-age pension
    disability_pension,       # §2.10: Työkyvyttömyyseläke - full disability pension
    partial_disability_pension, # §2.10: Osatyökyvyttömyyseläke - partial disability
    survivor_pension,         # §2.11: Perhe-eläke - surviving dependent pension
    unemployment_pension,     # §2.12: Työttömyyseläke (phased out)
    farmers_pension           # §2.13: Luopumiseläke (phased out)
    ]
  - pensionStartDate: date
  - pensionEndDate: date (if applicable)
  - pensionAmount: decimal
  - isReceivingAtTimeOfAccident: boolean - §56.4
  - affectsCompensationCalculation: boolean - certain pensions reduce daily allowance
  - reductionPercentage: decimal - applicable reduction per §56.4

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
- **Legal Basis**: §3.3, §207
- **Description**: Pays compensation for state employees when the State is the employer (state employees exempt from mandatory insurance per §3.3)
- **Attributes**:
  - institutionName: "Valtiokonttori"
  - role: enum [compensation_payer_for_state_employees]
  - legalBasis: "§207"
- **Relationships**:
  - pays_compensation_for: Employee (when employer.isStateEmployer = true)
  - alternative_to: InsuranceCompany (for state employees)
- **Note**: State Treasury (Valtiokonttori) is the institution responsible for compensating state employees per §207

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

### AppealChain (Muutoksenhaku)
- **Description**: Structured hierarchy of appeal bodies per §237-243
- **Legal Basis**: §237-243
- **Attributes**:
  - currentLevel: enum [accident_appeals_board, insurance_court, supreme_court]
  - nextLevelAvailable: boolean
  - appealDeadlineDays: integer - 30 days for first instance (§241)
  - supremeCourtDeadlineDays: integer - 60 days for Supreme Court (§241)
- **Appeal Progression**:
  1. AccidentAppealsBoard (§237) - 30 days
  2. InsuranceCourt (§227) - 30 days  
  3. SupremeCourt (Korkein oikeus) - 60 days with permission

### InsuranceCourt (Vakuutusoikeus)
- **Legal Basis**: §227
- **Description**: Appellate court for insurance decisions, hears appeals from Accident Appeals Board decisions
- **Attributes**:
  - courtName: "Vakuutusoikeus"
  - courtType: appellate
  - jurisdiction: insurance_matters
  - appealDeadlineDays: 30 (per §241 for board appeals)
- **Appeal Chain**: Insurance Company → Accident Appeals Board (§237) → Insurance Court (§227) → Supreme Court

### DistrictCourt (Käräjäoikeus)
- **Legal Basis**: §228
- **Description**: First instance court for certain disputes under the law
- **Attributes**:
  - courtName: "Käräjäoikeus"
  - courtType: first_instance
  - jurisdiction: general_disputes
- **Note**: Some cases may go directly to District Court rather than through administrative boards

### Appeal (Valitus)
- **Description**: Formal appeal against insurance company decision
- **Legal Basis**: §237-243
- **Attributes**:
  - appealType: enum [regular, premium, correction, base_appeal]
  - filingDate, deadline, status
  - groundsForAppeal: string - factual/legal basis
  - supportingDocuments: array
  - decisionDeadline: enum [
      {type: regular, days: 30, legalBasis: "§241.1"},
      {type: supreme_court_leave, days: 60, legalBasis: "§241.4"},
      {type: base_appeal, days: 730, legalBasis: "§240"}
    ]
- **Subclasses**:
  - RegularAppeal (Tavallinen valitus) - §237, standard appeal against compensation decision
  - PremiumAppeal (Maksuperustevalitus) - §238, appeal against premium assessment
  - BaseAppeal (Perustevalitus) - §240, appeal on fundamental legal questions

### AppealDecision (Valituspäätös)
- **Description**: Decision on appeal by Accident Appeals Board or court
- **Legal Basis**: §242-243
- **Attributes**: decisionDate, decisionType, reasoning, appealInstructions
- **decisionType values**: upheld, reversed, remanded, dismissed

### DistributionSystem (Jakojärjestelmä)
- **Legal Basis**: §231
- **Description**: System for sharing costs among insurance institutions when multiple insurers are involved or costs need redistribution based on collective risk
- **Attributes**:
  - **distributionType** (enum): [proportional, risk_based, claim_specific, periodic_balancing]
  - **participatingInsurers**: array of references to InsuranceCompany
  - **costPool**: MonetaryAmount - shared pool of costs to distribute
  - **distributionKey**: object - method for allocating costs
  - **settlementPeriod**: period - time period for settlement
  - **distributionAmount**: MonetaryAmount - total amount to be distributed
  - **settlementDate**: date - when settlement is finalized

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
