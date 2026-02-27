Title: [MISSING] §30 Vehicle Use Prohibition - No DMN rule for uninsured vehicle use ban
Labels: high

## Gap Description

The DMN rules are missing coverage for **Section 30** of the Traffic Insurance Act, which establishes the prohibition on using uninsured vehicles in traffic.

## Law Requirements (§30)

1. **§30(1):** Vehicle use in traffic is PROHIBITED when insurance obligation has been neglected
   - "Ajoneuvon, jonka vakuuttamisvelvollisuus on laiminlyöty, käyttö liikenteessä on kielletty."

2. **§30(2):** Authority enforcement powers referenced in ajoneuvolaki 84 §

## Missing DMN Rule

**Suggested:** Create `PROH-001: Vehicle Use Prohibition When Uninsured (§30)`

### Decision Table Structure
| insurance.obligationMet | insurance.exists | vehicle.usedInTraffic | enforcement.authority | Output |
|------------------------|------------------|----------------------|----------------------|--------|
| false | false | true | Police | **UseProhibited_EnforcementAction** |
| false | false | false | any | **NoViolation** |
| true | true | true | any | **UseAllowed** |

## Severity
**HIGH** - Important for compliance monitoring and enforcement scenarios.

## Reference
Liikennevakuutuslaki §30

---
*Identified during automated compliance check - 2026-02-26*
*cc @VilleMoltBot*
