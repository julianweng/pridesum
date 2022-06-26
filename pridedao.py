import streamlit as st
import requests
import pandas as pd

#st.set_page_config(layout="wide")

@st.cache
def getOwners(dao):
    payload= {"PublicKeyBase58Check":"","Username":dao,"FetchAll":True, "IsDAOCoin":True}
    response = requests.post(url="https://api.bitclout.com/api/v0/get-hodlers-for-public-key", json=payload)
    info = response.json()
    df = pd.DataFrame(columns=('Owner', 'Balance'))
    idx=0
    for i in info['Hodlers']:
        df.loc[idx] = [i['ProfileEntryResponse']['Username'], int(i['BalanceNanosUint256'],16)/10**18];
        idx += 1;
        #print(int(i['BalanceNanosUint256'],16)/10**18, i['ProfileEntryResponse']['Username'])
    return df
daos = ["PrideSeed","RainbowWave","PrideSanctuary","PrideBot"]
st.title('Pride DAO Exchange')

for i in daos:
    df = getOwners(i)
    st.subheader(i+" Owners")
    st.dataframe(df)


st.write(f"Made with love from [Pridesum](https://github.com/julianweng/pridesum)")