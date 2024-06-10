import pandas as pd

df = pd.read_csv(r'C:\Users\ferre\Documents\github week\job-search.csv', delimiter=';', index_col=0)

print(df.head())

unique_area_eng = df[df.iloc[:,1]=='Engenharia'].iloc[:,2].unique()
unique_area_IT = df[df.iloc[:,1]=='IT'].iloc[:,2].unique()

# for i in unique_area_eng:
#     print(df[df.iloc[:,1]=='Engenharia'][df.iloc[:,2]==i].iloc[:,6].unique())
# for i in unique_area_IT:
#     print(df[df.iloc[:,1]=='IT'][df.iloc[:,2]==i].iloc[:,6].unique())

source = [0,0,0,0,0,0,0,0,0,0,0,
          1,1,1,1,
          2,3,4,5,6,7,7,
          8,9,
          10,11,12,
          13,13,13,14,14]
target = [2,3,4,5,6,7,8,9,10,11,12,
          11,9,7,12,
          13,13,13,13,13,13,14,
          13,13,
          13,13,13,
          15,16,17,17,18]
value  = [7,10,1,2,6,7,2,4,3,1,1,
          6,1,6,3,
          7,10,1,2,6,10,3,
          2,5,
          3,7,4,
          29,27,1,2,1]

import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(valueformat = "d",arrangement='snap',
    node = dict(
      pad = 10,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = list(df.iloc[:,1].unique()) + list(unique_area_eng) + ['Não', 'Sim'] + list(df.iloc[:,7].unique())),
    link = dict(
      source = source, 
      target = target,
      value =  value,

  ))])

cols = df.columns[[1,2,6,7]]
for x_coordinate, column_name in enumerate(cols):
  fig.add_annotation(
          x=x_coordinate / (len(cols) - 1),
          y=1.05,
          xref="paper",
          yref="paper",
          text=column_name,
          showarrow=False,
          font=dict(
              family="Times",
              size=16,
              color="yellow"
              ),
          align="center",
          )

import plotlyshare

fig.update_layout(title_text="Busca por emprego Mai-Jun 2024",
                  font_size=12,font_color='yellow',
                  paper_bgcolor='black',
                  width=1000, height=700)
# fig.show(renderer='plotlyshare')
fig.show()