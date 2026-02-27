Title: [MISSING] §§93-94 Insolvency Additional Premium and Joint Guarantee - No DMN rules for insurer insolvency procedures
Labels: medium

## Gap Description

The DMN rules only cover **Section 92** (insolvency protection) but are missing **Sections 93-94**, which govern additional premium obligations and joint guarantee payments when an insurer enters insolvency.

## Law Requirements

### §93 - Additional Premium Obligation (Lisävakuutusmaksu)
- Applies when compensation remains unsecured after policyholder additional payment obligation
- Excludes consumers and small businesses (rinnastettavissa kuluttajaan)
- Applies to those with significant management influence over insurer
- Based on economic benefit from artificially low premiums
- Maximum 3-year lookback period
- LVK makes decision on amount and payment

### §94 - Joint Guarantee Payment (Yhteistakuumaksu)
- All traffic insurers jointly guarantee unpaid compensation after §93
- Funded by annual yhteistakuumaksu from all traffic insurers
- Maximum 2% of premium income per year
- Directly enforceable without court order (ulosottokelpoinen)
- Interest charged for late payment

## Current State
- Only §92 covered: `E13: Insolvency Protection (§92)` at line 690
- §93-94 not addressed

## Missing DMN Rule

**Suggested:** Create `INSOL-002: Insolvency Additional Premium and Joint Guarantee (§§93-94)`

### Decision Table Structure (§93)
| policyholder.type | management.influence | economic.benefitLowPremiums | lookback.years | Output |
|------------------|---------------------|----------------------------|----------------|--------|
| Consumer | any | any | any | **Exempt_FromAdditionalPremium** |
| SmallBusiness | any | any | any | **Exempt_FromAdditionalPremium** |
| LargeBusiness | true | true | ≤3 | **AdditionalPremiumRequired** |
| LargeBusiness | false | any | any | **Exempt_NoInfluence** |

### Decision Table Structure (§94)
| compensation.unsecuredAfter93 | insurer.insolvent | jointGuarantine.assessment | totalPremiumIncome | Output |
|------------------------------|-------------------|---------------------------|-------------------|--------|
| >0 | true | true | X | **Yhteistakuumaksu_Required_Max2PercentOfX** |
| 0 | true | false | any | **NoJointPaymentRequired** |

## Severity
**MEDIUM** - Important for understanding full insolvency protection mechanism.

## Reference
Liikennevakuutuslaki §§93-94

---
*Identified during automated compliance check - 2026-02-26*
*cc @VilleMoltBot*
