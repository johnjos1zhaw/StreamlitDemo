import streamlit as st
import pandas as pd
import plotly.express as px

url = 'https://storage.googleapis.com/kagglesdsdata/datasets/3052452/5245975/Methane_final.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230403%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230403T124951Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3032668656891a4fbe64c9416791af60d39d3c4cb6c3d5e045333fd2e72fac07da5241260ea0da07dd143cf6972e511c17d196e5f2990f302bec9cb577459382fc4775bead7cf3f22c9fdb4f65c0924b2e9368d3deec081ac3e6746e63e3fb451cb2bf6d7e4574152567e8860db70f9c71aa2018a1543814e571f48b2d7b8f386742b29cb0f97df4f4552d9dab0074cf5cef416dac2d0d7cf9f7299fdf2e6c09de489606144d5ea30729fbacadc7835b5e4910a4bd3a19ff523d4e427cc85d662c4477b731e05de3d7b2dc6eec7d1e4178286e4c90fb2599037d27e97134185c2da6e1e30a23531129f01f6667b62b684ba9c69f7b410bb17e6d54ed0536a8fd'
df = pd.read_csv(url)

st.title("Josh's Methane Emissions-Analytics App")
st.write('This is Joshs first demo of Streamlit using the methane emissions dataset from kaggle.')
st.write('https://www.kaggle.com/datasets/ashishraut64/global-methane-emissions')

st.write('The dataset contains the following relevant columns for our app:')
header_cols = list(df.columns[2:5])
st.write("**" + " | ".join(header_cols) + "**")

countries = df["country"].sort_values().unique()
selected_country = st.selectbox("**" + "Select a country" + "**", countries)

filtered_df = df[df["country"] == selected_country]

grouped_df = filtered_df.groupby("type")["emissions"].sum().reset_index()

st.write("This graph shows the total emissions by type for the selected country.")
fig = px.bar(grouped_df, x="type", y="emissions", color="type",
             title=f"Emissions by Type in {selected_country}")
st.plotly_chart(fig)
