# Car Insurance Dmn Rules DMN Rules

**Version:** 2.5.2
**Total Decisions:** 210

---

## Eligibility Administrative

### AD88_InformationToCentre

- **Description:** Obligation to provide info to Liikennevakuutuskeskus (§88)
- **Legal Source:** Section 88
- **Hit Policy:** COLLECT
- **Output:** obligation_status
- **Inputs:** information.type, timeliness

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| subrogation_info | required | MUST_PROVIDE | Section 88(1) |
| statistics | annual | MUST_PROVIDE | Section 88(2) |

## Eligibility Benefit_Entitlement

### E9_DeathCompensation

- **Description:** Calculate death compensation entitlements
- **Legal Source:** Sections 36-38
- **Hit Policy:** FIRST
- **Output:** compensationType
- **Inputs:** deceased.hasIncome, survivor.relationship, survivor.isDependent

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | Spouse | True | SpousePension_Plus_LumpSum | Section 36(1) |
| True | Child | True | ChildPension | Section 36(2) |
| False | Dependent | True | LumpSum | Section 38 |
| any | Parent | True | FuneralExpenses_Plus_Compensation | Section 38 |

### E10_DisabilityCompensation

- **Description:** Calculate disability compensation
- **Legal Source:** Section 35
- **Hit Policy:** UNIQUE
- **Output:** compensationType
- **Inputs:** injury.permanentDisabilityPercentage, injury.affectsWorkAbility, person.ageAtInjury

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 1-10_PERCENT | True | any | DisabilityPension_Low | Section 35(2) |
| 11-30_PERCENT | True | any | DisabilityPension_Medium | Section 35(2) |
| 31-100_PERCENT | True | any | DisabilityPension_High | Section 35(2) |

## Eligibility Claims_Handling

### CLM006_BoardRecommendationMandatory

- **Description:** MANDATORY board recommendation for certain claims (§66)
- **Legal Source:** Section 66
- **Hit Policy:** FIRST
- **Output:** board_request_required
- **Inputs:** claim.type, injury.severity, decision.changed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| permanent_loss_earnings | any | any | MUST_REQUEST | Section 66(1)1 |
| death_benefit | any | any | MUST_REQUEST | Section 66(1)1 |
| increase_continue_claim | any | any | MUST_REQUEST | Section 66(1)2 |
| severe_disability | any | any | MUST_REQUEST | Section 66(1)3 |

### CLM005_DelayedCompensationSeparated

- **Description:** Delayed compensation - SEPARATED rules (§67)
- **Legal Source:** Section 67
- **Hit Policy:** FIRST
- **Output:** penalty_rule
- **Inputs:** compensation.type, delay.reason, insurer.fault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| personal_injury | any | False | ENHANCED_INTEREST | Section 67(1) |
| property_damage | any | False | STANDARD_INTEREST | Section 67(1) |
| any | claimant_fault | True | NO_PENALTY | Section 67(2) |

## Eligibility Compensation_Calculation

### E5_MedicalExpenseCompensation

- **Description:** Calculate medical expense compensation
- **Legal Source:** Sections 53-59
- **Hit Policy:** FIRST
- **Output:** compensationPercentage
- **Inputs:** medicalExpense.treatmentType, medicalExpense.isNecessary, medicalExpense.providerType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Emergency | True | public | 100_PERCENT | Section 54 |
| Emergency | True | private | 100_PERCENT_REIMBURSEMENT | Section 54 |
| Surgery | True | any | 100_PERCENT | Section 54 |
| Medicines | True | pharmacy | 100_PERCENT | Section 54 |
| Rehabilitation | True | any | 100_PERCENT | Section 54 |
| DentalTreatment | True | any | 100_PERCENT | Section 54 |
| Prosthesis | True | any | 100_PERCENT | Section 54 |
| TravelToTreatment | True | any | 100_PERCENT | Section 54 |

### E6_LostWagesCompensation

- **Description:** Calculate lost wages compensation
- **Legal Source:** Section 34
- **Hit Policy:** UNIQUE
- **Output:** compensationAmount
- **Inputs:** person.incomeType, person.netMonthlyIncome, person.annualIncome, injury.workAbilityLostDays

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Employed | any | None | any | Calculate_NetMonthly_DividedBy30_MultipliedByDays | Section 34(1) |
| SelfEmployed | None | any | any | Calculate_AnnualDividedBy365_MultipliedByDays | Section 34(2) |
| Unemployed | any | None | any | Minimum_36_90_PerDay | Section 34(3) |
| Student | any | None | any | StudentGrant_Adjustment | Section 34(4) |

### E7_PainAndSufferingCompensation

- **Description:** Calculate pain and suffering compensation
- **Legal Source:** Section 35
- **Hit Policy:** UNIQUE
- **Output:** compensationAmount
- **Inputs:** injury.isPermanent, injury.permanentDisabilityPercentage, painSuffering.level

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | 1-10_PERCENT | moderate | Scale_1_10_Percent | Section 35(2) |
| True | 11-20_PERCENT | moderate | Scale_11_20_Percent | Section 35(2) |
| True | 21-50_PERCENT | significant | Scale_21_50_Percent | Section 35(2) |
| True | 51-100_PERCENT | severe | Scale_51_100_Percent | Section 35(2) |
| False | None | any | TemporaryPain_Scale | Section 35(1) |

### E8_PropertyDamageCompensation

- **Description:** Calculate property damage compensation
- **Legal Source:** Section 3
- **Hit Policy:** UNIQUE
- **Output:** compensationAmount
- **Inputs:** property.type, property.marketValue, damage.severity

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Vehicle | any | TotalLoss | MarketValue | Section 3(1) |
| Vehicle | any | PartialDamage | RepairCost | Section 3(1) |
| ThirdPartyProperty | any | any | ActualValue | Section 3(1) |
| Clothing | any | any | ReplacementValue | Section 3(2) |

### E8b_MultiVehicleLiability

- **Description:** Liability in multi-vehicle accidents (§33)
- **Legal Source:** Section 33
- **Hit Policy:** FIRST
- **Output:** liability_allocation
- **Inputs:** accident.vehicleCount, vehicleA.fault, vehicleB.fault, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 2 | no_fault | sole_fault | any | VehicleB_Sole_Liable | Section 33(1) |
| 2 | shared | shared | any | Shared_Liability | Section 33(2) |
| 2 | any | any | PersonalInjury | Passenger_Vehicle_Liable | Section 33(3) |

### E8c_VehicleCombinationLiability

- **Description:** Liability for vehicle combinations (§39a)
- **Legal Source:** Section 39a
- **Hit Policy:** FIRST
- **Output:** liable_insurer
- **Inputs:** vehicle.isCombination, vehicle.towingIdentified, damage.exceedsMaximum

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | False | Towing_Vehicle_Insurer | Section 39a(1) |
| True | False | False | Trailer_Insurer | Section 39a(2) |
| True | any | True | Excess_From_Other | Section 39a(3) |

### E8d_WorkAccidentCoordination

- **Description:** Coordination with occupational accident (§36)
- **Legal Source:** Section 36
- **Hit Policy:** FIRST
- **Output:** primary_insurer
- **Inputs:** injured.hasOccupationalInsurance, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | PersonalInjury | Occupational_First | Section 36 |
| False | PersonalInjury | Traffic_Insurance_Full | Section 36 |

### E14_MaximumPropertyDamage

- **Description:** Maximum property damage compensation (§38)
- **Legal Source:** Section 38
- **Hit Policy:** UNIQUE
- **Output:** compensation_cap
- **Inputs:** propertyDamage.amount, claimant.count

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=5000000 | 1 | MAX_5000000 | Section 38(1) |
| >=5000000 | >1 | Proportional | Section 38(2) |
| <5000000 | any | Full_Compensation | Section 38(1) |

### E15_InsurerLiabilityDistribution

- **Description:** Distribution of liability between insurers (§51)
- **Legal Source:** Section 51
- **Hit Policy:** FIRST
- **Output:** liability_share
- **Inputs:** multipleInsurers, cause.specificVehicle, fault.distribution

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | none | shared | Joint_Several_Proportional | Section 51(1) |
| True | identified | sole | Specific_Vehicle_Sole | Section 51(2) |
| True | any | any | Investigate | Section 51 |

### E8e_IndexAdjustment

- **Description:** Index adjustment of continuous compensations (§35)
- **Legal Source:** Section 35
- **Hit Policy:** UNIQUE
- **Output:** adjusted_amount
- **Inputs:** compensation.type, compensation.amount, year

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| continuous | any | any | Adjusted_By_WorkPensionIndex | Section 35(1) |

### E15b_RailTrafficLiability

- **Description:** Division with rail traffic liability (§52)
- **Legal Source:** Section 52
- **Hit Policy:** FIRST
- **Output:** liability_division
- **Inputs:** accident.involvesRailVehicle, fault.rail, fault.road

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | sole | no_fault | RailTraffic_Fully_Liable | Section 52(1) |
| True | shared | shared | Proportional_Division | Section 52(1) |
| True | no_fault | sole | RoadTraffic_Fully_Liable | Section 52(1) |

### E19_TravelCosts

- **Description:** Travel costs compensation (§59)
- **Legal Source:** Section 59
- **Hit Policy:** FIRST
- **Output:** compensation_amount
- **Inputs:** travel.reason, travel.distance, travel.mode

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| medical_appointment | any | any | COVERED_Kela_Rate | Section 59 |

### E22_AdvancePayment

- **Description:** Advance payment (§63)
- **Legal Source:** Section 63
- **Hit Policy:** FIRST
- **Output:** advance_eligibility
- **Inputs:** damage.likely, claim.amount_estimated, injury.severity

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | severe | Advance_Payment_Required | Section 63(1) |
| True | any | moderate | Advance_Payment_Consider | Section 63(2) |
| False | any | any | No_Advance | Section 63 |

