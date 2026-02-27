# Finnish Work Accident Ontology - Structure Compliance Analysis
## Työtapaturma- ja ammattitautilaki (459/2015)

**Analysis Date:** 2026-02-27  
**Ontology Version:** 1.0  
**Law Version:** 459/2015 (Effective 2016-01-01)

---

## Summary

This analysis identifies **12 NEW ontology structure gaps** beyond the 3 already identified issues (#276-278). The gaps are categorized by severity and organized by law chapter.

### Existing Issues (Already Identified)
- **Issue #278**: WorkMotionStrain missing exclusion attributes - §33
- **Issue #277**: ClaimApplication subtypes missing enumeration values - §128  
- **Issue #276**: Missing WorkCapacityReduction entity - §63

---

## NEW GAPS IDENTIFIED

### CRITICAL SEVERITY (4 gaps)

#### Gap #1: Missing WorkCapacityAssessment Entity
| | Details |
|---|---|
| **Law Section** | §63 (Työkyvyn heikentymisen arviointi) |
| **Missing** | Entity for formal work capacity assessment process |
| **Ontology vs Law** | Ontology has `WorkCapacity` with basic attributes (`capacityPercentage`, `capacityLevels`), but law §63 describes a formal assessment process considering: education, prior activity, age, residence, and other comparable factors. The assessment determines eligibility for disability pension. |
| **Required Entities/Attributes** | `WorkCapacityAssessment` entity with: `assessmentDate`, `assessor`, `educationConsidered`, `priorActivityConsidered`, `ageAtAssessment`, `residenceConsidered`, `assessmentBasis` (enumerated: medical_examination, functional_evaluation, work_trial) |
| **Impact** | Cannot properly model the assessment process that determines disability pension eligibility |

#### Gap #2: Missing DisabilityClassCombinationRules
| | Details |
| **Law Section** | §84 (Haittaluokkien yhdistäminen) |
| **Missing** | Entity/attributes for combining multiple disability classes |
| **Ontology vs Law** | Ontology lists DisabilityClass 1-20 enumeration but lacks the combination formula for multiple disabilities: K = A + B - (A×B)/20. Law §84.4 mandates specific calculation when multiple disabilities affect the same person. |
| **Required Entities/Attributes** | `DisabilityCombination` entity with: `formula` (string: "A + B - (A×B)/20"), `disabilityA` (int), `disabilityB` (int), `combinedDisability` (int), `isPairOrgan` (boolean - exemption from formula) |
| **Impact** | Cannot calculate correct disability class when injured party has multiple disabilities |

#### Gap #3: Missing PartialWorkCapacity Entity
| | Details |
| **Law Section** | §57 (Päiväraha osittaisen työkyvyttömyyden perusteella), §64 (Tapaturmaeläke osittaisen työkyvyttömyyden perusteella) |
| **Missing** | Dedicated entity for partial work capacity with specific calculation rules |
| **Ontology vs Law** | Ontology only has `WorkCapacity` with generic `capacityLevels` (full/partial/none). Law §57 and §64 specify partial disability calculations requiring: percentage reduction rounded to nearest 5%, comparison of pre/post accident earnings. |
| **Required Entities/Attributes** | `PartialWorkCapacity` entity with: `earningsReductionPercentage` (rounded to 5%), `preAccidentEarnings` (decimal), `postAccidentEarnings` (decimal), `comparisonMethod` (enumerated: same_employer, comparable_work, estimated_capacity) |
| **Impact** | Cannot properly model partial disability compensation calculations |

#### Gap #4: Missing ViolenceDamage Exclusions
| | Details |
| **Law Section** | §34 (Pahoinpitelyn ja toisen henkilön muun tahallisen teon aiheuttama vahinko) |
| **Missing** | Exclusion conditions for ViolenceDamage entity |
| **Ontology vs Law** | Ontology has `ViolenceDamage` entity with basic `causationType`, but law §34 specifies explicit exclusions: 1) If act primarily relates to family relations or private life, 2) If occurred during commute breaks (§23.2) or recreational activities (§24.1 paragraphs 2-8) unless it's intentional third-party damage related to work duties |
| **Required Entities/Attributes** | Add to `ViolenceDamage`: `exclusionType` (enumeration: family_related, private_life, commute_activity, recreational_activity), `isWorkRelatedCausation` (boolean), `locationType` (enumeration: workplace, commute_route, recreational_venue) |
| **Impact** | Cannot determine compensability of violence-related injuries correctly |

---

### HIGH SEVERITY (5 gaps)

