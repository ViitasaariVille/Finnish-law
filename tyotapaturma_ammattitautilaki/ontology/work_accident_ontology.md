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
- **Legal Basis**: §15-16, §111.2.1
- **Attributes**: 
  - injuryDate, injuryType, severity, medicalFindings
  - personId (henkilötunnus) - REQUIRED
  - name (nimi)
  - contactInformation (yhteystiedot)
  - otherEmployment (muu työsuhde) - §111.2.5
  - otherEntrepreneurWork (muu yrittäjätyö) - §111.2.5

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
- **Attributes**: relationshipType, sharesHousehold, relationshipStartDate, isForOwnershipCalculation, isForBenefitPurposes
- **relationshipType values**: spouse, cohabiting_partner, direct_ascendant, direct_descendant
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

### Notification (Ilmoitus)
- **Description**: Formal notification of accident
- **Legal Basis**: §110-113
- **Attributes**: notificationDate, notificationType, deadlineStatus
- **Subclasses**:
  - EmployeeNotification (§110) - to employer
  - EmployerNotification (§111) - to insurer, 10 working days deadline

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

### OccupationalAccident
- **Legal Basis**: Sections 17-25
- **Subclasses**:
  - WorkplaceAccident
  - CommuteAccident  
  - BusinessTripAccident
  - WorkRelatedActivityAccident

### OccupationalDisease
- **Legal Basis**: Sections 26-32
- **Attributes**: diseaseCode, exposureDuration, latencyPeriod
- **Subclasses**:
  - AmmattitautiluetteloSairaus (StatutoryListDisease) - diseases on official occupational disease list
  - YlaraajanJannetulehdus (UpperLimbTendonInflammation) - §28, condition: repetitive, unusual upper limb movements
  - Rannekanavaoireyhtyma (CarpalTunnelSyndrome) - §29, condition: repetitive, forceful, wrist-bending movements
  - TyostaAiheutunutPaheneminen (WorkRelatedDeterioration) - §30, essential worsening of pre-existing condition

### WorkMotionStrain (Työliikekipeytyminen)
- **Legal Basis**: Section 33
- **Description**: Acute muscle/tendon strain from single strenuous work movement (NOT repetitive)
- **Note**: Maximum 6 weeks compensation
- **Attributes**: strainLocation, workActivityDuringStrain, onsetDate

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

### DailyAllowance
- **Legal Basis**: Sections 56-62
- **Maximum Duration**: 1 year from accident date

### DisabilityPension
- **Legal Basis**: Sections 63-68
- **Requirement**: Minimum 10% work capacity reduction

### RehabilitationAllowance
- **Legal Basis**: Sections 69, 88-98

### PermanentDamageCompensation
- **Legal Basis**: Sections 83-87
- **Classes**: 1-20 based on severity
- **Base Amount**: €12,440
- **Haittaluokka (DisabilityClass) Enumeration**:
  - Class 1: 1.15%
  - Class 2: 2.27%
  - Class 3: 3.42%
  - Class 4: 4.60%
  - Class 5: 5.80%
  - Class 6: 7.03%
  - Class 7: 8.28%
  - Class 8: 9.55%
  - Class 9: 9.55%
  - Class 10: 10.15%
  - Class 11: 13%
  - Class 12: 16%
  - Class 13: 20%
  - Class 14: 25%
  - Class 15: 30%
  - Class 16: 35%
  - Class 17: 40%
  - Class 18: 45%
  - Class 19: 52%
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

### Takautumisoikeus (RecourseRight)
- **Description**: Right of recourse - insurer's right to claim compensation from liable third party
- **Attributes**: recourseType, liableParty, claimAmount
- **recourseType values**: subrogation, contribution, indemnification
- **Legal Basis**: §95-96

### DamageCauser (Vahingonaiheuttaja)
- **Description**: Party causing the damage/accident
- **Attributes**: causationType, liabilityBasis, faultLevel
- **causationType values**: direct, indirect, contributory
- **Legal Basis**: §95-96

### DeathCompensation
- **Legal Basis**: Sections 99-109
- **Includes**: SurvivorsPension, FuneralExpenses

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

### AccidentAppealsBoard (Tapaturma-asioiden muutoksenhakulautakunta)
- **Legal Basis**: §237
- **Description**: First instance appeal body for vakuutuslaitos decisions
- **Appeal deadline**: 30 days (§241)

### ApplicationDeterminationBody (Lain soveltaminen)
- **Legal Basis**: §7
- **Description**: Determines if law applies to specific work
- **Function**: Ratkaisee lain soveltamisesta

### InsuranceCourt (Vakuutusoikeus)
- **Legal Basis**: Section 227
- Appellate body for insurance decisions

### DistrictCourt (Käräjäoikeus)
- **Legal Basis**: Section 228
- First instance court for disputes

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
