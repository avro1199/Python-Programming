import pandas as pd

df = pd.DataFrame(
    {
        'Name':['Alice', 'Bob', 'Charlie'],
        'History':[78, 80, 92],
        'Geography':[85, 88, 75],
        'Literature':[92, 85, 87]
    }
)

print(df)

#add Total
df['Total'] = (df['History'] + df['Geography'] + df['Literature']) / 3

print('\n', df, '\n')

#Only Geography Column
print(df['Geography'], '\n')

#row with highest total marks
highest = df['Total'].max()

print(df[df['Total'] == highest])