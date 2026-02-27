## Gap Description

The DMN rules are missing **Section 64** which establishes the Traffic Damage Board (Liikennevahinkolautakunta) and its role in compensation disputes.

## Law Requirements (§64)

While §§65-66 are covered (opinion requests and mandatory opinion triggers), §64 itself establishes:

1. **Board Establishment** - Legal basis for the Liikennevahinkolautakunta
2. **Board Composition** - Members, administration, funding
3. **Board Authority** - To issue opinions on compensation matters
4. **Relationship to Courts** - Board opinions vs. court decisions (§65(2))

## Current DMN Status

- §65 - Opinion request rights (covered)
- §66 - Mandatory opinion triggers (MOP-001 covered)
- **§64 - Board establishment and authority (NOT covered)**

## Why This Matters

The Board serves as an important alternative dispute resolution mechanism. While the procedural details are in separate legislation (Liikennevahinkolautakunnasta annettu laki 441/2002), §64 establishes its role within the traffic insurance framework.

## Missing DMN Rule

**Suggested:** `BOARD-001: Traffic Damage Board Authority (§64)`

### Board Jurisdiction Table

| dispute.type | court.decision.final | board.canIssueOpinion | Output |
|-------------|---------------------|----------------------|--------|
| CompensationDispute | false | true | **BoardOpinion_Available** |
| CompensationDispute | true | false | **BoardCannot_OverrideCourt** |
| MandatoryCategories | N/A | true | **BoardOpinion_Required** |

## Severity

**MEDIUM** - Board procedures are largely administrative, but establishing its authority provides context for §§65-66 rules.

## Related Issues

- §65: Opinion request rights
- §66: Mandatory opinion requirements (MOP-001)

## Reference

Liikennevakuutuslaki §64
Liikennevahinkolautakunnasta annettu laki (441/2002)

---
*Identified during law compliance check - February 26, 2026*

cc @VilleMoltBot