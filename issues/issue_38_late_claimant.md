## Problem

The DMN rules (E8d) mention late claimant protection from §38(3) but **lack the detailed recalculation logic** required when a late claimant emerges after pro-rata distribution has already occurred.

**Law (§38(3)):**
> "Jos korvausvaatimusten tultua ratkaistuiksi osoittautuu, että jollakulla, joka ei ole vielä saanut korvausta, on siihen oikeus, korvataan hänen vahinkonsa siinäkin tapauksessa, että korvauksen enimmäismäärä siten ylittää. Korvauksen määrä ei kuitenkaan saa tällöin ylittää sitä suhteellista osuutta korvauksesta, jonka korvaukseen oikeutettu olisi saanut, jos hän olisi alun perin ollut korvauksensaajien joukossa."

## Gap Analysis

| Requirement | DMN Status |
|-------------|------------|
| €5M cap | ✅ E8b implemented |
| Pro-rata distribution | ✅ E8c implemented |
| Late claimant protection | ⚠️ E8d mentioned but **incomplete** |
| Recalculation formula | ❌ **MISSING** |

## Complex Scenario Not Handled

1. Claims distributed: A=€2M, B=€2M, C=€1M (total €5M cap reached)
2. Late claimant D emerges with €1M claim
3. Required: Recalculate all shares proportionally
4. New distribution: A=€1.67M, B=€1.67M, C=€0.83M, D=€0.83M
5. A and B must refund excess amounts

## Impact

Late claimants may not receive correct proportional share, or the €5M cap may be incorrectly exceeded.

## Suggested Fix

Complete **E8d** with recalculation formula:

```
originalShare = claim.amount / totalClaims × cap
lateClaimantShare = lateClaim.amount / (totalClaims + lateClaim.amount) × cap
adjustmentRequired = originalShare - newShare
```

## References
- laws/liikennevakuutuslaki.txt §38(3)
- Current DMN: E8d (incomplete)

---
**Severity:** CRITICAL - Financial cap protection
**Section:** §38
**Tagging @VilleMoltBot for review
