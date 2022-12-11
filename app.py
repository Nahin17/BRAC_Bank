import pandas as pd
import plotly.express as px
import streamlit as st



st.set_page_config(page_title= "Brac Bank",
                         page_icon= ":bar_chart:",
                          layout= "wide"
)


#st.title("Excel app")
df=pd.read_excel('bracbank.xlsx')


st.sidebar.header('Please Filter Here: ')
Region = st.sidebar.multiselect(
    'Select All the Region : ',
     options=df['Region'].unique(),
     default=df["Region"].unique()
     )
     
#st.sidebar.header('Please Filter Here: ')
#C_Submission = st.sidebar.multiselect(
 #   'Select Total the Submission File: ',
 #    options=df['C_Submission'].unique(),
 #    default=df["C_Submission"].unique()
  #   )

   
st.sidebar.header('Please Filter Here: ')
City = st.sidebar.multiselect(
    'Select City: ',
     options=df['City'].unique(),
     default=df["City"].unique()
     )
    

    
#st.sidebar.header('Please Filter Here: ')
#Tpositive = st.sidebar.multiselect(
  #  'Select Total Visited File: ',
 #    options=df['Total Positive'].unique(),
  #  default=df["Total Positive"].unique()
 #    )
df_selection = df.query(
     'City == @City & Region == @Region '
   # 'City == @City & Region == @Region  & C_Submission == @C_Submission '
)

# ------- Mainpage-------

#st.title(":Bar_chart: Dashboard")
#st.markdown('##')

#top kpi's




total_submission = int(df_selection["C_Submission"].sum())
total_visited = int(df_selection["C_Visited"].sum())
total_Approval = int(df_selection["Total Approval"].sum())


 #average_file = round(df_selection["C_Submission"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total File Submission: ")
    st.subheader(f"Count: {total_submission:,}")

with middle_column:
    st.subheader("Total Visited: ")
    st.subheader(f"Count: {total_visited}")

with right_column:
     st.subheader("Total Approval: ")
     st.subheader(f"Count: {total_Approval:,}")
     
#with right_column:
 #   st.subheader("Average File Submission")
 #   st.subheader(f"{average_file}")

st.markdown("___")
# chart
total_positive_line= (
    df_selection.groupby(by=["Region"]).sum()[["Total Approval"]].sort_values(by="Total Approval")

    )
fig_total_positive = px.bar(
    total_positive_line,
    x="Total Approval",
    y=total_positive_line.index,
  
    title="<b> Auguest Month </b>",
    color_discrete_sequence=["#F63366"] * len(total_positive_line),
    template="plotly_white",

)
#st.plotly_chart(fig_total_positive)

pie_chart=px.pie(df_selection,
title="Total Approval",
values="Total Approval",

names='Region'
)




#st.plotly_chart(pie_chart)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_total_positive, use_container_width=True )
right_column.plotly_chart(pie_chart, use_container_width=True)





 
st.dataframe(df_selection)