### E60_DamageRegardlessTort

- **Description:** Compensation regardless of tort liability (§31)
- **Legal Source:** Section 31
- **Hit Policy:** UNIQUE
- **Output:** compensation_basis
- **Inputs:** accident.occurred, vehicle.insured, tort.liable

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | any | Strict_Liability | Section 31 |

### E61_LiabilityForTrafficDamage

- **Description:** Liability for traffic damage (§32)
- **Legal Source:** Section 32
- **Hit Policy:** FIRST
- **Output:** liability_status
- **Inputs:** policy.active, accident.date

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | within_term | Insurer_Liable | Section 32(1) |

### E62_MedicalConditions

- **Description:** Conditions for medical care compensation (§53)
- **Legal Source:** Section 53
- **Hit Policy:** FIRST
- **Output:** compensation_eligibility
- **Inputs:** care.necessary, care.provider.approved

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Medical_Care_Covered | Section 53 |

### E67_PersonalInjuryCompensation

- **Description:** Personal injury compensation basis (§34)
- **Legal Source:** Section 34
- **Hit Policy:** UNIQUE
- **Output:** compensation_basis
- **Inputs:** injury.type, basis.law

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| any | vahingonkorvauslaki | Based_On_Law | Section 34 |

### E68_PropertyDamageBasis

- **Description:** Property damage compensation basis (§37)
- **Legal Source:** Section 37
- **Hit Policy:** FIRST
- **Output:** compensation_method
- **Inputs:** property.damaged, repair.possible

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| vehicle | True | Repair_Cost | Section 37(2) |
| vehicle | False | Market_Value | Section 37(3) |

### E87_VehicleToRailLiability

- **Description:** Liability when vehicle hits rail (§33)
- **Legal Source:** Section 33
- **Hit Policy:** FIRST
- **Output:** liability_rule
- **Inputs:** other_vehicle.rail, fault.road

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | no_fault | Road_Not_Liable | Section 33(1) |
| True | fault | Rail_Insurer_Full | Section 33(3) |

### E88_LossOfEarnings

- **Description:** Loss of earnings calculation (§34)
- **Legal Source:** Section 34
- **Hit Policy:** UNIQUE
- **Output:** compensation_calculation
- **Inputs:** income.type, income.amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| employed | net_monthly | Net_Monthly_30_Days | Section 34(1) |
| self_employed | annual | Annual_365_Days | Section 34(2) |
| unemployed | any | Minimum_36_90_Day | Section 34(3) |

### E89_IndexAdjustment

- **Description:** Index adjustment calculation (§35)
- **Legal Source:** Section 35
- **Hit Policy:** UNIQUE
- **Output:** indexed_amount
- **Inputs:** compensation.type, current_amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| continuous | amount | Adjusted_By_WorkPensionIndex | Section 35(1) |

### E90_PropertyDamageCalculation

- **Description:** Property damage calculation (§37)
- **Legal Source:** Section 37
- **Hit Policy:** FIRST
- **Output:** compensation_method
- **Inputs:** property.type, repair.possible, total_loss

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| vehicle | True | False | Repair_Cost | Section 37(2) |
| vehicle | False | True | Market_Value | Section 37(3) |

### E91_MaximumDetails

- **Description:** Maximum property damage (§38)
- **Legal Source:** Section 38
- **Hit Policy:** FIRST
- **Output:** cap_application
- **Inputs:** damage.amount, claimants.number

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=5000000 | 1 | MAX_5000000 | Section 38(1) |
| >=5000000 | >1 | Proportional | Section 38(2) |

### E92_CombinationLiabilityDetails

- **Description:** Vehicle combination liability details (§39a)
- **Legal Source:** Section 39a
- **Hit Policy:** FIRST
- **Output:** liability_details
- **Inputs:** combination.towing_identified, combination.trailer_identified, damage.exceeds_max

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | False | Towing_Insurer | Section 39a(1) |
| False | True | False | Trailer_Insurer | Section 39a(2) |
| any | any | True | Excess_From_Other | Section 39a(3) |

### E94_LiabilityDistributionDetails

- **Description:** Liability distribution details (§51)
- **Legal Source:** Section 51
- **Hit Policy:** FIRST
- **Output:** distribution_rule
- **Inputs:** insurers.multiple, fault.distribution, cause.specific

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | shared | none | JOINT_SEVERAL | Section 51(1) |
| True | no_fault | identified | SPECIFIC_SOLE | Section 51(2) |

### E95_RailLiabilityDivision

- **Description:** Rail liability division (§52)
- **Legal Source:** Section 52
- **Hit Policy:** FIRST
- **Output:** division_rule
- **Inputs:** accident.involves_rail, fault.rail, fault.road

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | sole | no_fault | RAIL_SOLE | Section 52(1) |
| True | shared | shared | PROPORTIONAL | Section 52(1) |
| True | no_fault | sole | ROAD_SOLE | Section 52(1) |

### E96_MedicalCareConditions

- **Description:** Medical care conditions (§53)
- **Legal Source:** Section 53
- **Hit Policy:** FIRST
- **Output:** coverage_eligibility
- **Inputs:** care.necessary, care.provider.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | public | COVERED | Section 53 |
| True | private | COVERED_REIMBURSABLE | Section 53 |

### E97_PublicHealthcareCosts

- **Description:** Public healthcare costs (§54)
- **Legal Source:** Section 54
- **Hit Policy:** UNIQUE
- **Output:** cost_coverage
- **Inputs:** care.type, patient.fee

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| any | patient_fee | PATIENT_FEE_COVERED | Section 54 |

### E98_FullCostPayment

- **Description:** Full cost payment (§55)
- **Legal Source:** Section 55
- **Hit Policy:** UNIQUE
- **Output:** payment_type
- **Inputs:** care.provided, authority.reported

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | FULL_COST | Section 55(1) |

### E99_MedicineCosts

- **Description:** Medicine costs (§58)
- **Legal Source:** Section 58
- **Hit Policy:** UNIQUE
- **Output:** cost_coverage
- **Inputs:** medicine.prescribed, pharmacy.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | COVERED | Section 58 |

### E116_DisabilityPercentage

- **Description:** Disability compensation percentage (§35)
- **Legal Source:** Section 35
- **Hit Policy:** UNIQUE
- **Output:** compensation_type
- **Inputs:** disability.percentage, affects_work

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 1-10 | True | LOW_DISABILITY | Section 35(2) |
| 11-30 | True | MEDIUM_DISABILITY | Section 35(2) |
| 31-100 | True | HIGH_DISABILITY | Section 35(2) |

### E117_DeathCompensationType

- **Description:** Death compensation types (§36-38)
- **Legal Source:** Sections 36-38
- **Hit Policy:** FIRST
- **Output:** compensation_type
- **Inputs:** survivor.relationship, deceased.income, survivor.dependent

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| spouse | True | True | SPOUSE_PENSION_LUMP | Section 36(1) |
| child | any | True | CHILD_PENSION | Section 36(2) |
| dependent | False | True | LUMP_SUM | Section 38 |

### E118_WorkAccidentCoordination

- **Description:** Work accident coordination details (§36)
- **Legal Source:** Section 36
- **Hit Policy:** FIRST
- **Output:** coordination_rule
- **Inputs:** has_work_insurance, injury.type, owner.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | personal | any | WORK_INSURANCE_FIRST | Section 36 |
| False | personal | any | TRAFFIC_INSURANCE_ONLY | Section 36 |

### E137_StrictLiability

- **Description:** Strict liability principle (§31)
- **Legal Source:** Section 31
- **Hit Policy:** UNIQUE
- **Output:** liability_basis
- **Inputs:** accident.occurred, vehicle.insured, driver.fault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | any | STRICT_LIABILITY | Section 31 |

### E138_InsurerLiabilityPeriod

- **Description:** Insurer liability period (§32)
- **Legal Source:** Section 32
- **Hit Policy:** UNIQUE
- **Output:** liability_status
- **Inputs:** policy.active, accident.date

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | within_term | INSURER_LIABLE | Section 32(1) |

### E139_WorkAccidentTypes

- **Description:** Work accident act types (§36)
- **Legal Source:** Section 36
- **Hit Policy:** COLLECT
- **Output:** coordination_type
- **Inputs:** injured.occupation, insurance.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| employee | tya | TYA_COORDINATION | Section 36 |
| farmer | myela | MYELA_COORDINATION | Section 36 |
| athlete | sport | SPORT_COORDINATION | Section 36 |

### E140_AssistingInjuredCompensation

- **Description:** Assisting injured compensation (§39)
- **Legal Source:** Section 39
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** person.assisting, person.is_professional, damage.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | any | COVERED | Section 39(1) |
| True | True | any | NOT_COVERED | Section 39(2) |

### E141_MedicalCarePublicConditions

- **Description:** Medical care public conditions (§53)
- **Legal Source:** Section 53
- **Hit Policy:** COLLECT
- **Output:** coverage_eligibility
- **Inputs:** care.provider.public, care.necessary, social_security

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | COVERED_PUBLIC | Section 53 |

### E142_HealthcareProviderTypes

- **Description:** Healthcare provider types (§54)
- **Legal Source:** Section 54
- **Hit Policy:** COLLECT
- **Output:** reimbursement_rate
- **Inputs:** provider.type, service.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| municipal | healthcare | CUSTOMER_FEE_ONLY | Section 54(1) |
| private | healthcare | REFUNDABLE | Section 54 |

### E161_AnimalDamage

- **Description:** Animal damage compensation (§37)
- **Legal Source:** Section 37
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** animal.type, animal.supervised, driver.fault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| pet | False | any | NOT_COVERED | Section 37(4) |
| wild_animal | no_fault | COVERED | Section 37(4) |

### E162_TheftGuaranteeFund

