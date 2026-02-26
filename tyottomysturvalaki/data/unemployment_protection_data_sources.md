# Unemployment Protection (Työttömyysturvalaki 1290/2002) - Data Sources for Each Data Point

This file maps each data point to potential **data sources** - where the data can be obtained from.

---

## Data Point → Source Mapping

### Person Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| person.type | Työnantaja / Verotoimisto | Employment contract / Tax records | Employer / Tax |
| person.age | Väestörekisteri (DVV) | Population register | DVV / Kela |
| person.employee | Työnantaja | Employment contract | Employer |
| person.entrepreneur | Patentti- ja rekisterihallitus (PRH) | Business register | PRH |
| person.unemployment_fund_member | Työttömyyskassa | Membership register | Fund |
| person.incarcerated | Rikosseuraamuslaitos | Prison register | Prison |
| person.abroad | Rajavartiolaitos / Väestörekisteri | Border / Population | Border / DVV |
| person.striking | Ammattiliitto / Työnantaja | Union / Employer | Union / Employer |

### Job Seeker Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| jobseeker.registered | TE-palvelut | Job seeker register | UIM / TE |
| jobseeker.available | TE-palvelut | Case management | TE services |
| jobseeker.actively_seeking | TE-palvelut | Job applications | TE services |
| interview.attended | TE-palvelut | Interview records | TE services |

### Employment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| employment.months_last_24 | Työnantaja / Tulorekisteri | Payslips / Income register | Employer / Incomes Register |
| employment.hours_per_week | Työnantaja | Employment contract | Employer |
| employment.ended_reason | Työnantaja | Certificate | Employer |
| employment.date_ended | Työnantaja / UIM | Notice | Employer / UIM |
| employment.total_years | Tulorekisteri / Työeläkelaitos | Tax / Pension records | Tax / Pension |

### Entrepreneur Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| entrepreneur.months_last_48 | Työeläkelaitos (TyEL) | Pension records | Pension provider |
| entrepreneur.annual_income | Verohallinto | Tax return | Tax |
| entrepreneur.tyel_insured | Työeläkelaitos | Insurance records | Pension |
| entrepreneur.active_business | PRH | Business register | PRH |

### Business Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| business.ended | PRH | Business registration | PRH |
| business.ended_date | PRH | Registration | PRH |
| entrepreneur.family_member | Verohallinto / PRH | Tax / Register | Tax / PRH |

### Wages/Income Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| wages.12_month_total | Tulorekisteri | Incomes register | Incomes Register |
| wages.daily_average | Laskettu | Calculated | System |
| income.household | Verohallinto | Tax return | Tax |
| income.other | Verohallinto | Tax return | Tax |
| earnings.monthly | Työnantaja / Tulorekisteri | Payslips | Employer / Register |
| earnings.below_limit | Laskettu | Calculation | System |
| income.verified | Verohallinto | Tax return | Tax |

### Children Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| children.count | Väestörekisteri (DVV) | Population register | DVV |
| children.ages | Väestörekisteri (DVV) | Population register | DVV |

### Work Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| work.hours_per_week | Työnantaja | Employment contract | Employer |

### Refusal Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| refusal.occurred | TE-palvelut | Case management | TE services |
| refusal.reason | Työnhakija | Self-declaration | Job seeker |
| refusal.count_previous | Työttömyyskassa / Kela | Benefit history | Fund / Kela |
| refusal.without_acceptable | TE-palvelut | Assessment | TE services |

### Reason Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| reason.health | Terveyspalvelut | Medical certificate | Doctor |
| reason.family | Työnhakija | Self-declaration | Job seeker |
| reason.education | Koulutus | Enrollment | Institution |
| reason.distance | Kartta / Osoitteet | Distance calculation | Map |

### Study Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| study.full_time | Koulutus | Enrollment | Institution |
| study.part_time | Työnhakija | Self-declaration | Job seeker |
| study.vocational | Koulutus | Program type | Institution |
| study.ended | Koulutus / Työnhakija | Completion / Dropout | Institution / Job seeker |

### Benefit Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| benefit.first_time | Työttömyyskassa / Kela | History | Fund / Kela |
| benefit.previous_periods | Työttömyyskassa / Kela | History | Fund / Kela |
| benefit.full_amount | Laskettu | Calculation | System |

