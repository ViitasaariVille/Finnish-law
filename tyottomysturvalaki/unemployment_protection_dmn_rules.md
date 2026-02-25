# Työttömyysturvalaki DMN Rules

## UnemploymentBenefitTypes

Types of unemployment benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Person,employee | Earnings-related allowance or basic allowance | Section 1 |
| Person,entrepreneur | Earnings-related allowance | Section 1 |
| Person,no_insurance | Labour market support | Section 7 |
| Person,member_fund | Earnings-related allowance from fund | Section 5 |

## EmploymentConditionEmployee

Employment condition for employees

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,months | At least 12 months in last 24 months | Section 5.3 |
| Work,hours | At least 18 hours per week OR 52 hours over 4 weeks | Section 5.3 |
| Work,termination | Employment ended not by own choice | Section 5.3 |

## EmploymentConditionEntrepreneur

Employment condition for entrepreneurs

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Entrepreneur,months | At least 24 months in last 48 months | Section 5.7 |
| Entrepreneur,income | At least 14,000 EUR annual income (verified 2024) | Section 5.7 |
| Entrepreneur,activity | Business actively conducted | Section 5.7 |

## BenefitAmountCalculation

Calculation of benefit amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Allowance,earnings_related | 45% of difference between wages and base | Section 6.2 |
| Allowance,basic | 38.86 EUR per day (2025 rate) | Section 6.1 |
| Allowance,with_children | Additional for dependent children | Section 6.3 |
| Age,over_58 | Higher rate for older workers | Section 6.9 |

## BenefitDuration

Maximum duration of benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Benefit,first_time | 300 days maximum | Section 6.7 |
| Benefit,renewed | New period after employment | Section 6.7 |
| Age,over_61 | Additional days available | Section 6.9 |
| Employment,short | Duration proportional to work | Section 6.7 |

## AdjustedBenefit

Adjusted benefit when working part-time

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,part_time | Benefit reduced by earnings | Section 4.1 |
| Earnings,below_limit | Full benefit if earnings low | Section 4.4 |
| Work,full_time | No benefit if working full-time | Section 4.1 |
| Calculation,per_day | Adjusted daily | Section 4.5 |

## LabourMarketPolicyConditions

Labour market policy conditions for benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Person,registered | Must be registered job seeker | Section 2.1 |
| Person,available | Must be available for work | Section 2.1 |
| Person,actively_seeking | Must actively seek work | Section 2.1 |
| Person,interview | Must attend interview | Section 2.1 |

## JobRefusalConsequences

Consequences of refusing suitable work

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Refusal,without_reason | Benefit reduced 50% for 60 days | Section 2a.4 |
| Refusal,repeated | Benefit cut off for 90 days | Section 2a.10 |
| Refusal,with_acceptable | No consequence if acceptable reason | Section 2a.2 |
| Training,refused | May affect benefit | Section 2a.14 |

## AcceptableReasonsForRefusal

Acceptable reasons for refusing work

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Reason,health | Health reasons | Section 2a.5 |
| Reason,family | Family reasons | Section 2a.5 |
| Reason,education | Starting education | Section 2a.5 |
| Reason,distance | Excessive travel distance | Section 2a.7 |

## SelfEmploymentConditions

Conditions for entrepreneur benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Entrepreneur,ended | Business ended or substantially reduced | Section 2.5 |
| Entrepreneur,family | Family member stopped working | Section 2.7 |
| Entrepreneur,start | Starting new business | Section 5a |
| Income,verified | Income verified | Section 5.7 |

## StudyAndBenefit

Effect of studies on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Study,full_time | No benefit during full-time study | Section 2.10 |
| Study,part_time | May receive benefit if part-time | Section 2.10 |
| Study,vocational | Vocational training qualifies | Section 2.13 |
| Study,ended | Benefit after studies end | Section 2.11 |

## RestrictionsOnBenefit

General restrictions on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Person,incarcerated | No benefit during imprisonment | Section 3.1 |
| Person,abroad | Limited benefit abroad | Section 3.1 |
| Person,striking | No benefit during strike | Section 3.1 |
| Income,high | Benefit reduced or denied | Section 3.7 |

## WaitingPeriod

Waiting period before benefit starts

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| First,benefit | 7-day waiting period | Section 5.13 |
| Employment,short | New waiting period if short work | Section 5.13 |
| Illness,during | Waiting period extended by illness | Section 5.13 |
| Activation,program | No waiting during activation | Section 5.13 |

## LabourMarketSupport

Labour market support conditions

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Person,no_earnings_related | Must have no earnings-related benefit | Section 7.1 |
| Income,test | Income test applies | Section 7.6 |
| Employment,history | Must meet employment condition | Section 7.1 |
| Age,under_65 | Under 65 years old | Section 7.1 |

