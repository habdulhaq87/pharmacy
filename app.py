import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Database App", layout="wide")

# Sidebar navigation with buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Home", key="home_button"):
    page = "Home"
elif st.sidebar.button("Generate Graphs", key="generate_graphs_button"):
    page = "Generate Graphs"
elif st.sidebar.button("Add Row", key="add_row_button_sidebar"):
    page = "Add Row"
elif st.sidebar.button("About", key="about_button"):
    page = "About"
else:
    page = "Home"  # Default page

# Load the database.csv file
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('database.csv')
        return data
    except FileNotFoundError:
        st.error("The file 'database.csv' was not found in the main directory.")
        return None

# Home Page
if page == "Home":
    st.title("Database Visualization")

    # Load data
    data = load_data()

    if data is not None:
        # Display raw data with an expander
        st.subheader("Raw Data")
        with st.expander("Click to view the raw data"):
            st.dataframe(data)

        # Display basic statistics
        st.subheader("Data Summary")
        st.write(data.describe())

    else:
        st.warning("No data to display. Ensure 'database.csv' is in the main directory.")

# Generate Graphs Page
elif page == "Generate Graphs":
    import generate  # Import the generate.py script

    generate.visualize_data()  # Call the function from generate.py

# Add Row Page
elif page == "Add Row":
    import add  # Import the add.py script

    add.add_new_row()  # Call the function from add.py

# About Page
elif page == "About":
    st.title("About This App")
    st.write("""
        This application is designed to visualize data from a file named `database.csv` located in the main directory. 
        It provides the following features:

        - **Raw Data View**: Explore the dataset in a tabular format.
        - **Data Summary**: View basic statistical summaries of the dataset.
        - **Interactive Charts**: Create scatter, line, or bar charts by selecting columns for the X and Y axes.
        - **Add Rows**: Add new rows to the database using the Add Row page.

        ### How to Use:
        1. Place the `database.csv` file in the same directory as this application.
        2. Navigate to the **Home** page to explore data.
        3. Use the **Generate Graphs** page to create interactive visualizations.
        4. Use the **Add Row** page to insert new rows into the dataset.
        5. Use the sidebar to switch between pages.

        For best results, ensure that the `database.csv` file is properly formatted with clear column headers.
    """)
