# DRD - Decision Requirements Diagram for Liikennevakuutuslaki (Traffic Insurance Act 460/2016)

## Overview

This document provides a text-based Decision Requirements Diagram (DRD) for the Finnish Traffic Insurance Act. In DMN, DRDs show the relationships between decision nodes, input data, and business knowledge models.

---

## Main DRD Structure

```
                                    ┌─────────────────────┐
                                    │   CLAIM RECEIVED    │
                                    │   (Input Data)      │
                                    └──────────┬──────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                              ┌────►│ 1. NEGATIVE CLAIMS  │────┐
                              │     │    (Decision)      │    │
                              │     └──────────┬──────────┘    │
                              │                │               │
                              │                ▼               │
                              │     ┌─────────────────────┐    │
                              │     │  Check Exclusions   │    │
                              │     │  (§§41-50)          │    │
                              │     └──────────┬──────────┘    │
                              │                │               │
                       NOT_COVERED           │          PASS
                              │                │               │
                              │                ▼               │
                              │     ┌─────────────────────┐    │
                              │     │ 2. ELIGIBILITY      │    │
                              └─────│    (Decision)       │◄───┘
                                    └──────────┬──────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                              ┌────►│ 3. COVERAGE         │────┐
                              │     │  DETERMINATION      │    │
                              │     └──────────┬──────────┘    │
                              │                │               │
                              │                ▼               │
                              │     ┌─────────────────────┐    │
                              │     │  Check Vehicle      │    │
                              │     │  Insurance Required │    │
                              │     └──────────┬──────────┘    │
                              │                │               │
                       NOT_COVERED           │          COVERED
                              │                │               │
                              │                ▼               │
                              │     ┌─────────────────────┐    │
                              │     │ 4. COMPENSATION     │    │
                              └─────│    CALCULATION      │◄───┘
                                    └─────────────────────┘
                                               │
                                               ▼
                                    ┌─────────────────────┐
                                    │  COMPENSATION PAID  │
                                    │   (Final Output)    │
                                    └─────────────────────┘
```

---

## Detailed Decision Nodes

### Level 1: Negative Claims (Exclusions)

| Decision Node | Description | Input Data | Business Knowledge |
|---------------|-------------|------------|-------------------|
| N1 | Unauthorized Use (§49) | vehicle.usedWithoutPermission, vehicle.ownerConsent | Excluded Uses Table |
| N2 | Insanity/Emergency (§50) | driver.isInsane, driver.inEmergency | Exclusion Criteria |
| N3 | Theft Property Damage (§41) | vehicle.theft.reported, accident.occurredAfterTheft | Theft Rules |
| N4 | Unauthorized Competition (§41a) | driver.isCompetitionParticipant, event.isAuthorized | Competition Rules |
| N5 | Exempt Vehicle Property (§43) | vehicle.isExempt, vehicle.exemptType | Exempt Vehicle List |
| N6 | Unknown Vehicle (§44) | vehicle.isUnknown, police.reportFiled | Unknown Vehicle Rules |
| N7 | No Insurance Property (§46) | insurance.obligationMet, insurance.exists | Insurance Obligation |
| N8 | Victim Gross Negligence (§47) | victim.contributionDegree | Negligence Scale |
| N9 | Drunk Driver Sole Fault (§48) | driver.bloodAlcoholLevel, driver.contributionDegree | Alcohol Thresholds |

### Level 2: Eligibility

| Decision Node | Description | Input Data | Business Knowledge |
|---------------|-------------|------------|-------------------|
| E1 | Vehicle Insurance Requirement (§5) | vehicle.registrationCountry, vehicle.vehicleType | Mandatory Insurance List |
| E2 | Damage Coverage (§§12-16) | damage.damageType | Coverage Types |
| E3 | International Coverage (§§10-11) | accident.locationCountry, greenCard.valid | Green Card Agreement |
| E4 | Insurance Obligation Liable Party (§6) | person.owner.exists, person.holder.exists | Liability Rules |

### Level 3: Compensation Calculation

| Decision Node | Description | Input Data | Business Knowledge |
|---------------|-------------|------------|-------------------|
| E5 | Medical Expense Compensation (§§53-59) | medicalExpense.treatmentType, providerType | Medical Fee Schedule |
| E6 | Lost Wages Compensation (§34) | person.incomeType, injury.workAbilityLostDays | Income Calculation |
| E7 | Pain and Suffering (§35) | injury.permanentDisabilityPercentage | Pain Scale |
| E8 | Property Damage Compensation (§3) | property.type, damage.severity | Property Value Table |
| E9 | Death Compensation (§§36-38) | survivor.relationship, survivor.isDependent | Death Benefit Table |
| E10 | Disability Compensation (§35) | injury.permanentDisabilityPercentage | Disability Scale |

---

## Business Knowledge Models (BKM)

```
┌─────────────────────────────────────────────┐
│         EXCLUSION_CRITERIA_BKM              │
│  (Blackbox Knowledge Model)                 │
├─────────────────────────────────────────────┤
│  Inputs:                                    │
│    - driver.bloodAlcoholLevel               │
│    - driver.isCompetitionParticipant        │
│    - vehicle.isExempt                       │
│    - insurance.exists                       │
│    - victim.contributionDegree              │
│                                             │
│  Output:                                    │
│    - EXCLUSION_REASON                      │
│    - COVERAGE_STATUS                       │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│         MEDICAL_FEE_SCHEDULE_BKM            │
│  (Decision Table)                           │
├─────────────────────────────────────────────┤
│  treatmentType    │ providerType │ coverage │
│  ─────────────────────────────────────────  │
│  Emergency        │ public       │ 100%     │
│  Emergency        │ private      │ 100%     │
│  Surgery          │ any          │ 100%     │
│  Medicines        │ pharmacy     │ 100%     │
│  Rehabilitation   │ any          │ 100%     │
│  DentalTreatment  │ any          │ 100%     │
│  Prosthesis       │ any          │ 100%     │
│  TravelToTreatment│ any          │ 100%     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│         ALCOHOL_IMPAIRMENT_BKM             │
│  (Decision Table)                           │
├─────────────────────────────────────────────┤
│  bloodAlcoholLevel │ contributionDegree │ output     │
│  ─────────────────────────────────────────────────│
│  >=1.2_permille    │ SoleFault         │ NOT_COVERED│
│  >=1.2_permille    │ PartialFault      │ 50%        │
│  0.5-1.19_permille│ PartialFault      │ 75%        │
│  <0.5_permille    │ any               │ COVERED    │
└─────────────────────────────────────────────┘
```