## MobilitySupport

Mobility support for moving for work

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Move,for_job | Moving for suitable job | Section 8.1 |
| Distance,over_150km | Over 150 km from previous residence | Section 8.1 |
| Job,permanent | Permanent or fixed-term over 2 years | Section 8.1 |
| Support,amount | 500 EUR one-time payment | Section 8.2 |

## RedundancyPayment

Redundancy payment conditions

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Layoff,reason | Due to employer bankruptcy or layoff | Section 9.1 |
| Tenure,years | At least 5 years with employer | Section 9.1 |
| Reemployment,refused | Not refused re-employment | Section 9.3 |
| Amount,calculation | Based on tenure and wages | Section 9.2 |

## EmploymentServicesBenefit

Benefit during employment services

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Service,training | Benefit during training | Section 10.1 |
| Service,rehabilitation | Benefit during rehabilitation | Section 10.1 |
| Service,placement | Benefit during work placement | Section 10.1 |
| Absence,reason | Acceptable reason prevents penalty | Section 10.3 |

## ApplicationAndPayment

Application and payment procedures

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Application,where | Unemployment fund or Kela | Section 11.1 |
| Decision,time | Decision within 30 days | Section 11.1a |
| Payment,frequency | Paid every two weeks | Section 11.5 |
| Direct_deposit,required | Must be paid to account | Section 11.5 |

## RecoveryOfOverpayment

Recovery of incorrectly paid benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Overpayment,intentional | Full recovery | Section 11.10 |
| Overpayment,negligent | May recover part | Section 11.10 |
| Repayment,installments | May pay in installments | Section 11.10 |
| Deduction,future | May deduct from future benefits | Section 11.13 |

## AppealProcedure

Right to appeal benefit decisions

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Appeal,where | To unemployment security board appeal committee | Section 12.1 |
| Appeal,time | Within 30 days of decision | Section 12.1 |
| Decision,incorrect | Can request correction | Section 12.4 |
| Court,final | Can appeal to court | Section 12.1 |

## InternationalCoordination

EU and international coordination

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,EU_country | Export benefit to EU/EEA | Section 8a |
| Insurance,other_country | Periods from other countries count | Section 5.9 |
| Job,search_EU | Can search for job in EU | Section 8b |
| Return,Finland | Return to Finland maintains rights | Section 8b |

## YouthUnemploymentBenefit

Youth additional benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Age,under_25 | Youth addition available | Section 6.5 |
| Employment,short | Youth addition if short employment | Section 6.5 |
| Amount,youth_bonus | Additional percentage | Section 6.5 |

## EmploymentInsuranceAccumulation

How employment insurance period accumulates

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,hours_per_week | 18+ hours = 1 month | Section 5.4 |
| Work,monthly_hours | 80+ hours = 1 month | Section 5.4 |
| Work,full_time | Full month counts fully | Section 5.4 |
| Work,multiple | Can combine multiple jobs | Section 5.4 |

## WorkDisabilityEffect

Effect of work disability on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Disability,full | No unemployment benefit | Section 3.3 |
| Disability,partial | May receive adjusted benefit | Section 3.3 |
| Disability,recovered | Can return to unemployment benefit | Section 3.3 |
| Pension,disability | Excludes unemployment benefit | Section 3.3 |

## LeaveAndBenefit

Parental leave and unemployment benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Leave,parental | No unemployment benefit during leave | Section 3.4 |
| Leave,care | Care leave affects benefit | Section 3.4 |
| Leave,studying | Study leave | Section 3.4 |

## EarnedIncomeEffect

Effect of earned income on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Income,below_300 | Full benefit | Section 3.7 |
| Income,300_850 | Benefit reduced 50% | Section 3.7 |
| Income,over_850 | No benefit | Section 3.7 |
| Income,net | Net income counted | Section 3.7 |

## TerminationByEmployee

Termination by employee (quitting)

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Quit,without_reason | Benefit cut off 90 days | Section 2a.1 |
| Quit,acceptable | No penalty if acceptable reason | Section 2a.2 |
| Quit,changed | Changed circumstances | Section 2a.2 |
| Quit,3_months | 3 month penalty period | Section 2a.1 |

## LayoffAndBenefit

Layoff (lomautus) and benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Layoff,full | Full benefit available | Section 2.1 |
| Layoff,partial | Partial benefit | Section 2.1 |
| Layoff,recalled | Return to work ends benefit | Section 2.1 |
| Layoff,ended | New application after layoff ends | Section 2.1 |

## SeasonalWorkEffect

Seasonal work and benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,seasonal | Seasonal work counted | Section 2.4 |
| Work,ended | Can claim after seasonal ends | Section 2.4 |
| Work,same_employer | Same employer next season | Section 2.4 |

