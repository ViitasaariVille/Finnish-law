# Finnish Unemployment Protection Act - DMN Business Rules

**Based on:** Työttömyysturvalaki (Unemployment Protection Act) 1290/2002  
**Version:** 1.0  
**Source:** https://www.finlex.fi/fi/lainsaadanto/2002/1290

---

## 1. Unemployment Benefit Types

| **OUTPUT: Benefit Type** | Person Type | Legal Basis | Source Text |
|-------------------------|-------------|-------------|-------------|
| Earnings-related or basic | Employee | Section 1 | Palkansaaja |
| Earnings-related | Entrepreneur | Section 1 | Yrittäjä |
| Labour market support | No insurance | Section 7 | Työmarkkinatuki |
| Earnings-related from fund | Fund member | Section 5 | Työttömyyskassan jäsen |

---

## 2. Employment Condition - Employee

| **OUTPUT: Requirement Met** | Condition | Legal Basis | Source Text |
|---------------------------|----------|-------------|-------------|
| Yes | At least 12 months in last 24 months | Section 5.3 | 12 kuukautta |
| Yes | At least 18 hours per week | Section 5.3 | 18 tuntia viikossa |
| Yes | Employment ended not by own choice | Section 5.3 | Työsuhde päättynyt |

---

## 3. Employment Condition - Entrepreneur

| **OUTPUT: Requirement Met** | Condition | Legal Basis | Source Text |
|---------------------------|----------|-------------|-------------|
| Yes | At least 24 months in last 48 months | Section 5.7 | 24 kuukautta |
| Yes | At least 13,457 EUR annual income | Section 5.7 | Tuloraja |
| Yes | Business actively conducted | Section 5.7 | Aktiivinen toiminta |

---

## 4. Benefit Amount Calculation

| **OUTPUT: Amount** | Type | Legal Basis | Source Text |
|--------------------|------|-------------|-------------|
| 45% of wage difference | Earnings-related | Section 6.2 | Ansio-osa |
| 33.66 EUR/day | Basic | Section 6.1 | Perusosa |
| Additional for children | With children | Section 6.3 | Lapsikorotus |
| Higher rate | Over 58 years | Section 6.9 | Yli 58-vuotias |

---

## 5. Benefit Duration

| **OUTPUT: Duration** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| 300 days | First-time benefit | Section 6.7 | 300 päivää |
| New period | After new employment | Section 6.7 | Uusi jakso |
| Additional days | Over 61 years | Section 6.9 | Lisäpäivät |
| Proportional | Short employment | Section 6.7 | Suhteutettu |

---

## 6. Adjusted Benefit

| **OUTPUT: Adjustment** | Condition | Legal Basis | Source Text |
|------------------------|-----------|-------------|-------------|
| Reduced by earnings | Part-time work | Section 4.1 | Osittainen työ |
| Full benefit | Earnings below limit | Section 4.4 | Tuloraja |
| No benefit | Full-time work | Section 4.1 | Kokoaikatyö |
| Adjusted daily | Calculation | Section 4.5 | Päivittäin |

---

## 7. Labour Market Policy Conditions

| **OUTPUT: Required** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Must be | Registered job seeker | Section 2.1 | Rekisteröity työnhakija |
| Must be | Available for work | Section 2.1 | Työmarkkinoiden käytettävissä |
| Must | Actively seek work | Section 2.1 | Aktiivisesti etsittävä työtä |
| Must | Attend interview | Section 2.1 | Haastatteluun osallistuttava |

---

## 8. Job Refusal Consequences

| **OUTPUT: Consequence** | Situation | Legal Basis | Source Text |
|-------------------------|-----------|-------------|-------------|
| 50% reduction for 60 days | Refused without reason | Section 2a.4 | 50% 60 päivää |
| Cut off for 90 days | Repeated refusal | Section 2a.10 | Korvauskatko 90 päivää |
| No consequence | Acceptable reason | Section 2a.2 | Pätevä syy |
| May affect | Refused training | Section 2a.14 | Koulutuksesta kieltäytyminen |

---

## 9. Acceptable Reasons for Refusal

| **OUTPUT: Acceptable** | Reason | Legal Basis | Source Text |
|------------------------|--------|-------------|-------------|
| Acceptable | Health reasons | Section 2a.5 | Terveydelliset syyt |
| Acceptable | Family reasons | Section 2a.5 | Perhesyyt |
| Acceptable | Starting education | Section 2a.5 | Koulutus |
| Acceptable | Excessive travel distance | Section 2a.7 | Matka-aika |

---

## 10. Self-Employment Conditions

| **OUTPUT: Eligible** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Eligible | Business ended | Section 2.5 | Yritystoiminta päättynyt |
| Eligible | Family member stopped | Section 2.7 | Perheenjäsenen työ |
| Eligible | Starting new business | Section 5a | Alkava yritystoiminta |
| Eligible | Income verified | Section 5.7 | Tulo todennettu |

