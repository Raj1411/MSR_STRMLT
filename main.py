from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import streamlit as st
from selenium.webdriver.firefox.options import Options



# ==============================================================================================================================

file_names = []
month_names = []
links = []
image_url = "https://cdn-icons-png.flaticon.com/512/1213/1213206.png"
download_link = []
# ===============================================================================================================================


# add image_url in the title
st.markdown(f'<img src="{image_url}" alt="Logo" width="100" height="100">', unsafe_allow_html=True)
st.title('Download Reports')


f_names = ('','BigBasket','Meesho','Boddess','Smytten')
m_names = ('','Jan-22','Feb-22','Mar-22','Apr-22','May-22','June-22','July-22','Aug-22','Sep-22','Oct-22','Nov-22','Dec-22')

portal_name_1 = st.selectbox('Select Portal', f_names)
month_name_1 = st.selectbox('Select Month', m_names)


start = st.button('Generate Report  ...')

def download_reports():
    if start:
        firefoxOptions = Options()
        firefoxOptions.add_argument('--headless')
        firefoxOptions.add_argument('--no-sandbox')
        firefoxOptions.add_argument('--disable-dev-shm-usage')
        firefoxOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
        url = "https://www.dropbox.com/sh/zdy808b2b9ip9s0/AAAPBGleZeOGZ1R_0qXMw2_da?dl=0"
        driver = webdriver.Firefox(executable_path="/home/appuser/.conda/bin/geckodriver",options=firefoxOptions)
        driver.get(url)

        sleep(3)

        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            sleep(5)
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                # print("break")
                break
            last_height = new_height

        url_link = driver.find_elements(By.XPATH, '//a[@href]')

        for link in url_link:
            ax = link.get_attribute('href')
            if "https://www.dropbox.com/sh" in ax:
                aa = ax.replace("dl=0", "dl=1")
                links.append(aa)
        
        driver.quit()


        for link_1 in links:
            if portal_name_1 in link_1 and month_name_1 in link_1:
                download_link.append(link_1)

        if len(download_link) == 0:
            st.info("Sorry, Report is Not Available for this Month: " + month_name_1)
        else:
            st.info('Report is Ready to Download')
            st.markdown(f'<a href="{download_link[0]}" download="{portal_name_1}_{month_name_1}.xlsx" target="_blank" rel="noopener noreferrer"><button class="css-1aumxhk">Download</button></a>',
                unsafe_allow_html=True)
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


    with st.sidebar:
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
    if st.form_submit_button('Submit'):
        st.experimental_rerun()
            
#         st.write("[Back to Website > ] (https://raj1411-msr-strmlt-main-za0rgt.streamlitapp.com/)")












if __name__== "__main__":
    download_reports()
    
    
    
    