## EntrepreneurStartPeriod

Starting entrepreneurship and benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Entrepreneur,starting | Business start period | Section 5a(1) |
| Entrepreneur,support | Start grant can affect benefit | Section 5a(2) |
| Entrepreneur,full_time | Must be full-time | Section 5a(1) |
| Entrepreneur,planned | Business plan required | Section 5a(1) |

## OldWorkerAdditionalDays

Additional days for older workers

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Age,over_61 | Additional 150 days available | Section 6.9(1) |
| Age,over_59 | Additional 100 days at 59 | Section 6.9(1) |
| Employment,years | At least 5 years employment | Section 6.9(1) |
| Benefit,exhausted | After regular benefit ends | Section 6.9(2) |

## LabourMarketSupportAmount

Labour market support amount

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Support,basic | 38.86 EUR per day (2025 rate) | Section 7.4 |
| Support,with_children | Increased with children | Section 7.4 |
| Income,test | Income test reduces | Section 7.6 |
| Support,full | Without income test at start | Section 7.8 |

## SolidarityAllowance

Solidarity allowance for certain groups

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Person,long_term | Long-term unemployed | Section 7.4a |
| Person,over_50 | Over 50 years old | Section 7.4a |
| Amount,solidarity | 43.07 EUR per day (2025 rate, basic + 4.21) | Section 7.4a |

## WorkingWhileUnemployed

Working while registered unemployed

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,trial | Trial work period allowed | Section 4.1a |
| Work,max_days | Maximum 5 days per week credit | Section 4.1a |
| Work,report | Must report earnings | Section 4.1a |
| Work,adjustment | Benefit adjusted next period | Section 4.1a |

## EmployeeQualifyingPeriod

Qualifying period calculation for employees

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,12_months | 12 months employment in last 24 months | Section 5.3 |
| Work,18_hours | Minimum 18 hours per week | Section 5.3 |
| Work,calendar_week | Employment calculated in calendar weeks | Section 5.4 |
| Work,combined | Can combine multiple employers | Section 5.4 |

## EntrepreneurQualifyingPeriod

Qualifying period for entrepreneurs

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Entrepreneur,24_months | 24 months in last 48 months | Section 5.7 |
| Entrepreneur,annual_income | Annual income at least 14,279 EUR (2025 rate) | Section 5.7 |
| Entrepreneur,TYEL | Must have TYEL insurance | Section 5.7 |
| Entrepreneur,active | Business actively conducted | Section 5.7 |

## ForeignWorkRecognition

Recognition of foreign work periods

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,EU_EEA | EU/EEA work periods count | Section 5.9 |
| Work,agreement | Countries with agreement | Section 5.9 |
| Work,certificate | Need certificate from country | Section 5.9 |
| Work,partial | Partial periods combined | Section 5.9 |

## PostProtection

Post-protection after employment ends

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Employment,ended | Post-protection available | Section 5.10a |
| Employment,3_years | At least 3 years of employment | Section 5.10a |
| Application,within_12 | Apply within 12 months | Section 5.10a |
| Employment,reason | Not due to own quitting | Section 5.10a |

## MarineInsurance

Special rules for maritime workers

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,sea | Sea work counts double | Section 5.12 |
| Work,additional | Additional insurance possible | Section 5.12 |
| Work,days_at_sea | Days at sea requirement | Section 5.12 |
| Work,certified | Must be certified seaman | Section 5.12 |

## OwnRiskPeriod

Own risk period (waiting period)

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Benefit,first | 7 calendar days waiting period | Section 5.13 |
| Benefit,short_work | New waiting for short employment | Section 5.13 |
| Benefit,activation | No waiting during activation | Section 5.13 |
| Illness,during_wait | Illness extends waiting | Section 5.13 |

## DailyAllowanceCalculation

Daily allowance amount calculation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Wages,calculated | Based on wages from 12 months | Section 6.1 |
| Percentage,45_percent | 45% of wage exceeding base | Section 6.2 |
| Percentage,20_percent | 20% of wage below base | Section 6.2 |
| Children,supplement | Supplement for dependent children | Section 6.3 |

## MaximumPeriod

Maximum benefit period

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Period,300_days | Maximum 300 days | Section 6.7 |
| Period,500_days | 500 days for those over 58 | Section 6.9 |
| Renewal,new_period | New 300-day period after work | Section 6.7 |
| Extension,additional | Additional days for older workers | Section 6.9 |

## ReducedBenefit60Days

60-day reduced benefit period

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Reduction,first | First 60 days at reduced rate | Section 6.3a |
| Percentage,80_percent | 80% of full benefit | Section 6.3a |
| Condition,no_children | Without children supplement | Section 6.3a |
| After,60_days | Full benefit after 60 days | Section 6.3a |

