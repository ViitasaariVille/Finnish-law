## Gap Description

The DMN rules are missing **Sections 23-25** which govern premium refunds on termination, late payment interest, and liability continuation when premiums are unpaid.

## Law Requirements

### §23 - Premium Refund on Early Termination
- If insurance ends before agreed date, insurer is entitled to premium only for active period
- Refund must be paid to policyholder
- No refund required if less than €8

### §24 - Late Payment Interest
- Interest on unpaid premiums: annual rate per Interest Act (korkolaki)
- Interest on delayed refunds: same rate from 1 month after refund claim received

### §25 - Liability Continuation and Enforceability
- **Key provision:** Insurer liability does NOT end even if premium unpaid
- Premium + interest is directly enforceable (ulosottokelpoinen)

## Why This Matters

These sections contain important consumer protections and enforcement mechanisms. §25(1) is particularly critical - coverage continues even without payment.

## Missing DMN Rules

**Suggested:** 
- `REFUND-001: Premium Refund on Termination (§23)`
- `INTEREST-001: Late Payment Interest (§24)`
- `LIAB-001: Liability Continuation When Premium Unpaid (§25)`

### §25 Critical Rule

| premium.paid | premium.overdue | insurer.liability | enforcement.available |
|-------------|-----------------|-------------------|----------------------|
| false | true | **CONTINUES** | yes |
| false | true | **CONTINUES** | yes |

**Important:** This is a consumer protection - insurance coverage cannot be terminated for non-payment alone.

## Severity

**HIGH** - Important for policy termination and enforcement scenarios.

## Reference

Liikennevakuutuslaki §§23-25

---
*Identified during law compliance check - February 26, 2026*

cc @VilleMoltBot