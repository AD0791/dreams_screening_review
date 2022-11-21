from pandas import (DataFrame, to_datetime)

from .data import (
    eligible_or_not,
    eligible,
    to_be_served,
    served
)

#screended
screened_FY18 = eligible_or_not[(eligible_or_not.interview_date >="2017-10-01") & (eligible_or_not.interview_date <="2018-09-30")]
screened_FY19 = eligible_or_not[(eligible_or_not.interview_date >="2018-10-01") & (eligible_or_not.interview_date <="2019-09-30")]
screened_FY20 = eligible_or_not[(eligible_or_not.interview_date >="2019-10-01") & (eligible_or_not.interview_date <="2020-09-30")]
screened_FY21 = eligible_or_not[(eligible_or_not.interview_date >="2020-10-01") & (eligible_or_not.interview_date <="2021-09-30")]
screened_FY22 = eligible_or_not[(eligible_or_not.interview_date >="2021-10-01") & (eligible_or_not.interview_date <="2022-09-30")]
screened_FY23 = eligible_or_not[(eligible_or_not.interview_date >="2022-10-01") & (eligible_or_not.interview_date <="2023-09-30")]
SCREENED = DataFrame(
  {
    "FY18":[screened_FY18.shape[0]],
    "FY19":[screened_FY19.shape[0]],
    "FY20":[screened_FY20.shape[0]],
    "FY21":[screened_FY21.shape[0]],
    "FY22":[screened_FY22.shape[0]],
    "FY23":[screened_FY23.shape[0]]
  }
)

# eligible
eligible_FY18 = eligible[(eligible.interview_date >="2017-10-01") & (eligible.interview_date <="2018-09-30")]
eligible_FY19 = eligible[(eligible.interview_date >="2018-10-01") & (eligible.interview_date <="2019-09-30")]
eligible_FY20 = eligible[(eligible.interview_date >="2019-10-01") & (eligible.interview_date <="2020-09-30")]
eligible_FY21 = eligible[(eligible.interview_date >="2020-10-01") & (eligible.interview_date <="2021-09-30")]
eligible_FY22 = eligible[(eligible.interview_date >="2021-10-01") & (eligible.interview_date <="2022-09-30")]
eligible_FY23 = eligible[(eligible.interview_date >="2022-10-01") & (eligible.interview_date <="2023-09-30")]
ELIGIBLE = DataFrame(
  {
    "FY18":[eligible_FY18.shape[0]],
    "FY19":[eligible_FY19.shape[0]],
    "FY20":[eligible_FY20.shape[0]],
    "FY21":[eligible_FY21.shape[0]],
    "FY22":[eligible_FY22.shape[0]],
    "FY23":[eligible_FY23.shape[0]]
  }
)

#to be served
to_be_served_FY18 = to_be_served[(to_be_served.interview_date >="2017-10-01") & (to_be_served.interview_date <="2018-09-30")]
to_be_served_FY19 = to_be_served[(to_be_served.interview_date >="2018-10-01") & (to_be_served.interview_date <="2019-09-30")]
to_be_served_FY20 = to_be_served[(to_be_served.interview_date >="2019-10-01") & (to_be_served.interview_date <="2020-09-30")]
to_be_served_FY21 = to_be_served[(to_be_served.interview_date >="2020-10-01") & (to_be_served.interview_date <="2021-09-30")]
to_be_served_FY22 = to_be_served[(to_be_served.interview_date >="2021-10-01") & (to_be_served.interview_date <="2022-09-30")]
to_be_served_FY23 = to_be_served[(to_be_served.interview_date >="2022-10-01") & (to_be_served.interview_date <="2023-09-30")]
TOBESERVED = DataFrame(
  {
    "FY18":[to_be_served_FY18.shape[0]],
    "FY19":[to_be_served_FY19.shape[0]],
    "FY20":[to_be_served_FY20.shape[0]],
    "FY21":[to_be_served_FY21.shape[0]],
    "FY22":[to_be_served_FY22.shape[0]],
    "FY23":[to_be_served_FY23.shape[0]]
  }
)

TOBESERVEDFY23 = to_be_served_FY23.fillna(-1)
TOBESERVEDFY23.dob = to_datetime(TOBESERVEDFY23.dob, utc=True)

# served
served_FY18 = served[(served.interview_date >="2017-10-01") & (served.interview_date <="2018-09-30")]
served_FY19 = served[(served.interview_date >="2018-10-01") & (served.interview_date <="2019-09-30")]
served_FY20 = served[(served.interview_date >="2019-10-01") & (served.interview_date <="2020-09-30")]
served_FY21 = served[(served.interview_date >="2020-10-01") & (served.interview_date <="2021-09-30")]
served_FY22 = served[(served.interview_date >="2021-10-01") & (served.interview_date <="2022-09-30")]
served_FY23 = served[(served.interview_date >="2022-10-01") & (served.interview_date <="2023-09-30")]
SERVED = DataFrame(
  {
    "FY18":[served_FY18.shape[0]],
    "FY19":[served_FY19.shape[0]],
    "FY20":[served_FY20.shape[0]],
    "FY21":[served_FY21.shape[0]],
    "FY22":[served_FY22.shape[0]],
    "FY23":[served_FY23.shape[0]]
  }
)

# to be served per Quater
unserved_Q1FY23 = to_be_served[(to_be_served.interview_date >="2022-10-01") & (to_be_served.interview_date <="2022-12-31")]

#unserved_FY22 = to_be_served[(to_be_served.interview_date >="2021-10-01") & (to_be_served.interview_date <="2022-09-30")]
unserved_Q1FY22 = to_be_served[(to_be_served.interview_date >="2021-10-01") & (to_be_served.interview_date <="2021-12-31")]
unserved_Q2FY22 = to_be_served[(to_be_served.interview_date >="2022-01-01") & (to_be_served.interview_date <="2022-03-31")]
unserved_Q3FY22 = to_be_served[(to_be_served.interview_date >="2022-04-01") & (to_be_served.interview_date <="2022-06-30")]
unserved_Q4FY22 = to_be_served[(to_be_served.interview_date >="2022-07-01") & (to_be_served.interview_date <="2022-09-30")]

#unserved_FY21 = to_be_served[(to_be_served.interview_date >="2020-10-01") & (to_be_served.interview_date <="2021-09-30")]

#unserved_FY20 = to_be_served[(to_be_served.interview_date >="2019-10-01") & (to_be_served.interview_date <="2020-09-30")]

#unserved_Before_FY20 = to_be_served[to_be_served.interview_date <= "2019-10-01"]

TOBESERVEDPERQUARTER = DataFrame.from_dict(
  {
    "unserved_Q1FY23":[unserved_Q1FY23.shape[0]],
    #"unserved_FY22":[unserved_FY22.shape[0]],
    #"unserved_FY21":[unserved_FY21.shape[0]],
    "unserved_Q1FY22":[unserved_Q1FY22.shape[0]],
    "unserved_Q2FY22":[unserved_Q2FY22.shape[0]],
    "unserved_Q3FY22":[unserved_Q3FY22.shape[0]],
    "unserved_Q4FY22":[unserved_Q4FY22.shape[0]],
    #"unserved_FY20":[unserved_FY20.shape[0]],
    #"unserved_Before_FY20":[unserved_Before_FY20.shape[0]]
  },
  orient='index',
  columns=["donnee"]
)