## ReemploymentBonus

Re-employment bonus

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Bonus,eligible | Bonus for quick re-employment | Section 6.3b |
| Bonus,amount | 50% of daily benefit for 100 days | Section 6.3b |
| Condition,within_65 | Within 65 days of application | Section 6.3b |
| Employment,min_12 | Minimum 12 months employment | Section 6.3b |

## LabourMarketSupportWaiting

Waiting period for labour market support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Support,first_time | 5-day waiting period | Section 7.2 |
| Support,previous | One waiting period per 12 months | Section 7.2 |
| Activation,program | No waiting during activation | Section 7.2 |
| Support,renewed | New waiting if renewed | Section 7.2 |

## IncomeSupportDetermination

Income test for labour market support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Income,household | Household income considered | Section 7.6 |
| Income,spouse | Spouse income affects | Section 7.6 |
| Deduction,children | Deduction for children | Section 7.6 |
| Calculation,monthly | Monthly income calculation | Section 7.7 |

## MobilitySupportConditions

Conditions for mobility support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Distance,150_km | Minimum 150 km | Section 8.1 |
| Job,permanent | Permanent or 2-year contract | Section 8.1 |
| Time,commute | Over 3 hours daily commute saved | Section 8.1 |
| Support,500_1000 | 500-1000 EUR one-time | Section 8.2 |

## RedundancyConditions

Conditions for redundancy payment

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Reason,bankruptcy | Employer bankruptcy | Section 9.1 |
| Reason,layoff | Employer layoff over 200 days | Section 9.1 |
| Tenure,5_years | At least 5 years employment | Section 9.1 |
| Not,refused | Not refused re-employment | Section 9.3 |

## ActivationServicesBenefit

Benefit during activation services

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Service,training | Full benefit during training | Section 10.1 |
| Service,rehabilitation | Full benefit during rehabilitation | Section 10.1 |
| Service,work_trial | During work trial | Section 10.1 |
| Cost,travel | Travel costs reimbursed | Section 10.6 |

## ApplicationProcess

Application process details

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Where,fund | Apply to unemployment fund | Section 11.1 |
| Where,kela | Or to Kela | Section 11.1 |
| Time,30_days | Decision within 30 days | Section 11.1a |
| Missing,info | Can request additional info | Section 11.1a |

## PaymentMethod

Payment method and frequency

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Method,bank | To Finnish bank account | Section 11.5 |
| Frequency,biweekly | Every two weeks | Section 11.5 |
| Abroad,EU | Can pay to EU account | Section 11.5 |
| Currency,euro | Paid in euros | Section 11.5 |

## SuspensionOfPayment

Suspension of benefit payment

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Suspended,information | Missing required information | Section 11.6 |
| Suspended,investigation | During investigation | Section 11.6 |
| Suspended,abroad | If abroad too long | Section 11.6 |
| Resumed,correct | Resume when correct | Section 11.6 |

## RecoveryConditions

Conditions for recovery of overpayment

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Recovery,full | Full if intentional | Section 11.10 |
| Recovery,negligent | May recover if negligent | Section 11.10 |
| Recovery,interest | Interest may be charged | Section 11.10 |
| Recovery,waiver | Can waive if small | Section 11.10 |

## DeductionFromBenefit

Deduction from future benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Deduction,overpayment | Can deduct overpayment | Section 11.13 |
| Deduction,max_15_percent | Maximum 15% of benefit | Section 11.13 |
| Deduction,debt | Can deduct debt to fund | Section 11.13 |
| Deduction,written | Must give written notice | Section 11.13 |

## AppealProcess

Appeal process details

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Appeal,to_board | Appeal to unemployment security board | Section 12.1 |
| Time,30_days | 30 days to appeal | Section 12.1 |
| Fee,none | No fee for appeal | Section 12.1 |
| Court,administrative | Then to Administrative Court | Section 12.1 |

## SelfCorrection

Self-correction of decision

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Correct,error | Can correct obvious error | Section 12.4 |
| Correct,new_info | New information received | Section 12.4 |
| Correct,request | Party can request correction | Section 12.4 |
| Time,within_year | Within one year | Section 12.4 |

## DataExchange

Data exchange between authorities

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Data,tax | Tax authority data | Section 13.1 |
| Data,employer | Employer information | Section 13.1 |
| Data,kela | Kela registers | Section 13.4 |
| Data,unemployment_fund | Unemployment fund data | Section 13.1 |

## IndexAdjustment

Index adjustment of benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Adjustment,wage | Wage coefficient adjustment | Section 14.1a |
| Adjustment,pension | Pension index | Section 14.1b |
| Adjustment,annually | Adjusted annually | Section 14.1 |
| Effective,january | Effective from January 1 | Section 14.1 |

