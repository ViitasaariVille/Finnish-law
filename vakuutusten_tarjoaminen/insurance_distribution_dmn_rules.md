# Finnish Insurance Distribution - DMN Business Rules

**Based on:** Laki vakuutusten tarjoamisesta (Insurance Distribution Act) 234/2018  
**Version:** 1.0  
**Source:** https://www.finlex.fi/fi/lainsaadanto/2018/234

---

## 1. Registration Requirement

| **OUTPUT: Must Register** | Entity Type | Activity Level | Legal Basis | Source Text |
|--------------------------|-------------|----------------|-------------|-------------|
| MustRegister | InsuranceBroker | Primary | Section 6(1) | Vakuutusmeklari rekisteröitävä |
| MustRegister | InsuranceAgent | Any | Section 6(1) | Asiamies rekisteröitävä |
| NotRequired | InsuranceCompany | Any | Section 6(3) | Vakuutuksenantajat |
| LimitedRegistration | PartTimeAgent | Within limits | Section 4 | Sivutoiminen vakuutusedustaja |

---

## 2. Broker Registration Conditions

| **OUTPUT: Registration Allowed** | Condition | Legal Basis | Source Text |
|--------------------------------|-----------|-------------|-------------|
| Yes | Not employed by single insurer | Section 8(1) | Yhden vakuutuksenantajan palveluksessa |
| Yes | Registered in Finland | Section 8(2) | Rekisteröity Suomessa |
| Yes | Not bankrupt | Section 8(3) | Ei konkurssissa |
| Yes | Good reputation | Section 8(4) | Hyvä maine |
| Yes | Professional qualification | Section 8(5) | Ammattipätevyys |
| Yes | Liability insurance | Section 8(6) | Vastuuvakuutus |
| Yes | Client asset system | Section 8(7) | Asiakasvarajärjestelmä |
| Yes | 30% staff registered | Section 8(8) | 30% henkilökunnasta rekisteröity |

---

## 3. Good Reputation

| **OUTPUT: Good Reputation** | Condition | Legal Basis | Source Text |
|---------------------------|-----------|-------------|-------------|
| Yes | No relevant conviction | Section 16 | Ei tuomio |
| No | Prison sentence within 5 years | Section 16 | Vankeusrangaistus 5 vuoden aikana |
| No | Fine sentence within 3 years | Section 16 | Sakkorangaistus 3 vuoden aikana |
| No | Active bankruptcy | Section 16 | Konkurssissa |
| No | Active business ban | Section 16 | Liiketoimintakielto |

---

## 4. Professional Qualification

| **OUTPUT: Qualified** | Condition | Legal Basis | Source Text |
|----------------------|-----------|-------------|-------------|
| Qualified | Broker exam passed | Section 18 | Vakuutusmeklaritutkinto |
| Qualified | Equivalent qualification | Section 18 | Vastaava pätevyys |
| NotQualified | No qualification | Section 18 | Ei pätevyysvaatimuksia |
| Exempt | Transitional provision | Section 84 | Siirtymäsäännös |

---

## 5. Continuing Education

| **OUTPUT: Compliant** | Training Hours | Legal Basis | Source Text |
|----------------------|----------------|-------------|-------------|
| Compliant | >= 15 hours/year | Section 20 | 15 tuntia vuodessa |
| NonCompliant | < 15 hours/year | Section 20 | Alle 15 tuntia |

---

## 6. Disclosure - Insurer

| **OUTPUT: Must Disclose** | Information | Legal Basis | Source Text |
|--------------------------|-------------|-------------|-------------|
| Required | Insurer name | Section 32(1) | Vakuutuksenantajan nimi |
| Required | Contact information | Section 32(1) | Yhteystiedot |
| Required | Licensing status | Section 32(1) | Lupatiedot |
| Required | Advisory services | Section 32 | Neuvontapalvelut |
| Required | Complaint procedures | Section 32 | Valitusmenettelyt |

---

## 7. Disclosure - Broker

