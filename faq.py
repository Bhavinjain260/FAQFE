import streamlit as st

st.title("FundExpert FAQ by Bhavin")

st.header("Q1: How to update BSe Password in FE?")
st.subheader("Solution")
st.write("""quick guide to update your BSE password:
1. Login to the Admin Panel. \n
2. Navigate to the MIS tab. \n
3. Select My App Details. \n
4. Click on Edit App Details. \n
5. Locate the BSE Password field. \n
6. Enter your new BSE password. \n
7. Click the Submit button to save t he changes. \n
This should update your BSE password in the system.""")
# st.code('''# Example setup code\nimport xyz\nxyz.setup()''')

st.subheader("Screenshot/Video")
st.write("Coming Soon...")
# st.image("path_to_screenshot.png", caption="Setup Screenshot")
# st.video("https://drive.google.com/file/d/196jnOcFdrlaEbKaWWZgjfd4xWrrR2LjN/view?usp=sharing")


st.header("Q2: How to create family accounts?")
st.subheader("Solution")
st.write("""1. Login to the Admin Panel and search for the investor who will be the family head. Open their profile 
by clicking on their name. \n 2. Click Action > Add a Family Member, then select and add the respective family 
members.\n 3. Once all members are added, click Submit to form the family account. \n 4. To view the family accounts, 
go to Admin Panel > Main > Client Families.""")
# st.code('''# Configuration code\nimport abc\nabc.configure()''')

st.subheader("Screenshot/Video")
st.write("Coming Soon...")
# st.subheader("Screenshot/Video")
# st.image("path_to_another_screenshot.png", caption="Configuration Screenshot")
# st.video("https://drive.google.com/file/d/10jPTeq2OR750SQpS-BI0OgCFus741ySP/view?usp=sharing")


st.header("Q3: How to remove Family Link?")
st.subheader("Solution 1: Remove via Admin Panel")
st.write("""1. Login to the Admin Panel and navigate to Main > Client Families.\n
2. Select the Family Head’s name. \n
3. Scroll down to the family member you want to remove.\n
4. Click Remove Family Link on the right side.""")
st.subheader("Solution 2: Remove via Front Panel")
st.write("""1. Login to the Front Panel and search for the Family Head’s account.\n
2. In the Left Menu, click on My Family Accounts.\n
3. Click the X icon next to the family member you want to remove.""")
st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q4: How to Register AMC in BSE Star MF?")
st.subheader("Solution")
st.write("""1. Login to the BSE Star MF portal.\n
2. Go to the Admin section.\n
3. Navigate to Member Masters > Member AMC Mapping.\n
4. Choose the AMC with which you are empaneled.\n
5. Click Submit to save changes.""")
st.subheader("Screenshot/Video")
st.write("Coming Soon...")
# st.video("https://drive.google.com/file/d/1az1I7kbeE-hI5F24_g8ksceoROwuXDdj/view?usp=sharing")

st.header("Q5: How to mark clients inactive?")
st.subheader("Solution")
st.write("""1. Select the user in the Admin Panel.\n
2. Click on Action.\n
3. Choose Update User Settings.\n
4. Mark as Inactive.\n
5. Click on Submit to save the changes""")
st.subheader("Screenshot/Video")
st.write("Coming Soon...")


st.header("Q6: How to delete External holdings?")
st.subheader("Solution")
st.write("""1. Go to the Admin Panel and navigate to Main > Clients.\n
2. Search for the client's name and open their profile.\n
3. Click on Action.\n
4. Select Delete All External Holdings.""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q7: How to Send Login details")
st.subheader("Option 1: Front Panel")
st.write("""
1. In the Front Panel, go to the Clients section and list the clients.\n
2. Click the Share icon beside "Login as this user" and confirm.""")
st.subheader("Option 2: Admin Panel")
st.write("""1. In the Admin Panel, go to Main > Email Login Details.\n 2. Select a specific client or all clients.\n 
3. Click Apply to share the login details via email, which will include your website and app links along with their 
credentials.""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q8: How to enable the redeem option for client?")
st.subheader("Solution")
st.write("""
1. In the Admin Panel, go to Main > Clients. \n
2. Select the Client name.\n
3. Click on Update User Settings. \n
4. Enable the Allow Redeem on App option.\n 
5. Click Submit to save the changes\n

""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q9: How to update BSE Client master?")
st.subheader("Solution")
st.write("""1. Login to BSE and go to Admin > Admin Reports > Client Master Report. \n
2. Select the Old Date and export the report as a text file. \n
3. In the Admin Panel, go to Upload Utilities > BSE > BSE Client Master. \n
4. Select the file (Client Master file) and click Submit.""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q10: How to change the Address and Email ID of IFA displayed in the Reports.?")
st.subheader("Solution")
st.write("""1. Login to the Admin Panel.
2. Go to MIS > My App Details.
3. Click on Edit App Details.
4. Update the address and email ID as needed.
5. Click Submit to save the changes.""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q11: How to merge client.?")
st.subheader("Solutions")
st.write("""
1. Go to the Admin Panel.\n
2. Enter the Name/Email/Number/Client ID of the client you want to retain in the Search Tab.\n
3. Click on the client's name to go to their login page.\n
4. Click Action and select Merge Another User with This User.\n
5. On the new page, select the accounts you wish to merge into this account.\n
6. From the User Accounts Tab, select the accounts and click Add Account. Repeat if necessary for additional duplicates.\n
7. Click Submit to complete the merge.\n
""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q12: How to Demerge the accounts.?")
st.subheader("Solutions")
st.write("""
1. Go to the Admin Panel.\n
2. Under Users/Transactions, click on Inactive Users Report.\n
3. Enter the Name/Email/Number/Client ID of the client you wish to reactivate.\n
4. In the Search Tab, click on the client's name to go to their account.\n
5. Click on ACTION and select Demerge and Unban User from the dropdown.\n
""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q13: How to make inactive client active again.?")
st.subheader("Solutions")
st.write("""

1. Go to the Admin Panel.\n
2. Under Users/Transactions, click on Inactive Users Report.\n
3. Enter the Name/Email/Number/Client ID of the client you wish to reactivate.\n
4. In the Search Tab, click on the client's name to go to their account.\n
5. Click on ACTION and select Update User Setting .\n
6. Untick Mark inactive and click on Submit.\n
""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")

st.header("Q14: How to upload NSDL CAS for Stocks.?")
st.subheader("Solution")
st.write("""
1. Log in to the client’s account on the Front Panel.\n
2. Go to Stocks or Overall Dashboard.\n
3. Click Add Stocks.\n
4. Upload the NSDL PDF shared by the client.\n
5. Click Submit to complete the upload.\n
""")

st.subheader("Screenshot/Video")
st.write("Coming Soon...")