## Financing

Financing of benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Financing,earnings_related | Funded by contributions | Section 14.3 |
| Financing,state | State funds basic | Section 14.3a |
| Financing,employer | Employer contribution | Section 14.3 |
| Financing,employee | Employee contribution | Section 14.3 |

## RegionalMobility

Regional mobility support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Move,region | Moving to another region | Section 8.1 |
| Job,suitable | Suitable job in new region | Section 8.1 |
| Support,amount | Up to 5000 EUR | Section 8.2 |
| Condition,6_months | Work minimum 6 months | Section 8.3 |

## CommutingSupport

Commuting support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Commute,long | Long commuting distance | Section 8.4a |
| Time,hours | Minimum 3 hours daily | Section 8.4a |
| Support,monthly | Monthly payment | Section 8.4a |
| Employer,not_provide | Employer does not pay | Section 8.4a |

## StartUpGrantEffect

Start-up grant effect on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Grant,received | Start-up grant affects benefit | Section 5a.2 |
| Grant,reduced | Benefit reduced during grant | Section 5a.2 |
| Grant,excluded | Grant period excluded | Section 5a.2 |
| After,grant | Benefit after grant ends | Section 5a.2 |

## FamilyPensionEffect

Family pension effect on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Pension,survivors | Survivors pension affects | Section 3.4 |
| Pension,orphans | Orphans pension | Section 3.4 |
| Full,excludes | Full pension excludes benefit | Section 3.4 |
| Partial,partial_benefit | Partial pension partial benefit | Section 3.4 |

## AccidentInsuranceEffect

Accident insurance effect

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Insurance,accident | Work accident insurance | Section 3.4a |
| Compensation,received | If compensation received | Section 3.4a |
| Deduction,from_benefit | May be deducted from benefit | Section 3.4a |
| Not,duplicate | No duplicate compensation | Section 3.4a |

## CriminalSanctionEffect

Criminal sanction effect on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Sanction,imprisonment | No benefit during imprisonment | Section 3.1 |
| Sanction,community | Community service affects | Section 3.1 |
| After,release | Benefit after release | Section 3.1 |
| Restriction,travel | Travel restriction affects | Section 3.1 |

## CooperationWithAuthorities

Cooperation with authorities requirement

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Provide,information | Must provide required information | Section 11.2 |
| Attend,interview | Must attend interviews | Section 11.2 |
| Meet,requirements | Must meet requirements | Section 11.2 |
| Sanction,penalty | Penalty for non-cooperation | Section 11.2 |

## LabourMarketPolicyStatement

Labour market policy statement

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Statement,required | TE services statement required | Section 11.4 |
| Content,availability | Statement on availability | Section 11.4 |
| Content,activity | Statement on job seeking | Section 11.4 |
| Effect,benefit | Affects benefit decision | Section 11.4 |

## EUCoordinationRules

EU coordination rules

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Export,EU | Can export to EU country | Section 8a |
| Period,3_months | Up to 3 months | Section 8a |
| Seek,job_EU | Can seek job in EU | Section 8b |
| Return,within_4 | Return within 4 weeks | Section 8b |

## RegisteredUnemploymentRate

Registered unemployment rate effect

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Rate,high | High unemployment area | Section 2.2 |
| Rate,15_percent | Over 15% in region | Section 2.2 |
| Relaxed,conditions | Relaxed availability | Section 2.2 |
| Notice,by_government | Government decides | Section 2.2 |

## WorkAbilityAssessment

Work ability assessment

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Assessment,required | Work ability may be assessed | Section 2a.11 |
| Assessment,authority | Kela or TE services | Section 2a.11 |
| Effect,benefit | Affects benefit eligibility | Section 2a.11 |
| Reassessment,possible | Can be reassessed | Section 2a.11 |

## NotificationDuties

Notification duties of beneficiary

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Notify,work | Must notify if starts working | Section 11.2a |
| Notify,abroad | Must notify if going abroad | Section 11.2a |
| Notify,address | Must notify address change | Section 11.2a |
| Notify,bankruptcy | Notify employer bankruptcy | Section 11.2a |

## ReducedEarningsCapacity

Reduced earning capacity

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Capacity,reduced | Reduced earning capacity | Section 3.3a |
| Assessment,medical | Medical assessment required | Section 3.3a |
| Benefit,adjusted | May receive adjusted benefit | Section 3.3a |
| Rehabilitation,offered | Rehabilitation offered | Section 3.3a |

## OlderWorkerProtection

Special protection for older workers

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Age,58_plus | Extended benefit period | Section 6.9 |
| Age,61_plus | Additional 150 days | Section 6.9 |
| Employment,long | Long employment history | Section 6.9 |
| Benefit,increased | Increased benefit amount | Section 6.10 |

