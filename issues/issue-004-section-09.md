## Gap Description

The DMN rules are missing §9 which mandates insurers to report certain events to Liikenteen turvallisuusvirasto (Traficom) within 7 days.

## Law Reference

**§9:**
> Vakuutusyhtiön on ilmoitettava Liikenteen turvallisuusvirastolle:
> 1) yhtiössä vakuutetulle ajoneuvolle otetusta uudesta vakuutuksesta seitsemän päivän kuluessa uuden vakuutuksen alkamisesta;
> 2) ajoneuvolle otetun vakuutuksen vakuutusmaksun laiminlyönnistä;
> 3) liikennekäytöstä poistetun ajoneuvon vakuutuksen irtisanomisesta.

**Reporting Requirements:**
1. New insurance policies → within 7 days of policy start
2. Premium payment defaults → notification required
3. Traffic removal vehicle policy cancellations → notification required

## Current DMN Status

- §90 covers Traficom→LVK reporting
- **NO rule for Insurer→Traficom reporting under §9**

## Missing DMN Rule

#### REPORT-001: Insurer Reporting to Traficom (§9)

| event.type | event.date | daysSinceEvent | traficom.notified | Output |
|------------|------------|----------------|-------------------|--------|
| NewPolicy | any | ≤7 | true | **Compliant** |
| NewPolicy | any | >7 | false | **NonCompliant_7DayDeadline** |
| PremiumDefault | any | any | true | **Compliant** |
| PremiumDefault | any | any | false | **NonCompliant** |
| TrafficRemovalCancellation | any | any | true | **Compliant** |
| TrafficRemovalCancellation | any | any | false | **NonCompliant** |

## Severity: HIGH

- **Regulatory compliance requirement**
- Enables Traficom enforcement of insurance obligations
- Links to §90 LVK penalty assessment

## Related Sections

- §90: Traficom reporting to LVK
- §27-28: Uninsured vehicle penalties

## Tags

@VilleMoltBot for review

---
*Identified during law compliance check - February 26, 2026*