---

## Information Requirements (Input Data)

```
┌────────────────────────────────────────────────────────────┐
│                    INPUT DATA NODES                        │
├────────────────────────────────────────────────────────────┤
│ VEHICLE                                                    │
│ ├─ registrationCountry: string                            │
│ ├─ vehicleType: enum (MotorVehicle, Trailer)             │
│ ├─ requiresInsurance: boolean                             │
│ ├─ isExempt: boolean                                      │
│ ├─ exemptType: enum (Military, Diplomatic, Government)    │
│ ├─ usedWithoutPermission: boolean                         │
│ ├─ ownerConsent: boolean                                  │
│ ├─ isUnknown: boolean                                     │
│ └─ theft.reported: boolean                                │
│                                                            │
│ DRIVER                                                     │
│ ├─ isAuthorized: boolean                                  │
│ ├─ isInsane: boolean                                      │
│ ├─ inEmergency: boolean                                  │
│ ├─ isCompetitionParticipant: boolean                       │
│ ├─ licenseValid: boolean                                  │
│ ├─ bloodAlcoholLevel: number (permille)                  │
│ ├─ breathAlcoholLevel: number (mg/L)                      │
│ ├─ drugImpaired: boolean                                  │
│ └─ contributionDegree: enum                               │
│                                                            │
│ DAMAGE                                                     │
│ ├─ damageType: enum (PersonalInjury, PropertyDamage)       │
│ ├─ isPersonalInjury: boolean                              │
│ ├─ isPropertyDamage: boolean                              │
│ └─ severity: enum (TotalLoss, PartialDamage)              │
│                                                            │
│ INSURANCE                                                  │
│ ├─ policyStatus: enum (active, terminated)                │
│ ├─ exists: boolean                                       │
│ └─ obligationMet: boolean                                 │
│                                                            │
│ CLAIM                                                      │
│ ├─ submissionDate: date                                   │
│ ├─ damageType: enum                                       │
│ └─ isPending: boolean                                     │
└────────────────────────────────────────────────────────────┘
```

---

## Decision Service Example

```xml
<decisionService name="TrafficInsuranceClaim">
    <decision name="NegativeClaimsCheck">
        <decisionRule>
            <!-- N1-N17 rules -->
        </decisionRule>
    </decision>
    <decision name="EligibilityCheck">
        <decisionRule>
            <!-- E1-E13 rules -->
        </decisionRule>
    </decision>
    <decision name="CompensationCalculation">
        <decisionRule>
            <!-- E5-E13 rules -->
        </decisionRule>
    </decision>
</decisionService>
```

---

## DRD Notation (XML DMN Format)

For import into Camunda/BPMN.io:

```xml
<definitions xmlns="https://www.omg.org/spec/DMN/20191111/MODEL/"
             xmlns:dmndi="https://www.omg.org/spec/DMN/20191111/DMNDI/"
             xmlns:dc="https://www.omg.org/spec/DMN/20191111/DC/"
             id="liikennevakuutuslaki_drd"
             name="Liikennevakuutuslaki DRD"
             namespace="http://flowable.org/dmn">

    <!-- Input Data -->
    <inputData id="Input_Claim" name="Claim Received"/>
    <inputData id="Input_Vehicle" name="Vehicle"/>
    <inputData id="Input_Driver" name="Driver"/>
    <inputData id="Input_Damage" name="Damage"/>
    <inputData id="Input_Insurance" name="Insurance"/>
    <inputData id="Input_Injury" name="Injury"/>
    <inputData id="Input_Person" name="Person"/>
    
    <!-- Decisions -->
    <decision id="Decision_NegativeClaims" name="1. Negative Claims">
        <informationRequirement>
            <requiredInput href="#Input_Claim"/>
        </informationRequirement>
    </decision>
    
    <decision id="Decision_Eligibility" name="2. Eligibility">
        <informationRequirement>
            <requiredDecision href="#Decision_NegativeClaims"/>
        </informationRequirement>
    </decision>
    
    <decision id="Decision_Coverage" name="3. Coverage Determination">
        <informationRequirement>
            <requiredDecision href="#Decision_Eligibility"/>
        </informationRequirement>
    </decision>
    
    <decision id="Decision_Comp4. Compensation Calculationensation" name="">
        <informationRequirement>
            <requiredDecision href="#Decision_Coverage"/>
        </informationRequirement>
    </decision>

</definitions>
```

---

## Summary

This DRD shows the decision flow for processing a traffic insurance claim under Finnish law:

1. **Negative Claims** - First check if any exclusions apply (§§41-50)
2. **Eligibility** - Verify coverage requirements (§§5-13)
3. **Coverage Determination** - Confirm the claim is covered
4. **Compensation Calculation** - Calculate the final compensation amount

Each decision node can be implemented as a separate DMN decision table or as a Python/JSON decision service.

---

*Generated: February 2026*
*Source: Liikennevakuutuslaki (460/2016)*
*Author: Molt AI*
