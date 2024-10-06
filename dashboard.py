import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data set
df = pd.read_csv('day.csv')

st.title('Bike Rental Dashboard')

# Display dataset information
st.subheader('Dataset Information')
st.write(df.describe())


# Sidebar to select features
st.sidebar.header('Settings')
selectedSeason = st.sidebar.selectbox('Choose Season', ['All', 'Summer', 'Winter', 'Spring', 'Autumn'])
selectedMonth = st.sidebar.selectbox('Choose Month', ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

if selectedSeason != 'All':
    seasonMap = {'Summer': 1, 'Winter': 2, 'Spring': 3, 'Autumn': 4}
    df = df[df['season'] == seasonMap[selectedSeason]]

if selectedMonth != 'All':
    monthMap = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    df = df[df['mnth'] == monthMap[selectedMonth]]
    
    
# Season Visualization
st.subheader('Number of Bike Rental Patterns by Season')
seasonal_rental_data = df.groupby('season')['cnt'].sum().reset_index()
season_mapping = {1: 'Summer', 2: 'Winter', 3: 'Spring', 4: 'Autumn'}
seasonal_rental_data['season'] = seasonal_rental_data['season'].map(season_mapping)

plt.figure(figsize=(10, 8))
sns.barplot(data=seasonal_rental_data, x='season', y='cnt', palette='viridis')
plt.title('Number of Bike Rental Patterns by Season')
plt.xlabel('Time of Year')
plt.ylabel('Rental Volume')
st.pyplot(plt)

# Visualization the number of bicycle renters in each month of the year
st.subheader('Number of Bike Renters in Each Month of The Year')
month_counts = df.groupby('mnth')['cnt'].sum().reset_index()


month_labels = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_counts['mnth'] = month_counts['mnth'].map(month_labels)


plt.figure(figsize=(10, 6))
sns.barplot(data=month_counts, x='mnth', y='cnt', palette='Blues')
plt.title('Number of Bicycle Renters in Each Month of the Year')
plt.xlabel('Month')
plt.ylabel('Number of Renters')
st.pyplot(plt)

# Conclusion
st.subheader('Conclusion')
st.write('This analysis shows The Number of Bike Rental Patterns by Season and Number of Bike Renters in Each Month of The Year.')


# Footer
st.markdown("""
*Developed by Shinta Praylina as part of the data analysis project.*
""")