| **OUTPUT: Must Disclose** | Information | Legal Basis | Source Text |
|--------------------------|-------------|-------------|-------------|
| Required | Registration number | Section 33 | Rekisterinumero |
| Required | Register verification | Section 33 | Rekisteriotteen |
| Required | Principals represented | Section 33 | Päämiesten tiedot |
| Required | Commission structure | Section 38 | Palkkio- ja palkkiosuoriteperusteet |
| Required | Conflicts of interest | Section 33 | Eturistiriidat |
| Required | Ownership >10% | Section 33 | Omistus >10% |
| IfRecommended | Recommendation basis | Section 37 | Suosituksen perusteet |

---

## 8. Needs Assessment

| **OUTPUT: Required Action** | Situation | Legal Basis | Source Text |
|---------------------------|-----------|-------------|-------------|
| MustAssess | Broker offers insurance | Section 35 | Vakuutusmeklari tarjoaa vakuutuksia |
| Collect | Existing coverage | Section 35 | Olemassa olevat vakuutukset |
| Collect | Risk profile | Section 35 | Riskiprofiili |
| Collect | Financial situation | Section 35 | Taloudellinen tilanne |

---

## 9. Product Governance

| **OUTPUT: Required** | Requirement | Legal Basis | Source Text |
|----------------------|-------------|-------------|-------------|
| Required | Target market definition | Section 42(2) | Kohdemarkkinan määrittely |
| Required | Risk assessment | Section 42(3) | Riskiarviointi |
| Required | Distribution plan | Section 42(4) | Jakelusuunnitelma |
| Required | Regular review | Section 42 | Säännöllinen tarkistaminen |

---

## 10. Investment Insurance - Suitability

| **OUTPUT: Assessment** | Customer Type | Recommendation | Legal Basis | Source Text |
|------------------------|---------------|----------------|-------------|-------------|
| MustAssess | Any | Personal recommendation | Section 50 | Soveltuvuuden arviointi |
| MustAssessAppropriateness | Any | No advice | Section 49 | Asianmukaisuuden arviointi |
| Exempt | Professional customer | Any | Section 54 | Ammattimainen asiakas |

---

## 11. Investment Insurance - Suitability Factors

| **OUTPUT: Assess** | Factor | Legal Basis | Source Text |
|-------------------|--------|-------------|-------------|
| Required | Customer experience | Section 50 | Kokemus |
| Required | Customer knowledge | Section 50 | Tietämys |
| Required | Financial situation | Section 50 | Taloudellinen tilanne |
| Required | Investment objectives | Section 50 | Sijoitustavoitteet |
| Required | Risk tolerance | Section 50 | Riskinsietokyky |

---

## 12. Professional Liability Insurance

| **OUTPUT: Minimum Coverage** | Coverage Type | Legal Basis | Source Text |
|---------------------------|---------------|-------------|-------------|
| 1,564,610 EUR | Per claim | Section 58(1) | Korvausvaade |
| 2,315,610 EUR | Annual aggregate | Section 58(1) | Vuosittainen kokonaiskorvaus |
| EEA | Geographic scope | Section 58(2) | Koko ETA-alue |
| >= 2 months | Cancellation notice | Section 58(2) | vähintään 2 kk irtisanomisaika |

---

## 13. Client Asset Segregation

| **OUTPUT: Requirement** | Situation | Legal Basis | Source Text |
|------------------------|-----------|-------------|-------------|
| Segregate | Holds client funds | Section 59 | Asiakasvarat eriytettävä |
| SeparateAccount | Bank account | Section 59 | Erillinen tili |
| PromptTransfer | To beneficiary | Section 59 | Siirto edunsaajalle |
| Prohibited | Consumer funds held | Section 59 | Kuluttajan varat |

---

## 14. Cross-Border Notification

| **OUTPUT: Required** | Activity | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Notify | EEA operations planned | Section 22 | ETA-toiminta |
| Provide | Registered details | Section 22 | Rekisteritiedot |
| Provide | Principals | Section 22 | Päämiesten tiedot |
| Provide | Insurance types | Section 22 | Vakuutuslajit |
| Provide | Target countries | Section 22 | Kohdemaat |
| IfEstablishment | Branch address | Section 22(2) | Toimipaikan osoite |
| IfEstablishment | Responsible person | Section 22(2) | Vastuuhenkilö |

---

## 15. Marketing Requirements

| **OUTPUT: Compliant** | Requirement | Legal Basis | Source Text |
|----------------------|-------------|-------------|-------------|
| MustIdentify | As marketing | Section 34 | Tunnistettava markkinoinniksi |
| Required | Accurate information | Section 34 | Täsmälliset tiedot |
| Prohibited | Misleading | Section 34 | Ei harhaanjohtavaa |