- **Description:** Theft - Guarantee Fund coverage (§41)
- **Legal Source:** Section 41
- **Hit Policy:** UNIQUE
- **Output:** fund_coverage
- **Inputs:** theft.terminated_policy, damage.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | personal | GUARANTEE_FUND_PAYS | Section 41(2) |
| True | property | NOT_COVERED | Section 41(1) |

### CC33_VehicleToVehicleLiability

- **Description:** Liability in two or more vehicle accidents (§33)
- **Legal Source:** Section 33
- **Hit Policy:** FIRST
- **Output:** liability_rule
- **Inputs:** accident.vehicles, fault.determined, victim.vehicle

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| two_vehicles | first_vehicle_fault | second_vehicle | NOT_COVERED_BY_FIRST | Section 33(1) |
| two_vehicles | second_vehicle_fault | first_vehicle | NOT_COVERED_BY_SECOND | Section 33(1) |
| two_vehicles | both_fault | any | SHARED_LIABILITY | Section 33(2) |
| rail_involved | any | any | RAIL_INSURER_PAYS | Section 33(3) |

### CC39_RescuerCompensation

- **Description:** Compensation for helping injured persons (§39)
- **Legal Source:** Section 39
- **Hit Policy:** FIRST
- **Output:** coverage_eligibility
- **Inputs:** person.helped, helper.is_professional, damage.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | personal | COVERED | Section 39(1) |
| True | False | property | COVERED | Section 39(1) |
| True | True | any | NOT_COVERED | Section 39(2) |

## Eligibility Coverage_Determination

### E1_VehicleInsuranceRequirement

- **Description:** Determine if vehicle requires mandatory traffic insurance
- **Legal Source:** Section 5
- **Hit Policy:** UNIQUE
- **Output:** insuranceRequirement
- **Inputs:** vehicle.registrationCountry, vehicle.requiresInsurance, vehicle.vehicleType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| FI | True | MotorVehicle | MandatoryTrafficInsurance | Section 5(1) |
| FI | True | Trailer | MandatoryTrafficInsurance | Section 5(1) |
| EEA | True | any | CheckRegistrationCountry | Section 6a |
| Non-EEA | True | any | MandatoryTrafficInsurance | Section 5(1) |

### E2_DamageCoverage

- **Description:** Determine what damage types are covered
- **Legal Source:** Section 31
- **Hit Policy:** COLLECT
- **Output:** coverageStatus
- **Inputs:** damage.damageType, damage.isPersonalInjury, damage.isPropertyDamage

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PersonalInjury | True | False | COVERED_100 | Section 12(1) |
| PersonalInjury | True | True | COVERED_100 | Section 12(1) |
| PropertyDamage | False | True | COVERED_100 | Section 12(1) |
| VehicleDamage | False | True | COVERED_100 | Section 12(1) |
| EnvironmentalDamage | False | True | COVERED_100 | Section 12(2) |

### E3_InternationalCoverage

- **Description:** Determine international coverage scope
- **Legal Source:** Sections 10-11
- **Hit Policy:** FIRST
- **Output:** internationalCoverage
- **Inputs:** accident.locationCountry, greenCard.valid, vehicle.registeredCountry

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Finland | any | FI | FullCoverage | Section 10(1) |
| EEA | True | any | FullCoverage_GreenCard | Section 10(2) |
| EEA | False | any | LimitedCoverage_BureauGuarantee | Section 10(3) |
| Non-EEA | any | any | CheckBilateralAgreement | Section 11 |

### E4_InsuranceObligationLiableParty

- **Description:** Determine who is liable for insurance obligation
- **Legal Source:** Section 6
- **Hit Policy:** FIRST
- **Output:** liableParty
- **Inputs:** person.owner.exists, person.holder.exists, vehicle.ownershipTransferred

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | OwnerAndHolderJointlyLiable | Section 6(1) |
| True | False | True | OwnerLiable | Section 6(1) |
| False | True | True | HolderLiable | Section 6(1) |
| True | False | False | OwnerLiableFromOwnership | Section 6(2) |

### E16_BorderTrafficInsurance

- **Description:** Border traffic insurance (§7)
- **Legal Source:** Section 7
- **Hit Policy:** FIRST
- **Output:** insurance_requirement
- **Inputs:** vehicle.permanentLocation, vehicle.hasGreenCard, accident.location

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Non-EEA | False | Finland | Border_Insurance_Required | Section 7(1) |
| Non-EEA | True | any | GreenCard_Accepted | Section 7(2) |
| Non-EEA | False | ['Sweden', 'Norway'] | Covered_Injury_Only | Section 7(3) |

### E17_HealthUnitReporting

- **Description:** Public health unit reporting obligation (§56)
- **Legal Source:** Section 56
- **Hit Policy:** FIRST
- **Output:** reporting_status
- **Inputs:** healthUnit.reported, patientInfo.provided, timeliness

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | timely | Reporting_Complete | Section 56 |
| True | False | any | Reporting_Incomplete | Section 56 |
| False | any | any | Reporting_Missing | Section 56 |

### E18_InsurerFacilityChoice

- **Description:** Insurer right to direct to facility (§57)
- **Legal Source:** Section 57
- **Hit Policy:** FIRST
- **Output:** authorization
- **Inputs:** insurer.authorization, facility.approved, treatment.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | planned_treatment | Authorization_Granted | Section 57 |
| False | any | any | No_Authorization_Required | Section 57 |

### E20_ClaimRightToCompensation

- **Description:** Right to compensation and claims procedure (§60)
- **Legal Source:** Section 60
- **Hit Policy:** FIRST
- **Output:** claim_status
- **Inputs:** claim.filed, claim.documentation, damage.verified

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | complete | True | Claim_Accepted | Section 60 |
| True | incomplete | any | Additional_Info_Required | Section 60 |
| True | complete | False | Claim_Denied | Section 60 |

### E23_Subrogation

- **Description:** Subrogation to injured party's rights (§68)
- **Legal Source:** Section 68
- **Hit Policy:** FIRST
- **Output:** subrogation_right
- **Inputs:** insurer.paid, third_party.liable, recovery.possible

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | Subrogation_Exercise | Section 68(1) |
| True | False | any | No_Subrogation | Section 68 |

### E27_DrivingSchoolVehicles

- **Description:** Driving school vehicles (§89)
- **Legal Source:** Section 89
- **Hit Policy:** FIRST
- **Output:** insurance_requirement
- **Inputs:** vehicle.type, drivingSchool.licensed, instruction.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| DrivingSchool | True | instruction | Special_Coverage | Section 89 |
| any | any | any | Standard_Coverage | Section 5 |

### E31_RecoveryFromThirdParty

- **Description:** Recovery from liable third party (§66)
- **Legal Source:** Section 66
- **Hit Policy:** FIRST
- **Output:** recovery_right
- **Inputs:** insurer.paid, thirdParty.liable

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Recovery_Possible | Section 66 |

### E32_RecoveryFromClaimant

- **Description:** Recovery from policyholder or injured (§67)
- **Legal Source:** Section 67
- **Hit Policy:** FIRST
- **Output:** recovery_right
- **Inputs:** fraud.determined, misrepresentation.found

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | Full_Recovery | Section 67 |

### E33_ClaimsHandlingCosts

- **Description:** Cost of claims handling (§69)
- **Legal Source:** Section 69
- **Hit Policy:** UNIQUE
- **Output:** cost_bearer
- **Inputs:** claim.processing.required

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | Insurer_Bears_Cost | Section 69 |

### E34_GuaranteeFundRecourse

- **Description:** Right of recourse to guarantee fund (§79)
- **Legal Source:** Section 79
- **Hit Policy:** FIRST
- **Output:** recourse_right
- **Inputs:** fund.paid, liable.party

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | identified | Recourse_Exercised | Section 79 |

### E35_VictimFinancialSupport

- **Description:** Financial support for victim (§82)
- **Legal Source:** Section 82
- **Hit Policy:** FIRST
- **Output:** support_eligibility
- **Inputs:** victim.financialHardship, compensation.delayed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Interim_Support | Section 82 |

### E36_Supervision

- **Description:** Supervision (§75)
- **Legal Source:** Section 75
- **Hit Policy:** UNIQUE
- **Output:** supervision_status
- **Inputs:** insurer.licensed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | Under_Supervision | Section 75 |

### E37_InsuranceRegister

- **Description:** Register of traffic insurance (§76)
- **Legal Source:** Section 76
- **Hit Policy:** UNIQUE
- **Output:** register_status
- **Inputs:** vehicle.registered, insurance.active

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Registered_Active | Section 76 |

### E38_MedicalExamination

- **Description:** Medical examination obligation (§72)
- **Legal Source:** Section 72
- **Hit Policy:** FIRST
- **Output:** examination_status
- **Inputs:** injury.personal, examination.completed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | Examination_Required | Section 72(1) |

### E39_InsuranceMediator

- **Description:** Insurance mediator (§70)
- **Legal Source:** Section 70
- **Hit Policy:** FIRST
- **Output:** mediation_status
- **Inputs:** claim.disputed, mediator.used

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Mediation_Used | Section 70 |

### E40_ClaimApplication

- **Description:** Application for compensation (§61)
- **Legal Source:** Section 61
- **Hit Policy:** FIRST
- **Output:** application_status
- **Inputs:** application.submitted, documentation.complete

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Application_Accepted | Section 61 |
| True | False | Additional_Docs_Required | Section 61 |

### E41_ClaimPayment

- **Description:** Payment of compensation (§62a)
- **Legal Source:** Section 62a
- **Hit Policy:** UNIQUE
- **Output:** payment_status
- **Inputs:** decision.issued, payment.method

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | bank_transfer | Payment_Processing | Section 62a |

### E42_RightToInformation

