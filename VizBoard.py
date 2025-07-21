# === IMPORT LIBRARIES ===
import streamlit as st                 # Web app UI
import pandas as pd                   # Data analysis and handling
from io import BytesIO                # In-memory file objects
import seaborn as sns                 # Data visualization (statistical)
import matplotlib.pyplot as plt       # Plotting (matplotlib backend)
import os
from fpdf import FPDF                 # Create PDFs
import plotly.express as px   
import streamlit as st
from PIL import Image

# Load and display the logo from the 'assets' folder
logo = Image.open("data:image/jpeg;base64,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")  # or logo.png
st.image(logo, width=145)# For interactive plots (optional usage)
# === WEBPAGE TITLE ===
st.markdown("""
    <h1 style='
        text-align: center;
        font-size: 48px;
        color: #ffffff;
        text-shadow: 2px 2px 4px #00cc99;
    '>Welcome to VizBoard</h1>
""", unsafe_allow_html=True)



# === DISPLAY STATIC IMAGE GALLERY OF GRAPH TYPES ===
st.subheader("Types of the Graphplots")

# First row (3 graph examples)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519083913/1.png", caption="Scatter Plot", use_container_width=True)
with col2:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519083914/2.png", caption="Line Plot", use_container_width=True)
with col3:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519083915/4.png", caption="Bar Plot", use_container_width=True)

# Second row (3 more graph examples)
col4, col5, col6 = st.columns(3)
with col4:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519083916/6.png", caption="Box Plot", use_container_width=True)
with col5:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519084142/11.png", caption="KDE Plot", use_container_width=True)
with col6:
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20240519084143/13.png", caption="ECDF Plot", use_container_width=True)

# === FUNCTION TO SHOW WHOLE GRAPH ON FULL DATA ===
def graph_show():
    st.subheader("The Full Data Graph")
    fig1 = plt.figure()
    if slide == "Scatter Plot":
        sns.scatterplot(df)
    elif slide == "Box Plot":
        sns.boxplot(df)
    elif slide == "Line Plot":
        sns.lineplot(df)
    elif slide == "Kernel Density Estimate Plot (kdeplot):":
        sns.kdeplot(df)
    elif slide == "Bar Plot":
        sns.barplot(df)
    elif slide == "Pairplot":
        sns.pairplot(df)
    st.pyplot(fig1)

# === FUNCTION TO PROCESS DATA (TOP, BOTTOM, DESCRIBE, FILTER) ===
def data_process():
    st.header("The Described Data Summary")

    global top, tail
    st.subheader("Top 10 Rows")
    top = df.head(10)
    st.write(top)

    st.subheader("Bottom 10 Rows")
    tail = df.tail(10)
    st.write(tail)

    st.subheader("Statistical Summary")
    st.write(df.describe())

    # Filter by X-axis value (in sidebar)
    if x_axis:
        global fa, filter_data, fi
        st.subheader(f"Filter by Unique {x_axis} Values")
        fa = df[x_axis].unique()
        filter_data = st.sidebar.selectbox(f"Filter {x_axis}", fa,key="filter x_axis")
        fi = df[df[x_axis] == filter_data]
        st.dataframe(fi)


    # Filter by Y-axis value (in sidebar)
    if y_axis:
        st.subheader(f"Filter by Unique {y_axis} Values")
        global la, ds, sd
        la = df[y_axis].unique()
        ds = st.sidebar.selectbox(f"Filter {y_axis}", la,key="filter y_axis")
        sd = df[df[y_axis] == ds]
        st.dataframe(sd)

       

    st.success("Data Summary Displayed Successfully!")

# === FUNCTION TO LET USER SELECT GRAPH TYPE FROM SIDEBAR ===
def graph():
    st.write("Select the type of graph:")
    global slide
    st.sidebar.subheader(" filters")
    slide = st.sidebar.selectbox("Select the Graph Plot", [
        "Scatter Plot", "Line Plot", "Bar Plot", "Box Plot",
        "Kernel Density Estimate Plot (kdeplot):", "Pairplot"
    ])

# === FUNCTION TO READ FILE ===
def read_file():
    global df
    df = pd.read_csv(file)
    graph()

# === FILE UPLOADER ===
file = st.file_uploader("Upload your file", type=["csv"])
if file:
    read_file()

# === BUTTON STYLING ===
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #ffcc00;
        color: black;
        border-radius: 10px;
        padding: 0.5em 2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# === STATE TO SWITCH BETWEEN PAGES ===
if "show_graphs" not in st.session_state:
    st.session_state.show_graphs = False

# === BUTTON TO PROCEED TO NEXT PAGE ===
col1, col2 = st.columns([1, 2])
with col2:
    if st.button("Show"):
        st.session_state.show_graphs = True
        st.rerun()

# === FUNCTION TO CREATE PDF FROM PLOT ONLY ===
from fpdf import FPDF
from PIL import Image
import tempfile
from io import BytesIO

def create_pdf_with_plot_only(plot_buf):
    plot_image = Image.open(plot_buf)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_plot:
        plot_image.save(tmp_plot.name)
        plot_path = tmp_plot.name

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Generated Plot", ln=True, align='C')
    pdf.image(plot_path, x=10, y=25, w=180)

    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_output = BytesIO(pdf_bytes)
    pdf_output.seek(0)

    return pdf_output

# === DISPLAY GRAPH + PROCESS DATA SECTION ===
if st.session_state.show_graphs:
    st.markdown("<h2 style='color:#00cc99;'>Graph Output Section</h2>", unsafe_allow_html=True)
    graph_show()

    # Select X and Y axis
    st.subheader("Compare the Graphs with X and Y")
    x_axis = st.sidebar.selectbox("Select X-axis column", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis column", df.columns)

    fig = plt.figure()

    if slide == "Scatter Plot":
        sns.scatterplot(data=df, x=x_axis, y=y_axis)
    elif slide == "Line Plot":
        sns.lineplot(data=df, x=x_axis, y=y_axis)
    elif slide == "Bar Plot":
        sns.barplot(data=df, x=x_axis, y=y_axis)
    elif slide == "Box Plot":
        sns.boxplot(data=df, x=x_axis, y=y_axis)
    elif slide == "Kernel Density Estimate Plot (kdeplot):":
        sns.kdeplot(data=df, x=x_axis, y=y_axis)
    elif slide == "Pairplot":
        st.pyplot(sns.pairplot(df))
        data_process()
        st.stop()

    plt.title(f"{y_axis} vs {x_axis} — {slide}")
    st.pyplot(fig)

    # Process data summary and filters
    data_process()

# === DOWNLOAD SECTION ===
col1, col2 = st.columns([1, 2])
with col2:
    file_name = st.text_input("Input the file name to save the graph:")
    if st.button("Download"):
        if file_name.strip():
            # Save plot to memory
            plot_buf = BytesIO()
            fig.savefig(plot_buf, format="png")
            plot_buf.seek(0)

            # Generate PDF and allow download
            pdf_file = create_pdf_with_plot_only(plot_buf)
            st.download_button(
                label="Download Graph + Data PDF",
                data=pdf_file,
                file_name=file_name.strip() + ".pdf",
                mime="application/pdf"
            )
            st.success("Graph + Data PDF downloaded successfully!")
