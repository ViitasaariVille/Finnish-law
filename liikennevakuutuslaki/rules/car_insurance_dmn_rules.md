# Finnish Traffic Insurance DMN Rules

Law: Liikennevakuutuslaki (Traffic Insurance Act) 460/2016

Version: 1.0

Total Decisions: 20

## MandatoryInsuranceRequirement

Determine if vehicle requires mandatory traffic insurance

Legal source: Section 5

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| FI, True, MotorVehicle | MandatoryTrafficInsurance | Section 5(1) |
| FI, True, Trailer | MandatoryTrafficInsurance | Section 5(1) |
| EEA, True, any | Check registration country | Section 6a |
| Non-EEA, True, any | MandatoryTrafficInsurance | Section 5(1) |

## InsuranceObligationLiableParty

Determine who is liable for insurance obligation

Legal source: Section 6

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| exists, exists, True | Owner and Holder jointly liable | Section 6(1) |
| exists, None, True | Owner liable | Section 6(1) |
| None, exists, True | Holder liable | Section 6(1) |
| exists, None, False | Owner liable from ownership | Section 6(2) |

## CoverageCompensation

Determine what is covered by traffic insurance

Legal source: Sections 12-16

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PersonalInjury, True, False | 100% covered | Section 12(1) |
| PersonalInjury, True, True | 100% covered | Section 12(1) |
| PropertyDamage, False, True | 100% covered | Section 12(1) |
| VehicleDamage, False, True | 100% covered | Section 12(1) |
| EnvironmentalDamage, False, True | 100% covered | Section 12(2) |

## Exclusions

Determine what is NOT covered by traffic insurance

Legal source: Sections 17-21

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Intentional, any, any, any | Excluded - Intentional damage | Section 17(1) |
| any,  intoxicated, any, any | Excluded - Drunken driving | Section 18(1) |
| any, any, Race, any | Excluded - Racing | Section 19(1) |
| any, any, Stunt, any | Excluded - Stunt driving | Section 19(2) |
| any, any, any, PrivateArea | May be excluded | Section 20 |

## MedicalExpenseCoverage

Determine medical expense compensation

Legal source: Section 5

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Emergency, required, public | 100% | Section 5a |
| Emergency, required, private | 100% (reimbursement) | Section 5a |
| Surgery, required, any | 100% | Section 5a |
| Medicines, prescribed, pharmacy | 100% | Section 5b |
| Rehabilitation, required, any | 100% | Section 5c |
| Dental, accident_related, any | 100% | Section 5e |
| Prosthesis, required, any | 100% | Section 5f |

## LostWagesCompensation

Calculate lost wages compensation

Legal source: Section 4

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Employed, net_monthly, any | net_monthly / 30 * days | Section 4(1) |
| SelfEmployed, annual, any | annual / 365 * days | Section 4(2) |
| Unemployed, any, any | Minimum 36.90/day | Section 4(3) |
| Student, any, any | Student grant adjustment | Section 4(4) |

## PainAndSufferingCompensation

Calculate pain and suffering compensation

Legal source: Section 5

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True, 1-10%, moderate | Section 5(2) scale | Section 5(2) |
| True, 11-20%, moderate | Section 5(2) scale | Section 5(2) |
| True, 21-50%, significant | Section 5(2) scale | Section 5(2) |
| True, 51-100%, severe | Section 5(2) scale | Section 5(2) |
| False, any, any | Temporary pain - scale | Section 5(1) |

## DeathCompensation

Calculate death compensation

Legal source: Sections 7-8

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| exists, Spouse, True | Spouse pension + lump sum | Section 7(1) |
| exists, Child, True | Child pension | Section 7(2) |
| none, Dependent, True | Lump sum | Section 8 |
| any, Parent, True | Funeral expenses + compensation | Section 8 |

## PropertyDamageCompensation

Calculate property damage compensation

Legal source: Section 3

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Vehicle, market_value, TotalLoss | Market value | Section 3(1) |
| Vehicle, market_value, Partial | Repair cost | Section 3(1) |
| Property, any, any | Actual value | Section 3(1) |
| Clothing, any, any | Replacement value | Section 3(2) |

## ClaimTimeLimit

Determine claim submission time limit

Legal source: Section 74

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PersonalInjury, any | 3 years from injury | Section 74(1) |
| PropertyDamage, within_1_year | 1 year from accident | Section 74(2) |
| PropertyDamage, after_1_year | Claim barred | Section 74(2) |

