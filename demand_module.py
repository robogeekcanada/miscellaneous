import pandas
import copy

percent = lambda x : x/100

def format_number(num):
  string = '{:,.2f}'.format(num)

  return string

def df_to_dict(df, Skus):

  Demand = {}

  for i, s in enumerate (Skus):

    row = df.iloc[i]
    row = row.to_dict()
    row = {int(k):int(v) for k,v in row.items()}

    sku_demand = {s: row} 
    #print(sku_demand)

    #create a new dictionary {A:{row A demand},... D:{row D demand}}
    Demand = dict(**Demand, **sku_demand)

  return Demand

def calculate_total_demand(Demand, Skus, Periods):
  
  total_demand = 0

  for i in Skus:
      sku_demand = Demand[i]
      for j in Periods:
        total_demand += sku_demand[j]

  return total_demand

def calculate_future_demand(Demand, Skus, Periods, compound_growth, period_year=0):

  future_demand = 0
  Demand_future = copy.deepcopy(Demand)

  for i in Skus:
    sku_demand = Demand_future[i]

    for j in Periods:
      future_demand = sku_demand[j]*(1+compound_growth)**period_year
      Demand_future[i][j] = future_demand

  return Demand_future


def calculate_future_demand2(Demand, Skus, Periods, growth, period_year=0):

  future_demand = 0
  Demand_future = copy.deepcopy(Demand)

  for i in Skus:
    sku_demand = Demand_future[i]

    for j in Periods:
      future_demand = sku_demand[j]*(1+percent(growth[i][j]))**period_year
      Demand_future[i][j] = future_demand

  return Demand_future


def calculate_total_production(Shifts, hours_shift, Rates):

  output = 0
  counter = 0

  total_shifts = 0
  rate_counter = 0

  for s in Shifts.values():

    output += s.varValue * list(Rates.values())[rate_counter]*hours_shift
    #print(list(Rates.values())[rate_counter], s.varValue, counter)

    total_shifts += s.varValue
    if (counter == 11):
      rate_counter +=1
      counter = -1
    
    counter +=1

  return output


