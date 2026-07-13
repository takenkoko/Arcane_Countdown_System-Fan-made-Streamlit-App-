import streamlit as st
import base64
from datetime import date
from datetime import date
import time
import random
import os


#=============
#背景設定
#=============
def set_background(image_file):
    with open(image_file, "rb")as f:
        data= base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp{{
           background-image:url("data:image/jpeg;base64,{data}");
           linear-gradient(rgba(0,0,0,0.35),rgba(0,0,0,0.35)),
           
           background-size: contain;   
           background-position: center bottom;
           background-attachment:fixed;
           background-repeat: no-repeat;
        }}
        .block-container{{
           background-color: transparent;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

if os.path.exists("images/Arcane_Coundown_Kaba-3.jpg"):
    set_background("images/Arcane_Coundown_Kaba-3.jpg")

#=============================
#アプリのスタイル、見た目の設定
#=============================
left, right = st.columns([1,2])

with right:
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.title("🚀Arcane Countdown System")
    st.subheader("Synchronizing with July 16, 2026...")
    
    release_date = date(2026,7,16)
    today = date.today()
    days_left = (release_date-today).days

#=============
#ボタンを設置
#=============
    if st.button("LAUNCH COUNTDOWN",use_container_width=True):
        status_text = st.empty()
        progress_bar = st.progress(0)
    
        #演出用カウントダウンループ
        for i in range(10,0,-1):
            status_text.markdown(f"### ⚙ Loading resources...{i}")
            progress_bar.progress((10 - i )* 10)
            time.sleep(0.3)
            
        status_text.empty()
        progress_bar.empty()
        
        #結果表示
        st.balloons()
        st.success(f"🎉Synchronized! {days_left} Days remaining until ARCANE!") 

        # 日替わりメッセージを追加
        messages=[
            "Stay hydrated,Endmin🥤",
            "May your pulls be blessed!",
            "Another day closer to ARCANE!",
            "Prepare youre squad!",
            "Don't forget to take a break."
            " The countdown continues!"
        ]
        
        daily_message = messages[date.today().toordinal() % len(messages)]

        st.info(f"🗓️Daily Message\n\n{daily_message}")

        luck_messages=[
            ("★★★★★","Incredible Luck!","Today might be your day!","images/08.png"),
            ("★★★★☆","Great Luck!","your chances look promising.","images/03.png"),
            ("★★★☆☆","Normal Luck","Anything can happen today.","images/07.png"),
            ("★★☆☆☆","Not Bad","Save some luck for tomorrow.","images/06.png"),
            ("★☆☆☆☆","uh-oh...","Maybe today isn't your day...😂","images/01.png")
        ]

        stars,title,messages,image = random.choice(luck_messages)

        st.info(f"""
                Today's Gacha Luck

                {stars}

                **{title}**

                {messages}
                
                """)
        
        image_col1,col2,col3 = st.columns([1,2,1])

        with col2:
            if os.path.exists(image):
                st.image(image,width=300)
            else:
                st.error(f"画像ファイルがみつかりません：{image}")

        st.caption("🎲Randomly generated for entertainment.")

        #==============
        #中央画像にする
        #==============
        #img_col1,col2,col3 = st.columns([1,2,1])

        #with col2:
        #    if os.path.exists("images/IMG_7200.png"):
        #        st.image("images/IMG_7200.png",width=300)

        #HTML設定
        st.markdown(
            """
        <h2 style="text-align:center; color:white; text-shadow:2px 2px 5px black;">
           ARCANE is waiting for you!
        </h2>
            """,unsafe_allow_html=True)
        
        if days_left <= 1:
            st.fireworks()#残り一日なら花火演出

        #================
        #EXITを中央に配置
        #================
        exit_col1,col2,col3 = st.columns([1,2,1])

        with col2:
            if st.button("EXIT",use_container_width=True):
                st.rerun()
        
    st.markdown(
        """
         <div style="
         display:flex;
         justify-content:center;
         align-items:center;
         text-align:center; 
         color:gray; 
         font-size:12px;">
         This is a fan-made project created for educational and non-commercial purposes.<br>
         All copyrights, trademarks, and related rights belong to their respective owners, including Gryphline.
        </div>
        """,
        unsafe_allow_html=True
        )

