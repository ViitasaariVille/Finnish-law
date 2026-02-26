## Gap Description

The DMN rules are missing §51 which defines how liability is apportioned between multiple insurance companies when two or more vehicles are involved in the same accident.

## Law Reference

**§51:**
> Jos kaksi tai useampi vakuutusyhtiö on vastuussa samasta liikennevahingosta, vakuutusyhtiöt vastaavat korvauksesta yhteisvastuullisesti sen mukaan kuin ilmenneeseen tuottamukseen ja muihin vahingon aiheuttaneisiin seikkoihin katsoen on kohtuullista. Jos vahinko on kuitenkin johtunut yksinomaan tietyn ajoneuvon puutteellisuudesta, virheellisestä kuormauksesta tai sen puolella olevasta tuottamuksesta, korvauksesta vastaa tälle ajoneuvolle vakuutuksen antanut vakuutusyhtiö.

**Key Principles:**
1. Multiple insurers → joint liability (yhteisvastuu)
2. Apportionment based on negligence/contributing factors
3. If damage caused SOLELY by one vehicle's defect/loading/negligence → that vehicle's insurer pays entirely

## Current DMN Status

- §33 covers multi-vehicle accident liability determination
- §52 covers rail-road liability apportionment (RAIL-001, RAIL-002)
- **NO rule for insurer-to-insurer apportionment under §51**

## Missing DMN Rule

#### INS-APPORTION-001: Multi-Insurer Liability Apportionment (§51)

| involvedInsurers.count | fault.determined | fault.soleVehicle | fault.soleVehicle.insurer | Output |
|-----------------------|------------------|-------------------|--------------------------|--------|
| 1 | any | N/A | N/A | **SingleInsurerLiable** |
| >1 | true | true | identified | **SoleVehicleInsurer_PaysFull** |
| >1 | true | false | N/A | **JointLiability_ByFaultRatio** |
| >1 | false | N/A | N/A | **JointLiability_EqualShares** |

## Severity: HIGH

- **Essential for multi-vehicle accident claims**
- Determines which insurer pays what share
- Currently undefined behavior for multi-insurer scenarios

## Related Sections

- §33: Multi-vehicle accident liability
- §52: Rail-road apportionment (similar logic)
- RAIL-001, RAIL-002

## Tags

@VilleMoltBot for review

---
*Identified during law compliance check - February 26, 2026*
