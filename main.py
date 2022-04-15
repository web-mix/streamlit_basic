import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

option = st.text_input('あなたの趣味は？')
'あなたの好きな趣味は',option,'です'
condition = st.slider('調子は？', 0, 100 ,70)
'調子は＝',condition


if st.checkbox('Show Image'):
    img = Image.open('pict.png')
    st.image(img, caption='Ring',use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)