### Illness Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| illness.during_wait | Terveyspalvelut | Medical certificate | Doctor |

### Activation Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| activation.program | TE-palvelut | Service plan | TE services |

### Service Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| service.type | TE-palvelut | Service decision | TE services |
| service.start_date | TE-palvelut | Service plan | TE services |
| attendance.required | TE-palvelut | Service plan | TE services |
| absence.reason | Työnhakija | Self-declaration | Job seeker |

### Mobility Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| move.distance_km | Väestörekisteri / Osoitteet | Address change | DVV |
| job.permanent | Työnantaja | Employment contract | Employer |
| job.duration_months | Työnantaja | Contract | Employer |
| previous.residence | Väestörekisteri | Population register | DVV |

### Employer Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| employer.bankruptcy | Ulosottolaitos / Tuomioistuin | Bankruptcy register | Bankruptcy |

### Layoff Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| layoff.duration_days | Työnantaja | Notice | Employer |

### Redundancy Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| refused.reemployment | TE-palvelut | Case management | TE services |

### Application Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| application.submitted | Työttömyyskassa / Kela | Application form | Fund / Kela |
| applicant.fund_or_kela | Työttömyyskassa / Kela | Application | Fund / Kela |

### Bank Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| bank.account_finnish | Pankki | Bank account | Bank |

### Payment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| payment.frequency | Järjestelmä | System default | System |

### Overpayment Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| overpayment.amount | Laskettu | Calculation | System |
| overpayment.intentional | Selvitys | Investigation | Fund / Kela |
| overpayment.negligent | Selvitys | Investigation | Fund / Kela |
| person.financial_situation | Velkaongelmat | Assessment | Kela / Debt |

### Appeal Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| appeal.submitted | Työttömyysturvalautakunta | Appeal | Board |
| decision.received_date | Työttömyyskassa / Kela | Notice | Fund / Kela |
| appeal.within_30_days | Laskettu | Date calculation | System |
| decision.type | Työttömyyskassa / Kela | Decision | Fund / Kela |

### International Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| work.country_eu | Työnantaja / Ulkomaille | Employment abroad | Employer |
| insurance.periods_other_country | Ulkomainen vakuutuslaitos | Foreign records | Country |
| job.search_eu | Työnhakija | Job applications | Job seeker |
| return.finland | Väestörekisteri | Population register | DVV |

---

## Data Source Summary by Authority

### Government Registers

| Authority | Register | Data Points |
|-----------|----------|-------------|
| **DVV** (Väestörekisterikeskus) | Population register | person.age, children.*, person.abroad, previous.residence, return.finland |
| **Verohallinto** (Tax Administration) | Tax returns / Tulorekisteri | wages.*, income.*, entrepreneur.*, employment.* |
| **PRH** (Patentti- ja rekisterihallitus) | Business register | entrepreneur.*, business.* |
| **TE-palvelut** (Employment Services) | Job seeker register | jobseeker.*, refusal.*, activation.*, service.*, refused.reemployment |
| **Kela** | Benefits register | benefit.*, person.*, children.* |
| **Työttömyyskassat** | Fund membership | person.unemployment_fund_member, benefit.*, application.*, appeal.* |
| **Ulosottolaitos** | Bankruptcy register | employer.bankruptcy |
| **Rikosseuraamuslaitos** | Prison register | person.incarcerated |

### Pension & Insurance

| Organization | Database | Data Points |
|-------------|----------|-------------|
| **Työeläkelaitos** (Pension providers) | TyEL records | entrepreneur.tyel_insured, employment.total_years |
| **Ulkomaiset vakuutuslaitokset** | Foreign insurance | insurance.periods_other_country |

### Employers

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **Työnantajat** | Employment contracts, notices | employment.*, work.*, job.*, layoff.*, employer.bankruptcy, work.country_eu |

### Healthcare & Education

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **Terveyspalvelut** (SOTE) | Medical certificates | reason.health, illness.during_wait |
| **Koulutus** (Education) | Enrollments | reason.education, study.* |

### Unions & Organizations

| Organization | Source | Data Points |
|-------------|--------|-------------|
| **Ammattiliitot** | Membership | person.striking |

