Title: [MISSING] §78 Portfolio Transfer Effects - No detailed DMN rule for distribution system adjustments
Labels: medium

## Gap Description

The DMN rules only reference **Section 78** of the Traffic Insurance Act in the §75 Large Loss Distribution table but lack a detailed rule for portfolio transfer effects on the distribution system.

## Law Requirements (§78)

When insurance portfolio transfers between companies (jakautuminen/vakuutuskannan luovutus):
- Costs and revenues from transferred policies belong to acquiring company
- Affects jakojärjestelmä calculations for the distribution year
- Must be accounted for when making preliminary estimates and final confirmations

## Current State
- Only mentioned as: "- §78: Vakuutuskannan siirron vaikutus (portfolio transfer effects)"
- Located in §75 Large Loss Distribution System table (line 739)

## Missing DMN Rule

**Suggested:** Create `S2: Portfolio Transfer Distribution Adjustment (§78)`

### Decision Table Structure
| portfolioTransfer.occurred | transfer.type | transfer.date | distribution.year | acquiringCompany | originalCompany | Output |
|---------------------------|---------------|---------------|-------------------|------------------|-----------------|--------|
| true | Jakautuminen | beforeEstimate | current | CompanyB | CompanyA | **CostsRevenues_TransferredToB** |
| true | KannanLuovutus | duringYear | current | CompanyB | CompanyA | **DistributionShare_CalculatedPerTransferDate** |
| false | any | any | any | any | any | **NormalDistributionRulesApply** |

## Severity
**MEDIUM** - Affects accuracy of distribution system calculations when portfolios transfer.

## Reference
Liikennevakuutuslaki §78

---
*Identified during automated compliance check - 2026-02-26*
*cc @VilleMoltBot*
