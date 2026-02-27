## Gap Description

The DMN rules are missing **Section 33** which defines how liability is determined in accidents involving two or more vehicles.

## Law Requirements (§33)

**§33(1):** Liability applies to damage caused by:
1. Owner, holder, driver, or passenger negligence
2. Traffic rule violations
3. Vehicle defects or improper loading

**§33(2):** If the victim also contributed, liability is apportioned based on all contributing factors.

**§33(3):** Personal injury is compensated in full from the vehicle where the victim was passenger/driver, or victim's choice of at-fault vehicle. Inter-insurer apportionment follows §51.

## Why This Matters

While §51 (insurer apportionment) is flagged in issue-002, the underlying **liability determination** under §33 must happen first. Currently no rule defines:
- How to determine which vehicle(s) are at fault
- How victim contribution affects liability
- The priority rule for personal injury claims

## Missing DMN Rule

**Suggested:** Create `MULTI-001: Multi-Vehicle Liability Determination (§33)`

### Liability Determination Table

| involvedVehicles.count | fault.determined | victim.contribution | primaryLiableVehicle | Output |
|-----------------------|------------------|--------------------|---------------------|--------|
| >1 | true | none | identified | **PrimaryVehicleLiable** |
| >1 | true | exists | identified | **ApportionedLiability_ByContribution** |
| >1 | false | any | unknown | **JointLiability_AllVehicles** |

### Personal Injury Priority Rule

| victim.location | victim.choice | Output |
|----------------|---------------|--------|
| PassengerInVehicleA | N/A | **VehicleA_Insurance_PaysFull** |
| DriverOfVehicleA | N/A | **VehicleA_Insurance_PaysFull** |
| ThirdParty | chose VehicleB | **VehicleB_Insurance_PaysFull** |

## Severity

**CRITICAL** - Essential for all multi-vehicle accident claims.

## Related Issues

- issue-002-section-51.md (insurer apportionment)
- §51: Inter-insurer liability division

## Reference

Liikennevakuutuslaki §33

---
*Identified during law compliance check - February 26, 2026*

cc @VilleMoltBot