---

## 11. Study and Benefit

| **OUTPUT: Effect** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| No benefit | Full-time study | Section 2.10 | Päätoiminen opiskelu |
| May receive | Part-time study | Section 2.10 | Sivutoiminen |
| Qualifies | Vocational training | Section 2.13 | Ammatillinen koulutus |
| Benefit after | Studies ended | Section 2.11 | Opintojen päättyminen |

---

## 12. Restrictions on Benefit

| **OUTPUT: Restricted** | Condition | Legal Basis | Source Text |
|------------------------|-----------|-------------|-------------|
| No benefit | During imprisonment | Section 3.1 | Vankeusrangaistus |
| Limited | While abroad | Section 3.1 | Ulkomailla |
| No benefit | During strike | Section 3.1 | Lakko |
| Reduced/denied | High income | Section 3.7 | Tulot |

---

## 13. Waiting Period

| **OUTPUT: Period** | Condition | Legal Basis | Source Text |
|--------------------|-----------|-------------|-------------|
| 7 days | First benefit | Section 5.13 | 7 päivää |
| New waiting period | Short work | Section 5.13 | Uusi omavastuu |
| Extended | During illness | Section 5.13 | Sairaus |
| No waiting | During activation | Section 5.13 | Aktivoinnin aikana |

---

## 14. Labour Market Support

| **OUTPUT: Eligible** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Eligible | No earnings-related benefit | Section 7.1 | Ei ansiopäivärahaa |
| Income test | Applies | Section 7.6 | Tuloharkinta |
| Must meet | Employment condition | Section 7.1 | Työssäoloehto |
| Age limit | Under 65 | Section 7.1 | Alle 65-vuotias |

---

## 15. Mobility Support

| **OUTPUT: Eligible** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Eligible | Moving for suitable job | Section 8.1 | Työn perusteella muutto |
| Eligible | Over 150 km from home | Section 8.1 | 150 km |
| Eligible | Permanent job over 2 years | Section 8.1 | Vakituinen työ |
| Amount | One-time 500 EUR | Section 8.2 | 500 euroa |

---

## 16. Redundancy Payment

| **OUTPUT: Eligible** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Eligible | Due to layoff or bankruptcy | Section 9.1 | Lomautus tai konkurssi |
| Eligible | At least 5 years employment | Section 9.1 | 5 vuotta |
| Eligible | Did not refuse re-employment | Section 9.3 | Ei ole kieltäytynyt |
| Amount | Based on tenure and wages | Section 9.2 | Laskenta |

---

## 17. Employment Services Benefit

| **OUTPUT: Eligible** | Service | Legal Basis | Source Text |
|----------------------|---------|-------------|-------------|
| Eligible | During training | Section 10.1 | Koulutus |
| Eligible | During rehabilitation | Section 10.1 | Kuntoutus |
| Eligible | During work placement | Section 10.1 | Työpaikalla |
| No penalty | Acceptable reason for absence | Section 10.3 | Pätevä syy |

---

## 18. Application and Payment

| **OUTPUT: Procedure** | Step | Legal Basis | Source Text |
|----------------------|------|-------------|-------------|
| Submit to | Fund or Kela | Section 11.1 | Hakemus |
| Decision within | 30 days | Section 11.1a | 30 päivää |
| Paid | Every two weeks | Section 11.5 | Kahden viikon välein |
| Method | To account | Section 11.5 | Tilisiirtona |

---

## 19. Recovery of Overpayment

| **OUTPUT: Recovery** | Situation | Legal Basis | Source Text |
|----------------------|-----------|-------------|-------------|
| Full recovery | Intentional | Section 11.10 | Tahallinen |
| May recover part | Negligent | Section 11.10 | Huolimaton |
| May pay installments | Repayment | Section 11.10 | Erissä |
| May deduct | From future benefits | Section 11.13 | Kuittaus |

---

## 20. Appeal Procedure

| **OUTPUT: Right** | Step | Legal Basis | Source Text |
|-------------------|------|-------------|-------------|
| Appeal to | Unemployment security board | Section 12.1 | Työttömyysturvalautakunta |
| Within | 30 days of decision | Section 12.1 | 30 päivää |
| Can request | Correction | Section 12.4 | Itseoikaisu |
| Final appeal | To court | Section 12.1 | Hallinto-oikeus |

---

## 21. International Coordination

| **OUTPUT: Right** | Situation | Legal Basis | Source Text |
|-------------------|-----------|-------------|-------------|
| Export | To EU/EEA | Section 8a | EU/ETA-maat |
| Count | Periods from other countries | Section 5.9 | Vakuutuskaudet |
| Can search | For job in EU | Section 8b | Työnhaku toisessa valtiossa |
| Maintains rights | Return to Finland | Section 8b | Paluu Suomeen |

---

*Total: 21 decision tables covering Työttömyysturvalaki (1290/2002)*