- **Description:** Right to information (§64)
- **Legal Source:** Section 64
- **Hit Policy:** FIRST
- **Output:** information_status
- **Inputs:** information.requested, claim.related

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Information_Provided | Section 64 |

### E43_ObligationToInvestigate

- **Description:** Obligation to provide information and investigate (§65)
- **Legal Source:** Section 65
- **Hit Policy:** FIRST
- **Output:** investigation_status
- **Inputs:** investigation.completed, evidence.gathered

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Investigation_Complete | Section 65 |

### E44_AppealToInsuranceCourt

- **Description:** Appeal to Insurance Court (§85)
- **Legal Source:** Section 85
- **Hit Policy:** FIRST
- **Output:** appeal_status
- **Inputs:** decision.appealed, appeal.filed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Appeal_Accepted | Section 85 |

### E45_AppealProcedure

- **Description:** Appeal procedure (§86)
- **Legal Source:** Section 86
- **Hit Policy:** UNIQUE
- **Output:** procedure_status
- **Inputs:** appeal.submitted, deadline.met

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Procedure_Followed | Section 86 |

### E46_EuropeanSmallClaims

- **Description:** European small claims procedure (§87)
- **Legal Source:** Section 87
- **Hit Policy:** FIRST
- **Output:** procedure_eligibility
- **Inputs:** claim.value, eu_member

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| <5000 | True | Small_Claims_Available | Section 87 |

### E47_ServiceOfDocuments

- **Description:** Service of documents (§80)
- **Legal Source:** Section 80
- **Hit Policy:** UNIQUE
- **Output:** service_method
- **Inputs:** document.type, recipient.located

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| legal | True | Service_Completed | Section 80 |

### E48_InternationalExchange

- **Description:** Information exchange with other countries (§83)
- **Legal Source:** Section 83
- **Hit Policy:** FIRST
- **Output:** exchange_status
- **Inputs:** request.country, data.exchanged

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EEA | True | Data_Exchanged | Section 83 |

### E49_VehicleRecords

- **Description:** Vehicle records (§92)
- **Legal Source:** Section 92
- **Hit Policy:** UNIQUE
- **Output:** record_status
- **Inputs:** register.maintained, vehicle.registered

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Records_Complete | Section 92 |

### E50_NotificationRegistration

- **Description:** Notification of vehicle registration (§93)
- **Legal Source:** Section 93
- **Hit Policy:** FIRST
- **Output:** notification_status
- **Inputs:** registration.notified, authority.received

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Notification_Complete | Section 93 |

### E51_VehicleInTraffic

- **Description:** Scope - what constitutes traffic (§1)
- **Legal Source:** Section 1
- **Hit Policy:** FIRST
- **Output:** traffic_determination
- **Inputs:** vehicle.location, vehicle.purpose, road_type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| road | transportation | public | In_Traffic | Section 1 |
| private_area | other | any | Not_In_Traffic | Section 1 |

### E52_VehicleIdentification

- **Description:** Vehicle identification in insurance contract (§10)
- **Legal Source:** Section 10
- **Hit Policy:** FIRST
- **Output:** identification_status
- **Inputs:** vehicle.identified, registration.match

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Properly_Identified | Section 10 |

### E53_InsuranceDocument

- **Description:** Insurance document and terms (§11)
- **Legal Source:** Section 11
- **Hit Policy:** FIRST
- **Output:** document_status
- **Inputs:** document.provided, terms.accepted

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Document_Provided | Section 11 |

### E54_InsuranceValidityPeriod

- **Description:** Insurance validity period (§12)
- **Legal Source:** Section 12
- **Hit Policy:** UNIQUE
- **Output:** validity_period
- **Inputs:** policy.startDate, policy.endDate, policy.terminated

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| set | future | False | Valid_Period | Section 12 |

### E55_BreachOfDutyToInform

- **Description:** Breach of duty to inform (§14)
- **Legal Source:** Section 14
- **Hit Policy:** FIRST
- **Output:** remedy
- **Inputs:** information.withheld, intentional, premium.affected

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | Retroactive_Premium | Section 14(1) |

### E56_IncreasedRiskNotification

- **Description:** Failure to notify increased risk (§15)
- **Legal Source:** Section 15
- **Hit Policy:** FIRST
- **Output:** premium_adjustment
- **Inputs:** risk.increased, notification.made, premium.impact

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | True | Retroactive_Increase | Section 15 |

### E57_CancellationRight

- **Description:** Right to cancel insurance (§16)
- **Legal Source:** Section 16
- **Hit Policy:** FIRST
- **Output:** cancellation_allowed
- **Inputs:** cancellation.requested, newInsurance.exists, theft.reported

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | any | Cancellation_Approved | Section 16(1) |
| True | False | True | Cancellation_Approved_Theft | Section 16(1) |

### E58_OwnerHolderChange

- **Description:** Change of owner or holder (§18)
- **Legal Source:** Section 18
- **Hit Policy:** FIRST
- **Output:** liability_status
- **Inputs:** ownership.transferred, insurance.transferred, days.within7

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | True | Original_Insurance_Covers | Section 18 |

### E59_DamageHistoryTransfer

- **Description:** Transfer of damage history to another insurer (§21)
- **Legal Source:** Section 21
- **Hit Policy:** FIRST
- **Output:** transfer_status
- **Inputs:** policy.transferred, history.available, transfer.requested

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | History_Transferred | Section 21 |

### E69_AuthorityRegulations

- **Description:** Authority to issue regulations (§81)
- **Legal Source:** Section 81
- **Hit Policy:** UNIQUE
- **Output:** regulation_status
- **Inputs:** authority.empowered, regulation.issued

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Regulation_In_Force | Section 81 |

### E70_IntlTransportVehicles

- **Description:** Vehicles in international transport (§90)
- **Legal Source:** Section 90
- **Hit Policy:** FIRST
- **Output:** coverage_type
- **Inputs:** vehicle.intlTransport, permit.valid

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | International_Coverage | Section 90 |

### E71_DocumentationRequirements

- **Description:** Insurance documentation requirements (§91)
- **Legal Source:** Section 91
- **Hit Policy:** UNIQUE
- **Output:** compliance_status
- **Inputs:** documentation.maintained, requirements.met

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Requirements_Met | Section 91 |

### E72_MilitaryVehicles

- **Description:** Military vehicles (§91a)
- **Legal Source:** Section 91a
- **Hit Policy:** FIRST
- **Output:** coverage_status
- **Inputs:** vehicle.military, vehicle.insured

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | Exempt_Military | Section 91a |
| True | True | Covered | Section 91a |

### E73_Penalties

- **Description:** Penalties (§94)
- **Legal Source:** Section 94
- **Hit Policy:** UNIQUE
- **Output:** penalty_status
- **Inputs:** offense.type, penalty.imposed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| no_insurance | any | Penalty_Applies | Section 94 |

### E74_ProcessingClaims

- **Description:** Special provisions on processing claims (§73)
- **Legal Source:** Section 73
- **Hit Policy:** UNIQUE
- **Output:** processing_method
- **Inputs:** claim.special, processing.special

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Special_Processing | Section 73 |

### E75_IntlAgreements

- **Description:** International agreements (§78)
- **Legal Source:** Section 78
- **Hit Policy:** FIRST
- **Output:** agreement_status
- **Inputs:** agreement.applies, country.party

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Agreement_Applies | Section 78 |

### E76_PrivateContracts

- **Description:** Private law contracts (§95)
- **Legal Source:** Section 95
- **Hit Policy:** UNIQUE
- **Output:** contract_status
- **Inputs:** contract.type, law.applicable

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| private | finland | Finnish_Law | Section 95 |

### E77_NotInTraffic_Situations

- **Description:** Situations NOT in traffic (§1)
- **Legal Source:** Section 1
- **Hit Policy:** COLLECT
- **Output:** traffic_status
- **Inputs:** vehicle.location, activity.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| construction_site | other_purpose | NOT_IN_TRAFFIC | Section 1(1) |
| repair_facility | maintenance | NOT_IN_TRAFFIC | Section 1(2) |

### E78_VehiclesExempt

- **Description:** Vehicles exempt from insurance (§8)
- **Legal Source:** Section 8
- **Hit Policy:** COLLECT
- **Output:** exemption_status
- **Inputs:** vehicle.type, vehicle.speed, vehicle.purpose

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| tractor | <15_kmh | agricultural | EXEMPT | Section 8(1) |
| trailer | not_registered | any | EXEMPT | Section 8(3) |

### E79_CoverageEEA

- **Description:** Coverage in EEA (§13)
- **Legal Source:** Section 13
- **Hit Policy:** COLLECT
- **Output:** coverage_scope
- **Inputs:** country, green_card, victim.residence

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EEA | True | any | Full_Coverage | Section 13(1) |
| EEA | False | Finnish | Finnish_Law_Option | Section 13(4) |

### E82_OwnershipTransferCoverage

- **Description:** Coverage during ownership transfer (§18)
- **Legal Source:** Section 18
- **Hit Policy:** FIRST
- **Output:** coverage_during_transfer
- **Inputs:** transfer.date, new_insurance.date, days_elapsed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| date | None | <=7 | Old_Policy_Covers_7_Days | Section 18(1) |
| date | date | >7 | New_Policy_Required | Section 18 |

### E100_RightToCompensation

- **Description:** Right to compensation details (§60)
- **Legal Source:** Section 60
- **Hit Policy:** FIRST
- **Output:** right_status
- **Inputs:** claim.submitted, damage.proven, liability.established

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | RIGHT_ESTABLISHED | Section 60 |
| True | False | any | RIGHT_NOT_ESTABLISHED | Section 60 |

### E101_ClaimApplicationDetails

- **Description:** Claim application details (§61)
- **Legal Source:** Section 61
- **Hit Policy:** FIRST
- **Output:** application_status
- **Inputs:** application.form, documentation, timeliness

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| complete | complete | timely | ACCEPTED | Section 61 |
| incomplete | any | any | ADDITIONAL_NEEDED | Section 61 |

