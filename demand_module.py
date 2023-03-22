import pandas
import copy

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

  return format_number(total_demand)

def calculate_future_demand(Demand, Skus, compound_growth, period_year=0):

  future_demand = 0
  Demand_future = copy.deepcopy(Demand)

  for i in Skus:
    sku_demand = Demand_future[i]

    for j in Periods:
      future_demand = sku_demand[j]*(1+compound_growth)**period_year
      Demand_future[i][j] = future_demand

  return Demand_future
