import streamlit as st
import plotly.express as px
import datetime
from functions import get_data

# Setup GUI in Streamlit
st.title("Weather Forecast")

place = st.text_input("Place: ", value="Tampa", help="Enter a city name")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")

option = st.selectbox("Select data to view",
                      ("Temperatures", "Forecast"))
hours = days * 24
st.subheader(f"Three Hour {option} for next {hours} Hours in {place}")


if place:
    # get the data
    filtered_data = get_data(place, days)

    # Create Temp Plot or Sky Conditions
    if option == "Temperatures":
        temperatures = [dict1["main"]["temp"] for dict1 in filtered_data]

        dates = [dict2["dt_txt"] for dict2 in filtered_data]

        figure = px.line(x=dates, y=temperatures, labels={"x": "", "y": "Temperature (F)"})
        st.plotly_chart(figure)

    if option == "Forecast":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        # Get dates and plit into [year-month-day] and time [hour:min:sec]
        dates = [dict3["dt_txt"].split(" ") for dict3 in filtered_data]

        # go through list and convert dates to "Day, Month Date" and "Time(Hour:Min)"
        combined = []

        for x in range(len(dates)):
            # Remove seconds from Time
            time = dates[x][1]
            time_trunc = (time[:-3])

            # Convert Dates from year-month-day to month date: day of week
            date_strip = dates[x][0]
            day = datetime.datetime.strptime(date_strip, '%Y-%m-%d').strftime('%b %d: %a')

            # Combine Day/Month/Date and time for caption (ex output Aug 25: Fri 21:00)
            combined.append(day + ' ' + time_trunc)

        # Get Forecast Images
        sky_conditions = [dict4["weather"][0]["main"] for dict4 in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]

        # Display Images with Day/Month/Date/Time caption
        st.image(image_paths, caption=combined, width=150)
