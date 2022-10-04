from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import streamlit as st
from selenium.webdriver.firefox.options import Options



file_names = []
month_names = []
links = []
image_url = "https://cdn-icons-png.flaticon.com/512/1213/1213206.png"






# add image_url in the title
st.markdown(f'<img src="{image_url}" alt="Logo" width="100" height="100">', unsafe_allow_html=True)
st.title('Download Reports')
start = st.button('Start...')


def download_reports():
    if "load_state" not in st.session_state:
        st.session_state.load_state = False
    if start or st.session_state.load_state:
        st.session_state.load_state = True
        firefoxOptions = Options()
        firefoxOptions.add_argument('--headless')
        firefoxOptions.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        firefoxOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
        url = "https://www.dropbox.com/sh/zdy808b2b9ip9s0/AAAPBGleZeOGZ1R_0qXMw2_da?dl=0"
        driver = webdriver.Firefox(executable_path="/home/appuser/.conda/bin/geckodriver",options=firefoxOptions)
        driver.get(url)

        sleep(5)

        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            sleep(10)
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("break")
                break
            last_height = new_height

        file_name = driver.find_elements(By.CLASS_NAME, 'mc-media-cell-content')
        url_link = driver.find_elements(By.XPATH, '//a[@href]')
        for file in file_name:
            if file.text.endswith('.xlsx') or file.text.endswith('.xls') or file.text.endswith('.csv'):
                entire_split = file.text.split('.')
                portal_name = entire_split[0].split('_')[0]
                months = entire_split[0].split('_')[1]
                if portal_name not in file_names:
                    file_names.append(portal_name)
                if months not in month_names:
                    month_names.append(months)


        for link in url_link:
            ax = link.get_attribute('href')
            if "https://www.dropbox.com/sh" in ax:
                links.append(ax)
        driver.quit()

        portal_name_1 = st.selectbox('**Select Portal**', list(file_names))
        month_name_1 = st.selectbox('Select Month', list(month_names))
        for link in links:
            if portal_name_1 in link and month_name_1 in link:
                replace_dl = link.replace('dl=0', 'dl=1')
                # design download button
                st.markdown(f'<a href="{replace_dl}" download="{portal_name_1}_{month_name_1}.xlsx" target="_blank" rel="noopener noreferrer"><button class="css-1aumxhk">Download</button></a>', unsafe_allow_html=True)
                # fill color of button
                st.markdown("""<style>
                .css-1aumxhk {
                    background-color: #ff0000;
                    color: #ffffff;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 20px;
                    font-weight: 600;
                    cursor: pointer;
                    }
                </style>""", unsafe_allow_html=True)
        st.write("Note: If Download Button is Not Available that Means Sales Report is Not Available for the Selected Month!")



    else:
        st.write('Press the button to start...')
    st.write("##")
    st.write("##")
    st.write("##")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            contact_form = """
            <div style="background-color:#f5f5f5;padding:8px;border-radius:15px">
            <h2 style="color:#ff0000;text-align:center;">Get In Touch With Me!</h2>
            <form action="https://formsubmit.co/rajinder@swissbeauty.in" method="POST">
            <div style="display:flex;justify-content:center;">
            <input type="text" name="name" placeholder="Your Name" style="width:300px;height:40px;border-radius:5px;border:1px solid #ccc;padding:10px;margin:10px;">
            </div>
            <div style="display:flex;justify-content:center;">
            <input type="email" name="email" placeholder="Your Email" style="width:300px;height:40px;border-radius:5px;border:1px solid #ccc;padding:10px;margin:10px;">
            </div>
            <div style="display:flex;justify-content:center;">
            <textarea name="message" placeholder="Message" style="width:300px;height:100px;border-radius:5px;border:1px solid #ccc;padding:10px;margin:10px;"></textarea>
            </div>
            <div style="display:flex;justify-content:center;">
            <button type="submit" style="width:300px;height:40px;border-radius:5px;border:1px solid #ccc;padding:10px;margin:10px;background-color:#ff0000;color:#ffffff;">Send</button>
            </div>
            </form>
            </div>

            """
            st.markdown(contact_form, unsafe_allow_html=True)

if __name__== "__main__":
    download_reports()