## PremiumCalculation

Calculate insurance premium

Legal source: Sections 89-92

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| PrivateCar, over_25, no_claims, Private | Base premium | Section 89 |
| PrivateCar, under_25, no_claims, Private | Base premium * 1.5 | Section 90 |
| PrivateCar, any, with_claims, any | Base premium + claim loading | Section 91 |
| Commercial, any, any, any | Commercial rate | Section 92 |

## InternationalCoverage

Determine international coverage

Legal source: Sections 10-11

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Finland, any, FI | Full coverage | Section 10(1) |
| EEA, True, any | Full coverage - Green Card | Section 10(2) |
| EEA, False, any | Limited - Bureau guarantee | Section 10(3) |
| Non-EEA, any, any | Check bilateral agreement | Section 11 |

## InsolvencyProtection

Protection when insurer becomes insolvent

Legal source: Section 77

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Insolvent, True, True | Finnish Guarantee Fund pays | Section 77(1) |
| Insolvent, True, False | Transfer to another insurer | Section 77(2) |
| Healthy, True, True | Normal claims process | Section 76 |

## TheftExclusion

Compensation after theft - Section 41

Legal source: Section 41

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True, any, before_theft, terminated | NOT COVERED - Insurance terminated due to theft | Section 41(1) |
| True, any, after_theft, active | Covered if theft reported and insurance active | Section 41(2) |
| False, N/A, any, any | Normal coverage applies | Section 41 |

## CompetitionExclusion

Exclusion for competition participants - Section 41a

Legal source: Section 41a

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True,  motorsport, False, any | NOT COVERED - Unauthorized competition | Section 41a(1) |
| True,  motorsport, True, valid | Covered - Authorized competition with license | Section 41a(2) |
| True, racing, False, any | NOT COVERED - Unauthorized racing | Section 41a(1) |
| False, any, any, any | Normal coverage applies | Section 41a |

## ExemptVehicleExclusion

Exclusion for exempt vehicles - Section 43

Legal source: Section 43

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True, military, none, any | NOT COVERED - Exempt military vehicle | Section 43(1) |
| True, diplomatic, none, any | NOT COVERED - Exempt diplomatic vehicle | Section 43(2) |
| True, any, none, PersonalInjury | Covered - Personal injury always compensated | Section 43(3) |
| False, any, any, any | Normal coverage applies | Section 43 |

## UnknownVehicleExclusion

Damage by unknown vehicle - Section 44

Legal source: Section 44

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True, False, PersonalInjury, True | Covered - Personal injury by unknown vehicle | Section 44(1) |
| True, False, PropertyDamage, True | Covered - Property damage (subrogation to guarantee fund) | Section 44(2) |
| True, False, PropertyDamage, False | NOT COVERED - No police report | Section 44(2) |
| True, True, any, any | Normal coverage - Vehicle identified | Section 44 |

## InsuranceObligationViolation

Compensation when insurance obligation violated - Section 46

Legal source: Section 46

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| False, False, True, False | Covered - Personal injury compensated from guarantee fund | Section 46(1) |
| False, False, False, True | NOT COVERED - Property damage when no insurance | Section 46(1) |
| False, True, True, True | Covered - Insurance exists but violated | Section 46(2) |
| True, True, any, any | Normal coverage applies | Section 46 |

## AlcoholLevelExclusion

Alcohol and drug influence on compensation - Section 48

Legal source: Section 48

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| >=1.2, True, sole, any | NOT COVERED - Driver solely responsible | Section 48(1) |
| >=1.2, True, partial, any | Reduced 50% - Driver contribution 50% | Section 48(1) |
| 0.5-1.19, False, partial, any | Reduced proportionally - Contribution 25% | Section 48(2) |
| <0.5, False, any, any | Full compensation | Section 48(2) |
| any, True, any, third_party | Full compensation - Victim not responsible | Section 48(3) |

## VictimContributionExclusion

Victim's own contribution to damage - Section 47

Legal source: Section 47

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| True, gross_negligence, any, any | NOT COVERED - Gross negligence | Section 47(1) |
| True, negligence, any, PropertyDamage | Reduced 50% - Property damage contribution | Section 47(2) |
| True, slight, any, any | Reduced 25% - Slight contribution | Section 47(2) |
| False, none, any, any | Full compensation | Section 47 |

