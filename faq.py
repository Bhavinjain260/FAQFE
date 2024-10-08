import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = st.secrets["smtp"]["server"]
SMTP_PORT = st.secrets["smtp"]["port"]
EMAIL_ADDRESS = st.secrets["smtp"]["email"]
EMAIL_PASSWORD = st.secrets["smtp"]["password"]  # Replace with your email password
TO_EMAIL_ADDRESS = st.secrets["smtp"]["to"]


# Function to send email
def send_email(name, arn, message):
    try:
        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Create the email content
        email_message = MIMEMultipart()
        email_message['From'] = EMAIL_ADDRESS
        email_message['To'] = TO_EMAIL_ADDRESS  # Sending to the same email
        email_message['Subject'] = "New Contact Us Form Submission"

        body = f"Name: {name}\nARN: {arn}\nMessage:\n{message}"
        email_message.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(email_message)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False


# Dictionaries for each section
home_solutions = {
    "How to Update BSE Password in FundExpert?": {
        "solution": """
        To update your BSE password, follow these steps:

        1. Log in to the **Admin Panel**.
        2. Navigate to the **MIS** tab.
        3. Select **My App Details**.
        4. Click on **Edit App Details**.
        5. Locate the **BSE Password** field.
        6. Enter your new BSE password.
        7. Click **Submit** to save the changes.

        Your BSE password will be updated in the system.
        """,
        "media": "https://drive.google.com/file/d/1XjT1B9V9VQRn8iYEwE8gebjFy_VJ2KhH/preview"
    },
    "How to Create Family Accounts?": {
        "solution": """
        To create family accounts:

        1. Log in to the **Admin Panel** and search for the investor who will be the family head. Open their profile by clicking on their name.
        2. Click **Action > Add a Family Member**, then select and add the respective family members.
        3. Once all members are added, click **Submit** to form the family account.
        4. To view the family accounts, go to **Admin Panel > Main > Client Families**.
        """,
        "media": "https://drive.google.com/file/d/1griEzJ3e1EIdhGV_-o3P67TkKQPIklQo/preview"
    },
    "How to Remove Family Link?": {
        "solution": """
        **Solution 1: Remove via Admin Panel**

        1. Log in to the **Admin Panel** and navigate to **Main > Client Families**.
        2. Select the Family Head’s name.
        3. Scroll down to the family member you want to remove.
        4. Click **Remove Family Link** on the right side.

        **Solution 2: Remove via Front Panel**

        1. Log in to the **Front Panel** and search for the Family Head’s account.
        2. In the **Left Menu**, click on **My Family Accounts**.
        3. Click the **X** icon next to the family member you want to remove.
        """,
        "media": "https://drive.google.com/file/d/1vFvOY9zNm6Z8X4LXUDv7jt2eK01mZ-Cu/preview"
    },
    "How to Mark Clients Inactive?": {
        "solution": """
        1. Select the user in the **Admin Panel**.
        2. Click on **Action**.
        3. Choose **Update User Settings**.
        4. Mark as **Inactive**.
        5. Click **Submit** to save the changes.
        """,
        "media": "https://drive.google.com/file/d/1uYZ2xj7s7vT6lY_eAy-iy-RYjk4PdfMM/preview"
    },
    "How to Delete External Holdings?": {
        "solution": """
        1. Go to the **Admin Panel** and navigate to **Main > Clients**.
        2. Search for the client's name and open their profile.
        3. Click on **Action**.
        4. Select **Delete All External Holdings**.
        """,
        "media": "https://drive.google.com/file/d/1-He13ftzVFHCjnPm8G1zrIPI092puNag/preview"
    },
    "How to Send Login Details?": {
        "solution": """
        **Option 1: Front Panel**

        1. In the **Front Panel**, go to the **Clients** section and list the clients.
        2. Click the **Share** icon beside "Login as this user" and confirm.

        **Option 2: Admin Panel**

        1. In the **Admin Panel**, go to **Main > Email Login Details**.
        2. Select a specific client or all clients.
        3. Click **Apply** to share the login details via email, which will include your website and app links along with their credentials.
        """,
        "media": "https://drive.google.com/file/d/1i9p-6tErEASNQA5MXpYdZWRx6vy2de4T/preview"
    },
    "How to Enable the Redeem Option for Clients?": {
        "solution": """
        1. In the **Admin Panel**, go to **Main > Clients**.
        2. Select the client's name.
        3. Click on **Update User Settings**.
        4. Enable the **Allow Redeem on App** option.
        5. Click **Submit** to save the changes.
        """,
        "media": "https://drive.google.com/file/d/1E1JMqD4_yxzY2LSpfNyyjV7ihNB26nk1/preview"
    },
    "How to Update BSE Client Master?": {
        "solution": """
        1. Log in to BSE and go to **Admin > Admin Reports > Client Master Report**.
        2. Select the old date and export the report as a text file.
        3. In the **Admin Panel**, go to **Upload Utilities > BSE > BSE Client Master**.
        4. Select the file (Client Master file) and click **Submit**.
        """,
        "media": "Coming Soon..."
    },
    "How to Change the Address and Email ID of IFA Displayed in the Reports?": {
        "solution": """
        1. Log in to the **Admin Panel**.
        2. Go to **MIS > My App Details**.
        3. Click on **Edit App Details**.
        4. Update the address and email ID as needed.
        5. Click **Submit** to save the changes.
        """,
        "media": "Coming Soon..."
    },
    "How to Merge Clients?": {
        "solution": """
        1. Go to the **Admin Panel**.
        2. Enter the Name/Email/Number/Client ID of the client you want to retain in the **Search** tab.
        3. Click on the client's name to go to their login page.
        4. Click **Action** and select **Merge Another User with This User**.
        5. On the new page, select the accounts you wish to merge into this account.
        6. From the **User Accounts** tab, select the accounts and click **Add Account**. Repeat if necessary for additional duplicates.
        7. Click **Submit** to complete the merge.
        """,
        "media": "Coming Soon..."
    },
    "How to Demerge the Accounts?": {
        "solution": """
        1. Go to the **Admin Panel**.
        2. Under **Users/Transactions**, click on **Inactive Users Report**.
        3. Enter the Name/Email/Number/Client ID of the client you wish to reactivate.
        4. In the **Search** tab, click on the client's name to go to their account.
        5. Click on **Action** and select **Demerge and Unban User** from the dropdown.
        """,
        "media": "Coming Soon..."
    },
    "How to Make an Inactive Client Active Again?": {
        "solution": """
        1. Go to the **Admin Panel**.
        2. Under **Users/Transactions**, click on **Inactive Users Report**.
        3. Enter the Name/Email/Number/Client ID of the client you wish to reactivate.
        4. In the **Search** tab, click on the client's name to go to their account.
        5. Click on **Action** and select **Update User Settings**.
        6. Untick **Mark Inactive** and click **Submit**.
        """,
        "media": "Coming Soon..."
    },
    "How to Upload NSDL CAS for Stocks?": {
        "solution": """
        1. Log in to the client’s account on the **Front Panel**.
        2. Go to **Stocks** or **Overall Dashboard**.
        3. Click **Add Stocks**.
        4. Upload the NSDL PDF shared by the client.
        5. Click **Submit** to complete the upload.
        """,
        "media": "Coming Soon..."
    },
    "How to upload Logo and Email Banner": {
        "solution": """
        1. Prepare files:

        > Logo: 600x600 pixels (name it "Logo").\n
        > Email Banner: 850x150 pixels (name it "EmailBanner").
        2. Go to Admin Panel > MIS > My App Details.
        3. Upload (left side options):
        > Logo.\n
        > Email Banner.
        """,
        "media": "Coming Soon..."
    },
    "CRM Training video": {
        "solution": """
        Kindly click [here](https://vimeo.com/fundexpert/otherproductscrmenglish?ts=124000) and watch the video from 1hr:02min onwards to know about CRM.
        """,
        "media": "Coming Soon..."
    },

    "How to Update Mandate from BSE": {
        "solution": """

        1. Go to Admin Panel > Clients under Main.
        2. Search and select the client by clicking on their name.
        3. Click Action and select Update Mandate from BSE.
        4. This will fetch all mandates attached to the UCC.
        """,
        "media": "https://drive.google.com/file/d/1l5GN2JNHQNnipOTS3ykQi13hOoy4dvLK/preview"

    },
    "How to Change the Family Head": {
        "solution": """
        1. Go to the Admin Panel > Clients under Main.
        2. Search and select the client by clicking on their name.
        3. Search and select the client by clicking on their name.
        4. Click Action and select Make User Family Head.

        Note: The selected member must already be an existing family member.
        """,
        "media": "Coming Soon..."

    },
    "How to Reuse the same UCC if expired": {
        "solution":
            """
            1. Go to **Admin Panel > Clients** under **Main**.
            2. Click **Action** and select **Register/Update Client on BSE**.
            3. This will register the client with the same UCC.
            4. Log in to **BSE** and trigger the UCC mail.
            """,
        "media": "Coming Soon..."
    },

    "How to Remove profile picture from app": {

        "solution": """
    1. Navigate to the admin panel.
    2. Click on Clients under Main.
    3. Search and click on the client's name to open the account.
    4. Click on Action.
    5. Click on "Remove Profile Picture."
            """,
        "media": "Coming Soon..."
    },

    "How to remove M-pin": {
        "solution": """
    1. Navigate to the admin panel.
    2. Click on Clients under Main.
    3. Search and click on the client's name to open the account.
    4. Click on Action.
    5. Click on "Remove Mpin."
    """,
        "media": "Coming Soon..."
    },

    "Digi Locker KYC Flow": {
        "solution": """

        Instructions to Investors

        Step 1 → Fill in your Identity details & upload a scanned copy of your PAN Card.
        Ensure the scanned image has PAN Number, Name, DOB, Signature, Father’s Name, Photo, and issuer name clearly visible.

        Step 2 → You will be redirected to the Digilocker platform to fetch address details & necessary address proof. 
        Aadhaar to Phone linking is mandatory for this step, so please ensure you have the registered phone number available to input the OTP**.

        Step 3 → Upload a scanned image of your signature.

        Step 4 → Enter additional details required for KYC.

        Step 5 → You will be redirected to review your KYC details and e-sign the document using Aadhaar for final submission.

        Step 6 → Completion of e-sign will put your KYC for review. In 5 to 7 working days, you will receive a notification via email.

        *NRIs, Minors, and Non-individuals cannot use the online Digilocker Aadhaar KYC mode. Please reach out to your advisor for further assistance.
        **If your Aadhaar Phone linking is not available, then the online Digilocker Aadhaar KYC mode cannot be completed. Please reach out to your advisor for further assistance.
                """,
        "media": "https://drive.google.com/file/d/1Icg0pDS-05KZjjHVvEgjVkQxyUH0cNgi/preview"
    },
}

