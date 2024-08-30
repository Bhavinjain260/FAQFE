import streamlit as st



faqs = {
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
        "media": "Coming Soon..."
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
        "media": "Coming Soon..."
    },
    "How to Register AMC in BSE Star MF?": {
        "solution": """
        1. Log in to the **BSE Star MF** portal.
        2. Go to the **Admin** section.
        3. Navigate to **Member Masters > Member AMC Mapping**.
        4. Choose the AMC with which you are empaneled.
        5. Click **Submit** to save changes.
        """,
        "media": "Coming Soon..."
    },
    "How to Mark Clients Inactive?": {
        "solution": """
        1. Select the user in the **Admin Panel**.
        2. Click on **Action**.
        3. Choose **Update User Settings**.
        4. Mark as **Inactive**.
        5. Click **Submit** to save the changes.
        """,
        "media": "Coming Soon..."
    },
    "How to Delete External Holdings?": {
        "solution": """
        1. Go to the **Admin Panel** and navigate to **Main > Clients**.
        2. Search for the client's name and open their profile.
        3. Click on **Action**.
        4. Select **Delete All External Holdings**.
        """,
        "media": "Coming Soon..."
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
        "media": "Coming Soon..."
    },
    "How to Enable the Redeem Option for Clients?": {
        "solution": """
        1. In the **Admin Panel**, go to **Main > Clients**.
        2. Select the client's name.
        3. Click on **Update User Settings**.
        4. Enable the **Allow Redeem on App** option.
        5. Click **Submit** to save the changes.
        """,
        "media": "Coming Soon..."
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
    "How to upload Logo and Email Banner":{
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
    "CRM Training video":{
        "solution": """
        Please find the CRS Training below
        """,
        "media": "https://player.vimeo.com/video/804824760#t=61m53s"

    }, "How to Update Mandate from BSE": {
        "solution": """
        
        1. Go to Admin Panel > Clients under Main.
        2. Search and select the client by clicking on their name.
        3. Click Action and select Update Mandate from BSE.
        4. This will fetch all mandates attached to the UCC.
        """,
        "media": "Coming Soon..."

    }, "How to Change the Family Head": {
        "solution": """
        1. Go to the Admin Panel > Clients under Main.
        2. Search and select the client by clicking on their name.
        3. Search and select the client by clicking on their name.
        4. Click Action and select Make User Family Head.
        
        Note: The selected member must already be an existing family member.
        """,
        "media": "Coming Soon..."

    }, "How to Reuse the same UCC if expired": {
        "solution":
        """
        1. Go to **Admin Panel > Clients** under **Main**.
        2. Click **Action** and select **Register/Update Client on BSE**.
        3. This will register the client with the same UCC.
        4. Log in to **BSE** and trigger the UCC mail.
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






}

st.title("FundExpert FAQ")
st.subheader("By Bhavin")

# Search functionality
search_query = st.text_input("Search FAQs", "")

# Filter FAQs based on the search query
if search_query:
    matched_faqs = {header: content for header, content in faqs.items() if search_query.lower() in header.lower()}
    if matched_faqs:
        for header, content in matched_faqs.items():
            st.header(header)
            st.subheader("Solution")
            st.write(content["solution"])
            st.subheader("Screenshot/Video")
            if content["media"] != "Coming Soon...":
                st.markdown(
                    f'<iframe src="{content["media"]}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                st.write(content["media"])
    else:
        st.write("No FAQs found for your search query.")
else:
    # Display all FAQs when there's no search query
    for header, content in faqs.items():
        st.header(header)
        st.subheader("Solution")
        st.write(content["solution"])
        st.subheader("Screenshot/Video")
        if content["media"] != "Coming Soon...":
            st.markdown(
                f'<iframe src="{content["media"]}" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>',
                unsafe_allow_html=True,
            )
        else:
            st.write(content["media"])