## PartialUnemployment

Partial unemployment (short-time work)

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,short_time | Short-time work arrangement | Section 4.2 |
| Reduction,percentage | 20-90% reduction in hours | Section 4.2 |
| Benefit,proportional | Proportional benefit | Section 4.2 |
| Employer,agreement | Employer must agree | Section 4.2 |

## EmployerInsolvency

Benefit during employer insolvency

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Insolvency,bankruptcy | Employer bankruptcy | Section 9a |
| Insolvency,payment | Unable to pay wages | Section 9a |
| Benefit,guarantee | Income guarantee from guarantee institution | Section 9a |
| Unemployment,from_insolvency | Unemployment due to insolvency | Section 9a |

## PublicWorksBenefit

Public works (työllistämistö) benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,public | Publicly subsidized work | Section 10.2 |
| Subsidy,employer | Employer subsidy applies | Section 10.2 |
| Benefit,full | Full unemployment benefit | Section 10.2 |
| Duration,limited | Maximum duration applies | Section 10.2 |

## JobClubBenefit

Job club (työklubi) benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Program,job_club | Job club programme | Section 10.2a |
| Group,activities | Group activities | Section 10.2a |
| Benefit,maintained | Benefit maintained | Section 10.2a |
| Attendance,required | Attendance required | Section 10.2a |

## VocationalRehabilitation

Vocational rehabilitation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Rehabilitation,vocational | Vocational rehabilitation | Section 10.3 |
| Rehabilitation,plan | Rehabilitation plan | Section 10.3 |
| Benefit,during_rehab | Benefit during rehabilitation | Section 10.3 |
| Rehabilitation,provider | Kela or insurance provider | Section 10.3 |

## WorkTrialPeriod

Work trial period

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Trial,work | Work trial allowed | Section 2a.8 |
| Duration,max_3_months | Maximum 3 months | Section 2a.8 |
| Benefit,not_affected | Benefit not affected | Section 2a.8 |
| Not,employment | Not considered employment | Section 2a.8 |

## JobSearchPlan

Job search plan

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Plan,created | Job search plan created | Section 2a.12 |
| Plan,content | Contains job search activities | Section 2a.12 |
| Plan,follow_up | Follow-up meetings | Section 2a.12 |
| Plan,updated | Updated regularly | Section 2a.12 |

## EmploymentPenaltyPeriods

Employment penalty periods

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Penalty,first | First refusal 30 days | Section 2a.9 |
| Penalty,second | Second refusal 60 days | Section 2a.9 |
| Penalty,third | Third refusal 90 days | Section 2a.10 |
| Penalty,grace | 180 days without penalty resets | Section 2a.9 |

## IncomeCalculationPeriod

Income calculation period

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Period,12_months | Based on 12 months | Section 6.1 |
| Excludes,illness | Excludes illness periods | Section 6.1 |
| Excludes,leave | Excludes leave periods | Section 6.1 |
| Average,daily | Calculated as daily average | Section 6.1 |

## MaximumDailyAllowance

Maximum daily allowance

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Maximum,2024 | Maximum 100.25 EUR/day (2024) | Section 6.1b |
| Annual,maximum | Annual maximum applies | Section 6.1b |
| Increase,annual | Increased annually | Section 6.1b |
| Exceeded,no_increase | If exceeded no increase | Section 6.1b |

## MinimumDailyAllowance

Minimum daily allowance

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Minimum,guaranteed | Minimum guaranteed | Section 6.1a |
| Minimum,amount | Minimum 7.62 EUR/day | Section 6.1a |
| Below,minimum | If calculated below minimum | Section 6.1a |
| Increase,annual | Adjusted annually | Section 6.1a |

## EarningsRelatedIncrease

Earnings-related increase

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Increase,long_employment | Increase for long employment | Section 6.4 |
| Years,20_years | 20+ years employment | Section 6.4 |
| Increase,percentage | Additional percentage | Section 6.4 |
| Maximum,increase | Maximum increase limit | Section 6.4 |

## ChildSupplement

Child supplement

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Children,one | One child 5 EUR/day | Section 6.3 |
| Children,two | Two children 10 EUR/day | Section 6.3 |
| Children,three_plus | Three+ children 15 EUR/day | Section 6.3 |
| Children,age | Until child turns 18 | Section 6.3 |

## ReducedBenefitFirst60

Reduced benefit first 60 days

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Reduced,first_60 | First 60 days reduced | Section 6.3a |
| Rate,80_percent | 80% of full rate | Section 6.3a |
| Condition,no_children | Without children supplement | Section 6.3a |
| After,60_days | Full rate after 60 days | Section 6.3a |

## UnemploymentFundMembership

