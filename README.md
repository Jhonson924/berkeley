# Berkeley
Berkeley ML/AI Modules and Practical application

## Practical Application1 <Will the Customer Accept the Coupon>

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/practical%20application1/coupons.ipynb)

### Context
A coupon is delivered to driver cell phone for a restaurant near where you are driving.

### Business Problem Statement

#### Consumer <Coupon>
- Would driver accept that coupon and take a short detour to the restaurant? 
- Would driver accept the coupon but use it on a subsequent trip? 
- Would driver ignore the coupon entirely? 
- What if the coupon was for a bar instead of a restaurant? What about a coffee house? 
- Would driver accept a bar coupon with a minor passenger in the car? 
- What about if it was just dirver and driver partner in the car? 
- Would weather impact the rate of acceptance? What about the time of day?

#### Business
- Whether the coupon is delivered to the driver or not, 
- What are the factors that determine whether a driver accepts the coupon once it is delivered to them? 
- How would business determine whether a driver is likely to accept a coupon

### Project Goal
- visualizations and probability distributions to distinguish between customers who accepted a driving coupon versus those that did not.

### Logical Data

![Business Process](./practical%20application1/images/data-logic.png)

### Findings

#### Gender vs CouponType
![Business Process](./practical%20application1/images/genderVsCouponType.png)

- Consistency Across Genders: For each activity, the distributions for Male and Female appear very similar in shape and spread.
- Uniformity in Distribution: The density for activities like "Bar" and "Coffee House" appears fairly uniform between genders, suggesting a similar engagement rate.
- Activity Engagement: The width of the violin plots indicates where most individuals fall in the distribution for a specific activity (e.g., people are more uniformly distributed in "Carry out & Take away").

#### ageAcceptanceRate
![Business Process](./practical%20application1/images/ageAcceptanceRate.png)

 - Younger individuals, especially those in their 20s and early 30s, show higher coupon acceptance (orange bars dominate in those age groups). Older age groups, while having fewer participants, seem less likely to accept coupons.
- Across most coupon types, the central tendency (median line) lies in the younger age groups (e.g., mid-20s to early 30s).
- Bar coupons show a slightly broader distribution, indicating some older individuals accept bar coupons compared to other types.
##### Summary
- Younger individuals (20-30 years old) are more likely to accept coupons, regardless of type.
- Coupon type matters: Bar and restaurant coupons seem to appeal to a broader age range compared to others like coffee houses or carry-out.

#### passangerAcceptanceRate
![Business Process](./practical%20application1/images/passangerAcceptanceRate.png)

- Drivers alone are the largest group and show a higher likelihood of accepting coupons (orange bar is taller than the blue bar for "Alone").
- Drivers with friends are also more likely to accept coupons, though the gap between acceptance (orange) and non-acceptance (blue) is smaller than for those alone.
- Drivers with kids or partners have fewer participants, and the acceptance rates are nearly balanced or slightly lower than non-acceptance.

- Across most coupon types, drivers who are alone dominate the density of acceptance, indicating they are more likely to use coupons regardless of type.
- Drivers with friends also show moderate densities, particularly for Bar and Coffee House coupons.
- Drivers with kids or partners have lower densities overall, indicating less engagement with coupons.

##### Summary
- Being alone significantly increases coupon acceptance rates across all types.
- Friends as passengers also positively influence acceptance but not as strongly as being alone.
- Kids and partners are associated with lower coupon acceptance rates, likely due to different priorities or constraints during travel.

#### BarCoupoun Analysis (1~3 times visited)
![Business Process](./practical%20application1/images/barCouponAnalysis1to3times_1.png)

-The majority (64.7%) of participants in the group(BAR) accepted the coupon, highlighting a clear preference or tendency to accept bar coupons.

#### onlyBarCoupon Analysis (1~3 times visited)
![Business Process](./practical%20application1/images/barCouponAnalysis1to3times.png)

1. Diagonal (Histograms):

- The diagonal of the pairplot contains histograms for each variable, showing its distribution.
- Variables like age or temperature may show the spread of values across the dataset.
- Categorical variables (e.g., has_children, accept_coupon) appear as bar plots since they represent discrete values.

2. Off-Diagonal (Scatterplots):

- The off-diagonal plots compare two variables, with each subplot showing the relationship between one pair.
- Temperature vs. Age: Scatterplot showing how these two variables relate.
- Acceptance Decision vs. Proximity (e.g., to_coupon_distance): Shows how coupon acceptance changes with distance.