#### Gap #5: Missing PsychologicalShock Preconditions
| | Details |
| **Law Section** | §35 (Henkinen järkytysreaktio työtapaturman seurauksena) |
| **Missing** | Specific preconditions and timing constraints for psychological shock compensation |
| **Ontology vs Law** | Ontology has `PsychologicalShock` with subclasses (AcuteStressReaction, PTSD, PersonalityChange) but missing §35 requirements: 1) Symptoms must be diagnosed within 6 months, 2) Person must have been directly involved in the event, 3) Event must have tight factual connection to work circumstances, 4) Exclusions for activities during commute/recreation (§23.2, §24.1 paragraphs 2-7) unless it's §34 intentional damage |
| **Required Entities/Attributes** | Add to `PsychologicalShock`: `diagnosisWithin6Months` (boolean), `directInvolvement` (boolean), `factualConnectionToWork` (boolean), `activityTypeAtIncident` (enumeration: work_activity, commute_activity, recreational_activity, training_activity), `symptomsOnsetDate` (date), `sixMonthDeadlineDate` (date) |
| **Impact** | Cannot validate eligibility for psychological shock compensation |

#### Gap #6: Missing CommuteAccident Specific Attributes
| | Details |
| **Law Section** | §23 (Tapaturma työntekopaikan alueen ulkopuolella) |
| **Missing** | Detailed attributes for commute accidents including deviations |
| **Ontology vs Law** | Ontology lists `CommuteAccident` as subclass but lacks §23 specifics: 1) "Tavanomainen" (customary) commute between home and work, 2) Minor deviations allowed for childcare, grocery shopping, or comparable reasons, 3) Normal meal/rest breaks near workplace area |
| **Required Entities/Attributes** | `CommuteAccident` entity with: `isCustomaryRoute` (boolean), `hasDeviation` (boolean), `deviationReason` (enumeration: childcare, grocery_shopping, other_comparable), `deviationDurationMinutes` (int), `isMealBreak` (boolean), `isRestBreak` (boolean), `proximityToWorkplace` (enumeration: near_area, normal_route) |
| **Impact** | Cannot determine if commute accident is compensable |

#### Gap #7: Missing OccupationalDiseaseManifestation Entity
| | Details |
| **Law Section** | §31 (Ammattitaudin ilmenemisaika) |
| **Missing** | Entity defining when occupational disease is considered manifested |
| **Ontology vs Law** | Ontology has `OccupationalDisease` with `diseaseCode`, `exposureDuration`, `latencyPeriod` but lacks §31 manifestation rules: Disease manifested on date when injured party first sought medical examination for symptoms later diagnosed as occupational disease |
| **Required Entities/Attributes** | `OccupationalDiseaseManifestation` entity with: `manifestationDate` (date - per §31), `firstMedicalExaminationDate` (date), `symptomOnsetDate` (date), `diagnosisDate` (date), `isManifestationDateSpecial` (boolean - "unless special reason"), `specialReasonDescription` (text) |
| **Impact** | Cannot determine correct manifestation date for occupational disease claims |

#### Gap #8: Missing Student Special Earnings Rules
| | Details |
| **Law Section** | §76 (Päätoimisesti ammattiin opiskelevan vuosityöansio), §77 (Koululaisen vuosityöansio) |
| **Missing** | Special annual earnings calculation attributes for students |
| **Ontology vs Law** | Ontology `Student` entity has `actualEarningsAtInjury` but missing §76/§77 specifics: 1) For vocational students: estimated earnings 3 years after graduation, 2) For pupils: minimum 2x basic amount (§77), 3) Applies within 1 year of study completion |
| **Required Entities/Attributes** | Add to `Student`: `estimatedEarnings3YearsPostGraduation` (decimal), `isWithinOneYearOfCompletion` (boolean), `studyCompletionStatus` (enumeration: ongoing, completed_within_year, completed_over_year_ago), `minimumEarningsMultiplier` (decimal - 2.0 for pupils per §77), `educationLevel` (enumeration: basic_secondary, vocational, higher_education) |
| **Impact** | Cannot calculate correct annual earnings for student compensation |

#### Gap #9: Missing RehabilitationAllowance Extension Conditions
| | Details |
| **Law Section** | §69 (Kuntoutusraha) |
| **Missing** | Detailed conditions for rehabilitation allowance extension |
| **Ontology vs Law** | Ontology has `RehabilitationAllowance` with basic duration but missing §69 specifics: 1) First year: full daily allowance regardless of capacity reduction, 2) After first year: full disability pension amount regardless of capacity, 3) If rehabilitation doesn't prevent suitable work: calculated per §56-57 or §63-64, 4) Includes vacation periods per §69.3 |
| **Required Entities/Attributes** | `RehabilitationAllowance` add: `phase` (enumeration: first_year, after_first_year), `calculationBasis` (enumeration: daily_allowance_full, disability_pension_full, partial_capacity_based), `includesVacationPeriods` (boolean), `vacationPeriodStart` (date), `vacationPeriodEnd` (date), `preventsSuitableWork` (boolean) |
| **Impact** | Cannot correctly calculate rehabilitation allowance amounts |

---

### MEDIUM SEVERITY (3 gaps)

#### Gap #10: Missing DailyAllowance WaitingPeriod Entity
| | Details |
| **Law Section** | §56.3 (Odotusaika) |
| **Missing** | Entity for waiting period calculation |
| **Ontology vs Law** | Ontology has `DailyAllowance` with `waitingDays` attribute but lacks structured entity for §56.3 waiting period rules: 1) 3 consecutive days, 2) Starting from accident day, 3) Compensation starts from day 4 |
| **Required Entities/Attributes** | `WaitingPeriod` entity with: `waitingDays` (int - fixed 3), `waitingPeriodStartDate` (date), `waitingPeriodEndDate` (date), `paymentStartDate` (date - day 4), `isConsecutiveDaysRequirementMet` (boolean) |
| **Impact** | Cannot properly calculate when daily allowance payments begin |