Unemployment fund membership

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Membership,required | Must be fund member | Section 5.1 |
| Membership,duration | Member for benefit period | Section 5.1 |
| Contribution,paid | Contributions paid | Section 5.1 |
| Exit,free | Can exit fund freely | Section 5.2 |

## BusinessStartUpAllowance

Business start-up allowance

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Start,business | Starting new business | Section 5a |
| Plan,business_plan | Business plan required | Section 5a |
| Full_time,required | Must be full-time | Section 5a |
| Support,startup | Start-up grant available | Section 5a |

## SeasonalWorkException

Seasonal work exception

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Work,seasonal | Seasonal work counted | Section 2.4 |
| Work,same_employer | Same employer next season | Section 2.4 |
| Benefit,after_season | Benefit after season ends | Section 2.4 |
| Waiting,exempt | May be exempt from waiting | Section 2.4 |

## ExceptionFromAvailability

Exceptions from availability requirement

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Exception,care | Family care responsibilities | Section 2.3 |
| Exception,studies | Studying | Section 2.3 |
| Exception,partial | Part-time availability | Section 2.3 |
| Approval,required | TE services approval | Section 2.3 |

## NoticePeriodEmployment

Notice period employment

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Notice,given | Given notice by employer | Section 2.1 |
| Notice,period | During notice period | Section 2.1 |
| Work,partial | Working during notice | Section 2.1 |
| Benefit,after_notice | Benefit after notice ends | Section 2.1 |

## WorkAbroadEffect

Work abroad effect on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Abroad,EU | Work in EU/EEA | Section 3.2 |
| Abroad,other | Work outside EU | Section 3.2 |
| Return,Finland | Return to Finland | Section 3.2 |
| Benefit,restricted | Benefit may be restricted | Section 3.2 |

## ServiceAbroad

Service abroad

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Service,military | Military service | Section 3.5 |
| Service,civil | Civil service | Section 3.5 |
| Return,after_service | Benefit after service | Section 3.5 |
| Condition,met | Employment condition met | Section 3.5 |

## CompanyTransaction

Company transaction effect

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Transaction,sale | Company sold | Section 2.6 |
| Transaction,inheritance | Inheritance | Section 2.6 |
| Work,continued | Work continued | Section 2.6 |
| Benefit,entitled | May be entitled | Section 2.6 |

## OldAgePensionEffect

Old age pension effect on benefit

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Pension,old_age | Old age pension | Section 3.2a |
| Age,flexible | Flexible retirement age | Section 3.2a |
| Work,while_pension | Work while on pension | Section 3.2a |
| Benefit,ceased | Unemployment benefit ceases | Section 3.2a |

## IndividualizedService

Individualized service

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| Service,individual | Individualized service | Section 2.9 |
| Plan,service_plan | Service plan | Section 2.9 |
| Support,intensive | Intensive support | Section 2.9 |
| Follow_up,regular | Regular follow-up | Section 2.9 |

## CommutingExpenses

Reimbursement of commuting expenses under Section 8.3

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| commute.distance_km,commute.public_transport_cost,job.permanent,residence.municipality | ['commute.monthly_max', 'commute.daily_travel_expense'] | Section 2.10 |
| commute.distance_km,commute.public_transport_cost,job.permanent,residence.municipality | ['commute.monthly_max', 'commute.daily_travel_expense'] | Section 2.10 |
| commute.distance_km,commute.public_transport_cost,job.permanent,residence.municipality | ['commute.monthly_max', 'commute.daily_travel_expense'] | Section 2.10 |

## TrainingAndRehabilitation

Benefit eligibility during training or rehabilitation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| training.vocational,training.employment_relation,training.voucher,rehabilitation.medical,rehabilitation.vocational | ['benefit.during_training', 'service.type'] | Section 2.10 |
| training.vocational,training.employment_relation,training.voucher,rehabilitation.medical,rehabilitation.vocational | ['benefit.during_training', 'service.type'] | Section 2.10 |
| training.vocational,training.employment_relation,training.voucher,rehabilitation.medical,rehabilitation.vocational | ['benefit.during_training', 'service.type'] | Section 2.10 |

## IncomeVerification2026

Income verification for new 2026 system

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| income.tygr_18_months,person.unemployment_fund_member,person.member_since,benefit.transitional_arrangement | ['income.insurable_earnings', 'benefit.earnings_related_eligible'] | Section 2.10 |
| income.tygr_18_months,person.unemployment_fund_member,person.member_since,benefit.transitional_arrangement | ['income.insurable_earnings', 'benefit.earnings_related_eligible'] | Section 2.10 |
| income.tygr_18_months,person.unemployment_fund_member,person.member_since,benefit.transitional_arrangement | ['income.insurable_earnings', 'benefit.earnings_related_eligible'] | Section 2.10 |