---

## API Integration Potential

### Real-Time APIs

| API | Provider | Data Points |
|-----|----------|-------------|
| Tulorekisteri (Incomes Register) | Verohallinto | wages.*, income.*, employment.months |
| Population Register API | DVV | person.*, children.*, previous.residence |
| Business Register API | PRH | entrepreneur.*, business.* |
| TyEL API | Työeläkelaitos | entrepreneur.tyel_insured |
| Job Seeker Register | TE-palvelut | jobseeker.*, refusal.* |
| Kela API | Kela | benefit.* |

### Batch Data

| Source | Update Frequency | Data Points |
|--------|------------------|-------------|
| Tax returns (Vero) | Annual | entrepreneur.annual_income, income.household |
| Bankruptcy register | Daily | employer.bankruptcy |
| Prison register | Daily | person.incarcerated |
| Population register | Real-time | person.*, children.* |

---

## Data Quality Considerations

### Critical Data Points (Must Have)
- employment.months_last_24 - From employer/Tulorekisteri
- wages.12_month_total - From tax records
- jobseeker.registered - From TE services
- person.age - From population register

### Important (Should Have)
- refusal.count_previous - From fund history
- children.count - From population register
- entrepreneur.annual_income - From tax return

### Nice to Have
- reason.distance - From map calculation
- study.vocational - From enrollment
- person.financial_situation - From debt register

---

## New Data Points (2026 Amendments)

### Commuting Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| commute.distance_km | Kartta / Osoitteet | Distance calculation | Map API |
| commute.public_transport_cost | VR / Matkahuolto | Timetables | Transport |
| commute.daily_travel_expense | Työnhakija | Receipts | Job seeker |
| commute.monthly_max | Laskettu | Calculation | System |
| residence.municipality | Väestörekisteri | Address | DVV |

### Housing Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| housing.cost | Vuokranantaja / Vuokrasopimus | Rental agreement | Landlord |
| housing.own | Väestörekisteri | Population register | DVV |
| housing.municipality | Väestörekisteri | Address | DVV |
| person.dependency | Väestörekisteri | Household | DVV |

### Education & Training Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| education.completed | Opetushallitus | Education register | EDUFI |
| training.vocational | Koulutus | Enrollment | Institution |
| training.employment_relation | TE-palvelut | Service decision | TE |
| training.voucher | TE-palvelut | Voucher system | TE |

### Rehabilitation Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| rehabilitation.medical | Terveyspalvelut | Medical certificate | Doctor |
| rehabilitation.vocational | Kela / TE-palvelut | Rehabilitation plan | Kela / TE |

### Income Data (2026 System)

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| income.tygr_18_months | Tulorekisteri | Incomes register | Incomes Register |
| income.insurable_earnings | Verohallinto | Tax records | Tax |
| person.member_since | Työttömyyskassa | Membership | Fund |
| benefit.transitional_arrangement | Työttömyyskassa / Kela | Decision | Fund / Kela |

### Youth & Older Worker Data

| Data Point | Data Source | Source Type | Access |
|-----------|-------------|-------------|--------|
| person.under_25 | Laskettu | Date calculation | System |
| person.age_60_plus | Laskettu | Date calculation | System |
| jobseeker.without_profession | TE-palvelut | Assessment | TE |
| redundancy.layoff_notice | Työnantaja | Notice | Employer |

---

## Updated API Integration (2026)

### Real-Time APIs

| API | Provider | New Data Points |
|-----|----------|------------------|
| Tulorekisteri (TYGR) | Verohallinto | income.tygr_18_months, income.insurable_earnings |
| Education Register | Opetushallitus | education.completed |
| Kela API | Kela | rehabilitation.vocational, benefit.transitional_arrangement |
| TE-palvelut API | TE-hallinto | training.voucher, jobseeker.without_profession |

### New Data Sources

| Authority | Register | New Data Points |
|-----------|----------|-----------------|
| **Opetushallitus** | Education register | education.completed |
| **VR / Matkahuolto** | Transport timetables | commute.public_transport_cost |
| **Työttömyyskassat** | Membership records | person.member_since, benefit.transitional_arrangement |
