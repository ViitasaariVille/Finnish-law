## Gap Description

The DMN rules are missing §10(3) which defines a critical 7-day liability termination rule when registered vehicles are not properly identified in insurance contracts.

## Law Reference

**§10(3):**
> Jos rekisteriin merkittyä ajoneuvoa ei ole vakuutussopimuksessa yksilöity ja tällaisen ajoneuvon omistus- tai hallintaoikeuden siirtymisestä vakuutuksenottajalle ei ole tehty ilmoitusta rekisteriin seitsemän päivän kuluessa muutoksen tapahtumisesta, vakuutusyhtiön vastuu lakkaa sanotun määräajan päättyessä. Jos muutosilmoitus rekisteriin tehdään myöhemmin, vakuutusyhtiön vastuu alkaa uudelleen ilmoituksen tekemisestä.

**Key Points:**
1. Registered vehicle must be identified in the insurance contract
2. If ownership/holdership changes and NOT reported to registry within 7 days → insurer liability ENDS after 7 days
3. If reported later → liability RESTARTS from the date of reporting

## Current DMN Status

- E4 covers insurance obligation start
- E15 covers 7-day coverage extension during ownership transfer
- **NO rule for liability TERMINATION when 7-day reporting window is missed**

## Missing DMN Rule

#### IDENT-001: 7-Day Liability Termination (§10(3))

| vehicle.isRegistered | vehicle.identifiedInContract | ownershipChange.reportedToRegistry | daysSinceOwnershipChange | Output |
|---------------------|------------------------------|-----------------------------------|-------------------------|--------|
| true | false | false | ≤7 | **LiabilityActive** |
| true | false | false | >7 | **LiabilityTerminated** |
| true | false | true | any | **LiabilityRestarts_FromReportDate** |
| true | true | any | any | **LiabilityActive** |
| false | any | any | any | **NotApplicable** |

## Severity: HIGH

- **Critical for coverage determination**
- Affects when insurer liability begins and ends
- Directly impacts claim validity

## Related Sections

- §6: Insurance obligation start
- §18: 7-day coverage extension after transfer
- E15: Coverage during ownership transfer

## Tags

@VilleMoltBot for review

---
*Identified during law compliance check - February 26, 2026*