### E103_AdvancePaymentDetails

- **Description:** Advance payment details (§63)
- **Legal Source:** Section 63
- **Hit Policy:** FIRST
- **Output:** advance_eligibility
- **Inputs:** damage.likely, injury.severity, claim.amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | severe | any | ADVANCE_MANDATORY | Section 63(1) |
| True | moderate | estimated |  | Section 63(2) |

### E104_InvestigationObligation

- **Description:** Investigation obligation (§65)
- **Legal Source:** Section 65
- **Hit Policy:** UNIQUE
- **Output:** investigation_status
- **Inputs:** investigation.completed, evidence.gathered

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | INVESTIGATION_COMPLETE | Section 65 |

### E105_RecoveryDetails

- **Description:** Recovery from third party details (§66)
- **Legal Source:** Section 66
- **Hit Policy:** FIRST
- **Output:** recovery_rule
- **Inputs:** insurer.paid, third_party.liable, third_party.asset

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | RECOVERY_EXERCISED | Section 66(1) |
| True | True | False | RECOVERY_NOT_POSSIBLE | Section 66 |

### E106_SubrogationDetails

- **Description:** Subrogation details (§68)
- **Legal Source:** Section 68
- **Hit Policy:** FIRST
- **Output:** subrogation_rule
- **Inputs:** insurer.paid, third_party.responsible, recovery.possible

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | SUBROGATION_EXERCISED | Section 68(1) |

### E107_CostsHandling

- **Description:** Costs of claims handling (§69)
- **Legal Source:** Section 69
- **Hit Policy:** UNIQUE
- **Output:** cost_bearer
- **Inputs:** handling.costs, claim.processed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| reasonable | True | INSURER_BEARS | Section 69 |

### E108_InsolvencyProtection

- **Description:** Insolvency protection details (§77)
- **Legal Source:** Section 77
- **Hit Policy:** FIRST
- **Output:** protection_mechanism
- **Inputs:** insurer.insolvent, policy.active, claim.pending

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | GUARANTEE_FUND | Section 77(1) |
| True | True | False | TRANSFER_TO_ANOTHER | Section 77(2) |

### E109_InsuranceCourtAppeal

- **Description:** Appeal to Insurance Court (§85)
- **Legal Source:** Section 85
- **Hit Policy:** FIRST
- **Output:** appeal_status
- **Inputs:** decision.appealable, appeal.filed, deadline.met

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | APPEAL_ACCEPTED | Section 85 |

### E119_ClaimFiling

- **Description:** Who can file claim (§60)
- **Legal Source:** Section 60
- **Hit Policy:** COLLECT
- **Output:** filing_right
- **Inputs:** claimant.relationship, claimant.legal_capacity

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| injured | True | CAN_FILE | Section 60 |
| representative | True | CAN_FILE_VIA | Section 60 |
| heir | True | CAN_FILE_HEIR | Section 60 |

### E120_DecisionContent

- **Description:** Decision content requirements (§62)
- **Legal Source:** Section 62
- **Hit Policy:** COLLECT
- **Output:** decision_validity
- **Inputs:** decision.includes, decision.amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| reasoning_amount | specified | VALID_DECISION | Section 62 |

### E121_PaymentMethod

- **Description:** Payment method (§62a)
- **Legal Source:** Section 62a
- **Hit Policy:** UNIQUE
- **Output:** payment_execution
- **Inputs:** recipient.account, decision.final

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| valid_account | True | PAYMENT_INITIATED | Section 62a |

### E122_MedicalExaminationRequired

- **Description:** Medical examination when required (§72)
- **Legal Source:** Section 72
- **Hit Policy:** FIRST
- **Output:** examination_status
- **Inputs:** injury.type, examination.requested

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| personal | True | EXAMINATION_MANDATORY | Section 72(1) |

### E123_InsuranceRegister

- **Description:** Insurance register content (§76)
- **Legal Source:** Section 76
- **Hit Policy:** COLLECT
- **Output:** register_content
- **Inputs:** register.contains, vehicle.registered

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| insurance_policy | True | REGISTERED | Section 76 |

### E124_DrivingSchoolCoverage

- **Description:** Driving school special coverage (§89)
- **Legal Source:** Section 89
- **Hit Policy:** FIRST
- **Output:** coverage_type
- **Inputs:** vehicle.driving_school, instruction.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | instruction | SPECIAL_COVERAGE | Section 89 |

### E125_IntlTransportCoverage

- **Description:** International transport coverage (§90)
- **Legal Source:** Section 90
- **Hit Policy:** FIRST
- **Output:** coverage_type
- **Inputs:** permit.type, country.destination

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| international_permit | any | INTL_COVERAGE | Section 90 |

### E126_Definition_RegisteredKeeper