## HousingCosts

Housing cost support under Section 7.6

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| housing.cost,housing.own,housing.municipality,income.household,person.dependency | ['housing.support_amount', 'housing.support_eligible'] | Section 2.10 |
| housing.cost,housing.own,housing.municipality,income.household,person.dependency | ['housing.support_amount', 'housing.support_eligible'] | Section 2.10 |
| housing.cost,housing.own,housing.municipality,income.household,person.dependency | ['housing.support_amount', 'housing.support_eligible'] | Section 2.10 |

## YouthJobSeekerRules

Special rules for job seekers under 25

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| person.age,person.under_25,education.completed,jobseeker.without_profession | ['youth.bonus_eligible', 'youth.addition_amount'] | Section 2.10 |
| person.age,person.under_25,education.completed,jobseeker.without_profession | ['youth.bonus_eligible', 'youth.addition_amount'] | Section 2.10 |
| person.age,person.under_25,education.completed,jobseeker.without_profession | ['youth.bonus_eligible', 'youth.addition_amount'] | Section 2.10 |

## DisabilityPensionInteraction

Interaction between unemployment benefit and disability pension

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| work_disability.exist,work_disability.partial,rehabilitation.medical | ['benefit.adjusted_for_disability', 'benefit.reduction_percentage'] | Section 2.10 |
| work_disability.exist,work_disability.partial,rehabilitation.medical | ['benefit.adjusted_for_disability', 'benefit.reduction_percentage'] | Section 2.10 |
| work_disability.exist,work_disability.partial,rehabilitation.medical | ['benefit.adjusted_for_disability', 'benefit.reduction_percentage'] | Section 2.10 |

## SocialBenefitIntegration

Integration of unemployment benefit with social benefits

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| social_benefit.type,income.household | ['benefit.integrated_amount', 'benefit.social_reduction'] | Section 2.10 |
| social_benefit.type,income.household | ['benefit.integrated_amount', 'benefit.social_reduction'] | Section 2.10 |
| social_benefit.type,income.household | ['benefit.integrated_amount', 'benefit.social_reduction'] | Section 2.10 |

## TrainingVoucherEligibility

Eligibility for training voucher

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| jobseeker.registered,person.age,employment.total_years | ['training.voucher_eligible', 'training.voucher_amount'] | Section 2.10 |
| jobseeker.registered,person.age,employment.total_years | ['training.voucher_eligible', 'training.voucher_amount'] | Section 2.10 |
| jobseeker.registered,person.age,employment.total_years | ['training.voucher_eligible', 'training.voucher_amount'] | Section 2.10 |

## TransitionalRules2026

Transitional rules for 2026 system change

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| benefit.previous_periods,person.unemployment_fund_member,person.member_since | ['benefit.transitional_arrangement', 'benefit.transitional_type'] | Section 2.10 |
| benefit.previous_periods,person.unemployment_fund_member,person.member_since | ['benefit.transitional_arrangement', 'benefit.transitional_type'] | Section 2.10 |
| benefit.previous_periods,person.unemployment_fund_member,person.member_since | ['benefit.transitional_arrangement', 'benefit.transitional_type'] | Section 2.10 |

## RedundancyLayoff

Redundancy and layoff procedures

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| employer.layoff_notice,layoff.duration_days | Redundancy eligible | Section 9.1 |
| employer.bankruptcy | Bankruptcy protection | Section 9a |

## RedundancyCompensation

Redundancy compensation calculation

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| employment.tenure_years,wages.daily_average | Compensation amount | Section 9.2 |

## LabourMarketSupportHousing

Housing supplements for labour market support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| income.household,housing.cost | Housing supplement | Section 7.6 |

## LabourMarketSupportDuration

Duration of labour market support

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| benefit.previous_periods,person.age | Maximum duration | Section 7.4 |

## AppealToInsuranceCourt

Appeal to insurance court

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| appeal.submitted,decision.type | Court appeal eligible | Section 12.2 |

## AppealTimeLimits

Time limits for appeals

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| decision.received_date,appeal.submitted | Appeal within time limit | Section 12.1 |

## JobSeekers500Days

Extended unemployment benefit for job seekers over 500 days

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| benefit.previous_days,person.age | Extended benefit eligible | Section 6.7 |

## IncreaseEarningsRelated

Increase to earnings-related allowance

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| children.count,wages.daily_average | Increase percentage | Section 6.4 |

## ReducedEarningsCapacityWork

Work with reduced earnings capacity

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| work.hours_per_week,earnings.monthly | Reduced capacity benefit | Section 6.2 |

## CorporationTaxCard

Tax card requirements for corporations

| Inputs | Output | Legal Basis |
|--------|--------|-------------|
| person.tax_card | Tax card valid | Section 11.7 |

