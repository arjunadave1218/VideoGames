from videogamesales import *
from data import *
import streamlit as st

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Video Game Success Prediction')
with row0_2:
    st.text("")
    st.subheader('By Arjuna Dave')

st.text("")
unsuccess = df.loc[df['Successful'] == 0]['Name'].count()
success = df.loc[df['Successful'] == 1]['Name'].count()

total = unsuccess+success
rate = "{:.2f}%".format(success/(unsuccess+success)*100)

col1, col2 = st.columns(2)
col1.markdown("<h4 style='text-align: center; color: grey;'>Total Available Video Games:</h4>", unsafe_allow_html=True)
col1.markdown("<h4 style='text-align: center; color: black; font-size: 40px'>" + str(total) + "</h4>", unsafe_allow_html=True)

col2.markdown("<h4 style='text-align: center; color: grey;'>Video Games with 1 Million or Higher sales:</h4>", unsafe_allow_html=True)
col2.markdown("<h4 style='text-align: center; color: black; font-size: 40px'>" + str(success) + "</h4>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>1 Million exceeding rate:</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green; font-size: 40px'>" + rate  + "</h1>", unsafe_allow_html=True)

st.text("")
st.text("")
with st.form("my_form"):
    st.write("")

    col1, col2 = st.columns(2)

    platform = col1.selectbox('Platform: ',platform_list)   
    genre = col2.selectbox('Genre: ', genre_list)  
    publisher = st.selectbox('Publisher: ', publishers_list) 
    Critic_Score = col1.number_input("Critic Score: ")
    Critic_Count = col2.number_input("Critic Count: ")
    User_Score = col1.number_input("User Score: ")
    User_Count = col2.number_input("User Count: ")
    developer = st.selectbox('Developer: ', developers_list)
    rating = col1.selectbox('Rating: ', rating_list)  

    Platform = platform_list.index(platform) + 1
    Genre = genre_list.index(genre) + 1
    Publisher = publishers_list.index(publisher) + 1
    Developer = developers_list.index(developer) + 1
    Rating = rating_list.index(rating) + 1
        
    try:
        col1, col2, col3 = st.columns((1.5,2,0.1))
        submitted = col2.form_submit_button("Submit")
        if submitted:
            new_row = [Platform, 
            Genre, 
            Publisher, 
            Critic_Score, 
            Critic_Count, 
            User_Score, 
            User_Count, 
            Developer, 
            Rating]

            df_columns = ['Platform', 
            'Genre', 
            'Publisher', 
            'Critic_Score', 
            'Critic_Count', 
            'User_Score', 
            'User_Count', 
            'Developer', 
            'Rating']
            
            dp_new = pd.DataFrame (new_row).T
            dp_new.columns = df_columns 
            
            
            # Random Forest
            rf_prediction = model_rf.predict(dp_new)
            if rf_prediction == 0:
                st.markdown("<h2 style='text-align: center; color: black;'>Video game will</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: center; color: grey; font-family:Courier; font-size: 40px;'>NOT EXCEED 1 MILLION SALES</h1>", unsafe_allow_html=True)

            else:
                st.markdown("<h2 style='text-align: center; color: black;'>Video game will</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: center; color: green; font-family:Courier; font-size: 40px;'>EXCEED 1 MILLION SALES</h1>", unsafe_allow_html=True)
                st.markdown("<h1 style='text-align: center; color: green; font-family:Courier; font-size: 60px;'>SUCCESSFUL!!</h1>", unsafe_allow_html=True)
                
            st.write("")
            st.write("")
            st.write("")
            
    except TypeError as err:
        st.write('err', err)