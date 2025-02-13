
# Random Function
# slicing

# Example: Slicing a 1D array
array_1d =np.array([10,20,30,40,50])
print("Slice from index 1 to 4",array_1d[1:5])  # array_2d[rows(elements ]
print("Slice with step 2",array_1d[::2])

# Example: Slicing a 2D array
array_2d =np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Slice rows 0 to 1 and columns 1 to 2 ",array_2d[0:2,1:3]) # array_2d[rows(exclude last row), column]
print("Slice all rows and every other column ",array_2d[:,::2])


# Getting Started with Pandas Library
import pandas as pd
import numpy as np


#
data = {
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'Salary':[50000,60000,70000]
    }


df = pd.DataFrame(data)

# print("DataFrame: \n ",df)
print("Selecting a col: \n ",df['Name'])
print("Selecting a row by label: \n ",df.loc[1])
print("Selecting a row by Position: \n ",df.iloc[2])
# print("Selecting Multiple col: \n ",df['Name','Salary'])

# Creating Dataframe from numpy array

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
df_array = pd.DataFrame(array,columns=['A','B','C'])
print("\nDataFrame from numpy array:\n",df_array)

# Adding new col
df['New Salary']= df['Salary']*1.1
print("After adding new col: \n ",df)

# Creating value with missing data

data = {
    'A':[1,2,np.nan],
    'B':[4,np.nan,6]
}

df = pd.DataFrame(data)
print("\nDataframe with missing data:\n",df)
print("\nIdentify missing data:\n",df.isna)

# Dropping missing Data
df_dropped = df.dropna()
print("\nDropping missing data:\n",df_dropped)

# Filling missing Data
df_filled = df.fillna(0)
print("\nFilling missing data:\n",df_filled)


# Agents


# Example

class simplereflexagent:
  def __init__(self):
    pass

  def act(self, percept):
    if percept == 'Dirty':
      return 'Clean room'
    else:
      return 'Room Already cleaned'

class Environment:
  def __init__(self, state = 'Dirty'):
    self.state = state

  def get_percept(self):
    return self.state

  def clean_room(self):
    self.state = 'Clean'


def run_agent(agent, enviroment, steps):
      for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        print(f"step {step+1}: percept - {percept}, Action - {action}")
        if percept == 'Dirty':
          environment.clean_room()

agent = simplereflexagent()
environment = Environment()

run_agent(agent, environment,5)


