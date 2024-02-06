import streamlit  as st
import pandas as pd 
import plotly.express as px 
from streamlit_option_menu import option_menu
from numerize.numerize import numerize


st.set_page_config(page_title="Dashbord",page_icon="🌍", layout="wide" )
st.subheader("🌍 Analyse de Donnnées  Business")
st.markdown("##")
df=pd.read_csv("customers.csv")

# side bar
st.sidebar.image("analyse.png", caption="Analyse en Ligne")

st.sidebar.header("Filtrer") 
City=st.sidebar.multiselect(
    "select city",
    options=df["City"].unique(),
    default=df["City"].unique(),
)
Country=st.sidebar.multiselect(
    "select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique(),
)

Age=st.sidebar.multiselect(
    "select Age",
    options=df["Age"].unique(),
    default=df["Age"].unique(),
)

Department=st.sidebar.multiselect(
    "select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
)

df_selection=df.query(
    "City==@City & Country==@Country & Age==@Age & Department==@Department"
)

#st.dataframe(df_selection)
def home():
 with st.expander("Tabular"):
        showData = st.multiselect('Filtrer', df_selection.columns.tolist(), default=[])
        st.write(df_selection[showData])
 # compute top analytics
 
 total_salaire=(df_selection["AnnualSalary"]).sum()
 salaire_mode=(df_selection["AnnualSalary"]).max()
 salaire_moyen=(df_selection["AnnualSalary"]).mean()
 salaire_median=(df_selection["AnnualSalary"]).median()
 Bonus=(df_selection["Bonus"]).sum()
 total1,total2,total3,total4,total5=st.columns(5,gap='large')
 with total1:
     st.info("Total Salary",icon="➕")
     st.metric(label="Somme dt", value=f"{total_salaire:,.0f}")
 with total2:
     st.info("Salary  moyen",icon="➕")
     st.metric(label="moyen  dt", value=f"{salaire_moyen:,.0f}")
 with total3:
     st.info("Salary  median",icon="➕")
     st.metric(label="median dt", value=f"{salaire_median:,.0f}")
 with total4:
     st.info("Salary  mode",icon="➕")
     st.metric(label="maximum dt", value=f"{salaire_mode:,.0f}")
 with total5:
     st.info("Bonus total",icon="➕")
     st.metric(label="Bonus", value=f"{Bonus:,.0f}")

home()



#create divs
div1, div2=st.columns(2)

#pie chart
def pie():
 with div1:
  theme_plotly = None # None or streamlit
  fig = px.pie(df_selection, values='AnnualSalary', names='Department', title='Customers by Country')
  fig.update_layout(legend_title="Country", legend_y=0.9)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#bar chart
def barchart():
  theme_plotly = None # None or streamlit
  with div2:
    fig = px.bar(df_selection, y='AnnualSalary', x='Department', text_auto='.2s',title="Controlled text sizes, positions and angles")
    fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")

pie()
barchart()



 