#### Gap #11: Missing PreExistingConditionDeterioration Timing
| | Details |
| **Law Section** | §19 (Tapaturman aiheuttama paheneminen), §30 (Ammattitaudista aiheutunut paheneminen) |
| **Missing** | Specific timing constraints for pre-existing condition deterioration |
| **Ontology vs Law** | Ontology has `PreExistingConditionDeterioration` with `duration` but missing §19/§30 specifics: 1) Accident-related: max 6 months from accident (extendable if recovery delayed by treatment/waiting), 2) Occupational disease-related: duration of essential deterioration only |
| **Required Entities/Attributes** | Add to `PreExistingConditionDeterioration`: `deteriorationType` (enumeration: accident_related, occupational_disease_related), `maxDurationMonths` (int - 6 for accident-related), `isExtended` (boolean), `extensionReason` (enumeration: treatment_choice_delay, waiting_delay), `extensionGrantedDate` (date) |
| **Impact** | Cannot correctly limit compensation duration for pre-existing condition deterioration |

#### Gap #12: Missing FuneralExpenses Detailed Attributes
| | Details |
| **Law Section** | §109 (Hautausapu ja vainajan kuljetuskustannukset) |
| **Missing** | Detailed recipient and transportation attributes for funeral expenses |
| **Ontology vs Law** | Ontology has `FuneralExpenses` with basic `amount`, `recipient` but missing §109 specifics: 1) Payment to deceased's estate if funeral costs paid from estate, 2) Otherwise to funeral arrangers up to estate amount, 3) Transportation costs from death location to residence covered |
| **Required Entities/Attributes** | `FuneralExpenses` add: `recipientType` (enumeration: deceased_estate, funeral_arranger), `paymentSource` (enumeration: estate_funds, third_party), `maxPayableAmount` (decimal - limited to estate amount), `transportationCostsCovered` (boolean), `deathLocation` (string), `homeLocality` (string), `transportationCostAmount` (decimal) |
| **Impact** | Cannot correctly determine funeral expenses recipient and amount |

---

## GitHub Issues Created

| Gap | Severity | Issue # | Title |
|-----|----------|---------|-------|
| #1 | CRITICAL | #316 | Missing WorkCapacityAssessment entity - §63 |
| #2 | CRITICAL | #317 | Missing DisabilityClassCombinationRules - §84 |
| #3 | CRITICAL | #318 | Missing PartialWorkCapacity entity - §57, §64 |
| #4 | CRITICAL | #319 | Missing ViolenceDamage exclusion attributes - §34 |
| #5 | HIGH | #320 | Missing PsychologicalShock preconditions - §35 |
| #6 | HIGH | #321 | Missing CommuteAccident specific attributes - §23 |
| #7 | HIGH | #322 | Missing OccupationalDiseaseManifestation entity - §31 |
| #8 | HIGH | #323 | Missing Student special earnings rules - §76, §77 |
| #9 | HIGH | #324 | Missing RehabilitationAllowance extension conditions - §69 |
| #10 | MEDIUM | #325 | Missing WaitingPeriod structured entity - §56.3 |
| #11 | MEDIUM | #326 | Missing PreExistingConditionDeterioration timing - §19, §30 |
| #12 | MEDIUM | #327 | Missing FuneralExpenses detailed attributes - §109 |

---

## Recommendations

### Priority Order for Implementation

1. **Critical Priority**: Issues #316-319 - These affect core compensation calculation and eligibility determination
2. **High Priority**: Issues #320-324 - These affect specific accident types and beneficiary groups  
3. **Medium Priority**: Issues #325-327 - These affect edge cases and administrative details

### Known Issues Still Open (from previous analysis)

- **Issue #276**: Missing WorkCapacityReduction entity - §63 työkyvyn heikentymä
- **Issue #277**: ClaimApplication subtypes missing enumeration values - §128
- **Issue #278**: WorkMotionStrain missing exclusion attributes - §33

---

## Appendix: Coverage Matrix

| Law Chapter | Section | Ontology Coverage | Gap ID |
|-------------|---------|-------------------|--------|
| 5 | §17-25 | Partial | #6 |
| 5 | §19 | Partial | #11 |
| 6 | §26-32 | Partial | #7 |
| 7 | §33 | Missing (known as #278) | #278 |
| 7 | §34 | Partial | #4 |
| 7 | §35 | Partial | #5 |
| 10 | §56 | Partial | #10 |
| 10 | §57, §63-64 | Missing | #1, #3 |
| 10 | §69 | Partial | #9 |
| 10 | §70, §76-77 | Partial | #8 |
| 11 | §83-87 | Partial | #2 |
| 13 | §109 | Partial | #12 |

---

*End of Analysis Report*