- **Description:** Definition: Registered keeper (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** keeper_definition
- **Inputs:** vehicle.registered, person.holder

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | registered_person | KEEPER_IS_REGISTERED | Section 2(8) |

### E127_Definition_PermanentLocation

- **Description:** Definition: Permanent location (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** location_definition
- **Inputs:** vehicle.plate, vehicle.insurance_card, person.residence

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| finnish_plate | any | any | LOCATION_IS_FINLAND | Section 2(9) |
| no_plate | none | finland | LOCATION_IS_FINLAND | Section 2(9) |

### E128_Definition_GreenCard

- **Description:** Definition: Green card system (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** green_card_status
- **Inputs:** country.system_member, card.valid

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | GREEN_CARD_VALID | Section 2(15-16) |

### E129_ImportFromEEA

- **Description:** Importing vehicle from EEA (§6a)
- **Legal Source:** Section 6a
- **Hit Policy:** FIRST
- **Output:** insurance_option
- **Inputs:** vehicle.imported_from, registration.country, insurance.country_choice

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EEA | origin_country | Finland | CAN_CHOOSE_FINLAND | Section 6a |

### E130_BorderTrafficInsuranceScope

- **Description:** Border traffic insurance scope (§7)
- **Legal Source:** Section 7
- **Hit Policy:** COLLECT
- **Output:** coverage_scope
- **Inputs:** vehicle.permanent_country, green_card, accident.country

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Non-EEA | False | Finland | MUST_INSURE | Section 7(1) |
| Non-EEA | True | any | GREEN_CARD_OK | Section 7(2) |
| Non-EEA | False | ['Sweden', 'Norway'] | INJURY_ONLY | Section 7(3) |

### E131_VehicleIdentificationRequirement

- **Description:** Vehicle identification requirement (§10)
- **Legal Source:** Section 10
- **Hit Policy:** FIRST
- **Output:** identification_rule
- **Inputs:** vehicle.registered, vehicle.identified, notification.days

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | >7 | LIABILITY_EXPIRES | Section 10(3) |

### E132_InsuranceDocumentContent

- **Description:** Insurance document content (§11)
- **Legal Source:** Section 11
- **Hit Policy:** COLLECT
- **Output:** document_validity
- **Inputs:** document.contains, terms.provided

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| key_terms | True | VALID_DOCUMENT | Section 11(1) |

### E133_CancellationConditions

- **Description:** Cancellation conditions (§16)
- **Legal Source:** Section 16
- **Hit Policy:** COLLECT
- **Output:** cancellation_allowed
- **Inputs:** cancellation.reason, new_insurance.exists, theft.reported

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| new_insurer | True | any | CANCELLATION_ALLOWED | Section 16(1) |
| theft | any | True | CANCELLATION_ALLOWED | Section 16(1) |

### E134_InsurerObligationToProvide

- **Description:** Insurer obligation to provide (§17)
- **Legal Source:** Section 17
- **Hit Policy:** FIRST
- **Output:** obligation_status
- **Inputs:** vehicle.type, insurer.licensed, insurer.authorized

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| covered_type | True | True | MUST_PROVIDE | Section 17(2) |

### E135_DamageHistoryContent

- **Description:** Damage history content (§19)
- **Legal Source:** Section 19
- **Hit Policy:** COLLECT
- **Output:** history_content
- **Inputs:** history.vehicles, history.claims, history.period

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| covered | paid | <=5_years | HISTORY_PROVIDED | Section 19(1) |

### E136_DamageHistoryTransfer

- **Description:** Damage history transfer (§21)
- **Legal Source:** Section 21
- **Hit Policy:** FIRST
- **Output:** transfer_rule
- **Inputs:** policy.new_company, history.exists, request.submitted

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | MUST_TRANSFER | Section 21 |

### E143_ReportingRequirements

- **Description:** Health unit reporting requirements (§56)
- **Legal Source:** Section 56
- **Hit Policy:** COLLECT
- **Output:** reporting_validity
- **Inputs:** report.includes, timeliness, content.complete

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| patient_ids | immediate | True | VALID_REPORT | Section 56 |

### E144_MediatorInvolvement

- **Description:** Mediator involvement (§70)
- **Legal Source:** Section 70
- **Hit Policy:** FIRST
- **Output:** mediation_approach
- **Inputs:** claim.disputed, mediation.requested

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | MEDIATOR_CAN_BE_USED | Section 70 |

### E145_PersonalInjuryProcessing

- **Description:** Personal injury processing (§71)
- **Legal Source:** Section 71
- **Hit Policy:** UNIQUE
- **Output:** processing_rule
- **Inputs:** injury.type, processing.special

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| personal | True | SPECIAL_PROCESSING | Section 71 |

### E146_SupervisionAuthority

- **Description:** Supervision authority (§75)
- **Legal Source:** Section 75
- **Hit Policy:** UNIQUE
- **Output:** authority_scope
- **Inputs:** authority.name, supervision.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Finanssivalvonta | financial | FIVA_SUPERVISES | Section 75 |

### E147_Definition_EEA

- **Description:** Definition: EEA state (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** eea_status
- **Inputs:** country.member EEA

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | EEA_STATE | Section 2(12) |

### E148_Definition_ThirdCountry

- **Description:** Definition: Third country (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** country_status
- **Inputs:** country.member EEA

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| False | THIRD_COUNTRY | Section 2(13) |

### E149_Definition_NationalBureau

- **Description:** Definition: National bureau (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** bureau_status
- **Inputs:** country.bureau member

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | NATIONAL_BUREAU_EXISTS | Section 2(14) |

### E150_Definition_GreenCardSystem

- **Description:** Definition: Green card system (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** system_status
- **Inputs:** system.international

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | GREEN_CARD_SYSTEM | Section 2(15) |

### E151_Definition_GuaranteeBody

- **Description:** Definition: Guarantee body (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** body_status
- **Inputs:** body.article10

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | GUARANTEE_BODY | Section 2(17) |

### E152_Definition_TransferInsurance

- **Description:** Definition: Transfer insurance (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** insurance_type
- **Inputs:** vehicle.transfer_permit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | TRANSFER_INSURANCE | Section 2(18) |

### E153_Definition_TrafficRoute

- **Description:** Definition: Traffic route (§2)
- **Legal Source:** Section 2
- **Hit Policy:** COLLECT
- **Output:** route_status
- **Inputs:** area.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| public_road | TRAFFIC_ROUTE | Section 2(19) |
| street | TRAFFIC_ROUTE | Section 2(19) |
| parking_area_public | TRAFFIC_ROUTE | Section 2(19) |

### E154_Definition_RentedEScooter

- **Description:** Definition: Rented e-scooter (§2)
- **Legal Source:** Section 2
- **Hit Policy:** UNIQUE
- **Output:** vehicle_definition
- **Inputs:** vehicle.escooter, rental.business, rented.available_public

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | RENTED_E_SCOOTER | Section 2(22) |

### E155_MandatoryProvisions

- **Description:** Mandatory nature of provisions (§3)
- **Legal Source:** Section 3
- **Hit Policy:** UNIQUE
- **Output:** contract_validity
- **Inputs:** contract.contrary_to_law, party.damaged

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | CONTRACT_VOID | Section 3 |

### E156_MotorInsuranceCentre

- **Description:** Motor Insurance Centre role (§4)
- **Legal Source:** Section 4
- **Hit Policy:** UNIQUE
- **Output:** centre_status
- **Inputs:** centre.funded, centre.administered

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | CENTRE_OPERATIONAL | Section 4 |

### E157_InsuranceContractActApplication

- **Description:** Insurance Contract Act application (§4a)
- **Legal Source:** Section 4a
- **Hit Policy:** COLLECT
- **Output:** application_status
- **Inputs:** section.applied

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 3 | APPLIES | Section 4a |
| 4b | APPLIES | Section 4a |
| 5a | APPLIES | Section 4a |

### E158_ConsumerProtectionApplication

- **Description:** Consumer Protection Act application (§4b)
- **Legal Source:** Section 4b
- **Hit Policy:** UNIQUE
- **Output:** application_status
- **Inputs:** policyholder.consumer

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | CONSUMER_PROTECTION_APPLIES | Section 4b |

### E159_JointLiability

- **Description:** Joint liability (§6)
- **Legal Source:** Section 6
- **Hit Policy:** FIRST
- **Output:** liability_type
- **Inputs:** multiple_obligors, obligation.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | insurance | JOINT_AND_SEVERAL | Section 6(1) |

### E160_InformationToAuthority

- **Description:** Information to Transport Agency (§9)
- **Legal Source:** Section 9
- **Hit Policy:** COLLECT
- **Output:** info_rule
- **Inputs:** info.type, timeliness

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| new_policy | WITHIN_7_DAYS | Section 9(1) |
| premium_default | REPORT_OBLIGATION | Section 9(2) |
| removal_from_traffic | REPORT_OBLIGATION | Section 9(3) |

### CD45_OutsideFinlandCompensation

- **Description:** Compensation for accidents outside Finland (§45)
- **Legal Source:** Section 45
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** accident.country, vehicle.home_country, victim.residence

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EEA_not_Finland | Finland | Finland | COVERED_BY_GUARANTEE | Section 45(1) |
| third_country | Finland | Finland | NOT_COVERED | Section 45 |
| EEA | other_EEA | Finland | COVERED_BY_LOCAL_OR_FINNISH | Section 45(3-4) |

### CD05_VehiclesToInsureFixed

- **Description:** Vehicles requiring insurance - FIXED (§5)
- **Legal Source:** Section 5
- **Hit Policy:** COLLECT
- **Output:** insurance_required
- **Inputs:** vehicle.permanent_location, vehicle.type, exemption.applies

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Finland | covered_type | False | MUST_INSURE | Section 5(1) |
| Finland | covered_type | True | EXEMPT | Section 5 |
| EEA_not_Finland | any | False | MAY_INSURE_FINLAND | Section 5(2) |

## Eligibility Information_Rights

### IR84_RightToInformation

- **Description:** Right to information from insurers (§84)
- **Legal Source:** Section 84
- **Hit Policy:** COLLECT
- **Output:** information_provided
- **Inputs:** information.type, requester.legitimate_interest

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| policy_coverage | True | MUST_PROVIDE | Section 84(1) |
| claim_status | True | MUST_PROVIDE | Section 84(2) |

## Eligibility Insurance_Matters

### IM91b_InsolvencyDuties

- **Description:** Insolvency handling duties (§91b)
- **Legal Source:** Section 91b
- **Hit Policy:** COLLECT
- **Output:** duty_status
- **Inputs:** insolvency.type, action.required

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| domestic_insurer | notify_authorities | MUST_NOTIFY_EEA_BODIES | Section 91b(1) |
| any_insolvency | coordinate_claims | MUST_COORDINATE | Section 91b(2) |

## Eligibility Premium_Calculation

### E11_PremiumCalculation

- **Description:** Calculate insurance premium
- **Legal Source:** Sections 89-92
- **Hit Policy:** UNIQUE
- **Output:** premiumAmount
- **Inputs:** vehicle.vehicleType, driver.age, claim.historyClaimCount, vehicle.usagePurpose

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PrivateCar | over_25 | 0 | Private | BasePremium | Section 89 |
| PrivateCar | under_25 | 0 | Private | BasePremium_Times_1_5 | Section 90 |
| PrivateCar | any | positive | any | BasePremium_Plus_ClaimLoading | Section 91 |
| Commercial | any | any | Commercial | CommercialRate | Section 92 |

### E24_DamageHistoryEffect

- **Description:** Damage history impact on premium (§20)
- **Legal Source:** Section 20
- **Hit Policy:** UNIQUE
- **Output:** premium_adjustment
- **Inputs:** damage.history.years, claim.count, vehicle.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 5 | 0 | any | No_Loading | Section 20 |
| 0 | 1 | any | Loading_50_Percent | Section 20 |
| 0 | 3 | any | Loading_100_Percent | Section 20 |

### E25_IncreasedPremiumRemoval

- **Description:** Increased premium during removal from traffic (§22)
- **Legal Source:** Section 22
- **Hit Policy:** UNIQUE
- **Output:** premium_calculation
- **Inputs:** vehicle.registeredAsRemoved, vehicle.usedDuringRemoval, premium.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | standard | Triple_Premium | Section 22 |
| True | False | any | Normal_Premium | Section 22 |

### E26_PremiumRefund

- **Description:** Premium refund upon termination (§23)
- **Legal Source:** Section 23
- **Hit Policy:** FIRST
- **Output:** refund_amount
- **Inputs:** insurance.terminated, premium.paid, coverage.days

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | excess | any | Refund_Excess | Section 23(1) |
| True | any | any | Proportional_Refund | Section 23(2) |

### E28_LatePaymentInterest

- **Description:** Late payment interest (§24)
- **Legal Source:** Section 24
- **Hit Policy:** UNIQUE
- **Output:** interest_amount
- **Inputs:** payment.overdue, days_late

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | >0 | Interest_Applied | Section 24(1) |

### E29_PenaltyFee

- **Description:** Penalty fee for no insurance (§28)
- **Legal Source:** Section 28
- **Hit Policy:** UNIQUE
- **Output:** penalty_amount
- **Inputs:** insurance.obligationViolated, premium.equivalent

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | Up_To_3x_Premium | Section 28(1) |

### E30_VehicleUsageBan

- **Description:** Vehicle usage ban (§30)
- **Legal Source:** Section 30
- **Hit Policy:** FIRST
- **Output:** ban_status
- **Inputs:** insurance.obligationViolated, vehicle.usedInTraffic

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Usage_Banned | Section 30(1) |
| False | any | No_Ban | Section 30 |

### E63_LiabilityContinues

- **Description:** Liability continuation despite non-payment (§25)
- **Legal Source:** Section 25
- **Hit Policy:** UNIQUE
- **Output:** liability_status
- **Inputs:** premium.unpaid, liability.continues

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Liability_Continues | Section 25(1) |

### E64_StatuteOfLimitations

- **Description:** Statute of limitations on premium (§26)
- **Legal Source:** Section 26
- **Hit Policy:** UNIQUE
- **Output:** limitations_status
- **Inputs:** premium.claim.year, claim.year

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >5 | any | Time_Barred | Section 26 |

### E65_PaymentEquivalent

- **Description:** Payment corresponding to premium (§27)
- **Legal Source:** Section 27
- **Hit Policy:** UNIQUE
- **Output:** payment_due
- **Inputs:** obligation.violated, premium.reasonable

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Reasonable_Payment | Section 27 |

### E66_PenaltyFeeDetermination

- **Description:** Determination of penalty fee (§29)
- **Legal Source:** Section 29
- **Hit Policy:** FIRST
- **Output:** penalty_status
- **Inputs:** violation.duration, violation.intentional, penalty.determined

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >0 | any | True | Penalty_Determined | Section 29 |

### E80_RetroactiveInfoWithheld

- **Description:** Retroactive premium for withheld info (§14)
- **Legal Source:** Section 14
- **Hit Policy:** UNIQUE
- **Output:** retroactive_amount
- **Inputs:** information.withheld, years_back

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | <=5 | Retroactive_5_Years | Section 14(1) |

### E81_RiskIncreaseRetroactive

- **Description:** Retroactive premium for risk increase (§15)
- **Legal Source:** Section 15
- **Hit Policy:** UNIQUE
- **Output:** retroactive_amount
- **Inputs:** risk.increased, years_back

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | <=5 | Retroactive_5_Years | Section 15(1) |

### E83_PremiumFactors

- **Description:** Premium calculation factors (§20)
- **Legal Source:** Section 20
- **Hit Policy:** COLLECT
- **Output:** premium_factors
- **Inputs:** vehicle.type, driver.age, claims.count

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| private_car | >25 | 0 | Base_Premium | Section 20 |
| private_car | <25 | any | Young_Driver_Loading | Section 20 |

### E84_UsageDuringRemoval

- **Description:** Premium when used during removal (§22)
- **Legal Source:** Section 22
- **Hit Policy:** FIRST
- **Output:** premium_multiplier
- **Inputs:** registered_removed, used_in_traffic

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | Triple_Premium | Section 22 |
| True | False | Normal_Premium | Section 22 |

### E85_LatePaymentInterest

- **Description:** Late payment interest rate (§24)
- **Legal Source:** Section 24
- **Hit Policy:** UNIQUE
- **Output:** interest_rate
- **Inputs:** overdue_days

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >0 | Interest_At_Reference_Rate | Section 24(1) |

### E86_UninsuredPayment

- **Description:** Payment when uninsured (§27)
- **Legal Source:** Section 27
- **Hit Policy:** UNIQUE
- **Output:** payment_due
- **Inputs:** obligation_violated, period_months

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | <=60 | Reasonable_Premium | Section 27(1) |

### E110_DamageHistoryYears

- **Description:** Damage history years impact (§20)
- **Legal Source:** Section 20
- **Hit Policy:** UNIQUE
- **Output:** history_adjustment
- **Inputs:** history.years, vehicle.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 5 | private | NO_LOADING | Section 20 |
| 0 | any | FULL_LOADING | Section 20 |

### E111_ClaimLoading

- **Description:** Claim-based loading (§20)
- **Legal Source:** Section 20
- **Hit Policy:** UNIQUE
- **Output:** loading_percentage
- **Inputs:** claims.last_5_years, vehicle.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| 0 | any | NO_LOADING | Section 20 |
| 1 | any | 50_PERCENT_LOADING | Section 20 |
| 3 | any | 100_PERCENT_LOADING | Section 20 |

### E112_RefundMinAmount

- **Description:** Minimum refund amount (§23)
- **Legal Source:** Section 23
- **Hit Policy:** UNIQUE
- **Output:** refund_status
- **Inputs:** refund.amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >8 | REFUND_PROCESSED | Section 23(2) |
| <=8 | NO_REFUND | Section 23(2) |

### E113_PaymentDueDate

- **Description:** Premium payment due (§24)
- **Legal Source:** Section 24
- **Hit Policy:** UNIQUE
- **Output:** payment_status
- **Inputs:** payment.due_date, payment.made

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| passed | False | OVERDUE | Section 24(1) |

### E114_LiabilityContinues

- **Description:** Liability continues despite non-payment (§25)
- **Legal Source:** Section 25
- **Hit Policy:** UNIQUE
- **Output:** status
- **Inputs:** premium.unpaid, liability.continues

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | LIABILITY_CONTINUES | Section 25(1) |

### E115_LimitationsPremium

- **Description:** Premium limitations (§26)
- **Legal Source:** Section 26
- **Hit Policy:** UNIQUE
- **Output:** limitation_status
- **Inputs:** claim.year, billing.year

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >5 | any | TIME_BARRED | Section 26 |

## Eligibility Time_Limits

### E12_ClaimTimeLimit

- **Description:** Determine claim submission time limit
- **Legal Source:** Section 74
- **Hit Policy:** UNIQUE
- **Output:** timeLimitStatus
- **Inputs:** claim.damageType, accident.date, claim.submissionDate

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PersonalInjury | any | any | Within_3_Years_From_Injury | Section 74(1) |
| PropertyDamage | any | within_1_year | Within_1_Year_From_Accident | Section 74(2) |
| PropertyDamage | any | after_1_year | ClaimTimeBarred | Section 74(2) |

### E13_InsolvencyProtection

- **Description:** Protection when insurer becomes insolvent
- **Legal Source:** Section 77
- **Hit Policy:** UNIQUE
- **Output:** protection_mechanism
- **Inputs:** insuranceCompany.status, insurance.policyActive, claim.isPending

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Insolvent | True | True | FinnishGuaranteeFund_Pays | Section 77(1) |
| Insolvent | True | False | TransferToAnotherInsurer | Section 77(2) |
| Healthy | True | True | NormalClaimsProcess | Section 76 |

### E21_ClaimDecisionTime

- **Description:** Decision on compensation time limits (§62)
- **Legal Source:** Section 62
- **Hit Policy:** UNIQUE
- **Output:** decision_deadline
- **Inputs:** claim.type, claim.complexity, days_elapsed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| property_damage | simple | any | 30_Days | Section 62 |
| personal_injury | any | any | 90_Days | Section 62 |
| complex | any | >90 | 180_Days | Section 62 |

### E102_ClaimDecisionDeadline

- **Description:** Claim decision deadline (§62)
- **Legal Source:** Section 62
- **Hit Policy:** UNIQUE
- **Output:** deadline_days
- **Inputs:** claim.complexity, injury.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| simple | property | 30_DAYS | Section 62 |
| any | personal | 90_DAYS | Section 62 |

## Negative_Claims Conditional_Compensation

### N12_TheftPersonalInjury

- **Description:** Theft - Personal injury may be covered
- **Legal Source:** Section 41
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.theft.reported, accident.occurredAfterTheft, insurance.policyStatus, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | active | PersonalInjury | COVERED | Section 41(2) |
| False | any | active | any | COVERED | Section 41 |

### N13_AuthorizedCompetition

- **Description:** Authorized competition - Conditional coverage
- **Legal Source:** Section 41a
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** driver.isCompetitionParticipant, event.isAuthorized, driver.licenseValid, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | PersonalInjury | COVERED | Section 41a(2) |
| True | True | True | PropertyDamage | COVERED | Section 41a(2) |
| False | any | any | any | COVERED | Section 41a |

### N14_ExemptVehiclePersonalInjury

- **Description:** Exempt vehicle - Personal injury always covered
- **Legal Source:** Section 43
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.isExempt, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | PersonalInjury | COVERED | Section 43(3) |

### N15_UnknownVehiclePersonalInjury

- **Description:** Unknown vehicle - Personal injury covered
- **Legal Source:** Section 44
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.isUnknown, police.reportFiled, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | PersonalInjury | COVERED | Section 44(1) |
| True | True | PropertyDamage | COVERED_GuaranteeFund | Section 44(2) |

### N16_NoInsurancePersonalInjury

- **Description:** No insurance - Personal injury from guarantee fund
- **Legal Source:** Section 46
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** insurance.exists, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| False | PersonalInjury | COVERED_GuaranteeFund | Section 46(1) |
| True | any | COVERED | Section 46(2) |

### N17_ThirdPartyVictim

- **Description:** Third party victim - Full compensation
- **Legal Source:** Section 48
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** driver.bloodAlcoholLevel, victim.relationshipType, victim.isAtFault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2_permille | ThirdParty | False | COVERED | Section 48(3) |
| 0.5-1.19_permille | ThirdParty | False | COVERED | Section 48(3) |
| <0.5_permille | any | False | COVERED | Section 48(2) |

### N19_EScooterCompensation

- **Description:** Hired e-scooter driver injuries - Limited coverage (§34a)
- **Legal Source:** Section 34a
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.vehicleType, vehicle.isHired, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EScooter | True | PersonalInjury | COVERED_LIMITED_MEDICAL | Section 34a |
| EScooter | False | PersonalInjury | COVERED_100 | Section 34 |
| EScooter | True | PropertyDamage | NOT_COVERED | Section 34a |

### N20_OutsideFinland

- **Description:** Damages outside Finland - Conditional (§45)
- **Legal Source:** Section 45
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** accident.locationCountry, vehicle.permanentLocation, victim.residenceCountry

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| EEA | Finland | Finland | COVERED | Section 45(1) |
| Non-EEA | Finland | Finland | NOT_COVERED | Section 45 |
| EEA | Finland | Finland | COVERED_GUARANTEE_FUND | Section 45(2) |

### N21_AssistingInjured

- **Description:** Damages from assisting injured person (§39)
- **Legal Source:** Section 39
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** person.assistingInjured, person.isProfessionalRescuer

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | COVERED | Section 39(1) |
| True | True | NOT_COVERED | Section 39(2) |

### N24_TheftDetails

- **Description:** Theft compensation details (§41)
- **Legal Source:** Section 41
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** theft.reported, insurance.terminated, damage.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | PropertyDamage | NOT_COVERED | Section 41(1) |
| True | True | PersonalInjury | COVERED_GUARANTEE_FUND | Section 41(2) |

### N29_CompetitionRules

- **Description:** Competition rules (§41a)
- **Legal Source:** Section 41a
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** driver.competing, rules.followed, license.valid

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | True | COVERED | Section 41a(2) |
| True | False | any | NOT_COVERED | Section 41a(1) |

### N30_OutsideFinlandExceptions

- **Description:** Outside Finland exceptions (§45)
- **Legal Source:** Section 45
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** vehicle.home_country, accident.country, victim.home_country

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Finland | EEA | Finland | COVERED_GUARANTEE | Section 45(1) |
| Finland | Non-EEA | Finland | NOT_COVERED | Section 45 |

### N31_ExemptVehicleTypes

- **Description:** Exempt vehicle types (§43)
- **Legal Source:** Section 43
- **Hit Policy:** COLLECT
- **Output:** coverage_rule
- **Inputs:** vehicle.category, damage.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| diplomatic | personal | COVERED_GUARANTEE | Section 43(3) |
| military | personal | COVERED_GUARANTEE | Section 43(3) |
| diplomatic | property | NOT_COVERED | Section 43(2) |

### N32_UnknownVehicleCoverage

- **Description:** Unknown vehicle coverage (§44)
- **Legal Source:** Section 44
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** vehicle.identified, damage.type, police.report

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| False | personal | True | COVERED_GUARANTEE | Section 44(1) |
| False | property | True | COVERED_GUARANTEE | Section 44(2) |
| False | any | False | NOT_COVERED | Section 44 |

### N33_NoInsuranceExceptions

- **Description:** No insurance exceptions (§46)
- **Legal Source:** Section 46
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** no_insurance, victim.relationship, victim.knew_uninsured

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | passenger_owner | True | NOT_COVERED | Section 46(2) |
| True | passenger_owner | False | COVERED_GUARANTEE | Section 46(1) |
| True | third_party | any | COVERED_GUARANTEE | Section 46(1) |

## Negative_Claims Full_Denial

### N1_UntitledUse

- **Description:** Unauthorized use of vehicle - Full denial
- **Legal Source:** Section 49
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.usedWithoutPermission, vehicle.ownerConsent, driver.isAuthorized

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | False | NOT_COVERED | Section 49(1) |

### N2_InsanityEmergency

- **Description:** Insanity or emergency situation - Full denial
- **Legal Source:** Section 50
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** driver.isInsane, driver.inEmergency, driver.isResponsible

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | False | NOT_COVERED | Section 50(1) |
| False | True | False | NOT_COVERED | Section 50(2) |

### N3_TheftPropertyDamage

- **Description:** Theft - Property damage after insurance terminated
- **Legal Source:** Section 41
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.theft.reported, accident.occurredAfterTheft, insurance.policyStatus, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | terminated | PropertyDamage | NOT_COVERED | Section 41(1) |

### N4_UnauthorizedCompetition

- **Description:** Unauthorized competition/racing - Full denial
- **Legal Source:** Section 41a
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** driver.isCompetitionParticipant, event.isAuthorized, driver.licenseValid

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | any | NOT_COVERED | Section 41a(1) |
| True | True | False | NOT_COVERED | Section 41a(2) |

### N5_ExemptVehicleProperty

- **Description:** Exempt vehicle property damage - Full denial
- **Legal Source:** Section 43
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.isExempt, vehicle.exemptType, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | Military | PropertyDamage | NOT_COVERED | Section 43(1) |
| True | Diplomatic | PropertyDamage | NOT_COVERED | Section 43(2) |
| True | Government | PropertyDamage | NOT_COVERED | Section 43(2) |

### N6_UnknownVehicleNoReport

- **Description:** Unknown vehicle without police report - Full denial
- **Legal Source:** Section 44
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** vehicle.isUnknown, police.reportFiled, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | False | PropertyDamage | NOT_COVERED | Section 44(2) |

### N7_NoInsuranceProperty

- **Description:** No insurance property damage - Full denial
- **Legal Source:** Section 46
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** insurance.obligationMet, insurance.exists, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| False | False | PropertyDamage | NOT_COVERED | Section 46(1) |

### N8_VictimGrossNegligence

- **Description:** Victim gross negligence - Full denial
- **Legal Source:** Section 47
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** victim.causedDamage, victim.contributionDegree

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | GrossNegligence | NOT_COVERED | Section 47(1) |

### N9_DrunkDriverSoleFault

- **Description:** Drunk driver sole fault - Full denial
- **Legal Source:** Section 48
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** driver.bloodAlcoholLevel, driver.contributionDegree, victim.isAtFault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2_permille | SoleFault | False | NOT_COVERED | Section 48(1) |

### N18_WorkPerformanceDamages

- **Description:** Work performance damages - Full denial (§42)
- **Legal Source:** Section 42
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** accident.occurredDuringWork, vehicle.wasStationary, injured.personRole

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | owner_or_holder | NOT_COVERED | Section 42(1) |
| True | True | worker | NOT_COVERED | Section 42(1) |
| True | True | property_work | NOT_COVERED | Section 42(2) |

### N22_PropertyExclusions

- **Description:** Certain property damages not compensated (§40)
- **Legal Source:** Section 40
- **Hit Policy:** FIRST
- **Output:** compensation_decision
- **Inputs:** damage.vehicle, damage.connectedVehicle, damage.ownerProperty

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | any | NOT_COVERED | Section 40(1) |
| True | False | True | NOT_COVERED | Section 40(2) |

### N23_PropertyExclusionsDetails

- **Description:** Property exclusion details (§40)
- **Legal Source:** Section 40
- **Hit Policy:** COLLECT
- **Output:** exclusion_type
- **Inputs:** damage.to_own_vehicle, damage.to_connected, damage.owner_property

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | any | NOT_COVERED | Section 40(1) |
| False | True | any | NOT_COVERED | Section 40(1) |
| False | False | True | NOT_COVERED | Section 40(2) |

### N27_IllegalUseDetails

- **Description:** Illegal use details (§49)
- **Legal Source:** Section 49
- **Hit Policy:** FIRST
- **Output:** coverage_rule
- **Inputs:** vehicle.illegal_use, victim.knows_illegal

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | True | NOT_COVERED | Section 49(1) |
| True | False | COVERED_SPECIAL_REASON | Section 49(1) |

### N28_InsanityExemption

- **Description:** Insanity exemption details (§50)
- **Legal Source:** Section 50
- **Hit Policy:** FIRST
- **Output:** exemption_rule
- **Inputs:** victim.age, victim.mental_state, victim.emergency_action

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| <12 | any | any | NOT_APPLY_EXEMPTION | Section 50 |
| any | insane | any | NOT_APPLY_EXEMPTION | Section 50(1) |
| any | any | True | NOT_APPLY_EXEMPTION | Section 50(2) |

### EXC50_InsanityAndNecessityExemption

- **Description:** Exemption for insanity and necessity (§50)
- **Legal Source:** Section 50
- **Hit Policy:** FIRST
- **Output:** exemption_status
- **Inputs:** victim.age, victim.mental_state, victim.emergency_action, victim.defensive_action

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| <12 | any | any | any | NOT_APPLY_EXEMPTION | Section 50 |
| any | insane | any | any | NOT_APPLY_EXEMPTION | Section 50(1) |
| any | any | True | any | NOT_APPLY_EXEMPTION | Section 50(2) |
| any | any | any | True | NOT_APPLY_EXEMPTION | Section 50(2) |

## Negative_Claims Reduced_Compensation

### N10_VictimContribution

- **Description:** Victim contribution - Reduced compensation
- **Legal Source:** Section 47
- **Hit Policy:** FIRST
- **Output:** compensation_percentage
- **Inputs:** victim.causedDamage, victim.contributionDegree, damage.damageType

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | Negligence | PropertyDamage | 50_PERCENT | Section 47(2) |
| True | Slight | any | 75_PERCENT | Section 47(2) |
| True | Moderate | any | 50_PERCENT | Section 47(2) |

### N11_AlcoholImpairment

- **Description:** Alcohol impairment - Reduced compensation
- **Legal Source:** Section 48
- **Hit Policy:** FIRST
- **Output:** compensation_percentage
- **Inputs:** driver.bloodAlcoholLevel, driver.contributionDegree, victim.isAtFault

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2_permille | PartialFault | False | 50_PERCENT | Section 48(1) |
| 0.5-1.19_permille | PartialFault | False | 75_PERCENT | Section 48(2) |
| 0.5-1.19_permille | SoleFault | False | NOT_COVERED | Section 48(2) |

### N25_VictimContributionDetails

- **Description:** Victim contribution details (§47)
- **Legal Source:** Section 47
- **Hit Policy:** COLLECT
- **Output:** reduction_rule
- **Inputs:** victim.intentional, victim.gross_negligence, victim.contribution

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True | any | any | REDUCE_OR_DENY | Section 47(1) |
| False | True | any | REDUCE_OR_DENY | Section 47(1) |
| False | False | moderate | REDUCE_50_PERCENT | Section 47(2) |

### N26_AlcoholDetails

- **Description:** Alcohol impairment details (§48)
- **Legal Source:** Section 48
- **Hit Policy:** COLLECT
- **Output:** compensation_rule
- **Inputs:** driver.bac_permille, driver.substance, victim.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2 | any | driver | REDUCE_OR_DENY | Section 48(1) |
| >=0.5 | any | any | REDUCE_PROPORTIONALLY | Section 48(2) |
| any | narcotic | third_party | FULL_COVERED | Section 48(3) |

### EXC48_AlcoholImpairmentFixed

- **Description:** Alcohol impairment - FIXED language (§48)
- **Legal Source:** Section 48
- **Hit Policy:** FIRST
- **Output:** compensation_rule
- **Inputs:** driver.bac_permille, driver.substance, injury.type

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2 | any | personal | ONLY_OTHER_FACTORS | Section 48(1) |
| >=0.5 | <1.2 | personal | PROPORTIONAL_REDUCTION | Section 48(2) |
| any | narcotic | personal | PROPORTIONAL_REDUCTION | Section 48(2) |
| <0.5 | none | any | FULL_COVERED | Section 48 |