bse_solutions = {

    "BSE Onboarding Checklist": {

        "solution": """
    DETAILS required to onboard a new client who is
    KYC compliant on FundExpert to open an account at BSEStar:
    1. **Full Name as per PAN:**
    2. **Email:**
    3. **Mobile:**
    4. **PAN No:**
    5. **Date of Birth:**
    6. **Occupation:**
    7. **Marital Status:**
    8. **Address & Pincode:**
    9. **Bank Details:**
        - a) Bank IFSC Code:
        - b) Bank Account Number:
        - c) Bank Account Type:
    10. **Nominee Details:**
        - a) Nominee Name:
        - b) Relation with Nominee:
        - c) Percentage:
    11. **Place of Birth:**
    12. **Specimen Signature Image:** 
        - On white plain paper with blue ink pen.
            """,
        "media": "Coming Soon..."
    },

    "How to resend UCC Authentication mail from BSE": {
        "solution": """
    1. Log in to **BSE**.
    2. Go to **Admin > Resend Email Authentication**.
    3. Select **Process Type: UCC Authentication**.
    4. Enter **Client ID**.
    5. Click **Send** to resend the UCC Authentication mail.
    """,
        "media": "Coming Soon..."
    },

    "How to check Nominee authentication status": {
        "solution": """
        1. Navigate to BSE.
        2. Go to Admin.
        3. Click on Admin Report.
        4. Select Client Master Report New to check the nominee authentication status.
                """,
        "media": "Coming Soon..."
    },
    "How to resend Nominee authentication link": {
        "solution": """
    1. Navigate to BSE.
    2. Go to Admin.
    3. Click on Nominee Resend Authentication.
    4. Click on the Clients name from the list and click on resend 
            """,
        "media": "Coming Soon..."
    },

    "How to Onboard Minor Client": {

        "solution": """
    Documents for Minor:
    1. Proof of Date of Birth of the Minor:
       - You can click a picture of either of the following documents:
         Birth Certificate, School Leaving Certificate, or others.
    2. If the guardian is not a parent, then a picture of the court order specifying the individual as the Guardian.
    3. Signature Image of the guardian in blue ink on a white sheet of paper.

    Process:
    1. Onboard the client on FundExpert and create the UCC.
    2. Once the UCC is created, ensure it is authenticated.
    3. For minors, upload the cheque or bank statement directly on BSE:
       - From FE’s admin, directly login to BSE.
       - In BSE -> Admin -> Client Details -> Elog/Image Upload.
       - Enter the client code, select the type as cheque, and upload the bank proof in PDF.
       - BSE will take 24 hours to make the UCC active.

    4. From the front panel:
       - Upload all the documents and download the AOF by clicking on "Download Generated AOF".

    5. From FE’s admin, directly login to BSE:
       - In BSE -> Admin -> Client Details -> Elog/Image Upload.
       - Enter the client code, select the type as UCC, and upload the downloaded AOF.

    6. In FE:
       - Go to Admin -> Main -> Users.
       - Click on "Mark AOF as Done" in Quick Action for that client.
    """,
        "media": "Coming Soon..."
    },

    "How to Onboard NRI Clients": {
        "solution": """

    **Documents Required:**
    1. **Cheque Copy with NRI Tax Status:**
       - The cheque copy must clearly display the NRI Tax status.
    2. **Standard Onboarding Documents:**
       - All other documents required for individual client onboarding (e.g., PAN card, proof of address, etc.).

    **Onboarding Process from Fund Expert (FE):**

    1. **Add Client:**
       - Navigate to the "Add Client" option in FundExpert.
       - Select the client type as **NRI** to onboard the client accordingly.

    2. **Fill out Details and Create UCC:**
       - Enter all necessary client details in the onboarding form.
       - Create the **Unique Client Code (UCC)** for the client.
       - **Important:** Ensure that the UCC is authenticated by the client to proceed.

    3. **Upload Documents:**
       - Go to the "Upload Document" section within FundExpert.
       - Upload the **Cheque Copy with NRI Tax Status** and any other required standard documents.
       - After uploading, click on **"Download Generated AOF"** to obtain the Application-cum-Client Agreement Form (AOF).

    4. Complete the Profile by Submitting the AOF and FATCA (Same as individual client)

    **Completion:**
    - Once all the above steps are completed, the NRI client's onboarding process is successfully finalized.
    - The client's UCC will become active within 24 hours after uploading the necessary documents in BSE.
    """,
        "media": "Coming Soon..."
    },

    "How to onboard HUF client": {

        "solution": """

    Documentation Required:
    1. HUF PAN Copy
    2. Image of KARTA's signature under his seal (blue ink)

    Onboarding Process from Fund Expert (FE):

    1. Add Client:
    - Use the "Add Client" option to onboard the client as HUF.

    2. Fill out Details and Create UCC:
    - Fill out all necessary details and create the UCC.
    - Ensure the UCC is authenticated by the client.

    3. Upload Documents:
    - In the "Upload Document" section, upload the HUF PAN and Karta’s signature image.
    - Download AOF (Application-cum-Client Agreement Form): Click on "Download Generated AOF" to download the AOF.

    4. Upload AOF in BSE:
    - Navigate to BSE -> Admin -> Client Details -> Elog/Image Uploaded.
    - Enter the client code, select the type as UCC, and upload the downloaded AOF.

    5. Mark AOF as Done in FE:
    - In FE, go to admin -> Main -> Users.
    - Click on "Mark AOF as Done" in Quick Action for that client.

    6. Fill out FATCA and Submit from FE:
    - Fill out the FATCA form and submit it from FE.
    - Download AOF in PDF from BSE: Login to BSE and download the AOF in PDF format.
    - Path: Admin » Client Details » AOF / FATCA Download.

    7. Upload FATCA in BSE:
    - Navigate to BSE -> Admin -> Client Details -> Elog/Image Uploaded.
    - Upload the first 3 pages of the FATCA as a PDF, ensuring the client's signature is included on the 3rd page.

    8. Mark FATCA as Done in FE:
    - In FE, go to admin -> Main -> Users.
    - Click on "Mark FATCA as Done" in Quick Action for that client.

    By following these steps, you can successfully onboard HUF clients and ensure all necessary documentation is submitted and authenticated.
    """,
        "media": "Coming Soon..."
    },

    "How to onboard PartnerShip firm": {
        "solution": """

    How to Onboard a Partnership Firm

    **Required Documents:**
    1. Cancelled Cheque
    2. PAN Image
    3. Company's Sign with Seal (on white paper)
    4. Partnership Deed (First and Last Page)

    **Process:**

    1. **Onboard the Client on FundExpert:**
        - Register the partnership firm as a client in FundExpert.
        - After the profile is saved, the BSE UCC will be created.

    2. **Complete Required Authentication:**
        - Once the UCC is created, ensure that the required authentication is done.

    3. **Upload Documents and Download AOF:**
        - Upload all the required documents listed above.
        - Download the AOF (Account Opening Form) by clicking on "Download AOF Generated."

    4. **Upload AOF to BSE:**
        - In FundExpert (FE) Admin, use the option "Directly Login to BSE."
        - In BSE, navigate to: 
          - Admin → Client Details → Elog/Image Upload
        - Enter the client code, select the type as "UCC," and upload the downloaded AOF.

    5. **Mark AOF as Done in FundExpert:**
        - In FE, go to:
          - Admin → Main → Users
        - Click on "Mark AOF as Done" in Quick Action for that client.

    6. **Fill Out and Submit FATCA in FundExpert:**
        - Fill out the FATCA form and submit it from FE.

    7. **Download AOF from BSE:**
        - Login to BSE and download the AOF in PDF format.
        - Path: Admin → Client Details → AOF/FATCA Download

    8. **Upload FATCA to BSE:**
        - Navigate to:
          - BSE → Admin → Client Details → Elog/Image Upload
        - Upload the first 3 pages of the FATCA as a PDF, ensuring the client's signature is included on the 3rd page.

    9. **Mark FATCA as Done in FundExpert:**
        - In FE, go to:
          - Admin → Main → Users
        - Click on "Mark FATCA as Done" in Quick Action for that client.

    By following these steps, you can successfully onboard a partnership account and ensure all necessary documentation is submitted and authenticated.
            """,
        "media": "Coming Soon..."
    },
    "How to onboard Private Limted Company using BSE": {
        "solution": """
        Here’s the complete onboarding process tailored for a Private Limited Company:

        ### **Private Limited Company Onboarding Process**
        **Documents and Details Required:**

        - **PAN Card**: Company PAN
        - **Board Resolution**: Authorizing the account opening
        - **Authorized Signatory List**
        - **Signature Image**: With seal (blue ink)

        ### **Onboarding Process via Fund Expert (FE):**

        1. **Add Client as a Private Limited Company:**
           - Use the "Add Client" option in Fund Expert to onboard the client as a Private Limited Company.
           - Fill out all necessary details such as the company's name, contact information, and address.

        2. **Fill out Details and Create UCC:**
           - Complete the required fields to create the UCC (Unique Client Code).
           - Ensure the UCC is authenticated by the client.

        3. **Upload Documents:**
           - In the "Upload Document" section, upload the company's PAN, Board Resolution, Authorized Signatory list, and the signature image with the blue ink seal.

        4. **Download the AOF (Account Opening Form):**
           - After filling out the details, download the AOF by clicking on the "Download Generated AOF" option.

        5. **Upload the AOF to BSE:**
           - Go to BSE > Admin > Client Details > Elog/Image Uploaded.
           - Enter the client code and select "UCC" as the document type.
           - Upload the AOF that was generated and downloaded in the previous step.

        6. **Mark AOF as Done in FE:**
           - In Fund Expert, navigate to Admin > Main > Users.
           - Use the "Quick Action" option to select "Mark AOF as Done" for that client.

        7. **Complete FATCA and Submit from FE:**
           - Complete the FATCA form in FE with the required financial and tax information.
           - Submit the FATCA form from Fund Expert.

        8. **Download the AOF from BSE in PDF format:**
           - In BSE, navigate to Admin > Client Details > AOF / FATCA Download.
           - Download the AOF document in PDF format.

        9. **Upload FATCA in BSE:**
           - Go to BSE > Admin > Client Details > Elog/Image Uploaded.
           - Upload the first 3 pages of the FATCA form as a PDF.
           - Ensure the company's authorized signatory's signature is on the third page.

        10. **Mark FATCA as Done in FE:**
            - In FE, go to Admin > Main > Users.
            - Select the client and click on "Mark FATCA as Done" under Quick Actions.

        By following these steps, you can successfully complete the onboarding process for Private Limited Company clients, ensuring all documents are authenticated and properly submitted. Let me know if there's anything else you need!

        """, "media": "Coming Soon..."

    },

    " How to onboard Proprietorship using BSE": {
        "solution": """
        Documents and Details Required:
        
        Bank Details: Provide the current account details.
        Signature: Proprietor’s signature on a white paper.
        Onboarding Process via Fund Expert (FE):
        1. Add Client as Proprietorship:
        
        Use the "Add Client" option in Fund Expert to onboard the client as a Proprietorship.
        Fill out all necessary details such as the proprietor's name, contact information, and address.
        2. Fill out Details and Create UCC:
        
        Complete the required fields to create the UCC (Unique Client Code).
        Ensure the UCC is authenticated by the client.
        3. Upload Documents:
        
        In the "Upload Document" section, upload the Proprietorship PAN and the proprietor’s signature.
        4. Download the AOF (Account Opening Form):
        
        After filling out the details, download the AOF by clicking on the "Download Generated AOF" option.
        5. Upload the AOF to BSE:
        
        Go to BSE > Admin > Client Details > Elog/Image Uploaded.
        Enter the client code and select "UCC" as the document type.
        Upload the AOF that was generated and downloaded in the previous step.
        6. Mark AOF as Done in FE:
        
        In Fund Expert, navigate to Admin > Main > Users.
        Use the "Quick Action" option to select "Mark AOF as Done" for that client.
        7. Complete FATCA and Submit from FE:
        
        Complete the FATCA form in FE with the required financial and tax information.
        Submit the FATCA form from Fund Expert.
        8. Download the AOF from BSE in PDF format:
        
        In BSE, navigate to Admin > Client Details > AOF / FATCA Download.
        Download the AOF document in PDF format.
        9. Upload FATCA in BSE:
        
        Go to BSE > Admin > Client Details > Elog/Image Uploaded.
        Upload the first 3 pages of the FATCA form as a PDF.
        Ensure the client's signature is on the third page.
        10. Mark FATCA as Done in FE:
        
        In FE, go to Admin > Main > Users.
        Select the client and click on "Mark FATCA as Done" under Quick Actions.
        
        By following these steps, you can successfully complete the onboarding process for Proprietorship clients, ensuring all documents are authenticated and properly submitted.
                
    """, "media": "Coming Soon..."

    }

}