---

## 16. Tying and Bundling

| **OUTPUT: Rule** | Customer Type | Situation | Legal Basis | Source Text |
|-----------------|---------------|-----------|-------------|-------------|
| Prohibited | Consumer | Tied to other | Section 40 | Kielletty kuluttajalle |
| Required | Consumer | Offer separately | Section 40 | Tarjottava erikseen |
| RequiredDisclosure | Business | Bundled | Section 41 | Ilmoitettava erikseen ostosta |

---

## 17. Investment Insurance - Conflicts

| **OUTPUT: Required** | Situation | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| MustDisclose | Conflict of interest | Section 45 | Eturistiriita |
| MustNotImpair | Incentive received | Section 46 | Ei saa heikentää laatua |

---

## 18. Regular Service Summary

| **OUTPUT: Required** | Service Type | Legal Basis | Source Text |
|---------------------|--------------|-------------|-------------|
| Provide | Ongoing broker service | Section 52 | Palveluiden yhteenveto |
| Frequency | At least annually | Section 52 | Vuosittain |

---

## 19. Sustainability Disclosure

| **OUTPUT: Required** | Condition | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Required | Investment insurance | Section 54a | Kestävyysriskit |
| Required | >3 employees | Section 54a | yli 3 työntekijää |

---

## 20. Administrative Sanctions

| **OUTPUT: Sanction** | Violation | Legal Basis | Source Text |
|---------------------|-----------|-------------|-------------|
| Prohibition | Unregistered operation | Section 70 | Toiminnan kieltäminen |
| AdministrativeFine | Serious violation | Section 71 | Seuraamusmaksu |
| PublicWarning | Public interest at risk | Section 71 | Julkinen varoitus |
| Deregistration | Repeated violations | Section 73 | Poistaminen rekisteristä |

---

## 21. Compensation Liability

| **OUTPUT: Liable** | Breach | Legal Basis | Source Text |
|-------------------|--------|-------------|-------------|
| BrokerLiable | Breach of duty | Section 74 | Välitysvelvollisuuden rikkominen |
| Compensate | Information omission | Section 74 | Tiedonantovelvollisuuden laiminlyönti |
| InsurerLiable | Breach of §§30,34,45,46 | Section 75 | Vakuutuksenantajan korvausvastuu |

---

## 22. Confidentiality

| **OUTPUT: Allowed** | Purpose | Legal Basis | Source Text |
|--------------------|---------|-------------|-------------|
| Protected | Customer information | Section 79 | Salassapitovelvollisuus |
| Allowed | Authority request | Section 80 | Viranomaisen pyyntö |
| Allowed | Legal proceedings | Section 80 | Oikeudenkäynti |
| Allowed | Research (no harm) | Section 80 | Tutkimus |

---

## 23. Document Retention

| **OUTPUT: Period** | Document Type | Legal Basis | Source Text |
|-------------------|---------------|-------------|-------------|
| 5 years minimum | Qualification records | Section 78 | Pätevyysasiakirjat |
| 5 years minimum | Customer contracts | Section 78(2) | Sopimukset |
| 5 years minimum | Training records | Section 78 | Koulutustiedot |
| 5 years minimum | Whistleblowing records | Section 72 | Ilmoitustiedot |

---

## 24. Whistleblowing Procedure

| **OUTPUT: Required** | Requirement | Legal Basis | Source Text |
|---------------------|-------------|-------------|-------------|
| MustEstablish | Reporting procedure | Section 72(1) | Ilmoitusmenettely |
| MustProtect | Reporter identity | Section 72 | Suojaa ilmoittaja |
| MustRetain | Records 5 years | Section 72(2) | Säilytys 5 vuotta |

---

## 25. Right to Appeal

| **OUTPUT: Forum** | Decision Type | Legal Basis | Source Text |
|-------------------|---------------|-------------|-------------|
| AdministrativeCourt | Board decision | Section 65 | Hallinto-oikeus |
| AdministrativeCourt | FIN-FSA decision | Section 82 | Hallinto-oikeus |

---

*Total: 25 decision tables covering all major requirements of the Insurance Distribution Act (234/2018)*