nse_solutions = {

    "How to update Nse data for all clients": {
        "solution": """
    1. Navigate to the admin panel.
    2. Under Upload Utilities, click on NSE.
    3. For updating the IINs, click on "Add all IINs."
       - For updating the Mandates, click on "Update all Mandates."
       - For updating bank details, click on "Update all bank details for all IINs."
            """,
        "media": "Coming Soon..."
    },
    "How to update Nse data for specific client": {
        "solution": """
    1. Navigate to the admin panel.
    2. Click on Clients under Main.
    3. Search and click on the client's name to open the account.
    4. Click on Action.
       - For updating the mandate data, click on "Update Mandates from NSE."
       - For updating the details in IIN, click on "Update IIN details from NSE."
       - For updating the bank details, click on "Update All Bank Accounts as per NSE."
            """,
        "media": "Coming Soon..."},
}

mfu_solutions = {
}


def search_solution(query, solutions_dicts):
    results = {}
    for solutions_dict in solutions_dicts:
        for title, content in solutions_dict.items():
            if query.lower() in title.lower():
                results[title] = content
    return results if results else {}


# Main function for Streamlit app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "BSE", "NSE", "MFU", "Contact Us"])

    st.title("FundExpert - Financial Portal")
    st.text("By Bhavin")

    # Search functionality
    search_query = st.text_input("Search for solutions")

    # Create a list of all solution dictionaries
    all_solutions = [home_solutions, bse_solutions, nse_solutions]  # Add mfu_solutions when available

    # Determine which page's solutions to display
    if page == "Home":
        solutions_dict = home_solutions
    elif page == "BSE":
        solutions_dict = bse_solutions
    elif page == "NSE":
        solutions_dict = nse_solutions
    elif page == "MFU":
        solutions_dict = {}  # Replace with actual MFU solutions
    else:  # Contact Us
        solutions_dict = {}

    # Display matching solutions or all solutions if no search
    if search_query:
        results = search_solution(search_query, all_solutions)  # Search in all solutions
    else:
        results = solutions_dict

    if results:
        for title, content in results.items():
            st.subheader(title)
            st.write(content["solution"])
            if content["media"] != "Coming Soon...":
                st.markdown(
                    f'<iframe src="{content["media"]}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                st.write(content["media"])

    # Contact Us page
    if page == "Contact Us":
        st.subheader("Contact Us Form")
        with st.form("contact_form"):
            name = st.text_input("Name")
            arn = st.text_input("ARN")
            message = st.text_area("Message")
            submit_button = st.form_submit_button(label="Submit")

            if submit_button:
                if send_email(name, arn, message):
                    st.success("Thank you for reaching out! We'll get back to you soon.")
                else:
                    st.error("Failed to send your message. Please try again later.")


if __name__ == "__main__":
    main()
